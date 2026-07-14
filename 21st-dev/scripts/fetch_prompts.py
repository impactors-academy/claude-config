#!/usr/bin/env python3
"""
21st.dev Prompt Fetcher
=======================
Uses the 21st.dev search API + shadcn registry endpoint to fetch full
integration prompts (component code + demo + deps + CSS + guidelines)
for each category and writes them to the references/ folder.

Usage:
    API_KEY_21ST=your_key python3 fetch_prompts.py
    python3 fetch_prompts.py --key your_key --category heroes
    python3 fetch_prompts.py --key your_key --category all

Get your free API key at: https://21st.dev/magic/console
"""

import os, sys, json, time, re, argparse
import urllib.request, urllib.error

# ── Config ───────────────────────────────────────────────────────────────────

SKILL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REFS_DIR  = os.path.join(SKILL_DIR, "references")

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

GUIDELINES = """\
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

# ── HTTP ──────────────────────────────────────────────────────────────────────

def http_get(url, headers=None, timeout=10):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0', **(headers or {})})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.read().decode('utf-8', errors='ignore')
    except:
        return None

def http_post_json(url, data, headers=None, timeout=15):
    body = json.dumps(data).encode('utf-8')
    req = urllib.request.Request(url, data=body, headers={
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0',
        **(headers or {})
    })
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        return {'error': f"HTTP {e.code}: {e.read().decode()[:100]}"}
    except Exception as e:
        return {'error': str(e)}

# ── API ───────────────────────────────────────────────────────────────────────

def search(query, api_key, page=1, per_page=20):
    return http_post_json(
        "https://api.21st.dev/api/search",
        {"search": query, "page": page, "per_page": per_page},
        {"x-api-key": api_key}
    )

def fetch_registry(username, slug, api_key):
    raw = http_get(f"https://21st.dev/r/{username}/{slug}?api_key={api_key}")
    if not raw:
        return None
    try:
        data = json.loads(raw)
        return data if data.get('files') else None
    except:
        return None

def get_cdn_demo(page_url):
    html = http_get(page_url)
    if not html:
        return None
    chunks = re.findall(r'self\.__next_f\.push\(\[1,(.+?)\]\)', html, re.DOTALL)
    combined = ''
    for c in chunks:
        try: combined += json.loads(c)
        except: pass
    urls = re.findall(r'https://cdn\.21st\.dev/[^\s"\\]+code\.demo\.[^\s"\\]+\.tsx', combined)
    if not urls:
        return None
    return http_get(urls[0])

# ── Prompt builders ───────────────────────────────────────────────────────────

def prompt_from_registry(reg, username, slug):
    files = reg.get('files', [])
    deps = reg.get('dependencies', [])
    registry_deps = reg.get('registryDependencies', [])

    component_files = [f for f in files if 'demo' not in f.get('path','').lower()]
    demo_files      = [f for f in files if 'demo' in  f.get('path','').lower()]

    code_blocks = []
    for f in component_files + demo_files:
        fname = f['path'].split('/')[-1]
        code_blocks.append(f"{fname}\n{f.get('content','')}")

    deps_str = ', '.join(deps) if deps else 'none'
    shadcn_cmd = (f"\nInstall shadcn/ui components:\n```bash\nnpx shadcn@latest add "
                  + ' '.join(registry_deps) + "\n```\n") if registry_deps else ''

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
{chr(10).join(code_blocks)}
```

Install NPM dependencies:
```bash
{deps_str}
```
{shadcn_cmd}
Extend existing Tailwind 4 index.css with this code (or if project uses Tailwind 3, extend tailwind.config.js or globals.css):
```css
{SHADCN_CSS}
```

{GUIDELINES}"""

def prompt_from_cdn(demo_code, slug, username):
    deps_map = {
        'framer-motion': ['framer-motion'], 'three': ['three','@react-three/fiber'],
        '@react-three/fiber': ['three','@react-three/fiber'], 'gsap': ['gsap'],
        'lottie': ['lottie-react'], 'animejs': ['animejs'],
        'locomotive': ['locomotive-scroll'], 'pixi': ['pixi.js'],
        '@react-spring': ['@react-spring/web'], 'motion': ['motion'],
    }
    found = set()
    for pkg, d in deps_map.items():
        if pkg in demo_code:
            found.update(d)
    deps_str = ', '.join(sorted(found)) if found else 'none'

    return f"""You are given a task to integrate an existing React component in the codebase

The codebase should support:
- shadcn project structure
- Tailwind CSS
- Typescript

Determine the default path for components and styles.
If default path for components is not /components/ui, provide instructions on why it's important to create this folder

Copy-paste this component to /components/ui folder:
```tsx
{slug}.tsx
// Full source available at: https://21st.dev/@{username}/components/{slug}
// Or install via: npx shadcn@latest add "https://21st.dev/r/{username}/{slug}?api_key=$API_KEY_21ST"

{demo_code}
```

Install NPM dependencies:
```bash
{deps_str}
```

Extend existing Tailwind 4 index.css with this code:
```css
{SHADCN_CSS}
```

{GUIDELINES}"""

# ── Category fetch ────────────────────────────────────────────────────────────

CATEGORIES = {
    'heroes': {
        'queries': ['hero section', 'landing hero', 'hero banner', 'animated hero', 'saas hero'],
        'label': 'Hero Sections',
        'max': 60,
    },
    'backgrounds': {
        'queries': ['background animation', 'aurora background', 'particle background',
                    'gradient background', 'shader background', 'mesh gradient', 'noise background'],
        'label': 'Backgrounds & Visual FX',
        'max': 40,
    },
    'pricing': {
        'queries': ['pricing section', 'pricing card', 'pricing table', 'pricing plans'],
        'label': 'Pricing Sections',
        'max': 30,
    },
    'testimonials': {
        'queries': ['testimonial', 'review card', 'testimonial carousel', 'social proof'],
        'label': 'Testimonials & Reviews',
        'max': 25,
    },
    'nav': {
        'queries': ['navbar', 'navigation menu', 'floating nav', 'header navigation'],
        'label': 'Navigation / Navbar',
        'max': 25,
    },
    'cards': {
        'queries': ['bento grid', 'feature card', 'tilt card', 'glass card', 'hover card'],
        'label': 'Cards — Bento / Tilt / Feature / Glass',
        'max': 25,
    },
    'buttons': {
        'queries': ['animated button', 'cta button', 'button effects', 'magnetic button'],
        'label': 'Buttons & CTAs',
        'max': 20,
    },
    'text': {
        'queries': ['animated text', 'text animation', 'typing effect', 'text reveal'],
        'label': 'Text Animations',
        'max': 20,
    },
}

def fetch_category(cat_key, api_key, limit=0):
    cat = CATEGORIES[cat_key]
    queries = cat['queries']
    max_results = limit or cat['max']
    out_file = os.path.join(REFS_DIR, f"{cat_key}-prompts.md")

    print(f"\n{'='*60}")
    print(f"Category: {cat['label']}")
    print(f"Queries: {queries}")
    print('='*60)

    # Collect unique components via search
    seen = set()
    components = []
    for q in queries:
        page = 1
        while len(components) < max_results:
            data = search(q, api_key, page=page, per_page=20)
            if not data or 'results' not in data:
                break
            for r in data['results']:
                cd = r['component_data']
                ud = r['component_user_data']
                key = f"{ud['username']}/{cd['component_slug']}"
                if key not in seen:
                    seen.add(key)
                    components.append({
                        'username': ud['username'],
                        'slug': cd['component_slug'],
                        'name': cd['name'],
                        'description': cd.get('description',''),
                        'install_command': cd.get('install_command',''),
                        'preview_url': r.get('preview_url',''),
                        'usage_count': r.get('usage_count', 0),
                    })
            pagination = data.get('metadata',{}).get('pagination',{})
            if page >= pagination.get('total_pages', 1):
                break
            page += 1
            time.sleep(0.2)
        if len(components) >= max_results:
            break

    components = sorted(components, key=lambda x: x['usage_count'], reverse=True)[:max_results]
    print(f"  Found {len(components)} unique components")

    header = f"""# 21st.dev — {cat['label']} — Full Integration Prompts

{len(components)} components sorted by popularity.
Each section is a copy-paste ready prompt for Claude or any AI coding tool.

---

"""
    sections = []
    for i, comp in enumerate(components):
        username, slug = comp['username'], comp['slug']
        print(f"  [{i+1:3d}/{len(components)}] @{username}/{slug}", end='', flush=True)

        # Try registry first
        reg = fetch_registry(username, slug, api_key)
        if reg:
            prompt = prompt_from_registry(reg, username, slug)
            src = '✓ full source'
        else:
            # Fallback to CDN demo
            demo = get_cdn_demo(f"https://21st.dev/@{username}/components/{slug}")
            if demo:
                prompt = prompt_from_cdn(demo, slug, username)
                src = '○ demo only'
            else:
                print(' ✗ skip', flush=True)
                continue

        print(f' {src}', flush=True)
        time.sleep(0.3)

        desc_line = f"\n**Description:** {comp['description']}" if comp['description'] else ''
        url = f"https://21st.dev/@{username}/components/{slug}"
        sections.append(f"""## {comp['name']}

**Author:** @{username} | **Used:** {comp['usage_count']:,}x
**URL:** {url}
**Install:** `{comp['install_command']}`{desc_line}

```
{prompt.strip()}
```

---

""")

    content = header + '\n'.join(sections)
    os.makedirs(REFS_DIR, exist_ok=True)
    with open(out_file, 'w') as f:
        f.write(content)

    full = sum(1 for s in sections if '✓' in s or 'full source' in content)
    print(f"  → Wrote {len(sections)} prompts to {os.path.basename(out_file)}")
    return len(sections)

# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--key', default=os.environ.get('API_KEY_21ST',''), help='21st.dev API key')
    parser.add_argument('--category', default='all', help=f'Category: {"|".join(CATEGORIES)}|all')
    parser.add_argument('--limit', type=int, default=0, help='Max components per category')
    args = parser.parse_args()

    if not args.key:
        print("⚠️  No API key. Get one at: https://21st.dev/magic/console")
        print("   Run: API_KEY_21ST=your_key python3 fetch_prompts.py")
        sys.exit(1)

    print(f"✓ API key: {args.key[:12]}***")

    cats = list(CATEGORIES.keys()) if args.category == 'all' else [args.category]
    total = 0
    for cat in cats:
        if cat not in CATEGORIES:
            print(f"Unknown category: {cat}")
            continue
        n = fetch_category(cat, args.key, limit=args.limit)
        total += n

    print(f"\n✅ Done! {total} prompts total in {REFS_DIR}/")
    print("   To push: cd ~/.claude/skills && git add . && git commit -m 'update 21st.dev prompts' && git push")

if __name__ == '__main__':
    main()
