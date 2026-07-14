# 21st.dev — Cards — Bento / Tilt / Feature / Glass — Full Integration Prompts

25 components sorted by popularity.
Each section is a copy-paste ready prompt for Claude or any AI coding tool.

---

## Bento Product Features

**Author:** @kavikatiyar | **Used:** 350x
**URL:** https://21st.dev/@kavikatiyar/components/bento-product-features
**Install:** `npx shadcn@latest add "https://21st.dev/r/kavikatiyar/bento-product-features?api_key=$API_KEY_21ST"`

```
You are given a task to integrate an existing React component in the codebase

The codebase should support:
- shadcn project structure
- Tailwind CSS
- Typescript

Determine the default path for components and styles.
If default path for components is not /components/ui, provide instructions on why it's important to create this folder

Copy-paste this component to /components/ui folder:
```tsx
bento-product-features.tsx
// Full source available at: https://21st.dev/@kavikatiyar/components/bento-product-features
// Or install via: npx shadcn@latest add "https://21st.dev/r/kavikatiyar/bento-product-features?api_key=$API_KEY_21ST"

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

Extend existing Tailwind 4 index.css with this code:
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


## Cybernetic Bento Grid

**Author:** @dhileepkumargm | **Used:** 339x
**URL:** https://21st.dev/@dhileepkumargm/components/cybernetic-bento-grid
**Install:** `npx shadcn@latest add "https://21st.dev/r/dhileepkumargm/cybernetic-bento-grid?api_key=$API_KEY_21ST"`
**Description:** This is a modern and highly popular layout style for showcasing features, portfolio items, or key information. I've designed this one with a futuristic, cyberpunk aesthetic, featuring glowing borders that animate on hover, a subtle background grid, and a clean, dark theme.

```
You are given a task to integrate an existing React component in the codebase

The codebase should support:
- shadcn project structure
- Tailwind CSS
- Typescript

Determine the default path for components and styles.
If default path for components is not /components/ui, provide instructions on why it's important to create this folder

Copy-paste this component to /components/ui folder:
```tsx
cybernetic-bento-grid.tsx
// Full source available at: https://21st.dev/@dhileepkumargm/components/cybernetic-bento-grid
// Or install via: npx shadcn@latest add "https://21st.dev/r/dhileepkumargm/cybernetic-bento-grid?api_key=$API_KEY_21ST"

import { CyberneticBentoGrid } from "@/components/ui/cybernetic-bento-grid";

export default function DemoOne() {
  return  <div className="App">
      <CyberneticBentoGrid />
    </div>
}

```

Install NPM dependencies:
```bash
none
```

Extend existing Tailwind 4 index.css with this code:
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


## Ruixen Bento Cards

**Author:** @ruixen.ui | **Used:** 270x
**URL:** https://21st.dev/@ruixen.ui/components/ruixen-bento-cards
**Install:** `npx shadcn@latest add "https://21st.dev/r/ruixen.ui/ruixen-bento-cards?api_key=$API_KEY_21ST"`
**Description:** 

Ruixen UI is built to make your job easier. These bento cards highlight what really matters when you're building modern UIs: beautiful components, smart layouts, performance, and flexibility. Whether you're working solo or with a team, Ruixen gives you a solid foundation that just works — clean code, great defaults, and the kind of polish that makes your product feel professional out of the box.

```
You are given a task to integrate an existing React component in the codebase

The codebase should support:
- shadcn project structure
- Tailwind CSS
- Typescript

Determine the default path for components and styles.
If default path for components is not /components/ui, provide instructions on why it's important to create this folder

Copy-paste this component to /components/ui folder:
```tsx
ruixen-bento-cards.tsx
// Full source available at: https://21st.dev/@ruixen.ui/components/ruixen-bento-cards
// Or install via: npx shadcn@latest add "https://21st.dev/r/ruixen.ui/ruixen-bento-cards?api_key=$API_KEY_21ST"

import RuixenBentoCards from "@/components/ui/ruixen-bento-cards";

export default function DemoOne() {
  return <RuixenBentoCards />;
}

```

Install NPM dependencies:
```bash
none
```

Extend existing Tailwind 4 index.css with this code:
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


## Shuffle Grid

**Author:** @vaib215 | **Used:** 263x
**URL:** https://21st.dev/@vaib215/components/shuffle-grid
**Install:** `npx shadcn@latest add "https://21st.dev/r/vaib215/shuffle-grid?api_key=$API_KEY_21ST"`
**Description:** An eye-catching presentation element which you can use to showcase your clients, users, features or whatever you like.

```
You are given a task to integrate an existing React component in the codebase

The codebase should support:
- shadcn project structure
- Tailwind CSS
- Typescript

Determine the default path for components and styles.
If default path for components is not /components/ui, provide instructions on why it's important to create this folder

Copy-paste this component to /components/ui folder:
```tsx
shuffle-grid.tsx
// Full source available at: https://21st.dev/@vaib215/components/shuffle-grid
// Or install via: npx shadcn@latest add "https://21st.dev/r/vaib215/shuffle-grid?api_key=$API_KEY_21ST"

import { ShuffleHero } from "@/components/ui/shuffle-grid";

const ShuffleHeroDemo = () => {
  return (
    <div className="flex w-full h-screen justify-center items-center">
      <ShuffleHero />
    </div>
  );
};

export { ShuffleHeroDemo };

```

Install NPM dependencies:
```bash
none
```

Extend existing Tailwind 4 index.css with this code:
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


## bento grid 01

**Author:** @avanishverma4 | **Used:** 247x
**URL:** https://21st.dev/@avanishverma4/components/bento-grid-01
**Install:** `npx shadcn@latest add "https://21st.dev/r/avanishverma4/bento-grid-01?api_key=$API_KEY_21ST"`
**Description:** A reusable and responsive bento grid layout with animation

```
You are given a task to integrate an existing React component in the codebase

The codebase should support:
- shadcn project structure
- Tailwind CSS
- Typescript

Determine the default path for components and styles.
If default path for components is not /components/ui, provide instructions on why it's important to create this folder

Copy-paste this component to /components/ui folder:
```tsx
bento-grid-01.tsx
// Full source available at: https://21st.dev/@avanishverma4/components/bento-grid-01
// Or install via: npx shadcn@latest add "https://21st.dev/r/avanishverma4/bento-grid-01?api_key=$API_KEY_21ST"

import Component from "@/components/ui/bento-grid-01";

export default function DemoOne() {
  return <Component />;
}

```

Install NPM dependencies:
```bash
none
```

Extend existing Tailwind 4 index.css with this code:
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


## Bento Gallery

**Author:** @ravikatiyar162 | **Used:** 227x
**URL:** https://21st.dev/@ravikatiyar162/components/bento-gallery
**Install:** `npx shadcn@latest add "https://21st.dev/r/ravikatiyar162/bento-gallery?api_key=$API_KEY_21ST"`
**Description:** Interactive Image Bento Gallery
Description: A responsive, horizontally draggable bento-style gallery designed exclusively for images. It features smooth animations powered by Framer Motion, a clean shadcn/ui aesthetic, and an elegant full-screen modal for viewing individual images.

```
You are given a task to integrate an existing React component in the codebase

The codebase should support:
- shadcn project structure
- Tailwind CSS
- Typescript

Determine the default path for components and styles.
If default path for components is not /components/ui, provide instructions on why it's important to create this folder

Copy-paste this component to /components/ui folder:
```tsx
bento-gallery.tsx
// Full source available at: https://21st.dev/@ravikatiyar162/components/bento-gallery
// Or install via: npx shadcn@latest add "https://21st.dev/r/ravikatiyar162/bento-gallery?api_key=$API_KEY_21ST"

import InteractiveImageBentoGallery from "@/components/ui/bento-gallery"

// Sample data for the image gallery
const imageItems = [
  {
    id: 1,
    title: "Mountain Vista",
    desc: "Serenity above the clouds.",
    url: "https://images.unsplash.com/photo-1486870591958-9b9d0d1dda99?w=800&q=80",
    span: "md:col-span-2 md:row-span-2",
  },
  {
    id: 2,
    title: "Coastal Arch",
    desc: "Where the land meets the sea.",
    url: "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=800&q=80",
    span: "md:row-span-1",
  },
  {
    id: 3,
    title: "Forest Canopy",
    desc: "Sunlight filtering through leaves.",
    url: "https://images.unsplash.com/photo-1441974231531-c6227db76b6e?w=800&q=80",
    span: "md:row-span-1",
  },
  {
    id: 4,
    title: "Desert Dunes",
    desc: "Golden sands under the sun.",
    url: "https://images.unsplash.com/photo-1473580044384-7ba9967e16a0?w=800&q=80",
    span: "md:row-span-2",
  },
  {
    id: 5,
    title: "City at Night",
    desc: "A vibrant urban landscape.",
    url: "https://images.unsplash.com/photo-1506606401543-2e73709cebb4?w=900&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8Q2l0eSUyMGF0JTIwTmlnaHR8ZW58MHx8MHx8fDA%3D?w=800&q=80",
    span: "md:row-span-1",
  },
  {
    id: 6,
    title: "Misty Lake",
    desc: "Morning fog over calm waters.",
    url: "https://images.unsplash.com/photo-1634023233766-0c16b151bfb0?w=900&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8TWlzdHklMjBMYWtlfGVufDB8fDB8fHww?w=800&q=80",
    span: "md:col-span-2 md:row-span-1",
  },
]

export default function InteractiveImageBentoGalleryDemo() {
  return (
    <div className="w-full antialiased">
      <InteractiveImageBentoGallery
        imageItems={imageItems}
        title="Curated Moments"
        description="A collection of stunning landscapes. Drag to explore, click to expand."
      />
    </div>
  )
}
```

Install NPM dependencies:
```bash
none
```

Extend existing Tailwind 4 index.css with this code:
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

**Author:** @sshahaider | **Used:** 216x
**URL:** https://21st.dev/@sshahaider/components/bento-pricing
**Install:** `npx shadcn@latest add "https://21st.dev/r/sshahaider/bento-pricing?api_key=$API_KEY_21ST"`
**Description:** A clean and responsive pricing table with a bento-style layout, feature checklists, and call-to-action buttons. Ideal for SaaS apps, startups, and subscription websites, it makes plan comparison simple and visually engaging.

```
You are given a task to integrate an existing React component in the codebase

The codebase should support:
- shadcn project structure
- Tailwind CSS
- Typescript

Determine the default path for components and styles.
If default path for components is not /components/ui, provide instructions on why it's important to create this folder

Copy-paste this component to /components/ui folder:
```tsx
bento-pricing.tsx
// Full source available at: https://21st.dev/@sshahaider/components/bento-pricing
// Or install via: npx shadcn@latest add "https://21st.dev/r/sshahaider/bento-pricing?api_key=$API_KEY_21ST"

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

Extend existing Tailwind 4 index.css with this code:
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


## infinite grid integration

**Author:** @avanishverma4 | **Used:** 208x
**URL:** https://21st.dev/@avanishverma4/components/infinite-grid-integration
**Install:** `npx shadcn@latest add "https://21st.dev/r/avanishverma4/infinite-grid-integration?api_key=$API_KEY_21ST"`
**Description:** A reusable component for grid integration animation.

```
You are given a task to integrate an existing React component in the codebase

The codebase should support:
- shadcn project structure
- Tailwind CSS
- Typescript

Determine the default path for components and styles.
If default path for components is not /components/ui, provide instructions on why it's important to create this folder

Copy-paste this component to /components/ui folder:
```tsx
infinite-grid-integration.tsx
// Full source available at: https://21st.dev/@avanishverma4/components/infinite-grid-integration
// Or install via: npx shadcn@latest add "https://21st.dev/r/avanishverma4/infinite-grid-integration?api_key=$API_KEY_21ST"

import Component from "@/components/ui/infinite-grid-integration";

export default function DemoOne() {
  return <Component />;
}

```

Install NPM dependencies:
```bash
none
```

Extend existing Tailwind 4 index.css with this code:
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


## Background snippets

**Author:** @bg.ibelick | **Used:** 191x
**URL:** https://21st.dev/@bg.ibelick/components/background-snippets
**Install:** `npx shadcn@latest add "https://21st.dev/r/bg.ibelick/background-snippets?api_key=$API_KEY_21ST"`
**Description:** Here is Background snippets component

```
You are given a task to integrate an existing React component in the codebase

The codebase should support:
- shadcn project structure
- Tailwind CSS
- Typescript

Determine the default path for components and styles.
If default path for components is not /components/ui, provide instructions on why it's important to create this folder

Copy-paste this component to /components/ui folder:
```tsx
background-snippets.tsx
// Full source available at: https://21st.dev/@bg.ibelick/components/background-snippets
// Or install via: npx shadcn@latest add "https://21st.dev/r/bg.ibelick/background-snippets?api_key=$API_KEY_21ST"

import { Component } from "@/components/ui/background-snippets";

export default function Demo() {
  return <Component />;
}

```

Install NPM dependencies:
```bash
none
```

Extend existing Tailwind 4 index.css with this code:
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

**Author:** @shadcnblockscom | **Used:** 152x
**URL:** https://21st.dev/@shadcnblockscom/components/casestudy-5
**Install:** `npx shadcn@latest add "https://21st.dev/r/shadcnblockscom/casestudy-5?api_key=$API_KEY_21ST"`
**Description:** A bento grid of cards with a feature card and smaller cards below. Minimal design and dotted backgrounds.

```
You are given a task to integrate an existing React component in the codebase

The codebase should support:
- shadcn project structure
- Tailwind CSS
- Typescript

Determine the default path for components and styles.
If default path for components is not /components/ui, provide instructions on why it's important to create this folder

Copy-paste this component to /components/ui folder:
```tsx
casestudy-5.tsx
// Full source available at: https://21st.dev/@shadcnblockscom/components/casestudy-5
// Or install via: npx shadcn@latest add "https://21st.dev/r/shadcnblockscom/casestudy-5?api_key=$API_KEY_21ST"

import { Casestudy5 } from "@/components/ui/casestudy-5";

const DemoOne = () => {
  return (
    <Casestudy5 featuredCasestudy={{
      logo: "https://shadcnblocks.com/images/block/block-1.svg",
      company: "Acme",
      tags: "ARTIFICIAL INTELLIGENCE / ENTERPRISE SOLUTIONS",
      title: "Workflow Automation for the Digital Age.",
      subtitle: "How to automate your workflow with AI.",
      image: "https://shadcnblocks.com/images/block/placeholder-1.svg",
      link: "https://shadcnblocks.com",
    }}
    casestudies={[
      {
        logo: "https://shadcnblocks.com/images/block/block-2.svg",
        company: "Super",
        tags: "DATA MIGRATION / SOFTWARE SOLUTIONS",
        title: "Enhance data migration with AI.",
        subtitle: "A data migration platform toward a data-driven future.",
        image: "",
        link: "https://shadcnblocks.com",
      },
      {
        logo: "https://shadcnblocks.com/images/block/block-3.svg",
        company: "Advent",
        tags: "ARTIFICIAL INTELLIGENCE / DATA SOLUTIONS",
        title: "Strategic AI for a future-proof business.",
        subtitle: "Mastering AI for more efficient operations.",
        image: "",
        link: "https://shadcnblocks.com",
      },
    ]}
     />
  );
};

export { DemoOne };

```

Install NPM dependencies:
```bash
none
```

Extend existing Tailwind 4 index.css with this code:
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


## Data Grid Table

**Author:** @sean0205 | **Used:** 125x
**URL:** https://21st.dev/@sean0205/components/data-grid-table
**Install:** `npx shadcn@latest add "https://21st.dev/r/sean0205/data-grid-table?api_key=$API_KEY_21ST"`
**Description:** Here is Data Grid Table component

```
You are given a task to integrate an existing React component in the codebase

The codebase should support:
- shadcn project structure
- Tailwind CSS
- Typescript

Determine the default path for components and styles.
If default path for components is not /components/ui, provide instructions on why it's important to create this folder

Copy-paste this component to /components/ui folder:
```tsx
data-grid-table.tsx
// Full source available at: https://21st.dev/@sean0205/components/data-grid-table
// Or install via: npx shadcn@latest add "https://21st.dev/r/sean0205/data-grid-table?api_key=$API_KEY_21ST"

import { useMemo, useState } from 'react';
import Link from 'next/link';
import { DataGrid, DataGridContainer } from '@/components/ui/data-grid-table';
import { DataGridPagination } from '@/components/ui/data-grid-table';
import { DataGridTable } from '@/components/ui/data-grid-table';
import { ScrollArea, ScrollBar } from '@/components/ui/scroll-area';
import {
  ColumnDef,
  getCoreRowModel,
  getFilteredRowModel,
  getPaginationRowModel,
  getSortedRowModel,
  PaginationState,
  SortingState,
  useReactTable,
} from '@tanstack/react-table';

interface IData {
  id: string;
  name: string;
  availability: 'online' | 'away' | 'busy' | 'offline';
  avatar: string;
  status: 'active' | 'inactive';
  flag: string; // Emoji flags
  email: string;
  company: string;
  role: string;
  joined: string;
  location: string;
  balance: number;
}

const demoData: IData[] = [
  {
    id: '1',
    name: 'Kathryn Campbell',
    email: 'kathryn@apple.com',
    location: 'San Francisco, USA',
    balance: 5143.03,
  },
  {
    id: '2',
    name: 'Robert Smith',
    email: 'robert@openai.com',
    location: 'London, UK',
    balance: 4321.87,
  },
  {
    id: '3',
    name: 'Sophia Johnson',
    email: 'sophia@meta.com',
    location: 'Toronto, Canada',
    balance: 7654.98,
  },
  {
    id: '4',
    name: 'Lucas Walker',
    email: 'lucas@tesla.com',
    location: 'Sydney, Australia',
    balance: 3456.45,
  },
  {
    id: '5',
    name: 'Emily Davis',
    email: 'emily@sap.com',
    location: 'Berlin, Germany',
    balance: 9876.54,
  },
  {
    id: '6',
    name: 'James Lee',
    email: 'james@keenthemes.com',
    location: 'Kuala Lumpur, MY',
    balance: 6214.22,
  },
  {
    id: '7',
    name: 'Isabella Martinez',
    email: 'isabella@bbva.es',
    location: 'Barcelona, Spain',
    balance: 5321.77,
  },
  {
    id: '8',
    name: 'Benjamin Harris',
    email: 'benjamin@sony.jp',
    location: 'Tokyo, Japan',
    balance: 8452.39,
  },
  {
    id: '9',
    name: 'Olivia Brown',
    email: 'olivia@lvmh.fr',
    location: 'Paris, France',
    balance: 7345.1,
  },
  {
    id: '10',
    name: 'Michael Clark',
    email: 'michael@eni.it',
    location: 'Milan, Italy',
    balance: 5214.88,
  },
  {
    id: '11',
    name: 'Ava Wilson',
    email: 'ava@vale.br',
    location: 'Rio de Janeiro, Brazil',
    balance: 9421.5,
  },
  {
    id: '12',
    name: 'David Young',
    email: 'david@tata.in',
    location: 'Mumbai, India',
    balance: 4521.67,
  },
];

export default function DataGridDemo() {
  const [pagination, setPagination] = useState<PaginationState>({
    pageIndex: 0,
    pageSize: 5,
  });
  const [sorting, setSorting] = useState<SortingState>([{ id: 'name', desc: true }]);

  const columns = useMemo<ColumnDef<IData>[]>(
    () => [
      {
        accessorKey: 'name',
        header: 'Name',
        cell: (info) => <span className="font-medium">{info.getValue() as string}</span>,
        size: 175,
        meta: {
          headerClassName: '',
          cellClassName: '',
        },
      },
      {
        accessorKey: 'email',
        header: 'Email',
        cell: (info) => (
          <Link href={`mailto:${info.getValue()}`} className="hover:text-primary hover:underline">
            {info.getValue() as string}
          </Link>
        ),
        size: 150,
        meta: {
          headerClassName: '',
          cellClassName: '',
        },
      },
      {
        accessorKey: 'location',
        header: 'Location',
        cell: (info) => <span>{info.getValue() as string}</span>,
        size: 125,
        meta: {
          headerClassName: '',
          cellClassName: '',
        },
      },
      {
        accessorKey: 'balance',
        header: 'Balance ($)',
        cell: (info) => <span className="font-semibold">${(info.getValue() as number).toFixed(2)}</span>,
        size: 120,
        meta: {
          headerClassName: 'text-right rtl:text-left',
          cellClassName: 'text-right rtl:text-left',
        },
      },
    ],
    [],
  );

  const table = useReactTable({
    columns,
    data: demoData,
    pageCount: Math.ceil((demoData?.length || 0) / pagination.pageSize),
    getRowId: (row: IData) => row.id,
    state: {
      pagination,
      sorting,
    },
    onPaginationChange: setPagination,
    onSortingChange: setSorting,
    getCoreRowModel: getCoreRowModel(),
    getFilteredRowModel: getFilteredRowModel(),
    getPaginationRowModel: getPaginationRowModel(),
    getSortedRowModel: getSortedRowModel(),
  });

  return (
    <DataGrid table={table} recordCount={demoData?.length || 0}>
      <div className="w-full px-5 space-y-2.5">
        <DataGridContainer>
          <ScrollArea>
            <DataGridTable />
            <ScrollBar orientation="horizontal" />
          </ScrollArea>
        </DataGridContainer>
        <DataGridPagination />
      </div>
    </DataGrid>
  );
}

```

Install NPM dependencies:
```bash
none
```

Extend existing Tailwind 4 index.css with this code:
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


## Bento

**Author:** @kinfe123 | **Used:** 117x
**URL:** https://21st.dev/@kinfe123/components/bento
**Install:** `npx shadcn@latest add "https://21st.dev/r/kinfe123/bento?api_key=$API_KEY_21ST"`
**Description:** Beautifully designed, fully responsive, expertly crafted Bento section

```
You are given a task to integrate an existing React component in the codebase

The codebase should support:
- shadcn project structure
- Tailwind CSS
- Typescript

Determine the default path for components and styles.
If default path for components is not /components/ui, provide instructions on why it's important to create this folder

Copy-paste this component to /components/ui folder:
```tsx
bento.tsx
// Full source available at: https://21st.dev/@kinfe123/components/bento
// Or install via: npx shadcn@latest add "https://21st.dev/r/kinfe123/bento?api_key=$API_KEY_21ST"

import FUIBentoGridDark from "@/components/ui/bento";

export default function DemoOne() {
  return <FUIBentoGridDark />;
}

```

Install NPM dependencies:
```bash
none
```

Extend existing Tailwind 4 index.css with this code:
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


## Bento Monochrome

**Author:** @larsen66 | **Used:** 116x
**URL:** https://21st.dev/@larsen66/components/bento-monochrome
**Install:** `npx shadcn@latest add "https://21st.dev/r/larsen66/bento-monochrome?api_key=$API_KEY_21ST"`
**Description:** Here is Bento Monochrome component

```
You are given a task to integrate an existing React component in the codebase

The codebase should support:
- shadcn project structure
- Tailwind CSS
- Typescript

Determine the default path for components and styles.
If default path for components is not /components/ui, provide instructions on why it's important to create this folder

Copy-paste this component to /components/ui folder:
```tsx
bento-monochrome.tsx
// Full source available at: https://21st.dev/@larsen66/components/bento-monochrome
// Or install via: npx shadcn@latest add "https://21st.dev/r/larsen66/bento-monochrome?api_key=$API_KEY_21ST"

import FeaturesSectionMinimal from "@/components/ui/bento-monochrome";

export default function DemoOne() {
  return <FeaturesSectionMinimal />;
}

```

Install NPM dependencies:
```bash
none
```

Extend existing Tailwind 4 index.css with this code:
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


## Colorful Bento Grid

**Author:** @radu | **Used:** 110x
**URL:** https://21st.dev/@radu/components/colorful-bento-grid
**Install:** `npx shadcn@latest add "https://21st.dev/r/radu/colorful-bento-grid?api_key=$API_KEY_21ST"`
**Description:** A section with live and coming soon pages to show on your landing page, no matter if you're a SaaS (show features) or an Agency. 

```
You are given a task to integrate an existing React component in the codebase

The codebase should support:
- shadcn project structure
- Tailwind CSS
- Typescript

Determine the default path for components and styles.
If default path for components is not /components/ui, provide instructions on why it's important to create this folder

Copy-paste this component to /components/ui folder:
```tsx
colorful-bento-grid.tsx
// Full source available at: https://21st.dev/@radu/components/colorful-bento-grid
// Or install via: npx shadcn@latest add "https://21st.dev/r/radu/colorful-bento-grid?api_key=$API_KEY_21ST"

import { Component } from "@/components/ui/colorful-bento-grid";

export default function DemoOne() {
  return (
    <main className="bg-[#F0F0F0] w-screen min-h-screen">
    <Component />
    </main>
  ) 
}

```

Install NPM dependencies:
```bash
none
```

Extend existing Tailwind 4 index.css with this code:
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

