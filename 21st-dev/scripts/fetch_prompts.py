#!/usr/bin/env python3
"""
21st.dev Prompt Fetcher
=======================
Fetches full integration prompts (component code + demo + deps + CSS + guidelines)
for every component in our reference categories and writes them to the references/ folder.

Usage:
    API_KEY_21ST=your_key python3 fetch_prompts.py
    # or
    python3 fetch_prompts.py --key your_key

Get your free API key at: https://21st.dev/magic/console
"""

import os, sys, json, time, re, argparse
import urllib.request, urllib.error

# ── Config ───────────────────────────────────────────────────────────────────

API_BASE = "https://magic.21st.dev"
CDN_BASE = "https://cdn.21st.dev"

SKILL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REFS_DIR  = os.path.join(SKILL_DIR, "references")

SITEMAP_URL = "https://21st.dev/sitemap.xml"

# Standard shadcn dark theme CSS (same for all components)
SHADCN_CSS = """\
@import "tailwindcss";
@import "tw-animate-css";

:root {
  --background: oklch(0.145 0 0);
  --foreground: oklch(0.985 0 0);
  --card: oklch(0.205 0 0);
  --card-foreground: oklch(0.985 0 0);
  --popover: oklch(0.205 0 0);
  --popover-foreground: oklch(0.985 0 0);
  --primary: oklch(0.922 0 0);
  --primary-foreground: oklch(0.205 0 0);
  --secondary: oklch(0.269 0 0);
  --secondary-foreground: oklch(0.985 0 0);
  --muted: oklch(0.269 0 0);
  --muted-foreground: oklch(0.708 0 0);
  --accent: oklch(0.269 0 0);
  --accent-foreground: oklch(0.985 0 0);
  --destructive: oklch(0.704 0.191 22.216);
  --border: oklch(1 0 0 / 10%);
  --input: oklch(1 0 0 / 15%);
  --ring: oklch(0.556 0 0);
  --chart-1: oklch(0.488 0.243 264.376);
  --chart-2: oklch(0.696 0.17 162.48);
  --chart-3: oklch(0.769 0.188 70.08);
  --chart-4: oklch(0.627 0.265 303.9);
  --chart-5: oklch(0.645 0.246 16.439);
  --sidebar: oklch(0.205 0 0);
  --sidebar-foreground: oklch(0.985 0 0);
  --sidebar-primary: oklch(0.488 0.243 264.376);
  --sidebar-accent: oklch(0.269 0 0);
  --sidebar-accent-foreground: oklch(0.985 0 0);
  --sidebar-border: oklch(1 0 0 / 10%);
  --sidebar-ring: oklch(0.556 0 0);
}
"""

IMPLEMENTATION_GUIDELINES = """\
Implementation Guidelines
 1. Analyze the component structure and identify all required dependencies
 2. Review the component's arguments and state
 3. Identify any required context providers or hooks and install them
 4. Questions to Ask
 - What data/props will be passed to this component?
 - Are there any specific state management requirements?
 - Are there any required assets (images, icons, etc.)?
 - What is the expected responsive behavior?
 - What is the best place to use this component in the app?

Steps to integrate
 0. Copy paste all the code above in the correct directories
 1. Install external dependencies
 2. Fill image assets with Unsplash stock images you know exist
 3. Use lucide-react icons for svgs or logos if component requires them
"""

# ── HTTP helpers ──────────────────────────────────────────────────────────────

def http_get(url, headers=None, timeout=10):
    req = urllib.request.Request(url, headers={
        'User-Agent': 'Mozilla/5.0 Claude/SkillBuilder',
        **(headers or {})
    })
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.read().decode('utf-8', errors='ignore')
    except Exception as e:
        return None

def api_post(endpoint, data, api_key, timeout=15):
    url = f"{API_BASE}{endpoint}"
    body = json.dumps(data).encode('utf-8')
    req = urllib.request.Request(url, data=body, headers={
        'Content-Type': 'application/json',
        'x-api-key': api_key,
    })
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        body = e.read().decode('utf-8', errors='ignore')
        return {'error': f"HTTP {e.code}: {body[:200]}"}
    except Exception as e:
        return {'error': str(e)}

# ── CDN helpers ───────────────────────────────────────────────────────────────

def get_cdn_demo_code(component_page_url):
    """Fetch a component page and extract the CDN demo code URL + code."""
    html = http_get(component_page_url)
    if not html:
        return None, None, None

    chunks = re.findall(r'self\.__next_f\.push\(\[1,(.+?)\]\)', html, re.DOTALL)
    combined = ''
    for c in chunks:
        try: combined += json.loads(c)
        except: pass

    code_urls = re.findall(r'https://cdn\.21st\.dev/[^\s"\\]+code\.demo\.[^\s"\\]+\.tsx', combined)
    preview_urls = [p for p in re.findall(r'https://cdn\.21st\.dev/[^\s"\\]+\.png', combined) if 'avatar' not in p]

    demo_code = None
    code_url = code_urls[0] if code_urls else None
    if code_url:
        demo_code = http_get(code_url)

    return demo_code, preview_urls[0] if preview_urls else None, code_url

def infer_npm_deps(code: str) -> str:
    """Infer npm dependencies from import statements."""
    dep_map = {
        'framer-motion': ['framer-motion'],
        'three': ['three', '@react-three/fiber', '@react-three/drei'],
        '@react-three/fiber': ['three', '@react-three/fiber'],
        '@react-three/drei': ['@react-three/drei'],
        'gsap': ['gsap'],
        'lottie': ['lottie-react'],
        'animejs': ['animejs'],
        'locomotive': ['locomotive-scroll'],
        'pixi': ['pixi.js'],
        'babylon': ['@babylonjs/core'],
        'react-spring': ['@react-spring/web'],
        'motion': ['motion'],
        'canvas-confetti': ['canvas-confetti'],
        'matter-js': ['matter-js'],
        'p5': ['p5'],
    }
    found = set()
    for pkg, deps in dep_map.items():
        if pkg in code:
            found.update(deps)
    return ', '.join(sorted(found)) if found else 'none'

# ── Prompt builders ───────────────────────────────────────────────────────────

def build_prompt_from_api(api_response: dict, slug: str) -> str:
    """Build prompt from the API /fetch-ui response."""
    text = api_response.get('text', '')
    if not text:
        return None
    return text

def build_prompt_from_cdn(demo_code: str, slug: str, username: str, title: str) -> str:
    """Build a prompt from CDN demo code (fallback when API isn't available or for offline use)."""
    deps = infer_npm_deps(demo_code)
    component_name = slug.replace('-', '_')

    return f"""You are given a task to integrate an existing React component in the codebase

The codebase should support:
- shadcn project structure
- Tailwind CSS
- Typescript

If it doesn't, provide instructions on how to setup project via shadcn CLI, install Tailwind or Typescript.

Determine the default path for components and styles.
If default path for components is not /components/ui, provide instructions on why it's important to create this folder

Copy-paste this component to /components/ui folder:
```tsx
{slug}.tsx
// Full source: https://21st.dev/@{username}/components/{slug}
// Install via: npx @21st-dev/magic add {slug}
// Or copy the component code from the 21st.dev page above.

{demo_code}
```

Install NPM dependencies:
```bash
{deps}
```

Extend existing Tailwind 4 index.css with this code (or if project uses Tailwind 3, extend tailwind.config.js or globals.css):
```css
{SHADCN_CSS}
```

{IMPLEMENTATION_GUIDELINES}
"""

# ── Main fetch flow ───────────────────────────────────────────────────────────

def fetch_components_for_category(urls, category_name, api_key, output_file):
    """Fetch prompts for a list of component URLs and write to output_file."""
    print(f"\n{'='*60}")
    print(f"Category: {category_name} ({len(urls)} components)")
    print(f"Output: {output_file}")
    print('='*60)

    header = f"""# 21st.dev — {category_name} — Full Integration Prompts

Each section below is a **copy-paste ready integration prompt** for that component.
Use it directly with Claude or any AI coding tool to drop the component into your project.

---

"""
    sections = []

    for i, url in enumerate(urls):
        slug = url.split('/')[-1]
        username = re.search(r'/@([^/]+)/', url).group(1)
        title = slug.replace('-', ' ').title()

        print(f"  [{i+1:3d}/{len(urls)}] @{username}/{slug}", end='', flush=True)

        prompt = None

        # Try API first (gets full component source code)
        if api_key:
            result = api_post('/api/fetch-ui', {
                'message': f'{title} component',
                'searchQuery': slug.replace('-', ' ')
            }, api_key)

            if 'text' in result and len(result['text']) > 100:
                prompt = result['text']
                print(' ✓ API', flush=True)
            else:
                print(f' ✗ API ({result.get("error", result.get("text","?"))[:40]})', flush=True)
            time.sleep(0.5)  # rate limit

        # Fallback: build from CDN demo code
        if not prompt:
            demo_code, preview, _ = get_cdn_demo_code(url)
            if demo_code:
                prompt = build_prompt_from_cdn(demo_code, slug, username, title)
                print(' ○ CDN', flush=True)
            else:
                print(' ✗ skip', flush=True)
                continue

            time.sleep(0.2)

        section = f"""## {title}

**Author:** @{username}
**URL:** {url}

```
{prompt.strip()}
```

---

"""
        sections.append(section)

    content = header + '\n'.join(sections)
    with open(output_file, 'w') as f:
        f.write(content)

    print(f"  → Wrote {len(sections)} prompts to {os.path.basename(output_file)}")
    return len(sections)


# ── Category definitions ──────────────────────────────────────────────────────

def load_sitemap_urls():
    print("Loading sitemap...")
    xml = http_get(SITEMAP_URL)
    if not xml:
        print("ERROR: Could not fetch sitemap")
        sys.exit(1)
    return re.findall(r'<loc>([^<]+)</loc>', xml)

def get_category_urls(all_urls):
    def top_level(u): return bool(re.search(r'/@[^/]+/components/[^/]+$', u))

    return {
        'heroes': [u for u in all_urls if top_level(u) and 'hero' in u.lower()
                   and '@hero_ui' not in u and '@heroui' not in u and '21st-indexer' not in u][:80],
        'backgrounds': [u for u in all_urls if top_level(u)
                        and any(k in u.lower() for k in ['background','aurora','particle','gradient','mesh','shader','wave','beam','noise','orb'])
                        and '21st-indexer' not in u][:40],
        'pricing': [u for u in all_urls if top_level(u) and 'pricing' in u.lower()
                    and '21st-indexer' not in u][:30],
        'testimonials': [u for u in all_urls if top_level(u)
                         and any(k in u.lower() for k in ['testimonial','review'])
                         and '21st-indexer' not in u][:25],
        'nav': [u for u in all_urls if top_level(u)
                and any(k in u.lower() for k in ['navbar','navigation','-nav-'])
                and '21st-indexer' not in u][:25],
        'cards': [u for u in all_urls if top_level(u)
                  and any(k in u.lower() for k in ['bento','feature-card','glass-card','tilt-card','hover-card'])
                  and '21st-indexer' not in u][:25],
    }


# ── Entry point ───────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description='Fetch 21st.dev component prompts')
    parser.add_argument('--key', default=os.environ.get('API_KEY_21ST', ''),
                        help='21st.dev API key (or set API_KEY_21ST env var)')
    parser.add_argument('--category', default='all',
                        help='Category to fetch: heroes|backgrounds|pricing|testimonials|nav|cards|all')
    parser.add_argument('--limit', type=int, default=0,
                        help='Limit components per category (0 = no limit)')
    args = parser.parse_args()

    if not args.key:
        print("⚠️  No API key provided. Will fall back to CDN demo code only.")
        print("   Get your free key at: https://21st.dev/magic/console")
        print("   Then run: API_KEY_21ST=your_key python3 fetch_prompts.py\n")
    else:
        print(f"✓ Using API key: {args.key[:8]}***")

    all_urls = load_sitemap_urls()
    categories = get_category_urls(all_urls)

    if args.category != 'all':
        categories = {k: v for k, v in categories.items() if k == args.category}

    if args.limit:
        categories = {k: v[:args.limit] for k, v in categories.items()}

    os.makedirs(REFS_DIR, exist_ok=True)
    total = 0
    for cat, urls in categories.items():
        out = os.path.join(REFS_DIR, f"{cat}-prompts.md")
        n = fetch_components_for_category(urls, cat.title(), args.key, out)
        total += n

    print(f"\n✅ Done! {total} prompts written to {REFS_DIR}/")
    print("   Commit with: cd ~/.claude/skills && git add . && git commit -m 'update 21st.dev prompts' && git push")

if __name__ == '__main__':
    main()
