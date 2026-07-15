# Claude Config — Impactors Academy

Personal Claude Code configuration: 460+ AI skills, 21st.dev UI inspiration with full prompts, animation/3D skills, and business tools — all backed up here so any new machine is one command away.

**GitHub:** `github.com/impactors-academy/claude-config` (private)
**Owner:** Impactors Academy

> **New to the library?** Read the [complete usage guide](AGENT_LIBRARY_GUIDE.md) — prompting examples, invocation patterns, power workflows, and a full categorized skill index.

---

## Quick Start — New Machine Setup

```bash
# 1. Login to GitHub as impactors-academy
gh auth login

# 2. Clone directly into Claude's skills folder
git clone https://github.com/impactors-academy/claude-config.git ~/.claude/skills

# 3. Restart Claude Code — all 460+ skills are live immediately
```

That's it. No reinstalling packages, no running scripts. Every skill in this repo is available the moment Claude Code restarts.

---

## What's In This Repo

```
~/.claude/skills/
├── README.md                    ← this file
├── 21st-dev/                    ← UI inspiration + integration prompts
│   ├── SKILL.md                 ← skill definition (auto-loaded by Claude)
│   ├── references/
│   │   ├── heroes.md            ← 80 hero section examples
│   │   ├── heroes-prompts.md    ← 43 full copy-paste hero prompts
│   │   ├── backgrounds.md       ← 40 background components
│   │   ├── backgrounds-prompts.md
│   │   ├── pricing-prompts.md   ← 17 pricing sections
│   │   ├── testimonials-prompts.md
│   │   ├── nav-prompts.md
│   │   ├── cards-prompts.md
│   │   ├── buttons-prompts.md
│   │   └── text-prompts.md
│   └── scripts/
│       └── fetch_prompts.py     ← re-fetch prompts from 21st.dev API
├── ui-ux-pro-max/               ← 84 UI styles, 161 palettes, 73 font pairs
├── ui-styling/                  ← Tailwind + shadcn theming
├── design-system/               ← design tokens, component specs
├── motion-framer/               ← Framer Motion deep expertise
├── gsap-scrolltrigger/          ← GSAP + ScrollTrigger animations
├── threejs-webgl/               ← Three.js / WebGL 3D
├── react-three-fiber/           ← R3F declarative 3D
├── [430+ more skills]/          ← see categories below
```

---

## How to Use Skills

Skills are plain markdown files Claude reads automatically. You use them in two ways:

### 1. Invoke a skill with a slash command

Type `/skill-name` in the Claude Code prompt:

```
/ui-ux-pro-max       → activates UI/UX guidance with palettes, styles, font pairings
/motion-framer       → activates Framer Motion expertise
/gsap-scrolltrigger  → activates GSAP + ScrollTrigger guidance
/21st-dev            → activates 21st.dev component inspiration
/design-system       → activates design token architecture mode
```

### 2. Skills activate automatically by context

Claude reads the skill listing at startup and activates relevant skills based on what you're working on. If you're building a landing page, the `21st-dev`, `ui-ux-pro-max`, and `motion-framer` skills will inform Claude's suggestions automatically — no slash command needed.

---

## Using 21st.dev Inspiration

The `21st-dev/` skill is the most directly useful for building UI. Here's the step-by-step workflow:

### Step 1 — Browse inspiration

Open any reference file for ideas:

```bash
# From terminal
cat ~/.claude/skills/21st-dev/references/heroes.md

# Or just ask Claude:
# "Show me hero section options from 21st.dev"
```

### Step 2 — Pick a component and use its prompt

Each `*-prompts.md` file has a ready-to-use integration prompt. Example workflow:

```
You: "I want to add a hero section like the one from @ravikatiyar162 on 21st.dev"

Claude reads heroes-prompts.md → finds the component → 
pastes the full code into your project → installs dependencies
```

Or copy a prompt directly and paste it in chat:

```
You: [paste the full prompt from heroes-prompts.md]
Claude: [drops the component into /components/ui/, installs deps, wires it up]
```

### Step 3 — Install any component on demand via MCP

The 21st.dev MCP server is configured. After Claude Code restarts, you can ask:

```
You: "Find me an aurora background component from 21st.dev and install it"
Claude: [searches 21st.dev, installs the best match directly into your project]
```

### Step 4 — Refresh prompts when you want new components

Run this to pull the latest from 21st.dev:

```bash
cd ~/.claude/skills/21st-dev
API_KEY_21ST=21st_sk_50b68ccc... python3 scripts/fetch_prompts.py

# Then push to keep the GitHub backup current
cd ~/.claude/skills
git add . && git commit -m "refresh 21st.dev prompts" && git push
```

---

## Using Animation Skills

### Framer Motion (`/motion-framer`)

Activates when you need React animations. The skill knows:
- Variants, transitions, gestures, layout animations
- AnimatePresence, useMotionValue, useSpring
- Page transitions, shared element transitions
- Performance patterns

**Example prompts:**
```
"Add a stagger animation to this list using Framer Motion"
"Build a scroll-linked parallax hero with Framer Motion"
"Create a page transition that slides between routes"
```

### GSAP + ScrollTrigger (`/gsap-scrolltrigger`)

Activates for scroll-driven animations. The skill includes starter templates and pattern references.

**Example prompts:**
```
"Pin this section and animate the text as the user scrolls"
"Create a horizontal scroll section with GSAP"
"Add a timeline animation that plays on page load"
```

### Three.js (`/threejs-webgl`) + React Three Fiber (`/react-three-fiber`)

For 3D scenes in the browser.

**Example prompts:**
```
"Add a rotating 3D logo to the hero using React Three Fiber"
"Create a particle system background with Three.js"
"Load and display a GLTF model with proper lighting"
```

### Other animation skills:
| Skill | Use for |
|---|---|
| `/animejs` | Lightweight timeline animations |
| `/lottie-animations` | After Effects exports in React |
| `/locomotive-scroll` | Smooth scroll + parallax |
| `/scroll-reveal-libraries` | AOS, Intersection Observer patterns |
| `/react-spring-physics` | Physics-based spring animations |
| `/barba-js` | Page transition effects |

---

## Using UI/Design Skills

### UI/UX Pro Max (`/ui-ux-pro-max`)

The most powerful design skill — 84 UI styles, 161 color palettes, 73 font pairings, 99 UX guidelines.

**How to use:**
```
"Build a SaaS landing page — use the glassmorphism style with a blue-purple palette"
"Design a dashboard with a minimal dark theme — pick a good font pairing"
"What UI style would work best for an edtech platform?"
```

Claude will consult the style/palette/typography data and apply it consistently.

### UI Styling (`/ui-styling`)

Tailwind and shadcn/ui specific guidance — theming, customization, responsive patterns.

```
"Set up a dark theme with custom brand colors in Tailwind 4"
"Add shadcn/ui to this project and configure the design tokens"
```

### Design System (`/design-system`)

For building or extending a design system.

```
"Create a token architecture for our brand colors (primary: #6366f1)"
"Define semantic tokens for spacing, typography, and color in this project"
```

### Brand (`/brand`)

Brand guideline creation and consistency.

```
"Create a brand guideline document for Impactors Academy"
"Check if this design is consistent with our brand voice"
```

---

## Using Business Skills

These 430+ skills cover everything from marketing to C-level strategy. Invoke by name:

### Marketing
```
/ad-creative          → ad copy and creative briefs
/video-content-strategist → video content planning
/youtube-full         → YouTube growth strategy
/x-twitter-growth     → Twitter/X growth
```

### Engineering
```
/tdd                  → test-driven development
/api-design-reviewer  → REST/GraphQL API review
/zero-hallucination-coder → strict citation-backed code
/tech-debt-tracker    → identify and track tech debt
/aws-solution-architect → AWS architecture guidance
```

### Product & Business
```
/agile-product-owner  → backlog, sprint planning, user stories
/business-growth-skills → revenue growth strategies
/boardroom            → full board-level strategic review
/c-level-agents       → multi-CXO perspective on any decision
```

### Research & Productivity
```
/research             → research frameworks
/ux-researcher-designer → UX research methods
/productivity         → personal productivity systems
/workflow-builder     → workflow automation
```

**Tip:** You don't always need to invoke explicitly. Just describe what you need and Claude will pull the right skills:
```
"Help me write a YouTube script for our course launch"
→ Claude automatically uses /video-content-strategist + /youtube-full
```

---

## MCP Servers (Configured)

Beyond skills, two MCP servers are active after Claude Code restart:

### 21st.dev Magic (`21st-dev-magic`)

Search and install UI components from 21st.dev directly in conversation.

```
"Search 21st.dev for a glassmorphism pricing card and install it"
"Find the most popular hero section on 21st.dev"
"Install an animated button from 21st.dev into this project"
```

**API key:** Already configured in `~/.claude.json`

### How to verify MCP is working:

After restarting Claude Code, run `/mcp` in the prompt to see connected servers.

---

## Adding New Skills

### Option A — Install from GitHub (recommended)

```bash
# Add a skill from any GitHub repo
git clone https://github.com/author/skill-repo.git /tmp/new-skill
cp -r /tmp/new-skill/.claude/skills/* ~/.claude/skills/

# Back it up
cd ~/.claude/skills
git add . && git commit -m "add new-skill from author/skill-repo" && git push
```

### Option B — Install via npx (21st.dev style)

```bash
npx some-skill-cli init --ai claude

# Move to global if it installed locally
cp -r .claude/skills/* ~/.claude/skills/

# Push backup
cd ~/.claude/skills
git add . && git commit -m "add skill-name" && git push
```

### Option C — Create your own skill

A skill is just a folder with a `SKILL.md` file:

```bash
mkdir ~/.claude/skills/my-skill
cat > ~/.claude/skills/my-skill/SKILL.md << 'EOF'
---
name: my-skill
description: What this skill does — one line used by Claude to decide when to activate it
triggers:
  - "keyword that activates this skill"
---

# My Skill

Write your skill content here in plain markdown.
Claude reads this when the skill is active.
EOF

# Push backup
cd ~/.claude/skills
git add . && git commit -m "add my custom skill" && git push
```

---

## Keeping Everything Updated

### Update 21st.dev prompts
```bash
API_KEY_21ST=21st_sk_50b68ccc... python3 ~/.claude/skills/21st-dev/scripts/fetch_prompts.py
cd ~/.claude/skills && git add . && git commit -m "refresh 21st.dev prompts $(date +%Y-%m-%d)" && git push
```

### Update skills from source repos
```bash
# Re-run the original installers
npx ui-ux-pro-max-cli init --ai claude
cp -r .claude/skills/* ~/.claude/skills/

git -C ~/.claude/skills add . && git -C ~/.claude/skills commit -m "update ui-ux-pro-max" && git -C ~/.claude/skills push
```

### Pull latest on an existing machine
```bash
git -C ~/.claude/skills pull
# Restart Claude Code
```

---

## Skill Sources

| Skills | Source | Count |
|---|---|---|
| UI/UX Pro Max suite | `nextlevelbuilder/ui-ux-pro-max-skill` | 7 |
| Business / Marketing / Engineering | `alirezarezvani/claude-skills` | 430 |
| Animation / 3D / Design | `freshtechbro/claudedesignskills` | 23 |
| 21st.dev Inspiration | Custom + 21st.dev API | 1 (with 148 prompts) |
| **Total** | | **461** |

---

## Skill Categories at a Glance

| Category | Key Skills |
|---|---|
| **UI / Design** | `ui-ux-pro-max`, `ui-styling`, `design-system`, `design`, `brand`, `slides`, `banner-design` |
| **Animation** | `motion-framer`, `gsap-scrolltrigger`, `animejs`, `lottie-animations`, `locomotive-scroll`, `scroll-reveal-libraries`, `react-spring-physics`, `barba-js`, `animated-component-libraries` |
| **3D / WebGL** | `threejs-webgl`, `react-three-fiber`, `babylonjs-engine`, `pixijs-2d`, `playcanvas-engine`, `aframe-webxr`, `spline-interactive`, `rive-interactive`, `blender-web-pipeline` |
| **Engineering** | `tdd`, `api-design-reviewer`, `zero-hallucination-coder`, `tech-debt-tracker`, `aws-solution-architect`, `azure-cloud-architect`, `a11y-audit`, `stripe-integration-expert` |
| **Product / PM** | `agile-product-owner`, `user-story`, `product-team`, `project-management`, `board-deck-builder` |
| **Business** | `business-growth-skills`, `sales-engineer`, `revenue-operations`, `customer-success-manager` |
| **Marketing** | `ad-creative`, `video-content-strategist`, `youtube-full`, `x-twitter-growth`, `app-store-optimization` |
| **C-Level** | `boardroom`, `c-level-agents`, `chief-ai-officer-advisor`, `vpe-advisor` |
| **Research** | `research`, `ux-researcher-designer`, `statistical-analyst`, `autoresearch-agent` |
| **Operations** | `process-mapper`, `knowledge-ops`, `vendor-management`, `capacity-planner` |
| **Compliance** | `compliance-os`, `ai-act-readiness`, `ai-security`, `threat-detection` |
| **Productivity** | `productivity`, `orchestration`, `workflow-builder`, `write-a-skill`, `skill-creator` |

---

*Last updated: 2026-07-14*
