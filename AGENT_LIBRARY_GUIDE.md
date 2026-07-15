# Impactors Academy — Claude Agent Library Guide

> **484 skills installed globally.** This guide covers how to use them effectively: how to invoke, how to prompt, what each category is for, and how to combine them for complex work.

---

## Table of Contents

1. [How Skills Work](#how-skills-work)
2. [The Two Ways to Invoke a Skill](#the-two-ways-to-invoke-a-skill)
3. [UI & Design Skills](#ui--design-skills)
4. [Animation & Motion Skills](#animation--motion-skills)
5. [3D & WebGL Skills](#3d--webgl-skills)
6. [Engineering Skills](#engineering-skills)
7. [Product & PM Skills](#product--pm-skills)
8. [Research Skills](#research-skills)
9. [Marketing & Content Skills](#marketing--content-skills)
10. [Business & Strategy Skills](#business--strategy-skills)
11. [C-Level & Advisory Skills](#c-level--advisory-skills)
12. [Compliance & Security Skills](#compliance--security-skills)
13. [Operations & Productivity Skills](#operations--productivity-skills)
14. [MCP Servers](#mcp-servers)
15. [Combining Skills — Power Patterns](#combining-skills--power-patterns)
16. [Creating a Custom Skill](#creating-a-custom-skill)
17. [Managing & Updating the Library](#managing--updating-the-library)
18. [Complete Skill Index](#complete-skill-index)

---

## How Skills Work

Skills are plain Markdown files stored at `~/.claude/skills/<skill-name>/SKILL.md`. When Claude Code starts, it reads the `description:` field of every skill in that folder to understand what's available. When you invoke a skill (or when Claude detects context that matches), it loads the full `SKILL.md` — which may include frameworks, reference data, personas, checklists, or workflow phases — and applies that knowledge to your request.

**Key points:**
- Skills are stateless — they load fresh context each time they're invoked
- Multiple skills can be active simultaneously
- Skills don't execute code on their own; they shape *how Claude thinks and responds*
- The `description:` field is the matching signal — it determines when auto-activation fires

---

## The Two Ways to Invoke a Skill

### Method 1 — Slash command (explicit)

Type `/skill-name` anywhere in your message:

```
/ui-ux-pro-max build a SaaS pricing page
/deep-research what are the top LMS platforms in 2025?
/zero-hallucination-coder add Stripe webhooks to this project
```

The skill activates immediately and shapes the entire response.

### Method 2 — Contextual (automatic)

Don't type anything. Just describe what you need. Claude scans the active skill list and loads the most relevant ones based on your request.

```
"Help me write a YouTube script for our course launch"
→ Claude auto-loads: /youtube-full, /video-content-strategist, /content-creator

"Build a landing page with scroll animations"
→ Claude auto-loads: /ui-ux-pro-max, /gsap-scrolltrigger, /motion-framer, /21st-dev

"Review this auth implementation for security issues"
→ Claude auto-loads: /security-pen-testing, /senior-security, /zero-hallucination-coder
```

**Rule of thumb:** Use explicit `/skill-name` when you want a specific mode or persona. Let auto-activation handle it when your request is descriptive enough.

---

## UI & Design Skills

### `/ui-ux-pro-max` — The flagship design skill

Contains 84 UI styles, 161 color palettes, 73 font pairings, 99 UX guidelines, and 25 chart types across 22 tech stacks. Activates for any visual or design task.

**When to use:** Building new pages, choosing a visual direction, design reviews, component styling.

**Prompting examples:**

```
/ui-ux-pro-max build a SaaS dashboard — dark mode, glassmorphism style
```
```
/ui-ux-pro-max what color palette and font pairing works for an edtech platform?
```
```
/ui-ux-pro-max this landing page looks amateur — what's wrong with it and how do I fix it?
```
```
/ui-ux-pro-max design a bento grid layout for our course feature showcase
```
```
/ui-ux-pro-max give me 3 UI style options for this admin panel with pros/cons
```

**Styles you can reference by name:**
`glassmorphism`, `claymorphism`, `neumorphism`, `brutalism`, `minimalism`, `bento grid`, `flat design`, `skeuomorphism`, `dark mode`, `aurora gradient`

---

### `/ui-styling` — Tailwind + shadcn/ui theming

Deep expertise in Tailwind CSS and shadcn/ui configuration, theming, and customization.

```
/ui-styling set up a dark/light theme with our brand colors (#6366f1 primary) in Tailwind 4
```
```
/ui-styling configure shadcn/ui with custom tokens for Impactors Academy
```
```
/ui-styling why is my Tailwind config not applying the custom font?
```

---

### `/design-system` — Design tokens & component architecture

For building or extending a design system from scratch.

```
/design-system create a token architecture for spacing, typography, and color
```
```
/design-system what's the right way to structure component variants for a button in shadcn?
```
```
/design-system audit this component library for consistency issues
```

---

### `/brand` — Brand identity & guidelines

Brand voice, visual identity, and consistency checking.

```
/brand create a brand guideline document for Impactors Academy
```
```
/brand does this landing page copy match our brand voice?
```
```
/brand define our brand personality, tone, and visual direction
```

---

### `/design` — General design consultation

Broader design thinking and feedback.

```
/design review this wireframe and give me UX feedback
```
```
/design what layout pattern works best for a course catalog page?
```

---

### `/banner-design` — Marketing banners & ads

Optimized for creating visual ad assets, social banners, and promotional graphics.

```
/banner-design create a LinkedIn banner for our next cohort launch
```
```
/banner-design design a YouTube thumbnail template for our course videos
```

---

### `/slides` — Presentation design

For creating decks, pitch presentations, and slide content.

```
/slides build a 10-slide pitch deck for Impactors Academy Series A
```
```
/slides design a course preview presentation for enterprise clients
```

---

### `/21st-dev` — Component inspiration library

Access to 148 ready-to-use UI component prompts from 21st.dev (heroes, backgrounds, pricing, navbars, cards, buttons, testimonials).

```
/21st-dev show me hero section options — I want something with aurora gradient
```
```
/21st-dev install the most popular animated pricing card from 21st.dev
```
```
/21st-dev give me a glassmorphism card component prompt I can drop in
```

**Reference files you can ask Claude to browse:**
- `heroes-prompts.md` — 43 hero section prompts
- `backgrounds-prompts.md` — 40 background components
- `pricing-prompts.md` — 17 pricing sections
- `testimonials-prompts.md`, `nav-prompts.md`, `cards-prompts.md`, `buttons-prompts.md`

---

## Animation & Motion Skills

### `/motion-framer` — Framer Motion (React)

Complete Framer Motion expertise: variants, AnimatePresence, layout animations, gestures, scroll-linked motion, page transitions.

```
/motion-framer add a stagger animation to this course card list
```
```
/motion-framer build a hero with scroll-linked parallax using useScroll + useTransform
```
```
/motion-framer create a shared element transition between the course card and course page
```
```
/motion-framer add a page transition that slides between routes
```
```
/motion-framer animate this sidebar — slide in on open, fade children sequentially
```

---

### `/gsap-scrolltrigger` — GSAP scroll animations

Production-grade scroll-driven animations with ScrollTrigger, timelines, and pinning.

```
/gsap-scrolltrigger pin this section and animate the headline word by word as user scrolls
```
```
/gsap-scrolltrigger create a horizontal scroll section with snap for our feature showcase
```
```
/gsap-scrolltrigger add a counter animation that triggers when it enters the viewport
```
```
/gsap-scrolltrigger build a timeline that sequences 4 elements on page load
```

---

### `/threejs-webgl` — Three.js / WebGL

For 3D scenes, shaders, particle systems, and WebGL effects directly in the browser.

```
/threejs-webgl add a rotating 3D logo to the hero section
```
```
/threejs-webgl create a particle field background that reacts to mouse movement
```
```
/threejs-webgl build a morphing blob shape using custom geometry
```

---

### `/react-three-fiber` — R3F declarative 3D

React-idiomatic Three.js — declarative scenes, hooks, Drei helpers.

```
/react-three-fiber load and display a GLTF model with orbit controls and proper lighting
```
```
/react-three-fiber create a floating card stack with physics using Rapier
```
```
/react-three-fiber build a 3D text component with reflection and environment maps
```

---

### `/animejs` — Anime.js lightweight animations

Timeline-based animations without a heavy library dependency.

```
/animejs animate this SVG path drawing itself in on load
```
```
/animejs stagger a grid of cards entering the viewport
```

---

### `/lottie-animations` — After Effects exports in React

Render Lottie JSON files, control playback, and integrate with React.

```
/lottie-animations add this loading animation Lottie JSON to the button
```
```
/lottie-animations play the success animation when the form submits
```

---

### `/locomotive-scroll` — Smooth scroll + parallax

Smooth scrolling with parallax layers and scroll-based class triggering.

```
/locomotive-scroll set up smooth scroll on this Next.js page
```
```
/locomotive-scroll add parallax depth to the hero image on scroll
```

---

### `/react-spring-physics` — Physics-based animations

Spring physics, interpolation, and natural-feeling motion.

```
/react-spring-physics make this modal bounce open with spring physics
```
```
/react-spring-physics add a drag interaction with spring snap-back
```

---

### `/barba-js` — Page transitions

AJAX page transitions and view routing effects.

```
/barba-js add a crossfade transition between pages in this multi-page site
```

---

### Other animation skills

| Skill | Use for |
|---|---|
| `/scroll-reveal-libraries` | AOS, Intersection Observer patterns |
| `/animated-component-libraries` | Pre-built component animation libraries |
| `/lightweight-3d-effects` | CSS 3D and simple tilt/perspective effects |

---

## 3D & WebGL Skills

| Skill | Best for |
|---|---|
| `/babylonjs-engine` | Game-level 3D, physics, complex scenes |
| `/pixijs-2d` | 2D WebGL: sprites, effects, games |
| `/playcanvas-engine` | Browser-based 3D games and experiences |
| `/aframe-webxr` | WebXR / VR / AR scenes |
| `/spline-interactive` | Embedding Spline 3D scenes |
| `/rive-interactive` | Rive state-machine animations |
| `/blender-web-pipeline` | Blender → Web export workflow |
| `/substance-3d-texturing` | 3D texture creation |
| `/web3d-integration-patterns` | Architecture patterns for 3D on the web |

```
/babylonjs-engine build a product showcase that lets users rotate a 3D model
/pixijs-2d create an interactive particle burst on click
/aframe-webxr set up a basic VR scene I can load on a headset
```

---

## Engineering Skills

### `/zero-hallucination-coder` — High-stakes, rigorous coding

5-phase loop (Discuss → Map → Decompose → Execute → Verify) that grounds every line in real, verified code. No invented APIs, no placeholders, no assumed imports.

**Use when:** Migrations, auth, databases, multi-file features, anything hard to undo.

```
/zero-hallucination-coder add Stripe webhook handling to this Next.js app
```
```
/zero-hallucination-coder migrate this schema — add nullable column, backfill, make NOT NULL
```
```
/zero-hallucination-coder implement JWT refresh token rotation in this Express app
```

---

### `/spec-to-repo` — Turn a spec into a repo

Converts a natural-language project description into a complete, runnable starter codebase.

```
/spec-to-repo build me a Next.js SaaS app with Stripe, Clerk auth, Prisma/Postgres, and a course dashboard
```
```
/spec-to-repo create a FastAPI backend with JWT auth, SQLAlchemy, and a /users CRUD endpoint
```
```
/spec-to-repo scaffold a React Native app with Expo, tab navigation, and a Firebase backend
```

---

### `/tdd` — Test-driven development

Enforces red-green-refactor. Writes tests first, then minimum code to pass.

```
/tdd add unit tests for this payment service — write tests first
```
```
/tdd I want to add an email validation utility — drive it with TDD
```

---

### `/api-design-reviewer` — REST/GraphQL API review

Reviews API design for consistency, versioning, error shapes, and best practices.

```
/api-design-reviewer review these endpoint definitions — am I following REST conventions?
```
```
/api-design-reviewer should this be a query or mutation in GraphQL?
```

---

### `/senior-architect` — System design

High-level architecture decisions, tradeoffs, and system design.

```
/senior-architect how should I structure this monorepo for a web app + mobile + API?
```
```
/senior-architect design the notification system — we need real-time + email + push
```

---

### `/aws-solution-architect` / `/azure-cloud-architect` / `/gcp-cloud-architect`

Cloud architecture, infra design, and service selection for each platform.

```
/aws-solution-architect design a serverless architecture for our video processing pipeline
```
```
/gcp-cloud-architect set up a GKE deployment with Cloud SQL and Cloud Run for our API
```

---

### Other engineering skills

| Skill | Use for |
|---|---|
| `/senior-backend` | Backend code review and architecture |
| `/senior-frontend` | Frontend code review, React patterns |
| `/senior-fullstack` | Full-stack design and implementation |
| `/senior-devops` | CI/CD, containers, infrastructure |
| `/tech-debt-tracker` | Identify and categorize tech debt |
| `/a11y-audit` | Accessibility audit and fixes |
| `/stripe-integration-expert` | Stripe Checkout, webhooks, subscriptions |
| `/database-designer` | Schema design and normalization |
| `/mcp-server-builder` | Build custom MCP servers for Claude |
| `/ci-cd-pipeline-builder` | GitHub Actions, GitLab CI pipelines |
| `/docker-development` | Dockerfile and Compose configuration |
| `/performance-profiler` | Frontend and backend performance |
| `/chaos-engineering` | Resilience testing strategies |

---

## Product & PM Skills

### `/agile-product-owner`

Sprint planning, backlog grooming, user stories, acceptance criteria.

```
/agile-product-owner write user stories for our course enrollment flow
```
```
/agile-product-owner groom this backlog — what should go in the next sprint?
```
```
/agile-product-owner write acceptance criteria for the certificate generation feature
```

---

### `/epic-design`

Break a large feature into epics, stories, and tasks with proper sequencing.

```
/epic-design I want to add a community forum to the platform — design the epic
```
```
/epic-design turn this product vision into a 3-month roadmap with epics
```

---

### `/product-strategist` / `/product-discovery`

Product strategy, opportunity sizing, and discovery frameworks.

```
/product-strategist what should we build next to increase retention for Impactors Academy?
```
```
/product-discovery run a discovery session — what are the biggest pain points for course creators?
```

---

### `/roadmap-communicator`

Translate engineering work into stakeholder-ready roadmap updates.

```
/roadmap-communicator turn this sprint summary into a roadmap update for our investors
```

---

### Other product skills

| Skill | Use for |
|---|---|
| `/user-story` | Write well-formed user stories |
| `/prd` | Create Product Requirements Documents |
| `/rice` | Prioritize features with RICE scoring |
| `/okr` | Define OKRs for the product team |
| `/sprint-plan` | Plan and structure a sprint |
| `/retro` | Run a retrospective |
| `/product-analytics` | Define metrics and analytics events |

---

## Research Skills

### `/deep-research` — Rigorous multi-source investigation

Heavy-weight research with falsifiable hypotheses, parallel sub-agents, source triangulation (3+ independent sources per claim), adversarial review, and per-source files for traceability.

**Use when:** Competitive analysis, strategy decisions, market sizing, anything where a wrong answer is expensive.

```
/deep-research what are the top 5 LMS platforms for corporate training in 2025 — pricing, features, weaknesses?
```
```
/deep-research what is the market size for online professional education in Africa?
```
```
/deep-research how do leading edtech companies structure their cohort-based courses?
```

---

### `/research` — Fast research framework

Lighter-weight research — topic overviews, quick comparisons, structured summaries.

```
/research summarize the current state of AI tutoring tools
```
```
/research compare Teachable vs Kajabi vs Thinkific for our use case
```

---

### `/competitive-teardown`

Structured 12-dimension competitor scoring.

```
/competitive-teardown do a full teardown of Maven.com as a competitor
```
```
/competitive-teardown score Coursera vs Udemy vs us on product, pricing, and reach
```

---

### `/market-research`

Market sizing, customer segmentation, trend analysis.

```
/market-research who is our primary customer and what are their top 3 unmet needs?
```
```
/market-research what does the B2B corporate training buyer look like?
```

---

### Other research skills

| Skill | Use for |
|---|---|
| `/ux-researcher-designer` | UX research methods, interview scripts, usability testing |
| `/statistical-analyst` | Data analysis, hypothesis testing |
| `/autoresearch-agent` | Autonomous research agent |
| `/competitive-intel` | Ongoing competitive monitoring |
| `/competitive-matrix` | Side-by-side feature matrix |

---

## Marketing & Content Skills

### `/youtube-full`

Full YouTube strategy — scripting, titles, thumbnails, SEO, channel growth.

```
/youtube-full write a script for "How AI is changing professional education" — hook, story, CTA
```
```
/youtube-full give me 10 video ideas for our channel that would rank
```
```
/youtube-full optimize this title and thumbnail concept for CTR
```

---

### `/x-twitter-growth`

Twitter/X content strategy, thread writing, growth tactics.

```
/x-twitter-growth write a thread about the Impactors Academy cohort model
```
```
/x-twitter-growth what's our posting strategy to grow from 0 to 10k followers?
```

---

### `/content-creator` / `/content-strategy`

Content planning, editorial calendar, and format selection.

```
/content-creator write a LinkedIn article about the future of cohort-based learning
```
```
/content-strategy build a 90-day content calendar for our course launch
```

---

### `/ad-creative`

Ad copy and creative briefs for paid channels.

```
/ad-creative write 5 Facebook ad variants for our next cohort — goal: lead gen
```
```
/ad-creative create a Google Ads brief for our "Product Management Bootcamp"
```

---

### `/email-sequence`

Drip campaigns, onboarding sequences, nurture flows.

```
/email-sequence write a 5-email welcome sequence for new trial users
```
```
/email-sequence design a re-engagement sequence for users who haven't logged in for 30 days
```

---

### `/seo-audit`

Technical SEO, on-page optimization, and content SEO.

```
/seo-audit audit our landing page for on-page SEO issues
```
```
/seo-audit what keywords should we target for our PM course?
```

---

### Other marketing skills

| Skill | Use for |
|---|---|
| `/cold-email` | Cold outreach sequences |
| `/copywriting` | Persuasive copy for any format |
| `/social-media-manager` | Multi-channel social strategy |
| `/webinar-marketing` | Webinar promotion and follow-up |
| `/app-store-optimization` | ASO for mobile apps |
| `/programmatic-seo` | Programmatic SEO at scale |
| `/landing-page-generator` | Full landing page copy + structure |
| `/launch-strategy` | Product/course launch planning |
| `/referral-program` | Referral program design |
| `/paid-ads` | Paid advertising strategy |

---

## Business & Strategy Skills

### `/boardroom`

Full board-level strategic review — brings in CEO, CFO, CMO, CTO, and investor perspectives simultaneously.

```
/boardroom we're deciding whether to raise a seed round or stay bootstrapped — give me the board view
```
```
/boardroom review this 12-month growth plan across all functions
```

---

### `/business-growth-skills`

Revenue growth frameworks, expansion strategies, unit economics.

```
/business-growth-skills how do we go from $10k to $100k MRR?
```
```
/business-growth-skills build a growth model for the next 12 months
```

---

### `/pricing-strategist`

Pricing model design, tiers, anchoring, and optimization.

```
/pricing-strategist design a 3-tier pricing model for our cohort-based courses
```
```
/pricing-strategist should we use per-seat, per-cohort, or annual subscription pricing for B2B?
```

---

### `/revenue-operations`

RevOps setup — CRM, funnel metrics, pipeline management.

```
/revenue-operations design our sales funnel from awareness to closed
```
```
/revenue-operations what CRM setup do we need at our stage?
```

---

### `/partnerships-architect`

Partnership strategy, deal structures, and outreach.

```
/partnerships-architect identify 5 partnership types that could accelerate Impactors Academy growth
```
```
/partnerships-architect write a partnership proposal for a corporate L&D department
```

---

### Other business skills

| Skill | Use for |
|---|---|
| `/deal-desk` | Pricing and contract negotiation |
| `/channel-economics` | Channel unit economics |
| `/commercial-forecaster` | Revenue forecasting |
| `/scenario-war-room` | Strategy under uncertainty |
| `/intl-expansion` | International expansion planning |
| `/ma-playbook` | M&A strategy and diligence |
| `/customer-success-manager` | CS strategy and playbooks |

---

## C-Level & Advisory Skills

These skills adopt the full perspective, knowledge base, and decision frameworks of a specific executive role.

### `/ceo-advisor`

```
/ceo-advisor I'm deciding between two strategic bets — help me think through it as a CEO
```

### `/cfo-advisor`

```
/cfo-advisor review this financial model — what are the biggest risks?
```
```
/cfo-advisor we're burning $40k/month — how do I extend runway without cutting product?
```

### `/cmo-advisor`

```
/cmo-advisor build a marketing strategy for our Series A announcement
```

### `/cto-advisor`

```
/cto-advisor should we build in-house or buy a video hosting solution?
```
```
/cto-advisor review our tech stack for scale — where are the risks?
```

### `/chief-ai-officer-advisor`

```
/chief-ai-officer-advisor how should we incorporate AI tutoring into the platform without replacing human coaches?
```

### `/vpe-advisor`

```
/vpe-advisor how should I structure engineering teams as we scale from 3 to 15 engineers?
```

### `/c-level-agents`

Invokes multiple C-suite perspectives at once on a single decision.

```
/c-level-agents review our plan to launch a B2B corporate training product
```

### Other C-level skills

| Skill | Use for |
|---|---|
| `/coo-advisor` | Operations and scaling |
| `/cpo-advisor` | Product strategy and roadmap |
| `/cro-advisor` | Conversion and revenue growth |
| `/chro-advisor` | People, culture, hiring |
| `/chief-customer-officer-advisor` | Customer experience strategy |
| `/chief-data-officer-advisor` | Data strategy and governance |
| `/general-counsel-advisor` | Legal and risk guidance |
| `/ciso-advisor` | Security strategy |

---

## Compliance & Security Skills

### `/ai-act-readiness`

EU AI Act compliance assessment and implementation guidance.

```
/ai-act-readiness is our AI tutoring feature subject to the EU AI Act — what do we need to do?
```

### `/security-pen-testing`

Security testing guidance for authorized internal work.

```
/security-pen-testing what should we test before launching our payment flow?
```

### `/soc2-compliance` / `/soc2-audit-prep`

SOC 2 readiness and evidence collection.

```
/soc2-compliance what controls do we need for SOC 2 Type 1?
```

### Other compliance skills

| Skill | Use for |
|---|---|
| `/gdpr-audit-prep` | GDPR compliance checklist |
| `/ai-security` | AI-specific security patterns |
| `/threat-detection` | Threat modeling |
| `/cloud-security` | Cloud security posture |
| `/information-security-manager-iso27001` | ISO 27001 guidance |
| `/compliance-os` | Compliance operating system |
| `/risk-management-specialist` | Risk frameworks |

---

## Operations & Productivity Skills

### `/process-mapper`

Document and optimize business processes.

```
/process-mapper map our student onboarding process from signup to first lesson
```

### `/knowledge-ops`

Knowledge base design and maintenance.

```
/knowledge-ops set up a knowledge base structure for our internal team docs
```

### `/vendor-management`

Vendor evaluation, contracts, and relationships.

```
/vendor-management evaluate 3 video hosting vendors for our course platform
```

### `/capacity-planner`

Resource and capacity planning.

```
/capacity-planner how many engineers do we need to build this feature by Q3?
```

### `/workflow-builder`

Design and document automated workflows.

```
/workflow-builder design an automation for our course completion → certificate → LinkedIn workflow
```

### Other operations skills

| Skill | Use for |
|---|---|
| `/jira-expert` | Jira configuration and workflows |
| `/confluence-expert` | Confluence setup and best practices |
| `/atlassian-admin` | Full Atlassian suite admin |
| `/google-workspace` | Google Workspace setup |
| `/ms365-tenant-manager` | Microsoft 365 management |
| `/incident-commander` | Incident response leadership |
| `/post-mortem` | Blameless post-mortem facilitation |
| `/change-management` | Organizational change frameworks |

---

## MCP Servers

Beyond skills, two MCP servers are configured and available in all sessions.

### 21st.dev Magic (`21st-dev-magic`)

Search and install UI components from 21st.dev directly in conversation — no manual download.

```
"Search 21st.dev for an aurora gradient hero and install it in this project"
"Find the most popular animated pricing card on 21st.dev"
"Install a glassmorphism navbar from 21st.dev into /components/ui/"
```

**Tools available:** `21st_magic_component_builder`, `21st_magic_component_inspiration`, `21st_magic_component_refiner`, `logo_search`

### Figma MCP

Read designs from Figma, push code into Figma, sync Code Connect mappings.

```
"Get the design context from this Figma frame and implement it"
"Push this component into Figma as a new frame"
"Find matching Figma components for these code files"
```

**To verify MCP servers are active:** type `/mcp` in the Claude Code prompt.

---

## Combining Skills — Power Patterns

Skills compose. Here are real workflow patterns.

### Pattern 1 — Full feature build

```
Step 1: /deep-research how do top edtech platforms structure their course completion flows?
Step 2: /agile-product-owner write epics and stories for our completion flow feature
Step 3: /ui-ux-pro-max design the completion screen — minimal, celebratory
Step 4: /motion-framer add a confetti + certificate reveal animation
Step 5: /zero-hallucination-coder implement the backend — mark complete, issue cert, trigger email
Step 6: /stripe-integration-expert add the upsell modal on completion
```

### Pattern 2 — Landing page from scratch

```
/21st-dev show me hero section options — I want something modern and bold
→ pick a hero style

/ui-ux-pro-max suggest a color palette and font pairing for edtech
→ apply the design direction

/gsap-scrolltrigger add scroll-triggered section reveals
/motion-framer animate the CTA button and headline

/seo-audit review the page for on-page SEO
/a11y-audit check accessibility compliance
```

### Pattern 3 — Strategic decision

```
/boardroom should we go B2B or stay B2C — give me the full multi-CXO analysis
→ get the strategic view

/deep-research what does B2B edtech sales motion look like for small teams?
→ validate with market data

/pricing-strategist design a B2B pricing model if we go that route
/cfo-advisor model out the financial impact of each path
```

### Pattern 4 — Course launch campaign

```
/launch-strategy build a 4-week pre-launch plan for our PM Bootcamp
/content-strategy create a content calendar supporting the launch
/youtube-full write 2 video scripts — "Why PM in 2025" and "What you'll learn"
/email-sequence write the launch announcement sequence (waitlist → open enrollment)
/ad-creative write Facebook and LinkedIn ad copy for cold traffic
/x-twitter-growth plan a Twitter launch thread
```

### Pattern 5 — Engineering code review

```
/zero-hallucination-coder review this PR — check for hallucinated APIs and logic errors
/senior-security audit the auth flow in this PR
/a11y-audit check the new components for accessibility
/performance-profiler identify any performance regressions
```

---

## Creating a Custom Skill

A skill is a folder with one file. Here's the minimum structure:

```bash
mkdir ~/.claude/skills/my-skill
```

```markdown
# File: ~/.claude/skills/my-skill/SKILL.md

---
name: my-skill
description: "One-line description Claude uses to decide when to auto-activate this skill. Include keywords for the use cases you want to trigger it."
triggers:
  - "keyword 1"
  - "keyword 2"
---

# My Skill Name

Write everything Claude should know when this skill is active. Plain markdown.

## When to Use

Describe the exact situations where this skill applies.

## Frameworks / Checklists

Add any structured knowledge, templates, or step-by-step processes here.
```

**Push to backup:**
```bash
cd ~/.claude/skills
git add my-skill/
git commit -m "add my-skill"
git push
```

**Advanced:** Look at `/skill-creator` and `/write-a-skill` for AI-assisted skill authoring.

---

## Managing & Updating the Library

### Restore on a new machine

```bash
gh auth login   # as impactors-academy
git clone https://github.com/impactors-academy/claude-config.git ~/.claude/skills
# restart Claude Code
```

### Pull updates

```bash
git -C ~/.claude/skills pull
# restart Claude Code
```

### Refresh 21st.dev component prompts

```bash
API_KEY_21ST=21st_sk_... python3 ~/.claude/skills/21st-dev/scripts/fetch_prompts.py
cd ~/.claude/skills && git add . && git commit -m "refresh 21st.dev prompts $(date +%Y-%m-%d)" && git push
```

### Add a skill from GitHub

```bash
git clone https://github.com/author/skill-repo.git /tmp/new-skill
cp -r /tmp/new-skill/.claude/skills/* ~/.claude/skills/
cd ~/.claude/skills && git add . && git commit -m "add skill-name" && git push
```

### Add a skill via npx

```bash
npx some-skill-cli init --ai claude
cp -r .claude/skills/* ~/.claude/skills/
cd ~/.claude/skills && git add . && git commit -m "add skill-name via npx" && git push
```

---

## Complete Skill Index

> 484 skills organized by category. Invoke any with `/skill-name`.

### UI & Design
`ui-ux-pro-max` · `ui-styling` · `design-system` · `design` · `brand` · `brand-guidelines` · `banner-design` · `slides` · `21st-dev` · `minimalist` · `modern-web-design`

### Animation & Motion
`motion-framer` · `gsap-scrolltrigger` · `animejs` · `lottie-animations` · `locomotive-scroll` · `react-spring-physics` · `barba-js` · `scroll-reveal-libraries` · `animated-component-libraries` · `lightweight-3d-effects`

### 3D & WebGL
`threejs-webgl` · `react-three-fiber` · `babylonjs-engine` · `pixijs-2d` · `playcanvas-engine` · `aframe-webxr` · `spline-interactive` · `rive-interactive` · `blender-web-pipeline` · `substance-3d-texturing` · `web3d-integration-patterns`

### Engineering
`zero-hallucination-coder` · `spec-to-repo` · `tdd` · `tdd-guide` · `senior-architect` · `senior-backend` · `senior-frontend` · `senior-fullstack` · `senior-devops` · `senior-ml-engineer` · `senior-data-engineer` · `senior-data-scientist` · `senior-computer-vision` · `senior-secops` · `senior-security` · `senior-qa` · `senior-prompt-engineer` · `api-design-reviewer` · `api-test-suite-builder` · `a11y-audit` · `stripe-integration-expert` · `database-designer` · `database-schema-designer` · `mcp-server-builder` · `ci-cd-pipeline-builder` · `docker-development` · `tech-debt-tracker` · `tech-debt` · `performance-profiler` · `chaos-engineering` · `chaos-experiment` · `dependency-auditor` · `feature-flags-architect` · `migration-architect` · `monorepo-navigator` · `observability-designer` · `rag-architect` · `runbook-generator` · `slo-architect` · `slo-design` · `kubernetes-operator` · `terraform-patterns` · `helm-chart-builder`

### Cloud
`aws-solution-architect` · `azure-cloud-architect` · `gcp-cloud-architect` · `cloud-security`

### Product & PM
`agile-product-owner` · `epic-design` · `product-strategist` · `product-discovery` · `product-analytics` · `product-manager-toolkit` · `product-skills` · `roadmap-communicator` · `user-story` · `prd` · `rice` · `okr` · `sprint-plan` · `sprint-health` · `retro` · `scrum-master` · `tech-stack-evaluator`

### Research
`deep-research` · `research` · `competitive-teardown` · `competitive-intel` · `competitive-matrix` · `market-research` · `ux-researcher-designer` · `statistical-analyst` · `autoresearch-agent` · `research-finance` · `research-ops-skills`

### Marketing & Content
`youtube-full` · `x-twitter-growth` · `content-creator` · `content-strategy` · `content-production` · `content-humanizer` · `ad-creative` · `email-sequence` · `email-template-builder` · `seo-audit` · `programmatic-seo` · `local-seo-manager` · `aeo` · `schema-markup` · `site-architecture` · `cold-email` · `copywriting` · `copy-editing` · `social-media-manager` · `social-content` · `social-media-analyzer` · `webinar-marketing` · `video-content-strategist` · `app-store-optimization` · `landing-page-generator` · `launch-strategy` · `referral-program` · `paid-ads` · `marketing-demand-acquisition` · `marketing-ideas` · `marketing-ops` · `marketing-psychology` · `marketing-skills` · `marketing-strategy-pmm` · `marketing-context` · `ab-test-setup` · `analytics-tracking` · `campaign-analytics`

### CRO & Growth
`onboarding-cro` · `signup-flow-cro` · `page-cro` · `form-cro` · `popup-cro` · `paywall-upgrade-cro` · `churn-prevention` · `free-tool-strategy` · `growth-marketer`

### Business & Strategy
`boardroom` · `business-growth-skills` · `pricing-strategist` · `pricing-strategy` · `revenue-operations` · `partnerships-architect` · `channel-economics` · `commercial-forecaster` · `commercial-policy` · `commercial-skills` · `deal-desk` · `scenario-war-room` · `intl-expansion` · `ma-playbook` · `customer-success-manager` · `saas-scaffolder` · `saas-health` · `saas-metrics-coach` · `financial-analyst` · `financial-health`

### C-Level Advisors
`ceo-advisor` · `cfo-advisor` · `cmo-advisor` · `cto-advisor` · `coo-advisor` · `cpo-advisor` · `cro-advisor` · `chro-advisor` · `chief-ai-officer-advisor` · `chief-customer-officer-advisor` · `chief-data-officer-advisor` · `general-counsel-advisor` · `ciso-advisor` · `vpe-advisor` · `c-level-agents` · `c-level-skills`

### Compliance & Security
`ai-act-readiness` · `ai-security` · `aims-audit` · `soc2-compliance` · `soc2-audit-prep` · `gdpr-audit-prep` · `gdpr-dsgvo-expert` · `iso27001-audit-prep` · `iso13485-audit-prep` · `iso42001-specialist` · `isms-audit-expert` · `qms-audit-expert` · `eu-ai-act-specialist` · `compliance-os` · `compliance-readiness` · `security-pen-testing` · `threat-detection` · `cloud-security` · `information-security-manager-iso27001` · `risk-management-specialist` · `red-team` · `ciso-advisor` · `fda-consultant-specialist` · `fda-qsr-audit-prep` · `mdr-745-specialist` · `ra-qm-skills` · `capa-officer` · `quality-documentation-manager` · `quality-manager-qmr` · `quality-manager-qms-iso13485` · `clinical-research` · `regulatory-affairs-head`

### Operations & Productivity
`process-mapper` · `knowledge-ops` · `vendor-management` · `capacity-planner` · `workflow-builder` · `jira-expert` · `confluence-expert` · `atlassian-admin` · `atlassian-templates` · `google-workspace` · `ms365-tenant-manager` · `incident-commander` · `incident-response` · `post-mortem` · `change-management` · `procurement-optimizer` · `org-health-diagnostic` · `culture-architect` · `internal-comms` · `internal-narrative` · `team-communications` · `chief-of-staff` · `board-meeting` · `board-deck-builder` · `strategic-alignment`

### Code Review & Quality
`code-reviewer` · `adversarial-reviewer` · `named-persona-adversarial-review` · `self-eval` · `cross-eval` · `karpathy-check` · `karpathy-coder` · `zero-hallucination-coder` · `strict-api` · `security-guidance` · `skill-security-auditor`

### Developer Tooling
`agent-harness` · `agent-protocol` · `agent-workflow-designer` · `agent-designer` · `agent-decision-receipts` · `self-improving-agent` · `prompt-engineer-toolkit` · `write-a-skill` · `skill-creator` · `context-engine` · `knowledge-ops` · `llm-cost-optimizer` · `llm-wiki` · `prompt-governance`

---

*Last updated: 2026-07-15 | 484 skills | GitHub: `github.com/impactors-academy/claude-config`*
