# 21st.dev — Cards — Full Integration Prompts

Each section below is a **copy-paste ready integration prompt** for that component.
Use it directly with Claude or any AI coding tool to drop the component into your project.

---

## Be Ui Tilt Card

**Author:** @saurra3h
**URL:** https://21st.dev/@saurra3h/components/be-ui-tilt-card

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
be-ui-tilt-card.tsx
// Full source: https://21st.dev/@saurra3h/components/be-ui-tilt-card
// Install via: npx @21st-dev/magic add be-ui-tilt-card
// Or copy the component code from the 21st.dev page above.

"use client";

import { TiltCard } from "@/components/ui/be-ui-tilt-card";

export default function TiltCardPreview() {
  return (
    <div className="flex items-center justify-center p-6">
      <TiltCard className="w-[280px] border border-border bg-card p-8">
        <div className="text-xs uppercase tracking-wider text-muted-foreground">Premium</div>
        <h3 className="mt-2 text-2xl font-semibold text-foreground">Tilt me</h3>
        <p className="mt-3 text-sm text-muted-foreground">Move your cursor across the card to see 3D tilt + glare.</p>
      </TiltCard>
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


## New Hover Card

**Author:** @edwinvakayil
**URL:** https://21st.dev/@edwinvakayil/components/new-hover-card

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
new-hover-card.tsx
// Full source: https://21st.dev/@edwinvakayil/components/new-hover-card
// Install via: npx @21st-dev/magic add new-hover-card
// Or copy the component code from the 21st.dev page above.

"use client";

import {
  HoverCard,
  HoverCardContent,
  HoverCardTrigger,
} from "../components/ui/hover-card-1";

export function HoverCardPreview() {
  return (
    <div className="flex min-h-[400px] items-center justify-center">
      <HoverCard>
        <div className="flex flex-col items-center gap-4 text-center">
          <HoverCardTrigger asChild>
            
             <a href="#"
              className="text-sm font-medium underline underline-offset-4"
              onClick={(e) => e.preventDefault()}
            >
              View profile
            </a>
          </HoverCardTrigger>
          <p className="max-w-sm text-sm text-muted-foreground">
            Hover for delayed reveal or focus the trigger to compare the same API on the dedicated Radix Hover Card primitive.
          </p>
        </div>
        <HoverCardContent className="w-72">
          <div className="space-y-1">
            <h4 className="text-sm font-semibold">@edwinvakayil</h4>
            <p className="text-[13px] leading-5 text-muted-foreground">
              @edwinvakayil · Design Engineer
            </p>
            <p className="text-[14px] leading-6 text-muted-foreground">
              Leading onboarding, motion systems, and dense product surfaces
              across the core workspace.
            </p>
          </div>
        </HoverCardContent>
      </HoverCard>
    </div>
  );
}

export default HoverCardPreview;
```

Install NPM dependencies:
```bash
motion
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


## 8Bit Hover Card

**Author:** @theorcdev
**URL:** https://21st.dev/@theorcdev/components/8bit-hover-card

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
8bit-hover-card.tsx
// Full source: https://21st.dev/@theorcdev/components/8bit-hover-card
// Install via: npx @21st-dev/magic add 8bit-hover-card
// Or copy the component code from the 21st.dev page above.

import { Button } from "@/components/ui/8bit-button";
import {
  HoverCard,
  HoverCardContent,
  HoverCardTrigger,
} from "@/components/ui/8bit-hover-card";

export default function Demo() {
  return (
    <div className="flex min-h-[200px] items-center justify-center p-8 retro">
      <HoverCard>
        <HoverCardTrigger>
          <Button variant="link">Hover</Button>
        </HoverCardTrigger>
        <HoverCardContent className="w-80">
          For the Horde! ⚔️
        </HoverCardContent>
      </HoverCard>
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


## Tilt Card

**Author:** @tom_ui
**URL:** https://21st.dev/@tom_ui/components/tilt-card

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
tilt-card.tsx
// Full source: https://21st.dev/@tom_ui/components/tilt-card
// Install via: npx @21st-dev/magic add tilt-card
// Or copy the component code from the 21st.dev page above.

"use client";

import { TiltCard } from "@/components/ui/tilt-card";

function Demo() {
  return (
    <div className="flex min-h-screen w-full items-center justify-center overflow-hidden bg-background p-8">
      <TiltCard className="w-[340px] rounded-3xl border bg-card p-7 shadow-2xl">
        <div className="relative z-20">
          <div className="mb-16 flex items-center justify-between">
            <span className="rounded-full bg-foreground px-3 py-1 text-xs font-medium text-background">
              Interactive
            </span>
            <span className="text-sm text-muted-foreground">3D hover</span>
          </div>
          <h3 className="text-3xl font-semibold tracking-tight">Tilt Card</h3>
          <p className="mt-3 text-sm leading-6 text-muted-foreground">
            Move the cursor across the card to bend perspective and reveal the
            spotlight.
          </p>
        </div>
      </TiltCard>
    </div>
  );
}


export default { Demo };

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


## Infinite Bento Pan

**Author:** @Remocn
**URL:** https://21st.dev/@Remocn/components/infinite-bento-pan

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
infinite-bento-pan.tsx
// Full source: https://21st.dev/@Remocn/components/infinite-bento-pan
// Install via: npx @21st-dev/magic add infinite-bento-pan
// Or copy the component code from the 21st.dev page above.

"use client";

import { useMemo } from "react";
import { Player } from "@remotion/player";
import { InfiniteBentoPan } from "@/components/ui/infinite-bento-pan";

export default function InfiniteBentoPanDemo() {
  const props = useMemo(() => ({
    speed: 1,
  }), []);

  return (
    <div className="flex w-full min-h-screen items-center justify-center overflow-hidden bg-background p-6 md:p-10">
      <div className="w-full max-w-[1200px]">
        <Player
          component={InfiniteBentoPan as any}
          inputProps={props}
          durationInFrames={240}
          fps={30}
          compositionWidth={1280}
          compositionHeight={720}
          autoPlay
          loop
          controls={false}
          clickToPlay={false}
          style={{
            width: "100%",
            height: "auto",
            aspectRatio: "16 / 9",
            borderRadius: 24,
            overflow: "hidden",
            background: "#050505",
            boxShadow: "0 40px 120px rgba(0,0,0,0.45)",
          }}
        />
      </div>
    </div>
  );
}

```

Install NPM dependencies:
```bash
motion
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


## Interfaces Hover Card

**Author:** @jshguo
**URL:** https://21st.dev/@jshguo/components/interfaces-hover-card

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
interfaces-hover-card.tsx
// Full source: https://21st.dev/@jshguo/components/interfaces-hover-card
// Install via: npx @21st-dev/magic add interfaces-hover-card
// Or copy the component code from the 21st.dev page above.

import {
  HoverCard,
  HoverCardContent,
  HoverCardTrigger,
} from "@/components/ui/interfaces-hover-card"

function CodeIcon() {
  return (
    <svg
      aria-hidden="true"
      viewBox="0 0 32 32"
      className="size-4"
      fill="currentColor"
    >
      <path d="M31 16 24 23 22.59 21.59 28.17 16 22.59 10.41 24 9 31 16z" />
      <path d="M1 16 8 9 9.41 10.41 3.83 16 9.41 21.59 8 23 1 16z" />
      <path d="M5.91 15H26.080000000000002V17H5.91z" transform="rotate(-75 15.996 16)" />
    </svg>
  )
}

export default function DefaultHoverCardDemo() {
  return (
    <div className="flex min-h-screen w-full items-center justify-center bg-background p-8 overflow-hidden">
      <HoverCard openDelay={0} closeDelay={75}>
        <HoverCardTrigger asChild>
          <button className="text-sm font-medium text-foreground underline underline-offset-4">
            @nextjs
          </button>
        </HoverCardTrigger>
        <HoverCardContent side="bottom" align="start" className="w-80">
          <div className="flex flex-col items-start justify-start gap-2">
            <div className="size-16 overflow-hidden border bg-background">
              <img
                src="https://github.com/vercel.png"
                alt="Next.js"
                className="size-full object-cover"
              />
            </div>
            <div className="flex flex-col">
              <h4 className="flex flex-row items-center gap-1 text-base font-semibold">
                Next.js
                <CodeIcon />
              </h4>
              <p className="text-sm text-muted-foreground">@nextjs</p>
            </div>
            <div className="space-y-2">
              <p className="text-sm">
                The React Framework – created and maintained by @vercel.
              </p>
            </div>
          </div>
        </HoverCardContent>
      </HoverCard>
    </div>
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


## Magnified Bento

**Author:** @0xUrvish
**URL:** https://21st.dev/@0xUrvish/components/magnified-bento

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
magnified-bento.tsx
// Full source: https://21st.dev/@0xUrvish/components/magnified-bento
// Install via: npx @21st-dev/magic add magnified-bento
// Or copy the component code from the 21st.dev page above.

"use client";
import MagnifiedBento from "@/components/ui/magnified-bento";

export default function Demo() {
  return (
    <div className="flex items-center justify-center w-full min-h-screen bg-background p-8">
      <MagnifiedBento />
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


## Bento Card

**Author:** @0xUrvish
**URL:** https://21st.dev/@0xUrvish/components/bento-card

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
bento-card.tsx
// Full source: https://21st.dev/@0xUrvish/components/bento-card
// Install via: npx @21st-dev/magic add bento-card
// Or copy the component code from the 21st.dev page above.

"use client";
import BentoCard from "@/components/ui/bento-card";

export default function Demo() {
  return (
    <div className="flex items-center justify-center w-full min-h-screen bg-background p-8">
      <BentoCard />
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


## Avatar Hover Card

**Author:** @moumensoliman
**URL:** https://21st.dev/@moumensoliman/components/avatar-hover-card

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
avatar-hover-card.tsx
// Full source: https://21st.dev/@moumensoliman/components/avatar-hover-card
// Install via: npx @21st-dev/magic add avatar-hover-card
// Or copy the component code from the 21st.dev page above.

import { Component } from "@/components/ui/avatar-hover-card";
import { Button } from "@/components/ui/button";
import { MessageCircle, UserPlus } from "lucide-react";

export default function DemoOne() {
  return <Component  
  imageSrc="https://github.com/shadcn.png"
        imageAlt="Profile"
        name="shadcn"
        username="shadcn"
        description="Community manager and content creator."
        buttonContent={
          <div className="flex gap-2 w-full">
            <Button size="sm" variant="outline" className="flex-1">
              <MessageCircle className="h-4 w-4 mr-2" />
              Message
            </Button>
            <Button size="sm" className="flex-1">
              <UserPlus className="h-4 w-4 mr-2" />
              Follow
            </Button>
          </div>
        }
  
   />;
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


## Analytics Bento

**Author:** @jatin-yadav05
**URL:** https://21st.dev/@jatin-yadav05/components/analytics-bento

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
analytics-bento.tsx
// Full source: https://21st.dev/@jatin-yadav05/components/analytics-bento
// Install via: npx @21st-dev/magic add analytics-bento
// Or copy the component code from the 21st.dev page above.

import { BudgetCard } from "@/components/ui/analytics-bento"

export default function Page() {
  return (
    <main className="flex min-h-screen items-center justify-center w-full p-8">
      <BudgetCard />
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


## Bento Grid 01

**Author:** @avanishverma4
**URL:** https://21st.dev/@avanishverma4/components/bento-grid-01

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
bento-grid-01.tsx
// Full source: https://21st.dev/@avanishverma4/components/bento-grid-01
// Install via: npx @21st-dev/magic add bento-grid-01
// Or copy the component code from the 21st.dev page above.

import Component from "@/components/ui/bento-grid-01";

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


## Bento Product Features

**Author:** @kavikatiyar
**URL:** https://21st.dev/@kavikatiyar/components/bento-product-features

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
bento-product-features.tsx
// Full source: https://21st.dev/@kavikatiyar/components/bento-product-features
// Install via: npx @21st-dev/magic add bento-product-features
// Or copy the component code from the 21st.dev page above.

import * as React from "react";
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { Switch } from "@/components/ui/switch";
import { BentoGridShowcase } from "@/components/ui/bento-product-features";
import {
  Settings2,
  Command,
  Plus,
} from "lucide-react";

// --- Helper Components for the Demo ---
// These components represent the content for each slot.

const IntegrationCard = () => (
  <Card className="flex h-full flex-col">
    <CardHeader>
      <div className="mb-4 flex h-12 w-12 items-center justify-center rounded-full bg-orange-100 dark:bg-orange-900/50">
        <span className="text-3xl" role="img" aria-label="sparkles">
          ✳️
        </span>
      </div>
      <CardTitle>Zapier Integration</CardTitle>
      <CardDescription>
        Unlock effortless automation. Your gateway to effortless automation
        connect your favourite apps, streamline workflows, and supercharge
        productivity with ease.
      </CardDescription>
    </CardHeader>
    <CardFooter className="mt-auto flex items-center justify-between">
      <Button variant="outline" size="sm">
        <Settings2 className="mr-2 h-4 w-4" />
        Configure
      </Button>
      <Switch
        className="data-[state=checked]:bg-red-500"
        aria-label="Toggle integration"
      />
    </CardFooter>
  </Card>
);

const TrackersCard = () => (
  <Card className="h-full">
    <CardContent className="flex h-full flex-col justify-between p-6">
      <div>
        <CardTitle className="text-base font-medium">
          Trackers Connected
        </CardTitle>
        <CardDescription>03 Active Integrations</CardDescription>
      </div>
      <div className="flex -space-x-2 overflow-hidden">
        <img
          className="inline-block h-8 w-8 rounded-full ring-2 ring-background"
          src="https://images.unsplash.com/photo-1491528323818-fdd1faba62cc?w=100&q=80"
          alt="User 1"
        />
        <img
          className="inline-block h-8 w-8 rounded-full ring-2 ring-background"
          src="https://images.unsplash.com/photo-1550525811-e5869dd03032?w=100&q=80"
          alt="User 2"
        />
        <img
          className="inline-block h-8 w-8 rounded-full ring-2 ring-background"
          src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=100&q=80"
          alt="User 3"
        />
      </div>
    </CardContent>
  </Card>
);

const FocusCard = () => (
  <Card className="h-full">
    <CardContent className="flex h-full flex-col justify-between p-6">
      <div className="flex items-start justify-between">
        <div>
          <CardTitle className="text-base font-medium">Focusing</CardTitle>
          <CardDescription>Productivity Analytics</CardDescription>
        </div>
        <Badge variant="outline" className="border-orange-300 text-orange-600">
          Range Ratio
        </Badge>
      </div>
      <div>
        <span className="text-6xl font-bold">42%</span>
      </div>
      <div className="flex justify-between text-xs text-muted-foreground">
        <span>Maximum of focus</span>
        <span>Monthly Focus</span>
      </div>
    </CardContent>
  </Card>
);

const StatisticCard = () => (
  <Card className="relative h-full w-full overflow-hidden">
    {/* Dotted background */}
    <div
      className="absolute inset-0 opacity-20"
      style={{
        backgroundImage: "radial-gradient(hsl(var(--foreground)) 1px, transparent 1px)",
        backgroundSize: "16px 16px",
      }}
    />
    <CardContent className="relative z-10 flex h-full items-center justify-center p-6">
      <span className="text-8xl font-bold text-foreground/90">10X</span>
    </CardContent>
  </Card>
);

const ProductivityCard = () => (
  <Card className="h-full">
    <CardContent className="flex h-full flex-col justify-end p-6">
      <CardTitle className="text-base font-medium">
        Team's Productivity
      </CardTitle>
      <CardDescription>
        Boost your team's efficiency with our next-gen productivity solutions.
      </CardDescription>
    </CardContent>
  </Card>
);

const ShortcutsCard = () => (
  <Card className="h-full">
    <CardContent className="flex h-full flex-wrap items-center justify-between gap-4 p-6">
      <div>
        <CardTitle className="text-base font-medium">Shortcut Keys</CardTitle>
        <CardDescription>
          Faster easier way to access the features.
        </CardDescription>
      </div>
      <div className="flex items-center gap-2">
        {/* Styled div replacing Kbd */}
        <div className="flex h-7 w-7 items-center justify-center rounded-md border bg-background font-mono text-xs font-medium text-muted-foreground">
          <Command className="h-3 w-3" />
        </div>
        <Plus className="h-3 w-3 text-muted-foreground" />
        {/* Styled div replacing Kbd */}
        <div className="flex h-7 w-7 items-center justify-center rounded-md border bg-background font-mono text-xs font-medium text-muted-foreground">
          M
        </div>
      </div>
    </CardContent>
  </Card>
);

// --- The Default Demo ---
export default function BentoGridShowcaseDemo() {
  return (
    <div className="w-full p-4 md:p-10">
      <div className="mb-8">
        <h1 className="text-center text-4xl font-bold tracking-tight">
          Product Features
        </h1>
        <p className="text-center text-lg text-muted-foreground">
          Organize, prioritize and control track your tasks more
          <br />
          efficiently in our trusted platform
        </p>
      </div>

      <BentoGridShowcase
        integration={<IntegrationCard />}
        trackers={<TrackersCard />}
        statistic={<StatisticCard />}
        focus={<FocusCard />}
        productivity={<ProductivityCard />}
        shortcuts={<ShortcutsCard />}
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


## Bento Grid

**Author:** @lavikatiyar
**URL:** https://21st.dev/@lavikatiyar/components/bento-grid

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
bento-grid.tsx
// Full source: https://21st.dev/@lavikatiyar/components/bento-grid
// Install via: npx @21st-dev/magic add bento-grid
// Or copy the component code from the 21st.dev page above.

import * as React from "react";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar";
import { BentoGridShowcase } from "@/components/ui/bento-grid";
import {
  Calendar,
  HeartPulse,
  Plus,
  Slack,
  Zap,
} from "lucide-react";

// --- Helper Components for the Demo ---
// These components represent the content for each slot.
// I've updated the image URLs to match your new layout.

const IntegrationsCard = () => (
  <Card className="h-full">
    <CardHeader>
      <CardTitle className="text-lg">Integrations</CardTitle>
      <CardDescription>
        Easily integrations of third party apps.
      </CardDescription>
    </CardHeader>
    <CardContent className="flex items-center justify-center gap-4">
      <div className="flex h-12 w-12 items-center justify-center rounded-full bg-muted">
        <Calendar className="h-6 w-6 text-muted-foreground" />
      </div>
      <div className="flex h-12 w-12 items-center justify-center rounded-full bg-muted">
        <Slack className="h-6 w-6 text-muted-foreground" />
      </div>
      <div className="flex h-12 w-12 items-center justify-center rounded-full bg-muted">
        <Zap className="h-6 w-6 text-muted-foreground" />
      </div>
    </CardContent>
  </Card>
);

const FeatureTagsCard = () => (
  <Card className="h-full">
    <CardContent className="flex h-full flex-col justify-center gap-3 p-6">
      <Badge
        variant="outline"
        className="w-fit items-center gap-1.5 border-purple-300 py-1.5 px-3 text-purple-700 dark:border-purple-700 dark:text-purple-300"
      >
        Innovative <Plus className="h-3 w-3" />
      </Badge>
      <Badge
        variant="secondary"
        className="w-fit items-center gap-1.5 bg-purple-100 py-1.5 px-3 text-purple-700 hover:bg-purple-200 dark:bg-purple-900/50 dark:text-purple-300 dark:hover:bg-purple-900/80"
      >
        Revolutionary
      </Badge>
      <Badge
        variant="outline"
        className="w-fit items-center gap-1.5 border-purple-300 py-1.5 px-3 text-purple-700 dark:border-purple-700 dark:text-purple-300"
      >
        Empowering <Plus className="h-3 w-3" />
      </Badge>
    </CardContent>
  </Card>
);

const MainFeatureCard = () => (
  <Card className="relative h-full w-full overflow-hidden">
    <div className="absolute top-6 left-6 z-10 rounded-lg bg-background/50 p-2 backdrop-blur-sm">
      <p className="text-xl font-bold tracking-tighter">Doc Hands.</p>
    </div>
    <img
      src="https://plus.unsplash.com/premium_photo-1705883267055-b4000d390bae?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MzN8fFNtaWxpbmclMjB3b21hbiUyMGluJTIwYSUyMHBpbmslMjBqYWNrZXR8ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&q=60&w=900"
      alt="Smiling woman in a pink traditional dress"
      className="h-full w-full object-cover"
    />
  </Card>
);

const StatCard = () => (
  <Card className="flex h-full flex-col justify-between bg-lime-100/80 p-6 dark:bg-lime-950/80">
    <HeartPulse className="h-8 w-8 text-lime-700 dark:text-lime-300" />
    <div>
      <p className="text-6xl font-bold text-lime-900 dark:text-lime-100">95%</p>
      <p className="text-sm text-lime-800 dark:text-lime-200">
        Clinical and Medical care satisfaction with DocHands Platforms.
      </p>
    </div>
  </Card>
);

const SecondaryFeatureCard = () => (
  <Card className="relative h-full w-full overflow-hidden">
    <img
      src="https://images.unsplash.com/photo-1667133295352-ef4c83620e8e?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mjd8fGRlbnRpc3R8ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&q=60&w=900"
      alt="Close-up of a smiling woman"
      className="h-60 w-full object-cover"
    />
    <div className="absolute inset-0 bg-gradient-to-t from-blue-500/30 via-transparent to-transparent dark:from-blue-900/40" />
    <p className="absolute bottom-6 left-6 z-10 max-w-[80%] text-xl font-bold text-white [text-shadow:_0_1px_4px_rgb(0_0_0_/_30%)]">
      Small changes and big impact on the way!
    </p>
  </Card>
);

const JourneyCard = () => (
  <Card className="relative h-full w-full overflow-hidden p-6">
    <CardTitle className="text-lg">Weekly Journey</CardTitle>
    <CardDescription>
      Workflow and Patient journey mapping within 02-03 Weeks.
    </CardDescription>
    {/* Avatar constellation */}
    <div className="absolute -right-4 -bottom-4 h-48 w-48">
      <div className="absolute top-8 left-20">
        <Avatar>
          <AvatarImage src="https://api.uifaces.co/our-content/faces/49.jpg" />
          <AvatarFallback>A</AvatarFallback>
        </Avatar>
      </div>
      <div className="absolute top-24 left-8">
        <Avatar>
          <AvatarImage src="https://api.uifaces.co/our-content/faces/14.jpg" />
          <AvatarFallback>B</AvatarFallback>
        </Avatar>
      </div>
    </div>
  </Card>
);

// --- The Default Demo ---
export default function BentoGridShowcaseDemo() {
  return (
    <div className="w-full p-4 md:p-10">
      <div className="mb-8">
        <h1 className="text-center text-4xl font-bold tracking-tight">
          Virtual Medical Care
        </h1>
        <p className="text-center text-lg text-muted-foreground">
          Full range of solutions to effectively enhance your virtual care.
        </p>
      </div>

      <BentoGridShowcase
        integrations={<IntegrationsCard />}
        featureTags={<FeatureTagsCard />}
        mainFeature={<MainFeatureCard />}
        secondaryFeature={<SecondaryFeatureCard />}
        statistic={<StatCard />}
        journey={<JourneyCard />}
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


## Cybernetic Bento Grid 1

**Author:** @dhiluxui
**URL:** https://21st.dev/@dhiluxui/components/cybernetic-bento-grid-1

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
cybernetic-bento-grid-1.tsx
// Full source: https://21st.dev/@dhiluxui/components/cybernetic-bento-grid-1
// Install via: npx @21st-dev/magic add cybernetic-bento-grid-1
// Or copy the component code from the 21st.dev page above.

import CyberneticBentoComponent from "@/components/ui/cybernetic-bento-grid-1";

export default function DemoOne() {
  return (
    <main className="relative w-screen min-h-screen bg-black overflow-x-hidden flex items-center justify-center font-mono">
      <CyberneticBentoComponent />
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


## 3D Tilt Card

**Author:** @avanishverma4
**URL:** https://21st.dev/@avanishverma4/components/3d-tilt-card

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
3d-tilt-card.tsx
// Full source: https://21st.dev/@avanishverma4/components/3d-tilt-card
// Install via: npx @21st-dev/magic add 3d-tilt-card
// Or copy the component code from the 21st.dev page above.

import Component from "@/components/ui/3d-tilt-card";

export default function TiltCard() {
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


## Bento Pricing

**Author:** @efferd
**URL:** https://21st.dev/@efferd/components/bento-pricing

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
bento-pricing.tsx
// Full source: https://21st.dev/@efferd/components/bento-pricing
// Install via: npx @21st-dev/magic add bento-pricing
// Or copy the component code from the 21st.dev page above.

import { BentoPricing } from "@/components/ui/bento-pricing";
import { cn } from '@/lib/utils';

export default function DemoOne() {
 return (
		<div className="bg-[radial-gradient(35%_80%_at_50%_0%,--theme(--color-foreground/.1),transparent)] relative flex size-full min-h-screen items-center justify-center">
			{/* Dots */}
			<div
				aria-hidden="true"
				className={cn(
					'absolute inset-0 -z-10 size-full',
					'bg-[radial-gradient(color-mix(in_oklab,--theme(--color-foreground/.2)30%,transparent)_1px,transparent_1px)]',
					'bg-[size:12px_12px]',
				)}
			/>

			<div
				aria-hidden
				className="absolute inset-0 isolate -z-10 opacity-80 contain-strict"
			>
				<div className="bg-[radial-gradient(68.54%_68.72%_at_55.02%_31.46%,--theme(--color-foreground/.06)_0,hsla(0,0%,55%,.02)_50%,--theme(--color-foreground/.01)_80%)] absolute top-0 left-0 h-320 w-140 -translate-y-87.5 -rotate-45 rounded-full" />
				<div className="bg-[radial-gradient(50%_50%_at_50%_50%,--theme(--color-foreground/.04)_0,--theme(--color-foreground/.01)_80%,transparent_100%)] absolute top-0 left-0 h-320 w-60 [translate:5%_-50%] -rotate-45 rounded-full" />
				<div className="bg-[radial-gradient(50%_50%_at_50%_50%,--theme(--color-foreground/.04)_0,--theme(--color-foreground/.01)_80%,transparent_100%)] absolute top-0 left-0 h-320 w-60 -translate-y-87.5 -rotate-45 rounded-full" />
			</div>

			<section className="mx-auto w-full max-w-5xl p-4">
				{/* Heading */}
				<div className="mx-auto mb-10 max-w-2xl text-center">
					<h1 className="text-4xl font-extrabold tracking-tight lg:text-6xl">
						Data-Driven Growth
					</h1>
					<p className="text-muted-foreground mt-4 text-sm md:text-base">
						Are you tired of using outdated tools and insights that hold your
						team back? We built our pricing around modern teams, so you can
						focus on what matters most.
					</p>
				</div>
				<BentoPricing />
			</section>
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


## Feature Card 1

**Author:** @ravikatiyar
**URL:** https://21st.dev/@ravikatiyar/components/feature-card-1

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
feature-card-1.tsx
// Full source: https://21st.dev/@ravikatiyar/components/feature-card-1
// Install via: npx @21st-dev/magic add feature-card-1
// Or copy the component code from the 21st.dev page above.

import { AnimatedFeatureCard } from "@/components/ui/feature-card-1";

// Data for the feature cards
const features = [
  {
    index: "001",
    tag: "HEALTHIFY",
    title: "Eat better to boost your gut health by 30s.",
    imageSrc: "https://www.thiings.co/_next/image?url=https%3A%2F%2Flftz25oez4aqbxpq.public.blob.vercel-storage.com%2Fimage-79XLKwCuOZGHdVcOlEApISx6x2nVd2.png&w=1000&q=75", // Replace with your image URL
    color: "orange" as const,
  },
  {
    index: "002",
    tag: "DETANE",
    title: "Avoid Chemicals to have a longer lifespan.",
    imageSrc: "https://www.thiings.co/_next/image?url=https%3A%2F%2Flftz25oez4aqbxpq.public.blob.vercel-storage.com%2Fimage-DtOMYxIaV2eptIhXTkorEzdNzhlgXK.png&w=1000&q=75", // Replace with your image URL
    color: "purple" as const,
  },
  {
    index: "003",
    tag: "MEDITATE",
    title: "Quick Calm Sessions that unlock your potential.",
    imageSrc: "https://www.thiings.co/_next/image?url=https%3A%2F%2Flftz25oez4aqbxpq.public.blob.vercel-storage.com%2Fimage-eDCSln4vQRsBBiP3mWirJOXYDyFO6q.png&w=1000&q=75", // Replace with your image URL
    color: "blue" as const,
  },
];

export default function FeatureCardDemo() {
  return (
    <div className="flex min-h-screen w-full items-center justify-center bg-background">
      <div className="container mx-auto grid max-w-5xl grid-cols-1 gap-8 p-4 md:grid-cols-2 lg:grid-cols-3">
        {features.map((feature) => (
          <AnimatedFeatureCard
            key={feature.index}
            index={feature.index}
            tag={feature.tag}
            title={feature.title}
            imageSrc={feature.imageSrc}
            color={feature.color}
          />
        ))}
      </div>
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


## Animated Feature Card

**Author:** @ravikatiyar
**URL:** https://21st.dev/@ravikatiyar/components/animated-feature-card

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
animated-feature-card.tsx
// Full source: https://21st.dev/@ravikatiyar/components/animated-feature-card
// Install via: npx @21st-dev/magic add animated-feature-card
// Or copy the component code from the 21st.dev page above.

import React from 'react';
import { AnimatedFeatureCard } from '@/components/ui/animated-feature-card'; // Adjust the import path

/**
 * A demo component to showcase the AnimatedFeatureCard.
 */
const FeatureCardDemo = () => {
  return (
    <div className="flex min-h-[500px] w-full items-center justify-center bg-background p-4">
      <AnimatedFeatureCard
        title="Generate a skeuomorphic isomorphic 3D icon of a modern coffee maker."
        description="Icons can be easily generated using AI. This lowers the barrier of entry."
        // A placeholder image that matches the style. Replace with your actual image URL.
        imageSrc="https://www.thiings.co/_next/image?url=https%3A%2F%2Flftz25oez4aqbxpq.public.blob.vercel-storage.com%2Fimage-u1weJfn0wFuPr9VJ0wUijZy2DVdtph.png&w=320&q=75"
        featureNumber="05"
        handle="@ravikatiyar"
      />
    </div>
  );
};

export default FeatureCardDemo;
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


## Feature Card

**Author:** @lavikatiyar
**URL:** https://21st.dev/@lavikatiyar/components/feature-card

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
feature-card.tsx
// Full source: https://21st.dev/@lavikatiyar/components/feature-card
// Install via: npx @21st-dev/magic add feature-card
// Or copy the component code from the 21st.dev page above.

import React from 'react';
import { motion } from 'framer-motion';
import { FeatureCard } from '@/components/ui/feature-card'; // Adjust the import path as needed

// Data for the feature cards
const features = [
  {
    icon: (
      <img 
        src="https://www.thiings.co/_next/image?url=https%3A%2F%2Flftz25oez4aqbxpq.public.blob.vercel-storage.com%2Fimage-XimLfa9nmGlBpUT8xFkxuwQFz2hhXO.png&w=320&q=75" 
        alt="Experience Icon" 
        className="h-12 w-12"
      />
    ),
    title: "Help us to Improve",
    description: "In order to provide a better service we would like to collect your data for research purposes, you can decline it anytime!",
  },
  {
    icon: (
       <img 
        src="https://www.thiings.co/_next/image?url=https%3A%2F%2Flftz25oez4aqbxpq.public.blob.vercel-storage.com%2Fimage-CK4odMSKWdmIj0ueBtNq9HOZR6Fbgv.png&w=320&q=75" 
        alt="Notification Icon" 
        className="h-12 w-12"
      />
    ),
    title: "Get Notified",
    description: "Enhance your user experience by ensuring a seamless flow through the activation of notifications.",
  },
  {
    icon: (
       <img 
        src="https://www.thiings.co/_next/image?url=https%3A%2F%2Flftz25oez4aqbxpq.public.blob.vercel-storage.com%2Fimage-JgVvskF7j2zQ9LmIWmnCHHInmpJcTJ.png&w=320&q=75" 
        alt="Location Icon" 
        className="h-12 w-12"
      />
    ),
    title: "Allow Location Access",
    description: "Your company needs it and Personalised recommendations of service providers.",
  },
];

// Animation variants for the container and items
const containerVariants = {
  hidden: { opacity: 0 },
  visible: {
    opacity: 1,
    transition: {
      staggerChildren: 0.2,
    },
  },
};

const itemVariants = {
  hidden: { y: 20, opacity: 0 },
  visible: {
    y: 0,
    opacity: 1,
    transition: {
      duration: 0.5,
      // CORRECTED: Replaced the invalid cubic-bezier array with a standard easing function.
      ease: "easeOut", 
    },
  },
};

/**
 * A demo component to display a grid of animated FeatureCards.
 */
const FeatureCardDemo = () => {
  return (
    <div className="w-full bg-background text-foreground p-8 md:p-12">
      <motion.div
        className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 max-w-6xl mx-auto"
        initial="hidden"
        animate="visible"
        variants={containerVariants}
      >
        {features.map((feature, index) => (
          <motion.div key={index} variants={itemVariants}>
            <FeatureCard
              icon={feature.icon}
              title={feature.title}
              description={feature.description}
            />
          </motion.div>
        ))}
      </motion.div>
    </div>
  );
};

export default FeatureCardDemo;
```

Install NPM dependencies:
```bash
framer-motion, motion
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


## Product Feature Card

**Author:** @kavikatiyar
**URL:** https://21st.dev/@kavikatiyar/components/product-feature-card

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
product-feature-card.tsx
// Full source: https://21st.dev/@kavikatiyar/components/product-feature-card
// Install via: npx @21st-dev/magic add product-feature-card
// Or copy the component code from the 21st.dev page above.

// demo.tsx

import { ProductFeatureCard } from "@/components/ui/product-feature-card";

export default function ProductFeatureCardDemo() {
  return (
    <div className="flex min-h-[500px] w-full items-center justify-center bg-background p-4">
      <ProductFeatureCard
        title="Personalized weight care,"
        description="lasting results by certified doctors."
        linkText="Take the quiz"
        linkHref="#"
        // Replace with your actual image source
        imageUrl="https://www.thiings.co/_next/image?url=https%3A%2F%2Flftz25oez4aqbxpq.public.blob.vercel-storage.com%2Fimage-0QlbZHclWAdizaFGxn2Nv3ECg3zLG7.png&w=320&q=75"
        imageAlt="Measured product box and vial"
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


## Feature Card

**Author:** @ravikatiyar
**URL:** https://21st.dev/@ravikatiyar/components/feature-card

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
feature-card.tsx
// Full source: https://21st.dev/@ravikatiyar/components/feature-card
// Install via: npx @21st-dev/magic add feature-card
// Or copy the component code from the 21st.dev page above.

// demo.tsx

import React from "react";
import { FeatureCard } from "@/components/ui/feature-card"; // Adjust the import path

// Helper component for the demo: Progress Item
const SavingsPlanItem = ({
  icon,
  title,
  members,
  progress,
  amount,
  target,
  daysLeft,
}: {
  icon: string;
  title: string;
  members: number;
  progress: number;
  amount: number;
  target: number;
  daysLeft?: number;
}) => (
  <div className="mb-4 flex items-center gap-4 last:mb-0">
    <div className="flex h-12 w-12 items-center justify-center rounded-full bg-muted">
      {/* In a real app, you'd use an Image component */}
      <img src={icon} alt={title} className="h-6 w-6" />
    </div>
    <div className="flex-1">
      <div className="flex justify-between">
        <p className="font-medium text-card-foreground">{title}</p>
        <p className="text-sm font-semibold text-card-foreground">{progress}%</p>
      </div>
      <div className="mt-1 h-2 w-full overflow-hidden rounded-full bg-muted">
        <div
          className="h-full bg-primary"
          style={{ width: `${progress}%` }}
        />
      </div>
      <div className="mt-1 flex justify-between text-xs text-muted-foreground">
        <span>${amount.toLocaleString()} of ${target.toLocaleString()}</span>
        {daysLeft && <span>{daysLeft} days left</span>}
        <span>{members} members</span>
      </div>
    </div>
  </div>
);

// The main demo component
const FeatureCardDemo = () => {
  return (
    <div className="w-full max-w-4xl p-4 md:p-8">
      <FeatureCard
        title="Multiple Savings Plan"
        description="Nest offers a variety of savings plans, from Flexible to Target Savings, to make sure you can save for what matters most, your way."
      >
        <div className="flex flex-col space-y-4">
          <SavingsPlanItem
            icon="https://www.thiings.co/_next/image?url=https%3A%2F%2Flftz25oez4aqbxpq.public.blob.vercel-storage.com%2Fimage-YimA3sxsT00vWqiUyzyLUshxsSZvll.png&w=320&q=75"
            title="Birthday"
            progress={63}
            amount={25200}
            target={40200}
            members={200}
          />
          <SavingsPlanItem
            icon="https://www.thiings.co/_next/image?url=https%3A%2F%2Flftz25oez4aqbxpq.public.blob.vercel-storage.com%2Fimage-iZKfmUSHuQtDn1W2NBIwoLZ0epsnzZ.png&w=320&q=75"
            title="Graduation"
            progress={63}
            amount={3500}
            target={45000}
            members={200}
          />
          <SavingsPlanItem
            icon="https://www.thiings.co/_next/image?url=https%3A%2F%2Flftz25oez4aqbxpq.public.blob.vercel-storage.com%2Fimage-CYiGxD8xsd3dQiAxNDGC5vDunvHJ4P.png&w=320&q=75"
            title="NYSC"
            progress={86}
            amount={38000}
            target={42000}
            members={200}
            daysLeft={28}
          />
        </div>
      </FeatureCard>
    </div>
  );
};

export default FeatureCardDemo;
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


## Glass Cards

**Author:** @kedhar
**URL:** https://21st.dev/@kedhar/components/glass-cards

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
glass-cards.tsx
// Full source: https://21st.dev/@kedhar/components/glass-cards
// Install via: npx @21st-dev/magic add glass-cards
// Or copy the component code from the 21st.dev page above.

import React from 'react';
import { StackedCards } from '../components/ui/glass-cards';
import '../index.css';

// Demo component showcasing the stacked cards with different configurations
export const DefaultDemo: React.FC = () => {
  return (
    <div style={{ 
      minHeight: '100vh',
      background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)'
    }}>
      <StackedCards />
    </div>
  );
};

// Alternative demo with different styling
export const AlternativeDemo: React.FC = () => {
  return (
    <div style={{ 
      minHeight: '100vh',
      background: 'linear-gradient(135deg, #ff9a9e 0%, #fecfef 50%, #fecfef 100%)'
    }}>
      <div style={{ padding: '2rem' }}>
        <h1 style={{ 
          textAlign: 'center', 
          color: 'white', 
          marginBottom: '2rem',
          fontSize: '2.5rem',
          textShadow: '0 4px 8px rgba(0, 0, 0, 0.3)'
        }}>
          Alternative Style Demo
        </h1>
        <StackedCards />
      </div>
    </div>
  );
};

export default DefaultDemo;
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


## Scrapbook Bento Grid

**Author:** @dhiluxui
**URL:** https://21st.dev/@dhiluxui/components/scrapbook-bento-grid

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
scrapbook-bento-grid.tsx
// Full source: https://21st.dev/@dhiluxui/components/scrapbook-bento-grid
// Install via: npx @21st-dev/magic add scrapbook-bento-grid
// Or copy the component code from the 21st.dev page above.

import BentoItem from "@/components/ui/scrapbook-bento-grid";

export default function DemoOne() {
    return (
            <div className="scrapbook-container scrapbook-scope">
                <div className="w-full max-w-6xl z-10 flex flex-col items-center">
                    <h1 className="scrapbook-title mb-12">Bits & Pieces</h1>

                    <div className="bento-grid">
                        <BentoItem className="item-1" rotation="-2deg">
                            <h2>Goals & Ideas</h2>
                            <ul>
                                <li>- Start a garden</li>
                                <li>- Learn to bake bread</li>
                                <li>- Plan a road trip</li>
                            </ul>
                        </BentoItem>
                        <BentoItem className="item-2" rotation="3deg">
                            <h2>Quote</h2>
                            <p>"Creativity is intelligence having fun."</p>
                        </BentoItem>
                        <BentoItem className="item-3" rotation="-1deg">
                            <h2>To-Do</h2>
                            <p>Finish reading that book!</p>
                        </BentoItem>
                        <BentoItem className="item-4" rotation="2deg">
                           <div className="w-full h-full bg-gray-300 border-4 border-gray-200 flex items-center justify-center text-gray-500 font-sans">[ Photo Placeholder ]</div>
                           <p className="absolute bottom-4 left-0 right-0 text-center">Summer '24</p>
                        </BentoItem>
                        <BentoItem className="item-5" rotation="1deg">
                            <h2>Favorite Recipe</h2>
                            <p>Lemon pasta: garlic, chili flakes, olive oil, parsley, and lots of lemon juice.</p>
                        </BentoItem>
                         <BentoItem className="item-6" rotation="-3deg">
                            <h2>Doodles</h2>
                            <p>Just some little sketches and thoughts here.</p>
                        </BentoItem>
                    </div>
                </div>
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


## Blueprint Bento Grid

**Author:** @dhiluxui
**URL:** https://21st.dev/@dhiluxui/components/blueprint-bento-grid

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
blueprint-bento-grid.tsx
// Full source: https://21st.dev/@dhiluxui/components/blueprint-bento-grid
// Install via: npx @21st-dev/magic add blueprint-bento-grid
// Or copy the component code from the 21st.dev page above.

import BentoItem from "@/components/ui/blueprint-bento-grid";

export default function DemoOne() {
  return (
                <div className="blueprint-container blueprint-theme-scope">
                <div className="w-full max-w-6xl z-10">
                    <h1 className="blueprint-title text-5xl font-bold text-center mb-10">SYSTEM SCHEMATICS</h1>

                    <div className="bento-grid">
                        <BentoItem className="col-span-3 row-span-2">
                            <h2 className="text-3xl font-bold mb-2">[ CORE PROCESSOR ]</h2>
                            <p>Status: Nominal</p>
                            <p>Temperature: 34°C</p>
                            <p>Load: 15%</p>
                        </BentoItem>

                        <BentoItem className="col-span-2">
                            <h2 className="text-2xl font-bold mb-2">[ ENERGY LEVELS ]</h2>
                            <p>Main Core: 98%</p>
                            <p>Auxiliary: 100%</p>
                        </BentoItem>
                        
                        <BentoItem className="col-span-2">
                            <h2 className="text-2xl font-bold mb-2">[ NETWORK NODES ]</h2>
                            <p>Active Connections: 1,284</p>
                            <p>Data Rate: 40 Gb/s</p>
                        </BentoItem>
                        
                        <BentoItem className="col-span-5 full-span-tablet">
                             <h2 className="text-2xl font-bold mb-2">[ DIAGNOSTICS LOG ]</h2>
                             <p>{'>'} All systems responding.</p>
                             <p>{'>'} Quantum entanglement stable.</p>
                             <p>{'>'} No anomalies detected.</p>
                        </BentoItem>
                    </div>
                </div>
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


## Brutalist Bento Grid

**Author:** @dhiluxui
**URL:** https://21st.dev/@dhiluxui/components/brutalist-bento-grid

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
brutalist-bento-grid.tsx
// Full source: https://21st.dev/@dhiluxui/components/brutalist-bento-grid
// Install via: npx @21st-dev/magic add brutalist-bento-grid
// Or copy the component code from the 21st.dev page above.

import BentoItem from "@/components/ui/brutalist-bento-grid";

export default function DemoOne() {
    return (
            <div className="brutalist-container brutalist-scope">
                <div className="w-full max-w-6xl z-10 flex flex-col items-center">
                    <h1 className="brutalist-title text-4xl sm:text-5xl text-center mb-12">Foundation Blocks</h1>

                    <div className="bento-grid">
                        <BentoItem className="item-1">
                            <h2>Core Module</h2>
                            <p>The central processing unit. All logic originates here.</p>
                        </BentoItem>
                        <BentoItem className="item-2">
                            <h2>Primary Structure</h2>
                            <p>Load-bearing framework and architectural integrity.</p>
                        </BentoItem>
                        <BentoItem className="item-3">
                            <h2>Input</h2>
                            <p>Data ingress.</p>
                        </BentoItem>
                        <BentoItem className="item-4">
                            <h2>Output</h2>
                            <p>Data egress.</p>
                        </BentoItem>
                        <BentoItem className="item-5">
                            <h2>Sub-System Support</h2>
                            <p>Auxiliary services and operational support infrastructure.</p>
                        </BentoItem>
                    </div>
                </div>
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

