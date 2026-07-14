# 21st.dev — Testimonials — Full Integration Prompts

Each section below is a **copy-paste ready integration prompt** for that component.
Use it directly with Claude or any AI coding tool to drop the component into your project.

---

## Scroll Reel Testimonials

**Author:** @smammar100
**URL:** https://21st.dev/@smammar100/components/scroll-reel-testimonials

```
You are given a task to integrate an existing React component in the codebase

The codebase should support:
- shadcn project structure
- Tailwind CSS
- Typescript

If it doesn't, provide instructions on how to setup project via shadcn CLI, install Tailwind or Typescript.

Determine the default path for components and styles.
If default path for components is not /components/ui, provide instructions on why it's important to create this folder

Copy-paste this component to /components/ui folder:
```tsx
scroll-reel-testimonials.tsx
// Full source: https://21st.dev/@smammar100/components/scroll-reel-testimonials
// Install via: npx @21st-dev/magic add scroll-reel-testimonials
// Or copy the component code from the 21st.dev page above.

import { ScrollReelTestimonials } from "@/components/ui/scroll-reel-testimonials";

const TESTIMONIALS = [
  {
    quote: "Big effort - high quality. Best Framer content out there.",
    author: "Jan Dittrich",
    image:
      "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=400&q=80&auto=format&fit=crop",
    alt: "Portrait of Jan Dittrich",
  },
  {
    quote:
      "I'm building a new website and it's absolutely ridiculous how valuable your content has been.",
    author: "Michael Riddering",
    image:
      "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=400&q=80&auto=format&fit=crop",
    alt: "Portrait of Michael Riddering",
  },
  {
    quote: "Way too much value for free to be honest.",
    author: "James Traf",
    image:
      "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=400&q=80&auto=format&fit=crop",
    alt: "Portrait of James Traf",
  },
];

export default function DemoOne() {
  return (
    <div className="flex min-h-screen items-center justify-center bg-background p-8">
      <ScrollReelTestimonials testimonials={TESTIMONIALS} />
    </div>
  );
}
```

Install NPM dependencies:
```bash
none
```

Extend existing Tailwind 4 index.css with this code (or if project uses Tailwind 3, extend tailwind.config.js or globals.css):
```css
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

```

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
```

---


## Preview Switch Hero

**Author:** @ruixenui
**URL:** https://21st.dev/@ruixenui/components/preview-switch-hero

```
You are given a task to integrate an existing React component in the codebase

The codebase should support:
- shadcn project structure
- Tailwind CSS
- Typescript

If it doesn't, provide instructions on how to setup project via shadcn CLI, install Tailwind or Typescript.

Determine the default path for components and styles.
If default path for components is not /components/ui, provide instructions on why it's important to create this folder

Copy-paste this component to /components/ui folder:
```tsx
preview-switch-hero.tsx
// Full source: https://21st.dev/@ruixenui/components/preview-switch-hero
// Install via: npx @21st-dev/magic add preview-switch-hero
// Or copy the component code from the 21st.dev page above.

import { PreviewSwitchHero } from "@/components/ui/preview-switch-hero";

import {
  Battery,
  Boxes,
  Gem,
  Hexagon,
  Orbit,
  Signal,
  Spline,
  Waypoints,
  Wifi,
} from "lucide-react";

/* ── minimal phone mock (iPhone frame + a single line of copy) ──── */

function PhonePanel({ title, subtitle }: { title: string; subtitle: string }) {
  return (
    // iPhone-style frame with a soft bottom fade so it dissolves into the page.
    <div className="relative mx-auto w-full max-w-[400px] px-2 [mask-image:linear-gradient(to_bottom,black_80%,transparent)]">
      {/* outer bezel */}
      <div className="overflow-hidden rounded-t-[2.5rem] bg-background/75 px-2 pt-2 shadow-md shadow-black/[0.06] ring-1 ring-foreground/10">
        {/* screen — fixed height so switching tabs never resizes the phone */}
        <div className="h-[320px] overflow-hidden rounded-t-[2rem] bg-foreground/[0.03] px-6 ring-1 ring-foreground/10 dark:bg-black">
          {/* status bar */}
          <div className="flex items-center justify-between py-2 text-xs text-foreground">
            <span className="font-semibold">9:41</span>
            <div className="flex items-end gap-1">
              <Signal aria-hidden className="size-4" />
              <Wifi aria-hidden className="size-[18px]" />
              <Battery aria-hidden className="-mb-px size-5" />
            </div>
          </div>

          {/* grabber */}
          <div className="mx-auto mt-3 h-1.5 w-10 rounded-full bg-foreground/15" />

          {/* small text */}
          <div className="px-2 pt-12 text-center">
            <p className="text-2xl font-semibold tracking-tight text-foreground/80">
              {title}
            </p>
            <p className="mt-2 text-sm text-muted-foreground">{subtitle}</p>
          </div>
        </div>
      </div>
    </div>
  );
}

const PANELS = [
  {
    title: "Pick a time",
    subtitle: "Guests book in two taps — no account needed.",
  },
  {
    title: "Always in sync",
    subtitle: "Reads every calendar so you're never double-booked.",
  },
  {
    title: "Zero no-shows",
    subtitle: "Automatic email and SMS nudges before each call.",
  },
  {
    title: "Round-robin",
    subtitle: "Route each booking to whoever's free first.",
  },
];

/* ── client logos ────────────────────────────────────────────────
 * Fictional brands rendered as icon + wordmark. Self-contained (no
 * external assets or real third-party marks) and theme-adaptive — the
 * icon inherits `currentColor`, so it tracks light/dark automatically.
 */

const LOGO_CLS =
  "inline-flex items-center gap-1.5 text-base font-semibold tracking-tight text-muted-foreground";

const CLIENT_LOGOS = [
  { name: "Hexa", Icon: Hexagon },
  { name: "Orbital", Icon: Orbit },
  { name: "Facet", Icon: Gem },
  { name: "Stackline", Icon: Boxes },
  { name: "Wayline", Icon: Waypoints },
  { name: "Curveo", Icon: Spline },
].map(({ name, Icon }) => ({
  name,
  logo: (
    <span className={LOGO_CLS}>
      <Icon aria-hidden className="size-5" />
      {name}
    </span>
  ),
}));

/* ── demo ─────────────────────────────────────────────────────────── */

export default function PreviewSwitchHeroDemo() {
  const tabs = [
    { id: "booking", label: "Booking" },
    { id: "availability", label: "Availability" },
    { id: "reminders", label: "Reminders" },
    { id: "team", label: "Team" },
  ].map((t, i) => ({ ...t, media: <PhonePanel {...PANELS[i]} /> }));

  return (
    <PreviewSwitchHero
      badge={{ tag: "New", label: "Round-robin scheduling for teams" }}
      title="Meetings booked without the back-and-forth"
      description="Share one link, sync every calendar, and let guests pick a time that actually works — no email ping-pong."
      ratings={[
        { source: "ease of use", score: "4.9" },
        { source: "support", score: "4.8" },
        { source: "value", score: "4.9" },
      ]}
      showEmail={false}
      primaryCta={{ label: "Get started", href: "#" }}
      secondaryCta={{ label: "Book a demo", href: "#" }}
      avatars={[
        { initials: "AK" },
        { initials: "MJ" },
        { initials: "RP" },
        { initials: "SL" },
        { initials: "TD" },
        { initials: "EV" },
      ]}
      socialProof="loved by 30,000+ teams"
      tabs={tabs}
      logos={CLIENT_LOGOS}
    />
  );
}

```

Install NPM dependencies:
```bash
none
```

Extend existing Tailwind 4 index.css with this code (or if project uses Tailwind 3, extend tailwind.config.js or globals.css):
```css
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

```

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
```

---


## Empty Testimonial

**Author:** @0xUrvish
**URL:** https://21st.dev/@0xUrvish/components/empty-testimonial

```
You are given a task to integrate an existing React component in the codebase

The codebase should support:
- shadcn project structure
- Tailwind CSS
- Typescript

If it doesn't, provide instructions on how to setup project via shadcn CLI, install Tailwind or Typescript.

Determine the default path for components and styles.
If default path for components is not /components/ui, provide instructions on why it's important to create this folder

Copy-paste this component to /components/ui folder:
```tsx
empty-testimonial.tsx
// Full source: https://21st.dev/@0xUrvish/components/empty-testimonial
// Install via: npx @21st-dev/magic add empty-testimonial
// Or copy the component code from the 21st.dev page above.

"use client";
import EmptyTestimonial from "@/components/ui/empty-testimonial";

export default function Demo() {
  return (
    <div className="flex items-center justify-center w-full min-h-screen bg-background p-8">
      <EmptyTestimonial />
    </div>
  );
}

```

Install NPM dependencies:
```bash
none
```

Extend existing Tailwind 4 index.css with this code (or if project uses Tailwind 3, extend tailwind.config.js or globals.css):
```css
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

```

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
```

---


## Twitter Testimonial Cards

**Author:** @nondualrandy
**URL:** https://21st.dev/@nondualrandy/components/twitter-testimonial-cards

```
You are given a task to integrate an existing React component in the codebase

The codebase should support:
- shadcn project structure
- Tailwind CSS
- Typescript

If it doesn't, provide instructions on how to setup project via shadcn CLI, install Tailwind or Typescript.

Determine the default path for components and styles.
If default path for components is not /components/ui, provide instructions on why it's important to create this folder

Copy-paste this component to /components/ui folder:
```tsx
twitter-testimonial-cards.tsx
// Full source: https://21st.dev/@nondualrandy/components/twitter-testimonial-cards
// Install via: npx @21st-dev/magic add twitter-testimonial-cards
// Or copy the component code from the 21st.dev page above.

import { Component } from "@/components/ui/twitter-testimonial-cards";

export default function DemoOne() {
  return <Component />;
}

```

Install NPM dependencies:
```bash
none
```

Extend existing Tailwind 4 index.css with this code (or if project uses Tailwind 3, extend tailwind.config.js or globals.css):
```css
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

```

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
```

---


## Design Testimonial

**Author:** @jatin-yadav05
**URL:** https://21st.dev/@jatin-yadav05/components/design-testimonial

```
You are given a task to integrate an existing React component in the codebase

The codebase should support:
- shadcn project structure
- Tailwind CSS
- Typescript

If it doesn't, provide instructions on how to setup project via shadcn CLI, install Tailwind or Typescript.

Determine the default path for components and styles.
If default path for components is not /components/ui, provide instructions on why it's important to create this folder

Copy-paste this component to /components/ui folder:
```tsx
design-testimonial.tsx
// Full source: https://21st.dev/@jatin-yadav05/components/design-testimonial
// Install via: npx @21st-dev/magic add design-testimonial
// Or copy the component code from the 21st.dev page above.

import { Testimonial } from "@/components/ui/design-testimonial"

export default function Page() {
  return (
    <main className="min-h-screen flex items-center justify-center bg-background w-full">
      <Testimonial />
    </main>
  )
}

```

Install NPM dependencies:
```bash
none
```

Extend existing Tailwind 4 index.css with this code (or if project uses Tailwind 3, extend tailwind.config.js or globals.css):
```css
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

```

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
```

---


## Testimonial V2

**Author:** @avanishverma4
**URL:** https://21st.dev/@avanishverma4/components/testimonial-v2

```
You are given a task to integrate an existing React component in the codebase

The codebase should support:
- shadcn project structure
- Tailwind CSS
- Typescript

If it doesn't, provide instructions on how to setup project via shadcn CLI, install Tailwind or Typescript.

Determine the default path for components and styles.
If default path for components is not /components/ui, provide instructions on why it's important to create this folder

Copy-paste this component to /components/ui folder:
```tsx
testimonial-v2.tsx
// Full source: https://21st.dev/@avanishverma4/components/testimonial-v2
// Install via: npx @21st-dev/magic add testimonial-v2
// Or copy the component code from the 21st.dev page above.

import Component from "@/components/ui/testimonial-v2";

export default function DemoOne() {
  return <Component />;
}

```

Install NPM dependencies:
```bash
none
```

Extend existing Tailwind 4 index.css with this code (or if project uses Tailwind 3, extend tailwind.config.js or globals.css):
```css
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

```

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
```

---


## Clean Testimonial

**Author:** @jatin-yadav05
**URL:** https://21st.dev/@jatin-yadav05/components/clean-testimonial

```
You are given a task to integrate an existing React component in the codebase

The codebase should support:
- shadcn project structure
- Tailwind CSS
- Typescript

If it doesn't, provide instructions on how to setup project via shadcn CLI, install Tailwind or Typescript.

Determine the default path for components and styles.
If default path for components is not /components/ui, provide instructions on why it's important to create this folder

Copy-paste this component to /components/ui folder:
```tsx
clean-testimonial.tsx
// Full source: https://21st.dev/@jatin-yadav05/components/clean-testimonial
// Install via: npx @21st-dev/magic add clean-testimonial
// Or copy the component code from the 21st.dev page above.

import { Testimonial } from "@/components/ui/clean-testimonial"

export default function Page() {
  return (
    <main className="min-h-screen flex items-center justify-center bg-background w-full">
      <Testimonial />
    </main>
  )
}

```

Install NPM dependencies:
```bash
none
```

Extend existing Tailwind 4 index.css with this code (or if project uses Tailwind 3, extend tailwind.config.js or globals.css):
```css
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

```

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
```

---


## Split Testimonial

**Author:** @jatin-yadav05
**URL:** https://21st.dev/@jatin-yadav05/components/split-testimonial

```
You are given a task to integrate an existing React component in the codebase

The codebase should support:
- shadcn project structure
- Tailwind CSS
- Typescript

If it doesn't, provide instructions on how to setup project via shadcn CLI, install Tailwind or Typescript.

Determine the default path for components and styles.
If default path for components is not /components/ui, provide instructions on why it's important to create this folder

Copy-paste this component to /components/ui folder:
```tsx
split-testimonial.tsx
// Full source: https://21st.dev/@jatin-yadav05/components/split-testimonial
// Install via: npx @21st-dev/magic add split-testimonial
// Or copy the component code from the 21st.dev page above.

import { TestimonialsSplit } from "@/components/ui/split-testimonial"

export default function Home() {
  return (
    <main className="min-h-screen flex items-center justify-center bg-background p-8 w-full">
      <TestimonialsSplit />
    </main>
  )
}

```

Install NPM dependencies:
```bash
none
```

Extend existing Tailwind 4 index.css with this code (or if project uses Tailwind 3, extend tailwind.config.js or globals.css):
```css
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

```

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
```

---


## Minimal Testimonial

**Author:** @jatin-yadav05
**URL:** https://21st.dev/@jatin-yadav05/components/minimal-testimonial

```
You are given a task to integrate an existing React component in the codebase

The codebase should support:
- shadcn project structure
- Tailwind CSS
- Typescript

If it doesn't, provide instructions on how to setup project via shadcn CLI, install Tailwind or Typescript.

Determine the default path for components and styles.
If default path for components is not /components/ui, provide instructions on why it's important to create this folder

Copy-paste this component to /components/ui folder:
```tsx
minimal-testimonial.tsx
// Full source: https://21st.dev/@jatin-yadav05/components/minimal-testimonial
// Install via: npx @21st-dev/magic add minimal-testimonial
// Or copy the component code from the 21st.dev page above.

import { TestimonialsMinimal } from "@/components/ui/minimal-testimonial"

export default function Home() {
  return (
    <main className="min-h-screen flex items-center justify-center bg-background p-8 w-full">
      <TestimonialsMinimal />
    </main>
  )
}

```

Install NPM dependencies:
```bash
none
```

Extend existing Tailwind 4 index.css with this code (or if project uses Tailwind 3, extend tailwind.config.js or globals.css):
```css
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

```

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
```

---


## Editorial Testimonial

**Author:** @jatin-yadav05
**URL:** https://21st.dev/@jatin-yadav05/components/editorial-testimonial

```
You are given a task to integrate an existing React component in the codebase

The codebase should support:
- shadcn project structure
- Tailwind CSS
- Typescript

If it doesn't, provide instructions on how to setup project via shadcn CLI, install Tailwind or Typescript.

Determine the default path for components and styles.
If default path for components is not /components/ui, provide instructions on why it's important to create this folder

Copy-paste this component to /components/ui folder:
```tsx
editorial-testimonial.tsx
// Full source: https://21st.dev/@jatin-yadav05/components/editorial-testimonial
// Install via: npx @21st-dev/magic add editorial-testimonial
// Or copy the component code from the 21st.dev page above.

import TestimonialsEditorial from "@/components/ui/editorial-testimonial"

export default function Home() {
  return (
    <main className="min-h-screen flex items-center justify-center bg-background p-8 w-full">
      <TestimonialsEditorial />
    </main>
  )
}

```

Install NPM dependencies:
```bash
none
```

Extend existing Tailwind 4 index.css with this code (or if project uses Tailwind 3, extend tailwind.config.js or globals.css):
```css
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

```

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
```

---


## Unique Testimonial

**Author:** @jatin-yadav05
**URL:** https://21st.dev/@jatin-yadav05/components/unique-testimonial

```
You are given a task to integrate an existing React component in the codebase

The codebase should support:
- shadcn project structure
- Tailwind CSS
- Typescript

If it doesn't, provide instructions on how to setup project via shadcn CLI, install Tailwind or Typescript.

Determine the default path for components and styles.
If default path for components is not /components/ui, provide instructions on why it's important to create this folder

Copy-paste this component to /components/ui folder:
```tsx
unique-testimonial.tsx
// Full source: https://21st.dev/@jatin-yadav05/components/unique-testimonial
// Install via: npx @21st-dev/magic add unique-testimonial
// Or copy the component code from the 21st.dev page above.

import { Testimonials } from "@/components/ui/unique-testimonial"

export default function Home() {
  return (
    <main className="min-h-screen flex items-center justify-center bg-background p-8">
      <Testimonials />
    </main>
  )
}

```

Install NPM dependencies:
```bash
none
```

Extend existing Tailwind 4 index.css with this code (or if project uses Tailwind 3, extend tailwind.config.js or globals.css):
```css
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

```

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
```

---


## Hover Image Preview

**Author:** @avanishverma4
**URL:** https://21st.dev/@avanishverma4/components/hover-image-preview

```
You are given a task to integrate an existing React component in the codebase

The codebase should support:
- shadcn project structure
- Tailwind CSS
- Typescript

If it doesn't, provide instructions on how to setup project via shadcn CLI, install Tailwind or Typescript.

Determine the default path for components and styles.
If default path for components is not /components/ui, provide instructions on why it's important to create this folder

Copy-paste this component to /components/ui folder:
```tsx
hover-image-preview.tsx
// Full source: https://21st.dev/@avanishverma4/components/hover-image-preview
// Install via: npx @21st-dev/magic add hover-image-preview
// Or copy the component code from the 21st.dev page above.

import Component from "@/components/ui/hover-image-preview";

export default function DemoOne() {
  return <Component />;
}

```

Install NPM dependencies:
```bash
none
```

Extend existing Tailwind 4 index.css with this code (or if project uses Tailwind 3, extend tailwind.config.js or globals.css):
```css
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

```

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
```

---


## Hover Preview

**Author:** @thanh
**URL:** https://21st.dev/@thanh/components/hover-preview

```
You are given a task to integrate an existing React component in the codebase

The codebase should support:
- shadcn project structure
- Tailwind CSS
- Typescript

If it doesn't, provide instructions on how to setup project via shadcn CLI, install Tailwind or Typescript.

Determine the default path for components and styles.
If default path for components is not /components/ui, provide instructions on why it's important to create this folder

Copy-paste this component to /components/ui folder:
```tsx
hover-preview.tsx
// Full source: https://21st.dev/@thanh/components/hover-preview
// Install via: npx @21st-dev/magic add hover-preview
// Or copy the component code from the 21st.dev page above.

import { HoverPreview } from "@/components/ui/hover-preview";

export default function DemoOne() {
  return <HoverPreview />;
}

```

Install NPM dependencies:
```bash
none
```

Extend existing Tailwind 4 index.css with this code (or if project uses Tailwind 3, extend tailwind.config.js or globals.css):
```css
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

```

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
```

---


## Multi Media Testimonial

**Author:** @ruixenui
**URL:** https://21st.dev/@ruixenui/components/multi-media-testimonial

```
You are given a task to integrate an existing React component in the codebase

The codebase should support:
- shadcn project structure
- Tailwind CSS
- Typescript

If it doesn't, provide instructions on how to setup project via shadcn CLI, install Tailwind or Typescript.

Determine the default path for components and styles.
If default path for components is not /components/ui, provide instructions on why it's important to create this folder

Copy-paste this component to /components/ui folder:
```tsx
multi-media-testimonial.tsx
// Full source: https://21st.dev/@ruixenui/components/multi-media-testimonial
// Install via: npx @21st-dev/magic add multi-media-testimonial
// Or copy the component code from the 21st.dev page above.

"use client";

import TestimonialCard, { Testimonial } from "@/components/ui/multi-media-testimonial";


const testimonials: Testimonial[] = [
  {
    name: "Alice Johnson",
    profile: "https://github.com/shadcn.png",
    title: "Improved Interview Workflow",
    designation: "Software Engineer",
    content:
      "Ruvy transformed the way I manage my interviews. Highly recommended for professionals looking to save time!",
  },
  {
    name: "Bob Smith",
    profile: "https://github.com/shadcn.png",
    title: "Simplicity at Its Best",
    designation: "Product Manager",
    content:
      "The simplicity of this platform is unmatched. Perfect for small teams and startups.",
    thumbnail: "https://pub-940ccf6255b54fa799a9b01050e6c227.r2.dev/components-preview/popular/three-dwall-calendar-dark.jpg",
  },
  {
    name: "Charlie Lee",
    profile: "https://github.com/shadcn.png",
    title: "Creative and Efficient Platform",
    designation: "UX Designer",
    content: "",
    mediaUrl: "https://pub-940ccf6255b54fa799a9b01050e6c227.r2.dev/crm(1)(1)(1).mp4",
    thumbnail: "https://pub-940ccf6255b54fa799a9b01050e6c227.r2.dev/dashboard-gradient.png",
  },
  {
    type: "text",
    name: "Diana Prince",
    profile: "https://github.com/shadcn.png",
    title: "Flawless Scheduling Experience",
    designation: "Full Stack Developer",
    content:
      "The UI is sleek, intuitive, and makes scheduling interviews a breeze. 10/10 experience!",
    rating: 5,
  },
  {
    name: "Ethan Hunt",
    profile: "https://github.com/shadcn.png",
    title: "Streamlined Pipeline Management",
    designation: "DevOps Engineer",
    content:
      "Managing my pipelines has never been easier thanks to this platform. Excellent UX!",
  },
  {
    name: "Fiona Gallagher",
    profile: "https://github.com/shadcn.png",
    title: "Smooth and Intuitive Interface",
    designation: "Frontend Developer",
    content: "",
    thumbnail: "https://pub-940ccf6255b54fa799a9b01050e6c227.r2.dev/dashboard-gradient.png",
  },
  {
    name: "George Martin",
    profile: "https://github.com/shadcn.png",
    title: "Visually Stunning Design",
    designation: "Backend Developer",
    content: "",
    mediaUrl: "https://pub-940ccf6255b54fa799a9b01050e6c227.r2.dev/crm(1)(1)(1).mp4",
    thumbnail: "https://pub-940ccf6255b54fa799a9b01050e6c227.r2.dev/dashboard-gradient.png",
  },
  {
    name: "Hannah Lee",
    profile: "https://github.com/shadcn.png",
    title: "Efficient Testing Workflow",
    designation: "QA Engineer",
    content:
      "Testing has become more efficient with the tools provided here. Very intuitive and well-designed.",
  },
  {
    type: "text",
    name: "Ian Wright",
    profile: "https://github.com/shadcn.png",
    title: "Time-Saving Integration",
    designation: "Data Scientist",
    content:
      "I can now schedule interviews without leaving my workspace. Saves so much time!",
  },
  {
    name: "Jane Doe",
    profile: "https://github.com/shadcn.png",
    title: "Clean Visual Presentation",
    designation: "AI Researcher",
    content: "",
    thumbnail: "https://pub-940ccf6255b54fa799a9b01050e6c227.r2.dev/components-preview/popular/ripple-distortion-dark.png",
  },
  {
    name: "Kyle Brown",
    profile: "https://github.com/shadcn.png",
    title: "Smooth Playback Experience",
    designation: "UI Designer",
    content: "",
    mediaUrl: "https://pub-940ccf6255b54fa799a9b01050e6c227.r2.dev/crm(1)(1)(1).mp4",
    thumbnail: "https://pub-940ccf6255b54fa799a9b01050e6c227.r2.dev/dashboard-gradient.png",
  },
  {
    name: "Laura Kim",
    profile: "https://github.com/shadcn.png",
    title: "Simple Yet Powerful",
    designation: "Full Stack Developer",
    content:
      "The simplicity of this platform is unmatched. Perfect for small teams and startups.",
  },
  {
    name: "Michael Scott",
    profile: "https://github.com/shadcn.png",
    title: "Organized Interview Management",
    designation: "Project Manager",
    content:
      "I can track and organize interviews effortlessly. Love the clean UI and responsiveness.",
  },
  {
    name: "Nina Patel",
    profile: "https://github.com/shadcn.png",
    title: "Elegant Visual Experience",
    designation: "Mobile Developer",
    content: "",
    mediaUrl: "https://pub-940ccf6255b54fa799a9b01050e6c227.r2.dev/crm(1)(1)(1).mp4",
    thumbnail: "https://pub-940ccf6255b54fa799a9b01050e6c227.r2.dev/dashboard-gradient.png",
  },
  {
    name: "Oscar Wilde",
    profile: "https://github.com/shadcn.png",
    title: "Impressive User Flow",
    designation: "Content Strategist",
    content: "",
    mediaUrl: "https://pub-940ccf6255b54fa799a9b01050e6c227.r2.dev/crm(1)(1)(1).mp4",
    thumbnail: "https://pub-940ccf6255b54fa799a9b01050e6c227.r2.dev/dashboard-gradient.png",
  },
  {
    name: "Pam Beesly",
    profile: "https://github.com/shadcn.png",
    title: "Showcasing Client Feedback",
    designation: "Graphic Designer",
    content:
      "Love the clean testimonial cards and how easy it is to showcase our client feedback.",
  },
  {
    name: "Quentin Tarantino",
    profile: "https://github.com/shadcn.png",
    title: "Perfect for Creative Professionals",
    designation: "Video Editor",
    content: "",
    thumbnail: "https://pub-940ccf6255b54fa799a9b01050e6c227.r2.dev/components-preview/popular/tag-cloud-select-dark.jpg",
  },
  {
    name: "Rachel Green",
    profile: "https://github.com/shadcn.png",
    title: "Enhanced Collaboration",
    designation: "Marketing Specialist",
    content: "",
    mediaUrl: "https://pub-940ccf6255b54fa799a9b01050e6c227.r2.dev/crm(1)(1)(1).mp4",
    thumbnail: "https://pub-940ccf6255b54fa799a9b01050e6c227.r2.dev/dashboard-gradient.png",
  },
  {
    name: "Steve Rogers",
    profile: "https://github.com/shadcn.png",
    title: "Streamlined Recruitment Process",
    designation: "Team Lead",
    content:
      "This platform streamlines our recruitment process like never before. Highly efficient!",
  },
  {
    name: "Tina Fey",
    profile: "https://github.com/shadcn.png",
    title: "Beautifully Designed Platform",
    designation: "Copywriter",
    content:
      "Beautifully designed, intuitive, and extremely user-friendly. Can't recommend enough!",
  },
];


export default function TestimonialsDemoPage() {
  return (
    <section className="px-6 py-16">
      <div className="max-w-7xl mx-auto">
        <h2 className="text-center text-4xl font-bold mb-12 text-foreground">
          Our clients love working with us because we go beyond great design to
          deliver real results.
        </h2>

        {Array.isArray(testimonials) && testimonials.length > 0 ? (
          <div className="columns-1 sm:columns-2 lg:columns-3 gap-3 [column-fill:_balance]">
            {testimonials.map((t, i) => (
              <TestimonialCard key={i} testimonial={t} />
            ))}
          </div>
        ) : (
          <p className="text-center text-muted-foreground">
            No testimonials yet.
          </p>
        )}
      </div>
    </section>
  );
}

```

Install NPM dependencies:
```bash
@react-three/drei, @react-three/fiber, three
```

Extend existing Tailwind 4 index.css with this code (or if project uses Tailwind 3, extend tailwind.config.js or globals.css):
```css
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

```

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
```

---


## Community Testimonial

**Author:** @dhiluxui
**URL:** https://21st.dev/@dhiluxui/components/community-testimonial

```
You are given a task to integrate an existing React component in the codebase

The codebase should support:
- shadcn project structure
- Tailwind CSS
- Typescript

If it doesn't, provide instructions on how to setup project via shadcn CLI, install Tailwind or Typescript.

Determine the default path for components and styles.
If default path for components is not /components/ui, provide instructions on why it's important to create this folder

Copy-paste this component to /components/ui folder:
```tsx
community-testimonial.tsx
// Full source: https://21st.dev/@dhiluxui/components/community-testimonial
// Install via: npx @21st-dev/magic add community-testimonial
// Or copy the component code from the 21st.dev page above.

import TestimonialsSection from "@/components/ui/community-testimonial";

export default function DemoOne() {
  const testimonialsData = {
    title: "Don't just take our word for it",
    subtitle:
      "See what our users are saying about how our app has transformed their daily routines and helped them build lasting habits.",
    rows: [
      {
        id: "row1",
        speed: "50s",
        direction: "left",
        testimonials: [
          {
            id: "t1",
            quote:
              "This app completely changed how I approach my goals. The visual feedback is incredibly motivating!",
            authorName: "Sarah K.",
            authorTitle: "Productivity Blogger",
            avatarUrl: "https://placehold.co/100x100/E2E8F0/A0AEC0?text=SK",
          },
          {
            id: "t2",
            quote:
              "I've tried countless habit trackers, and this is the first one that actually stuck. It's simple, beautiful, and effective.",
            authorName: "Michael B.",
            authorTitle: "Software Engineer",
            avatarUrl: "https://placehold.co/100x100/E2E8F0/A0AEC0?text=MB",
          },
          {
            id: "t3",
            quote:
              "The team accountability features are a game-changer. Our entire group is more motivated and connected.",
            authorName: "Emily W.",
            authorTitle: "Startup Founder",
            avatarUrl: "https://placehold.co/100x100/E2E8F0/A0AEC0?text=EW",
          },
        ],
      },
      {
        id: "row2",
        speed: "40s",
        direction: "right",
        testimonials: [
          {
            id: "t4",
            quote:
              "The design is just stunning. It feels less like a chore and more like a game. I'm hooked!",
            authorName: "David L.",
            authorTitle: "UX Designer",
            avatarUrl: "https://placehold.co/100x100/E2E8F0/A0AEC0?text=DL",
          },
          {
            id: "t5",
            quote:
              "Simple, no clutter, does exactly what it promises. The reminders are gentle but effective.",
            authorName: "Jessica P.",
            authorTitle: "Student",
            avatarUrl: "https://placehold.co/100x100/E2E8F0/A0AEC0?text=JP",
          },
          {
            id: "t6",
            quote:
              "Seeing my progress in the analytics section is the best part of my week. It shows my work is paying off.",
            authorName: "Alex C.",
            authorTitle: "Data Analyst",
            avatarUrl: "https://placehold.co/100x100/E2E8F0/A0AEC0?text=AC",
          },
        ],
      },
      {
        id: "row3",
        speed: "60s",
        direction: "left",
        testimonials: [
          {
            id: "t7",
            quote:
              "I love that my data is private. In a world where everything is tracked, this feels safe and personal.",
            authorName: "Kenji T.",
            authorTitle: "Privacy Advocate",
            avatarUrl: "https://placehold.co/100x100/E2E8F0/A0AEC0?text=KT",
          },
          {
            id: "t8",
            quote:
              "Finally, a habit app that isn't bloated with features I don't need. It's focused and powerful.",
            authorName: "Maria G.",
            authorTitle: "Writer",
            avatarUrl: "https://placehold.co/100x100/E2E8F0/A0AEC0?text=MG",
          },
          {
            id: "t9",
            quote:
              "The community support is surprisingly wholesome. It's a great place for accountability.",
            authorName: "Chris R.",
            authorTitle: "Fitness Coach",
            avatarUrl: "https://placehold.co/100x100/E2E8F0/A0AEC0?text=CR",
          },
        ],
      },
    ],
  };

  return (
    <div
      className="app-root bg-radial min-h-screen flex items-center justify-center py-20 px-4"
      aria-label="Testimonials showcase"
    >
      <TestimonialsSection data={testimonialsData} />
    </div>
  );
}

```

Install NPM dependencies:
```bash
none
```

Extend existing Tailwind 4 index.css with this code (or if project uses Tailwind 3, extend tailwind.config.js or globals.css):
```css
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

```

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
```

---


## Hero Preview Walls

**Author:** @ruixenui
**URL:** https://21st.dev/@ruixenui/components/hero-preview-walls

```
You are given a task to integrate an existing React component in the codebase

The codebase should support:
- shadcn project structure
- Tailwind CSS
- Typescript

If it doesn't, provide instructions on how to setup project via shadcn CLI, install Tailwind or Typescript.

Determine the default path for components and styles.
If default path for components is not /components/ui, provide instructions on why it's important to create this folder

Copy-paste this component to /components/ui folder:
```tsx
hero-preview-walls.tsx
// Full source: https://21st.dev/@ruixenui/components/hero-preview-walls
// Install via: npx @21st-dev/magic add hero-preview-walls
// Or copy the component code from the 21st.dev page above.

import { HeroPreviewWalls } from "@/components/ui/hero-preview-walls";

export default function Page() {
  return (
    <main>
      <HeroPreviewWalls />
    </main>
  );
}

```

Install NPM dependencies:
```bash
none
```

Extend existing Tailwind 4 index.css with this code (or if project uses Tailwind 3, extend tailwind.config.js or globals.css):
```css
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

```

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
```

---


## Testimonial Slider 1

**Author:** @kavikatiyar
**URL:** https://21st.dev/@kavikatiyar/components/testimonial-slider-1

```
You are given a task to integrate an existing React component in the codebase

The codebase should support:
- shadcn project structure
- Tailwind CSS
- Typescript

If it doesn't, provide instructions on how to setup project via shadcn CLI, install Tailwind or Typescript.

Determine the default path for components and styles.
If default path for components is not /components/ui, provide instructions on why it's important to create this folder

Copy-paste this component to /components/ui folder:
```tsx
testimonial-slider-1.tsx
// Full source: https://21st.dev/@kavikatiyar/components/testimonial-slider-1
// Install via: npx @21st-dev/magic add testimonial-slider-1
// Or copy the component code from the 21st.dev page above.

import * as React from "react";
import { TestimonialSlider } from "@/components/ui/testimonial-slider-1";

// 1. Define the review data
const reviews = [
  {
    id: 1,
    name: "Ashley Right",
    affiliation: "Pinterest",
    quote:
      "Professionals in their craft! All products were super amazing with strong attention to details, comps and overall vibe.",
    // Image from the provided screenshot
    imageSrc:
      "https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?w=400&h=600&fit=crop&q=80",
    thumbnailSrc:
      "https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?w=100&h=120&fit=crop&q=80",
  },
  {
    id: 2,
    name: "Jacob Jose",
    affiliation: "New York Times",
    quote:
      "Unlimited, instant access to hundreds of premium quality resources created by designers for designers.",
    // Image from the provided screenshot
    imageSrc:
      "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=400&h=600&fit=crop&q=80",
    thumbnailSrc:
      "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=100&h=120&fit=crop&q=80",
  },
  {
    id: 3,
    name: "Elara Sands",
    affiliation: "Behance",
    quote:
      "The attention to detail is immaculate. Every component feels polished and ready for production.",
    // Thumbnail from the provided screenshot
    imageSrc:
      "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=400&h=600&fit=crop&q=80",
    thumbnailSrc:
      "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=100&h=120&fit=crop&q=80",
  },
  {
    id: 4,
    name: "Marcus Cole",
    affiliation: "Dribbble",
    quote:
      "A true time-saver. I can focus on my core logic instead of pixel-pushing. Highly recommended.",
    // Thumbnail from the provided screenshot
    imageSrc:
      "https://images.unsplash.com/photo-1539571696357-5a69c17a67c6?w=400&h=600&fit=crop&q=80",
    thumbnailSrc:
      "https://images.unsplash.com/photo-1539571696357-5a69c17a67c6?w=100&h=120&fit=crop&q=80",
  },
  {
    id: 5,
    name: "Serena V.",
    affiliation: "Figma",
    quote:
      "This is the design system I've been waiting for. It's flexible, accessible, and beautiful.",
    imageSrc:
      "https://images.unsplash.com/photo-1524504388940-b1c1722653e1?w=400&h=600&fit=crop&q=80",
    thumbnailSrc:
      "https://images.unsplash.com/photo-1524504388940-b1c1722653e1?w=100&h=120&fit=crop&q=80",
  },
];

// 2. Render the component with the data
export default function TestimonialSliderDemo() {
  return (
    <div className="w-full">
      <TestimonialSlider reviews={reviews} />
    </div>
  );
}
```

Install NPM dependencies:
```bash
none
```

Extend existing Tailwind 4 index.css with this code (or if project uses Tailwind 3, extend tailwind.config.js or globals.css):
```css
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

```

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
```

---


## Testimonial

**Author:** @kavikatiyar
**URL:** https://21st.dev/@kavikatiyar/components/testimonial

```
You are given a task to integrate an existing React component in the codebase

The codebase should support:
- shadcn project structure
- Tailwind CSS
- Typescript

If it doesn't, provide instructions on how to setup project via shadcn CLI, install Tailwind or Typescript.

Determine the default path for components and styles.
If default path for components is not /components/ui, provide instructions on why it's important to create this folder

Copy-paste this component to /components/ui folder:
```tsx
testimonial.tsx
// Full source: https://21st.dev/@kavikatiyar/components/testimonial
// Install via: npx @21st-dev/magic add testimonial
// Or copy the component code from the 21st.dev page above.

import { TestimonialSection, Testimonial } from "@/components/ui/testimonial";

const testimonialsData: Testimonial[] = [
  {
    type: "user",
    quote: "I was self-employed for 13 years and I'd never really done any interviews. Using interview Warmup I learned how to answer questions in a much more professional way. It's been a big confidence boost.",
    name: "Le'mont C.",
    role: "Google Career Certificate graduate",
    avatarSrc: "https://i.pravatar.cc/150?u=lemont",
    avatarFallback: "LC",
  },
  {
    type: "quote",
    quote: "I feel much more confident in my ability to leverage generative AI tools effectively and responsibly. The hands-on activities and real-world examples were particularly helpful in solidifying my understanding.",
    name: "Susan R.", // Name and role are optional for quote type
    role: "Google Prompting Essentials graduate",
  },
  {
    type: "user",
    quote: "The AI Essentials course was instrumental in equipping me with a strong foundation in leveraging AI for daily tasks. I've achieved a dramatic improvement in my daily efficiency, freeing up time for more strategic tasks.",
    name: "Christian W.",
    role: "Google AI Essentials graduate",
    avatarSrc: "https://i.pravatar.cc/150?u=christian",
    avatarFallback: "CW",
  },
];

export default function TestimonialSectionDemo() {
  return (
    <div className="w-full bg-background">
      <TestimonialSection
        title="Empowering more people with AI"
        testimonials={testimonialsData}
      />
    </div>
  );
}
```

Install NPM dependencies:
```bash
none
```

Extend existing Tailwind 4 index.css with this code (or if project uses Tailwind 3, extend tailwind.config.js or globals.css):
```css
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

```

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
```

---


## Testimonials

**Author:** @ravikatiyar
**URL:** https://21st.dev/@ravikatiyar/components/testimonials

```
You are given a task to integrate an existing React component in the codebase

The codebase should support:
- shadcn project structure
- Tailwind CSS
- Typescript

If it doesn't, provide instructions on how to setup project via shadcn CLI, install Tailwind or Typescript.

Determine the default path for components and styles.
If default path for components is not /components/ui, provide instructions on why it's important to create this folder

Copy-paste this component to /components/ui folder:
```tsx
testimonials.tsx
// Full source: https://21st.dev/@ravikatiyar/components/testimonials
// Install via: npx @21st-dev/magic add testimonials
// Or copy the component code from the 21st.dev page above.

import { TestimonialSection } from "@/components/ui/testimonials"; // Adjust the import path as needed

// Sample data for the testimonials
const testimonialsData = [
  {
    id: 1,
    quote:
      "He is super fast and creative, delivered the website design within a week. Highly skilled and professional designer!",
    name: "Sarah",
    role: "Kickflip",
    imageSrc: "https://images.unsplash.com/photo-1581403341630-a6e0b9d2d257?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8ODR8fHByb2ZpbGV8ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&q=60&w=900?q=80&w=1965&auto=format&fit=crop",
  },
  {
    id: 2,
    quote:
      "Impressed by the professionalism and attention to details in UI design. Highly Recommended!",
    name: "Martha",
    role: "Unicell",
    imageSrc: "https://plus.unsplash.com/premium_photo-1690407617542-2f210cf20d7e?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NXx8cHJvZmlsZXxlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&q=60&w=900?q=80&w=1887&auto=format&fit=crop",
  },
  {
    id: 3,
    quote:
      "A seamless experience from start to finish. Josh made our app design and experience really impressive.",
    name: "Victor",
    role: "Horizone",
    imageSrc: "https://images.unsplash.com/photo-1524504388940-b1c1722653e1?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTAyfHxwcm9maWxlfGVufDB8fDB8fHww&auto=format&fit=crop&q=60&w=900?q=80&w=1887&auto=format&fit=crop",
  },
];

const TestimonialSectionDemo = () => {
  return (
    <TestimonialSection
      title="See what all the talk is about!"
      subtitle="Transformative Client experience from all around the globe"
      testimonials={testimonialsData}
    />
  );
};

export default TestimonialSectionDemo;
```

Install NPM dependencies:
```bash
none
```

Extend existing Tailwind 4 index.css with this code (or if project uses Tailwind 3, extend tailwind.config.js or globals.css):
```css
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

```

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
```

---


## Testimonial Slider

**Author:** @kavikatiyar
**URL:** https://21st.dev/@kavikatiyar/components/testimonial-slider

```
You are given a task to integrate an existing React component in the codebase

The codebase should support:
- shadcn project structure
- Tailwind CSS
- Typescript

If it doesn't, provide instructions on how to setup project via shadcn CLI, install Tailwind or Typescript.

Determine the default path for components and styles.
If default path for components is not /components/ui, provide instructions on why it's important to create this folder

Copy-paste this component to /components/ui folder:
```tsx
testimonial-slider.tsx
// Full source: https://21st.dev/@kavikatiyar/components/testimonial-slider
// Install via: npx @21st-dev/magic add testimonial-slider
// Or copy the component code from the 21st.dev page above.

import { TestimonialSlider, Testimonial } from '@/components/ui/testimonial-slider';

// Sample data for the testimonials. You can replace this with your own data.
const testimonialsData: Testimonial[] = [
  {
    image: 'https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?q=80&w=1888&auto=format&fit=crop',
    quote: "This is a game-changer. The design is intuitive, and the performance is unparalleled. It has streamlined our workflow significantly.",
    name: 'Emily Thomas',
    role: 'Product Designer',
    rating: 5,
  },
  {
    image: 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?q=80&w=1887&auto=format&fit=crop',
    quote: "An incredible experience from start to finish. The team was responsive, and the final product exceeded all our expectations. Highly recommended!",
    name: 'Michael Chen',
    role: 'Lead Developer',
    rating: 5,
  },
  {
    image: 'https://images.unsplash.com/photo-1494790108377-be9c29b29330?q=80&w=1887&auto=format&fit=crop',
    quote: "The attention to detail is what sets this apart. Every feature feels thoughtfully designed and implemented. It's a pleasure to use every day.",
    name: 'Sophia Rodriguez',
    role: 'UX Researcher',
    rating: 4,
  },
];

// The demo component that renders the slider
export default function TestimonialSliderDemo() {
  return (
    <div className="flex items-center justify-center w-full min-h-[450px] bg-background p-4">
      <TestimonialSlider testimonials={testimonialsData} />
    </div>
  );
}
```

Install NPM dependencies:
```bash
none
```

Extend existing Tailwind 4 index.css with this code (or if project uses Tailwind 3, extend tailwind.config.js or globals.css):
```css
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

```

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
```

---


## Testimonials Carousel

**Author:** @ruixenui
**URL:** https://21st.dev/@ruixenui/components/testimonials-carousel

```
You are given a task to integrate an existing React component in the codebase

The codebase should support:
- shadcn project structure
- Tailwind CSS
- Typescript

If it doesn't, provide instructions on how to setup project via shadcn CLI, install Tailwind or Typescript.

Determine the default path for components and styles.
If default path for components is not /components/ui, provide instructions on why it's important to create this folder

Copy-paste this component to /components/ui folder:
```tsx
testimonials-carousel.tsx
// Full source: https://21st.dev/@ruixenui/components/testimonials-carousel
// Install via: npx @21st-dev/magic add testimonials-carousel
// Or copy the component code from the 21st.dev page above.

"use client";

import React from "react";
import { TestimonialsCarousel, Testimonial } from "@/components/ui/testimonials-carousel";

const testimonials: Testimonial[] = [
  {
    text: "The collaboration tools completely changed how our teams work together efficiently. Our productivity has doubled, and communication between departments is seamless. The intuitive interface makes effortless.",
    highlight: "collaboration tools",
    image: "https://randomuser.me/api/portraits/women/21.jpg",
    name: "Priya Kapoor",
    role: "Team Lead",
  },
  {
    text: "Real-time reporting has made our management decisions much faster and accurate. The dashboard allows managers to get insights instantly, enabling proactive decisions and reducing errors.",
    highlight: "Real-time reporting",
    image: "https://randomuser.me/api/portraits/men/22.jpg",
    name: "Rohit Verma",
    role: "Operations Manager",
  },
  {
    text: "Customer engagement features allowed us to reach our clients better than ever. Automated notifications, feedback collection, and analytics have improved retention and satisfaction.",
    highlight: "Customer engagement features",
    image: "https://randomuser.me/api/portraits/women/23.jpg",
    name: "Anjali Mehta",
    role: "Marketing Head",
  },
  {
    text: "The automation workflow reduced repetitive tasks and improved productivity. Employees now spend more time on value-added work, which has improved our bottom line.",
    highlight: "automation workflow",
    image: "https://randomuser.me/api/portraits/men/24.jpg",
    name: "Siddharth Rao",
    role: "IT Specialist",
  },
  {
    text: "The AI analytics insights are invaluable for planning our next steps. Forecasting trends, predicting customer behavior, and analyzing sales data have never been easier.",
    highlight: "AI analytics insights",
    image: "https://randomuser.me/api/portraits/women/25.jpg",
    name: "Nisha Sharma",
    role: "Data Analyst",
  },
];

const TestimonialsDemoPage = () => {
  return (
    <section className="py-20">
      <div className="container mx-auto text-center max-w-3xl">
        <h2 className="text-3xl sm:text-4xl font-bold">What Our Clients Say</h2>
        <p className="mt-3 text-gray-600 dark:text-gray-300">
          Testimonials from companies using our platform to boost productivity.
        </p>
      </div>

      <div className="mt-10 px-6 space-y-6">
        <TestimonialsCarousel
          testimonials={testimonials}
          speed={25}
          direction="left"
          cardHeight={200}
        />
        <TestimonialsCarousel
          testimonials={testimonials}
          speed={30}
          direction="right"
          cardHeight={200}
        />
      </div>
    </section>
  );
};

export default TestimonialsDemoPage;

```

Install NPM dependencies:
```bash
none
```

Extend existing Tailwind 4 index.css with this code (or if project uses Tailwind 3, extend tailwind.config.js or globals.css):
```css
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

```

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
```

---


## Review Filter Bars

**Author:** @ruixenui
**URL:** https://21st.dev/@ruixenui/components/review-filter-bars

```
You are given a task to integrate an existing React component in the codebase

The codebase should support:
- shadcn project structure
- Tailwind CSS
- Typescript

If it doesn't, provide instructions on how to setup project via shadcn CLI, install Tailwind or Typescript.

Determine the default path for components and styles.
If default path for components is not /components/ui, provide instructions on why it's important to create this folder

Copy-paste this component to /components/ui folder:
```tsx
review-filter-bars.tsx
// Full source: https://21st.dev/@ruixenui/components/review-filter-bars
// Install via: npx @21st-dev/magic add review-filter-bars
// Or copy the component code from the 21st.dev page above.

"use client";

import { ReviewFilterGroup, ReviewFilterItem } from "@/components/ui/review-filter-bars";

function DemoPage() {
  const total = 12921;

  return (
    <div className="space-y-4">
      <h2 className="text-lg font-semibold">Filter by rating</h2>
      <p className="text-sm text-muted-foreground">Select a review group to filter results.</p>

      <ReviewFilterGroup defaultValue="all">
        <ReviewFilterItem value="5-stars" stars={5} count={5168} total={total} />
        <ReviewFilterItem value="4-stars" stars={4} count={4726} total={total} />
        <ReviewFilterItem value="3-stars" stars={3} count={3234} total={total} />
        <ReviewFilterItem value="2-stars" stars={2} count={1842} total={total} />
        <ReviewFilterItem value="1-star" stars={1} count={452} total={total} />
      </ReviewFilterGroup>
      <div className="mt-4 text-xs text-center text-muted-foreground">
        Minimal design • Made by{" "}
        <a href="https://www.ruixen.com" target="_blank" className="underline">
          ruixen.com
        </a>
      </div>
    </div>
  );
}

export default DemoPage;

```

Install NPM dependencies:
```bash
none
```

Extend existing Tailwind 4 index.css with this code (or if project uses Tailwind 3, extend tailwind.config.js or globals.css):
```css
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

```

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
```

---


## Testimonial Card 1

**Author:** @ravikatiyar
**URL:** https://21st.dev/@ravikatiyar/components/testimonial-card-1

```
You are given a task to integrate an existing React component in the codebase

The codebase should support:
- shadcn project structure
- Tailwind CSS
- Typescript

If it doesn't, provide instructions on how to setup project via shadcn CLI, install Tailwind or Typescript.

Determine the default path for components and styles.
If default path for components is not /components/ui, provide instructions on why it's important to create this folder

Copy-paste this component to /components/ui folder:
```tsx
testimonial-card-1.tsx
// Full source: https://21st.dev/@ravikatiyar/components/testimonial-card-1
// Install via: npx @21st-dev/magic add testimonial-card-1
// Or copy the component code from the 21st.dev page above.

import { TestimonialCard } from "@/components/ui/testimonial-card-1";

// A simple SVG component for the Trustpilot logo to keep the demo self-contained.
const TrustpilotLogo = () => (
    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M18.332 8.52227L12.0001 6.33398L5.66816 8.52227L7.02641 15.0163L2 19.6673L8.60458 17.0759L12.0001 22.0004L15.3956 17.0759L22 19.6673L16.9737 15.0163L18.332 8.52227Z" fill="#00B67A"/>
        <path d="M12 2L9.44 8.6L2 11L9.44 13.4L12 20L14.56 13.4L22 11L14.56 8.6L12 2Z" fill="white" transform="translate(-1, -1.5) scale(1.1)"/>
    </svg>
);


// Sample data for the demo
const featuresData = [
  "51K Happy customers",
  "4.4 Avg ratings",
  "6 months money back gurantee!",
  "Unlimited messaging with your provider",
];

const testimonialsData = [
  {
    name: "Laura Shouse",
    rating: 5,
    quote: "When I met Dr. Naji I knew my life was about to change. I have lost over 27 pounds since April of this year. he develops a very specific treatment plan for you that really works.",
  },
  {
    name: "Alex Johnson",
    rating: 5,
    quote: "A seamless experience from start to finish. The results exceeded all my expectations. Highly recommended for anyone looking for quality and reliability.",
  },
  {
    name: "Samantha Lee",
    rating: 4,
    quote: "Great service and a very professional team. They addressed all my concerns promptly. The final product was fantastic, though there was a slight delay.",
  },
];


export default function TestimonialCardDemo() {
  return (
    <div className="flex min-h-[600px] w-full items-center justify-center bg-background p-4">
      <TestimonialCard
        logo={<TrustpilotLogo />}
        overallRating={4.4}
        totalRatingsText="4.4 Ratings"
        title="Join thousands of happy customers"
        features={featuresData}
        testimonials={testimonialsData}
      />
    </div>
  );
}
```

Install NPM dependencies:
```bash
none
```

Extend existing Tailwind 4 index.css with this code (or if project uses Tailwind 3, extend tailwind.config.js or globals.css):
```css
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

```

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
```

---


## Testimonial 2

**Author:** @ravikatiyar
**URL:** https://21st.dev/@ravikatiyar/components/testimonial-2

```
You are given a task to integrate an existing React component in the codebase

The codebase should support:
- shadcn project structure
- Tailwind CSS
- Typescript

If it doesn't, provide instructions on how to setup project via shadcn CLI, install Tailwind or Typescript.

Determine the default path for components and styles.
If default path for components is not /components/ui, provide instructions on why it's important to create this folder

Copy-paste this component to /components/ui folder:
```tsx
testimonial-2.tsx
// Full source: https://21st.dev/@ravikatiyar/components/testimonial-2
// Install via: npx @21st-dev/magic add testimonial-2
// Or copy the component code from the 21st.dev page above.

import { AnimatedTestimonialGrid } from '@/components/ui/testimonial-2';

// --- SAMPLE DATA ---
const testimonials = [
  { imgSrc: 'https://images.unsplash.com/photo-1560250097-0b93528c311a?q=80&w=300', alt: 'Professional Man' },
  { imgSrc: 'https://images.unsplash.com/photo-1522075469751-3a6694fb2f61?q=80&w=300', alt: 'Smiling Man' },
  { imgSrc: 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?q=80&w=300', alt: 'Professional Woman' },
  { imgSrc: 'https://images.unsplash.com/photo-1580489944761-15a19d654956?q=80&w=300', alt: 'Smiling Woman' },
  { imgSrc: 'https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?q=80&w=300', alt: 'Man in a suit' },
  { imgSrc: 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?q=80&w=300', alt: 'Bearded Man' },
  { imgSrc: 'https://images.unsplash.com/photo-1557862921-37829c790f19?q=80&w=300', alt: 'Man in a blue shirt' },
  { imgSrc: 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?q=80&w=300', alt: 'Older Man' },
  { imgSrc: 'https://images.unsplash.com/photo-1619895862022-09114b41f16f?q=80&w=300', alt: 'Woman with curly hair' },
  { imgSrc: 'https://images.unsplash.com/photo-1531746020798-e6953c6e8e04?q=80&w=300', alt: 'Woman in an office' },
  { imgSrc: 'https://images.unsplash.com/photo-1438761681033-6461ffad8d80?q=80&w=300', alt: 'Woman with glasses' },
  { imgSrc: 'https://images.unsplash.com/photo-1517841905240-472988babdf9?q=80&w=300', alt: 'Woman with a dog' },
];

export default function TestimonialSectionDemo() {
  return (
    <div className="w-full bg-background">
      <AnimatedTestimonialGrid
        testimonials={testimonials}
        title={
          <>
            Trusted by leaders
            <br />
            from various industries
          </>
        }
        description="Learn why professionals trust our solutions to complete their customer journeys."
        ctaText="Read Success Stories"
        ctaHref="#"
      />
    </div>
  );
}
```

Install NPM dependencies:
```bash
none
```

Extend existing Tailwind 4 index.css with this code (or if project uses Tailwind 3, extend tailwind.config.js or globals.css):
```css
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

```

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
```

---


## Live Preview Style Select

**Author:** @ruixenui
**URL:** https://21st.dev/@ruixenui/components/live-preview-style-select

```
You are given a task to integrate an existing React component in the codebase

The codebase should support:
- shadcn project structure
- Tailwind CSS
- Typescript

If it doesn't, provide instructions on how to setup project via shadcn CLI, install Tailwind or Typescript.

Determine the default path for components and styles.
If default path for components is not /components/ui, provide instructions on why it's important to create this folder

Copy-paste this component to /components/ui folder:
```tsx
live-preview-style-select.tsx
// Full source: https://21st.dev/@ruixenui/components/live-preview-style-select
// Install via: npx @21st-dev/magic add live-preview-style-select
// Or copy the component code from the 21st.dev page above.

"use client";

import * as React from "react";
import {
  LivePreviewStyleSelect,
  StyleOption,
} from "@/components/ui/live-preview-style-select";

const gradientOptions: StyleOption[] = [
  {
    value: "sunset",
    label: "Sunset Glow",
    previewClass: "bg-gradient-to-r from-pink-500 via-orange-400 to-yellow-300",
    description: "Warm pink-orange-yellow gradient",
  },
  {
    value: "aqua",
    label: "Aqua Breeze",
    previewClass: "bg-gradient-to-r from-teal-400 to-cyan-500",
    description: "Cool teal and cyan tones",
  },
  {
    value: "night",
    label: "Night Sky",
    previewClass: "bg-gradient-to-r from-indigo-900 via-purple-800 to-black",
    description: "Dark indigo with deep purple accents",
  },
  {
    value: "forest",
    label: "Forest Haze",
    previewClass: "bg-gradient-to-r from-green-600 via-lime-400 to-emerald-500",
    description: "Lush green earthy tones",
  },
];

export default function DemoLivePreviewStyleSelect (){
  const [style, setStyle] = React.useState<string>("");

  return (
    <div className="p-4 space-y-4">
      <LivePreviewStyleSelect
        options={gradientOptions}
        label="Select Gradient"
        placeholder="Choose a gradient..."
        selectWidth="280px"  // fixed width for all options
        previewHeight="180px"
      />
      {style && (
        <p className="text-sm text-gray-700">
          Selected style: <span className="font-semibold">{style}</span>
        </p>
      )}
    </div>
  );
};

```

Install NPM dependencies:
```bash
none
```

Extend existing Tailwind 4 index.css with this code (or if project uses Tailwind 3, extend tailwind.config.js or globals.css):
```css
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

```

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
```

---

