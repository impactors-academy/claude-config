---
name: 21st-dev
description: UI component inspiration and installation from 21st.dev — community-crafted React components with Tailwind/shadcn
triggers:
  - "use 21st"
  - "21st.dev"
  - "find a component"
  - "ui inspiration"
  - "component library"
  - "design inspiration"
---

# 21st.dev — UI Component Intelligence

**Site:** https://21st.dev  
**What it is:** Community-crafted React components built with Tailwind CSS + shadcn/ui. Hand-designed, not AI-generated.

## MCP Integration (Active in Claude)

The 21st.dev MCP server is configured in Claude settings. Once your API key is set, you can:
- Semantically search components by intent ("glowing card", "animated hero")
- Install components directly into the project with all npm deps
- Generate UI variants with 21st AI (30 free credits/month)
- Search SVG logos by name

**Get your API key:** https://21st.dev/magic (sign in → API key)  
**Add key to:** `~/.claude/settings.json` → `mcpServers["21st-dev-magic"].env.API_KEY_21ST`

## Component Categories Reference

### Base UI Components
| Category | Examples |
|---|---|
| Layout | cards, grids, sidebars, dividers |
| Navigation | menus, tabs, breadcrumbs, docks, pagination |
| Forms | inputs, selects, checkboxes, toggles, sliders, date pickers |
| Feedback | toasts, alerts, badges, progress bars, notifications |
| Overlays | dialogs, popovers, tooltips, dropdowns |
| Data | tables, charts, stats, timelines, lists |
| Media | avatars, galleries, carousels, videos |
| Content | accordions, steppers, tags, calendars |

### Page Sections
| Section | Use case |
|---|---|
| Hero | Landing page openers with CTAs |
| Features | Product/service highlights |
| Pricing | Plans with comparison |
| Testimonials | Social proof blocks |
| FAQ | Accordion-style Q&A |
| CTA | Conversion sections |
| Footer | Links, newsletter, social |
| Team | People cards |
| Stats | Metrics display |
| Marquee | Scrolling logos/text |

### Visual Extras
- **Backgrounds** — animated gradients, particles, mesh, aurora, grid patterns
- **Borders** — glowing, animated, gradient borders
- **Shaders** — WebGL background effects
- **ASCII art** — text-based decorative elements
- **Themes** — full color system presets

### Templates
Landing pages · Portfolios · SaaS · Dashboards · Admin panels · AI chat · Ecommerce · Blogs · Docs

## Scraped Inspiration References (in this skill's /references/ folder)

| File | Contents |
|---|---|
| `references/heroes.md` | 80 hero sections grouped by style (aurora, glass, 3D/shader, gradient, scroll, text, AI/tech, etc.) with author, URL, and code snippet |
| `references/backgrounds.md` | 40 background components (aurora, shader, particle, mesh, noise, orb, grid, wave) |
| `references/pricing.md` | 30 pricing section layouts |
| `references/testimonials.md` | 25 testimonial/review components |
| `references/nav.md` | 25 navbar/navigation components |
| `references/cards.md` | 25 bento, tilt, feature, and glass card components |

When building any of these sections, read the relevant reference file first for inspiration, then pick the closest match and adapt or build from scratch with that aesthetic.

## Usage Patterns

### When building a new page section
1. Describe the component in plain English to the MCP tool
2. Review the component code (already tailwind + shadcn)
3. Install directly — MCP handles npm deps automatically

### Searching manually
Visit https://21st.dev and filter by:
- Component type (left sidebar categories)
- Framework (React by default)
- Style (minimal, glassmorphism, brutalist, etc.)

### CLI usage
```bash
npx @21st-dev/magic add <component-name>
# or with API key:
npx @21st-dev/magic add <component-name> --api-key $API_KEY_21ST
```

## Stack Compatibility

All components use:
- **React** (18+)
- **Tailwind CSS** (v3/v4)
- **shadcn/ui** primitives (Radix UI)
- **TypeScript** ready
- **Framer Motion** for animated variants

This project (`@ia/web` + `@ia/pro`) already has all these dependencies — components from 21st.dev drop in directly.
