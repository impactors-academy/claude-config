# Claude Config — Skills & Tools

Global Claude Code configuration for Impactors Academy.  
Backup repo: `github.com/impactors-academy/claude-config`

## Restore on a new machine
```bash
gh auth login  # as impactors-academy
git clone https://github.com/impactors-academy/claude-config.git ~/.claude/skills
# restart Claude Code
```

## Add a new skill
```bash
cp -r /path/to/skill ~/.claude/skills/<skill-name>
cd ~/.claude/skills && git add . && git commit -m "add <skill-name>" && git push
```

---

## Skill Categories

### UI / Design Inspiration
| Skill | What it does |
|---|---|
| `21st-dev` | 21st.dev component catalog reference — heroes, cards, forms, sections, templates |
| `ui-ux-pro-max` | 84 UI styles, 161 color palettes, 73 font pairings, 99 UX guidelines |
| `ui-styling` | Tailwind + shadcn/ui theming, responsive design, accessibility |
| `design-system` | Design token architecture, component specs, primitive/semantic tokens |
| `design` | Logo, icon, CIP, social media, slides design patterns |
| `brand` | Brand guidelines, visual identity, voice/tone, asset management |
| `banner-design` | Banner sizes, formats, and ad creative specs |
| `slides` | Presentation slide layouts, copywriting, HTML templates |
| `modern-web-design` | 2024 web design trends, interaction patterns, accessibility |

### Animation & Motion
| Skill | What it does |
|---|---|
| `motion-framer` | Framer Motion — variants, gestures, layout animations, springs |
| `gsap-scrolltrigger` | GSAP timelines, ScrollTrigger, easing, scroll-linked animations |
| `animejs` | Anime.js timelines, staggers, SVG animation |
| `react-spring-physics` | Physics-based springs, Popmotion |
| `lottie-animations` | Lottie / After Effects export, performance optimization |
| `scroll-reveal-libraries` | AOS, Intersection Observer, scroll reveal patterns |
| `animated-component-libraries` | Magic UI, React Bits, pre-built animated components |
| `barba-js` | Page transitions, view transitions API |
| `locomotive-scroll` | Smooth scroll, parallax, GSAP integration |

### 3D & WebGL
| Skill | What it does |
|---|---|
| `threejs-webgl` | Three.js scenes, materials, geometry, optimization |
| `react-three-fiber` | R3F for React — declarative Three.js |
| `babylonjs-engine` | Babylon.js 3D engine, physics, PBR |
| `pixijs-2d` | PixiJS 2D WebGL, sprites, filters, particles |
| `playcanvas-engine` | PlayCanvas real-time 3D, editor workflow |
| `aframe-webxr` | A-Frame WebXR, VR/AR, component system |
| `lightweight-3d-effects` | Zdog, Vanta.js, CSS 3D tricks |
| `web3d-integration-patterns` | Choosing 3D libs, loading GLTFs, performance budgets |
| `spline-interactive` | Spline 3D web integration, runtime API |
| `rive-interactive` | Rive state machines, interactive animations |
| `blender-web-pipeline` | Blender → web export, GLTF optimization |
| `substance-3d-texturing` | PBR textures, Substance export presets for web |

### Engineering
| Skill | What it does |
|---|---|
| `tdd` / `tdd-guide` | Test-driven development workflows |
| `api-design-reviewer` | REST/GraphQL API review |
| `api-test-suite-builder` | API test scaffolding |
| `zero-hallucination-coder` | Strict, citation-backed code generation |
| `tech-debt` / `tech-debt-tracker` | Tech debt identification and tracking |
| `tech-stack-evaluator` | Framework/library evaluation |
| `terraform-patterns` | Infrastructure as code patterns |
| `aws-solution-architect` | AWS architecture guidance |
| `azure-cloud-architect` | Azure architecture guidance |
| `a11y-audit` | Accessibility auditing, WCAG compliance |
| `ab-test-setup` | A/B test design and sample sizing |
| `browser-automation` | Playwright, Puppeteer patterns |
| `stripe-integration-expert` | Stripe payments integration |
| `react-three-fiber` | (see 3D section) |

### Product & Project Management
| Skill | What it does |
|---|---|
| `agile-product-owner` | Backlog grooming, sprint planning, user stories |
| `user-story` | User story writing framework |
| `product-team` | Product team workflows |
| `project-management` | Project tracking and planning |
| `board-deck-builder` | Board presentation decks |
| `board-prep` | Board meeting preparation |
| `board-meeting` | Meeting facilitation |

### Business & Growth
| Skill | What it does |
|---|---|
| `business-growth-skills` | Revenue growth strategies |
| `sales-engineer` | Technical sales support |
| `revenue-operations` | RevOps workflows |
| `customer-success-manager` | CS playbooks |
| `contract-and-proposal-writer` | Proposals and contracts |
| `commercial` | Commercial strategy |

### Marketing
| Skill | What it does |
|---|---|
| `ad-creative` | Ad copy and creative briefs |
| `marketing-skill` | Marketing strategy frameworks |
| `video-content-strategist` | Video content planning |
| `youtube-full` | YouTube growth strategy |
| `x-twitter-growth` | Twitter/X growth |
| `app-store-optimization` | ASO for mobile apps |
| `aeo` | Answer Engine Optimization |
| `webinar-marketing` | Webinar strategy |
| `social-media` / `social-photos-design` | Social content |

### C-Level Advisors
| Skill | What it does |
|---|---|
| `boardroom` | Full board-level strategic review |
| `c-level-agents` | Multi-CXO perspective review |
| `chief-ai-officer-advisor` | CAIO strategy |
| `chief-customer-officer-advisor` | CCO strategy |
| `chief-data-officer-advisor` | CDO strategy |
| `vpe-advisor` | VP Engineering advisory |

### Research & Analysis
| Skill | What it does |
|---|---|
| `research` | Research frameworks and methods |
| `research-ops` | Research operations |
| `ux-researcher-designer` | UX research methods |
| `statistical-analyst` | Statistical analysis |
| `autoresearch-agent` | Automated research workflows |

### Business Operations
| Skill | What it does |
|---|---|
| `business-operations-skills` | Ops strategy |
| `process-mapper` | Business process mapping |
| `knowledge-ops` | Knowledge management |
| `internal-comms` | Internal communications |
| `vendor-management` | Vendor evaluation and management |
| `capacity-planner` | Resource planning |
| `procurement-optimizer` | Procurement strategy |

### Finance
| Skill | What it does |
|---|---|
| `finance` | Financial modeling and analysis |

### Compliance & Security
| Skill | What it does |
|---|---|
| `compliance-os` | Compliance operating system |
| `ai-act-readiness` | EU AI Act compliance |
| `ai-security` | AI security frameworks |
| `threat-detection` | Security threat analysis |

### Productivity & Orchestration
| Skill | What it does |
|---|---|
| `productivity` | Personal productivity systems |
| `orchestration` | Multi-agent orchestration |
| `agent-designer` | Agent workflow design |
| `agent-workflow-designer` | Complex agent pipelines |
| `loop-library` | Looping and iteration patterns |
| `workflow-builder` | Workflow automation |
| `write-a-skill` | Create new Claude skills |
| `skill-creator` | Skill scaffolding tool |

---

## MCP Servers (configured in ~/.claude.json)
| Server | What it does |
|---|---|
| `21st-dev-magic` | Search + install components from 21st.dev directly in Claude (`npx @21st-dev/magic`) |

**21st.dev API key required** — get it at https://21st.dev/magic then set `API_KEY_21ST` in your environment.

---

*Last updated: 2026-07-13 | 460+ skills across 12 categories*
