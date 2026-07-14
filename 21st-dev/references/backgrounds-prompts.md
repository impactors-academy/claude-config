# 21st.dev — Backgrounds & Visual FX — Full Integration Prompts

40 components sorted by popularity.
Each section is a copy-paste ready prompt for Claude or any AI coding tool.

---

## Shader Animation

**Author:** @designali-in | **Used:** 2,586x
**URL:** https://21st.dev/@designali-in/components/shader-animation
**Install:** `npx shadcn@latest add "https://21st.dev/r/designali-in/shader-animation?api_key=$API_KEY_21ST"`
**Description:** The page will now show the beautiful animated ripple effect that fills the entire screen with the mesmerizing concentric circles and color gradients from your original Three.js shader code.

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
shader-animation.tsx
// Full source available at: https://21st.dev/@designali-in/components/shader-animation
// Or install via: npx shadcn@latest add "https://21st.dev/r/designali-in/shader-animation?api_key=$API_KEY_21ST"

import { ShaderAnimation } from "@/components/ui/shader-animation";

export default function DemoOne() {
  return (
    <div className="relative flex h-[650px] w-full flex-col items-center justify-center overflow-hidden rounded-xl border bg-blue-700">
      <ShaderAnimation/>
      <span className="absolute pointer-events-none z-10 text-center text-7xl leading-none font-semibold tracking-tighter whitespace-pre-wrap text-white">
        Shader Animation
      </span>
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


## Animated Shader Background

**Author:** @minhxthanh | **Used:** 1,817x
**URL:** https://21st.dev/@minhxthanh/components/animated-shader-background
**Install:** `npx shadcn@latest add "https://21st.dev/r/minhxthanh/animated-shader-background?api_key=$API_KEY_21ST"`
**Description:** a real-time animated shader background built with Three.js and GLSL

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
animated-shader-background.tsx
// Full source available at: https://21st.dev/@minhxthanh/components/animated-shader-background
// Or install via: npx shadcn@latest add "https://21st.dev/r/minhxthanh/animated-shader-background?api_key=$API_KEY_21ST"

import AnoAI from "@/components/ui/animated-shader-background";

const DemoOne = () => {
  return (
    <div className="w-full h-screen bg-black">
      <AnoAI/>
    </div>
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


## Animated Gradient Background

**Author:** @hammamikhairi | **Used:** 994x
**URL:** https://21st.dev/@hammamikhairi/components/animated-gradient-background
**Install:** `npx shadcn@latest add "https://21st.dev/r/hammamikhairi/animated-gradient-background?api_key=$API_KEY_21ST"`
**Description:** An animated Gradient Background

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
animated-gradient-background.tsx
// Full source available at: https://21st.dev/@hammamikhairi/components/animated-gradient-background
// Or install via: npx shadcn@latest add "https://21st.dev/r/hammamikhairi/animated-gradient-background?api_key=$API_KEY_21ST"

"use client"
import AnimatedGradientBackground from "@/components/ui/animated-gradient-background";
import { DotLottieReact } from '@lottiefiles/dotlottie-react';
import { AnimatePresence, motion, useInView, Variants } from "framer-motion";
import { useRef } from "react";

const DemoVariant1 = () => {
  return (
    <div className="relative w-full h-screen overflow-hidden">
      {/* Gradient Background */}
      <AnimatedGradientBackground />

      <div className="relative z-10 flex flex-col items-center justify-start h-full px-4 pt-32 text-center">
        <div delay={0.4}
          duration={0.9}
        >
          <DotLottieReact
            src="https://lottie.host/8cf4ba71-e5fb-44f3-8134-178c4d389417/0CCsdcgNIP.json"
            loop
            autoplay
          />
        </div>
          <p className="mt-4 text-lg text-gray-300 md:text-xl max-w-lg">
            A customizable animated radial gradient background with a subtle
            breathing effect.
          </p>
      </div>
    </div>
  );
};




export { DemoVariant1 };

```

Install NPM dependencies:
```bash
framer-motion, lottie-react, motion
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


## Border Trail

**Author:** @ibelick | **Used:** 548x
**URL:** https://21st.dev/@ibelick/components/border-trail
**Install:** `npx shadcn@latest add "https://21st.dev/r/ibelick/border-trail?api_key=$API_KEY_21ST"`
**Description:** Animated border effect that moves along the edges of its parent container.

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
border-trail.tsx
// Full source available at: https://21st.dev/@ibelick/components/border-trail
// Or install via: npx shadcn@latest add "https://21st.dev/r/ibelick/border-trail?api_key=$API_KEY_21ST"

"use client";

import { BorderTrail } from "@/components/ui/border-trail";

export function LoadingCardBorderTrail() {
  return (
    <div className="relative flex h-[200px] w-[300px] flex-col items-center justify-center rounded-md bg-zinc-200 px-5 py-2 dark:bg-zinc-900">
      <BorderTrail
        style={{
          boxShadow:
            "0px 0px 60px 30px rgb(255 255 255 / 50%), 0 0 100px 60px rgb(0 0 0 / 50%), 0 0 140px 90px rgb(0 0 0 / 50%)",
        }}
        size={100}
      />
      <div
        className="flex h-full animate-pulse flex-col items-start justify-center space-y-2"
        role="status"
        aria-label="Loading..."
      >
        <div className="h-1 w-4 rounded-[4px] bg-zinc-600"></div>
        <div className="h-1 w-10 rounded-[4px] bg-zinc-600"></div>
        <div className="h-1 w-12 rounded-[4px] bg-zinc-600"></div>
        <div className="h-1 w-12 rounded-[4px] bg-zinc-600"></div>
        <div className="h-1 w-12 rounded-[4px] bg-zinc-600"></div>
      </div>
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


## Gradient Background

**Author:** @sshahaider | **Used:** 276x
**URL:** https://21st.dev/@sshahaider/components/gradient-background
**Install:** `npx shadcn@latest add "https://21st.dev/r/sshahaider/gradient-background?api_key=$API_KEY_21ST"`
**Description:** A smooth, looping gradient background powered by Framer Motion, with optional overlay and center-aligned content.
Perfect for creating vibrant hero sections, landing pages, or fullscreen app backdrops.

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
gradient-background.tsx
// Full source available at: https://21st.dev/@sshahaider/components/gradient-background
// Or install via: npx shadcn@latest add "https://21st.dev/r/sshahaider/gradient-background?api_key=$API_KEY_21ST"

import { GradientBackground } from "@/components/ui/gradient-background";

export default function DefaultDemo() {
	return (
		<GradientBackground className="flex min-h-screen items-center justify-center">
			<div className="space-y-6 px-4 text-center text-white">
				<h1 className="text-4xl font-extrabold md:text-5xl">
					Animated Gradients Background
				</h1>
			</div>
		</GradientBackground>
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


## layout preloader

**Author:** @kedhareswer.12110626 | **Used:** 216x
**URL:** https://21st.dev/@kedhareswer.12110626/components/layout-preloader
**Install:** `npx shadcn@latest add "https://21st.dev/r/kedhareswer.12110626/layout-preloader?api_key=$API_KEY_21ST"`
**Description:** An animated image preloader with GSAP transitions, featuring sequential image reveals, smooth zoom effects, and grid-based layout animations with interactive restart functionality

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
layout-preloader.tsx
// Full source available at: https://21st.dev/@kedhareswer.12110626/components/layout-preloader
// Or install via: npx shadcn@latest add "https://21st.dev/r/kedhareswer.12110626/layout-preloader?api_key=$API_KEY_21ST"

import App from '../app';

export default function DefaultDemo() {
  return <App />;
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


## Silk-Background-animation

**Author:** @waleedkibhen | **Used:** 205x
**URL:** https://21st.dev/@waleedkibhen/components/silk-background-animation
**Install:** `npx shadcn@latest add "https://21st.dev/r/waleedkibhen/silk-background-animation?api_key=$API_KEY_21ST"`
**Description:** flowing silk background animation, animated hero section, react background animation, three.js shader hero background, css background animation fallback, glsl web background, realistic fabric animation, 3d background for website, webgpu canvas animation, react-three-fiber hero animation, high performance web animation, smooth motion UI component, modern UI texture effect, dynamic website intro, black silk animated backdrop

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
silk-background-animation.tsx
// Full source available at: https://21st.dev/@waleedkibhen/components/silk-background-animation
// Or install via: npx shadcn@latest add "https://21st.dev/r/waleedkibhen/silk-background-animation?api_key=$API_KEY_21ST"

import { Component } from "@/components/ui/silk-background-animation";

const DemoOne = () => {
  return <Component />;
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


## Dynamic Wave Canvas Background

**Author:** @minhxthanh | **Used:** 193x
**URL:** https://21st.dev/@minhxthanh/components/dynamic-wave-canvas-background
**Install:** `npx shadcn@latest add "https://21st.dev/r/minhxthanh/dynamic-wave-canvas-background?api_key=$API_KEY_21ST"`
**Description:** Component that creates a dynamic, colorful wave animation as a canvas background. Ideal for visually captivating hero sections, blending smooth animations with deep blues, purples, and gray tones for an engaging dark theme.

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
dynamic-wave-canvas-background.tsx
// Full source available at: https://21st.dev/@minhxthanh/components/dynamic-wave-canvas-background
// Or install via: npx shadcn@latest add "https://21st.dev/r/minhxthanh/dynamic-wave-canvas-background?api_key=$API_KEY_21ST"

// This is file with demos of your component
// Each export is one usecase for your component

import HeroWave from "@/components/ui/dynamic-wave-canvas-background";

const DemoOne = () => {
  return <HeroWave />;
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


## In view

**Author:** @ibelick | **Used:** 154x
**URL:** https://21st.dev/@ibelick/components/in-view
**Install:** `npx shadcn@latest add "https://21st.dev/r/ibelick/in-view?api_key=$API_KEY_21ST"`
**Description:** Easily animate elements when they come into view. You can apply animations to elements when they enter the viewport, or when they are fully visible.

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
in-view.tsx
// Full source available at: https://21st.dev/@ibelick/components/in-view
// Or install via: npx shadcn@latest add "https://21st.dev/r/ibelick/in-view?api_key=$API_KEY_21ST"

"use client";
import { InView } from "@/components/ui/in-view";
import { motion } from "framer-motion";

function InViewBasic() {
  return (
    <div className="h-[350px] w-full overflow-auto">
      <div className="py-12 text-center text-sm">Scroll down</div>
      <div className="flex h-[500px] items-end justify-center px-4 pb-24">
        <InView
          variants={{
            hidden: { opacity: 0, y: 100, filter: "blur(4px)" },
            visible: { opacity: 1, y: 0, filter: "blur(0px)" },
          }}
          viewOptions={{ margin: "0px 0px -200px 0px" }}
          transition={{ duration: 0.3, ease: "easeInOut" }}
        >
          <div className="max-w-96">
            <p className="">
              <strong className="font-medium">
                Craft beautiful animated components with Motion-Primitives.
              </strong>{" "}
              Designed for developers and designers. The library leverages the
              power of Framer Motion, with intuitive APIs that simplifies
              creating complex animations for any project. Start building more
              dynamic interfaces today.
            </p>
          </div>
        </InView>
      </div>
    </div>
  );
}


export default {
  InViewBasic
};

```

Install NPM dependencies:
```bash
framer-motion, motion
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


## Modern Background Paths

**Author:** @uniquesonu | **Used:** 141x
**URL:** https://21st.dev/@uniquesonu/components/modern-background-paths
**Install:** `npx shadcn@latest add "https://21st.dev/r/uniquesonu/modern-background-paths?api_key=$API_KEY_21ST"`
**Description:** BackgroundPaths: Dynamic SVG Paths & Animated Hero Section
The BackgroundPaths component creates a stunning and subtly animated background using dynamically generated SVG paths. It perfectly complements an engaging, animated hero title and a stylish call-to-action button, making it an excellent choice for a modern header or landing section on any website.

What It Is
This React component uses framer-motion to generate and animate a series of elegant, flowing SVG paths that gently shift and fade in the background. Overlaying this dynamic backdrop is a customizable title where each letter animates into view with a smooth, spring-like effect. Below the title, a stylish button with interactive hover effects invites user engagement.

Key Features
Animated SVG Background:

Dynamic Paths: The FloatingPaths sub-component creates 36 unique SVG <path> elements. Their shapes, stroke widths, and opacities are all dynamically generated, creating a sense of depth and variation.
Continuous Motion: Each path animates infinitely with varying durations, resulting in a mesmerizing, non-repeating flow of lines across the background.
Light/Dark Mode Support: The paths automatically adapt their color to match the surrounding text, seamlessly integrating with both light and dark themes.
Spring-Animated Hero Title:

Letter-by-Letter Entrance: The main title (controlled by the title prop) animates each individual letter into view with a "spring" effect, creating a lively and engaging entrance.
Gradient Text: The title text uses a gradient fill that changes based on the theme, providing a modern and polished look.
Customizable: Easily change the hero text by passing a different title prop.
Stylish Call-to-Action Button:

A beautifully designed button, "Discover Excellence," is positioned below the title.
It features subtle background gradients, a backdrop-blur effect for a frosted glass look, and a shadow for depth.
Interactive Hover Effects: On hover, the button scales slightly, its shadow deepens, and an arrow icon to the right smoothly translates, signaling interactivity.
Theme-Aware: The button's colors and hover states work flawlessly in both light and dark modes.
Responsive Layout: The component is designed for responsiveness, ensuring the title and button are well-centered and legible across various screen sizes.

Framer Motion Integration: Extensive use of framer-motion handles all animations, providing smooth, hardware-accelerated transitions and complex sequence orchestration.

Why It's Cool for Developers
This component is an excellent demonstration of:

Generative SVG Animation: Learn how to programmatically create and animate complex SVG paths for unique background effects.
Sophisticated framer-motion Usage: It showcases advanced framer-motion features like pathLength, pathOffset, and spring transitions for precise control over animations.
Layered UI Design: See how to combine background elements (SVG paths) with foreground content (text and a button) while maintaining proper z-index for visual hierarchy.
Theming and Responsiveness: Implement design that gracefully adapts to different themes and screen sizes.
Component Composition: It breaks down a complex UI into smaller, manageable sub-components (FloatingPaths).


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
modern-background-paths.tsx
// Full source available at: https://21st.dev/@uniquesonu/components/modern-background-paths
// Or install via: npx shadcn@latest add "https://21st.dev/r/uniquesonu/modern-background-paths?api_key=$API_KEY_21ST"

import BackgroundPaths from "@/components/ui/modern-background-paths";

const DemoOne = () => {
  return <BackgroundPaths />;
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


## Gradient Card Showcase

**Author:** @minhxthanh | **Used:** 138x
**URL:** https://21st.dev/@minhxthanh/components/gradient-card-showcase
**Install:** `npx shadcn@latest add "https://21st.dev/r/minhxthanh/gradient-card-showcase?api_key=$API_KEY_21ST"`
**Description:** Displays a set of interactive cards with skewed gradient back-panels, glowing blur highlights, and smooth hover transitions

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
gradient-card-showcase.tsx
// Full source available at: https://21st.dev/@minhxthanh/components/gradient-card-showcase
// Or install via: npx shadcn@latest add "https://21st.dev/r/minhxthanh/gradient-card-showcase?api_key=$API_KEY_21ST"

import SkewCards from "@/components/ui/gradient-card-showcase";

const DemoOne = () => {
  return (
      <SkewCards />
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


## 3D Animation

**Author:** @dhileepkumargm | **Used:** 126x
**URL:** https://21st.dev/@dhileepkumargm/components/3d-animation
**Install:** `npx shadcn@latest add "https://21st.dev/r/dhileepkumargm/3d-animation?api_key=$API_KEY_21ST"`
**Description:** A responsive and cinematic hero section component that displays text scrolling along the walls of a 3D animated hallway. It includes a reflection, parallax effects, and customizable imagery.

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
3d-animation.tsx
// Full source available at: https://21st.dev/@dhileepkumargm/components/3d-animation
// Or install via: npx shadcn@latest add "https://21st.dev/r/dhileepkumargm/3d-animation?api_key=$API_KEY_21ST"

import React from 'react';
import { PoemAnimation } from "@/components/ui/3d-animation";


// --- Data Configuration ---
const ANIMATION_DATA = {
    poemHTML: `
        <p>The <span>love</span> between Ayla and Leo ignited in the old courtyard, each morning their swords clashed under dawn’s glow, faces streaked with <span>dust</span> and sweat; they <span>danced</span> between parries, every laugh a spark of joy against uncertain hearts. She stepped forward with <span>courage</span>, he met her gaze with open warmth, two souls seeking a shared <span>triumph</span> in their vulnerability. When blades slipped and one <span>faltered</span>, the other caught them—forearms brushing, pulses aligned in a daring heartbeat. In failure they found grace; in triumph they discovered unity. Each moment spent <span>daring</span> to trust the other built a bond impervious to fear. At dusk, they sheathed their swords, stepping from the <span>arena</span> hand in hand, knowing love blooms not through perfection, but by <span>daring greatly</span> together.</p>
`,
    backgroundImageUrl: "https://i.ibb.co/q3XSxR9W/20250831-120144.jpg",
    boyImageUrl: "https://i.ibb.co/Y4FKvK38/20250831-113022.png"
};


/**
 * The main application component, which composes the page from different sections.
 */
export default function App() {
    // In a standard React project, you would place font links in your main public/index.html file.
    // For this environment, we assume they are available or can be added there.
    return (
        <PoemAnimation
            poemHTML={ANIMATION_DATA.poemHTML}
            backgroundImageUrl={ANIMATION_DATA.backgroundImageUrl}
            boyImageUrl={ANIMATION_DATA.boyImageUrl}
        />
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


## Animated Card

**Author:** @badtzx0 | **Used:** 126x
**URL:** https://21st.dev/@badtzx0/components/animated-card
**Install:** `npx shadcn@latest add "https://21st.dev/r/badtzx0/animated-card?api_key=$API_KEY_21ST"`
**Description:** Here is Animated Card component

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
animated-card.tsx
// Full source available at: https://21st.dev/@badtzx0/components/animated-card
// Or install via: npx shadcn@latest add "https://21st.dev/r/badtzx0/animated-card?api_key=$API_KEY_21ST"

import {
  AnimatedCard,
  CardBody,
  CardDescription,
  CardTitle,
  CardVisual,
} from "@/components/ui/animated-card"
import { Visual1 } from "@/components/ui/animated-card"

export default function AnimatedCard1Demo() {
  return (
    <AnimatedCard>
      <CardVisual>
        <Visual1 mainColor="#ff6900" secondaryColor="#f54900" />
      </CardVisual>
      <CardBody>
        <CardTitle>Just find the right caption</CardTitle>
        <CardDescription>
          This card will tell everything you want
        </CardDescription>
      </CardBody>
    </AnimatedCard>
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


## animated pattern cloud

**Author:** @ashishrajwaniai01 | **Used:** 116x
**URL:** https://21st.dev/@ashishrajwaniai01/components/animated-pattern-cloud
**Install:** `npx shadcn@latest add "https://21st.dev/r/ashishrajwaniai01/animated-pattern-cloud?api_key=$API_KEY_21ST"`
**Description:** wavy pattern cloud

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
animated-pattern-cloud.tsx
// Full source available at: https://21st.dev/@ashishrajwaniai01/components/animated-pattern-cloud
// Or install via: npx shadcn@latest add "https://21st.dev/r/ashishrajwaniai01/animated-pattern-cloud?api_key=$API_KEY_21ST"

import React, { useEffect, useRef } from 'react';

/**
 * ProceduralGroundBackground
 * A WebGL 2D background featuring topographic neon lines and sand-ripple movement.
 * Optimized for performance using fragment shaders.
 */
const ProceduralGroundBackground: React.FC = () => {
  const canvasRef = useRef<HTMLCanvasElement>(null);

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;

    const gl = canvas.getContext('webgl');
    if (!gl) return;

    const vsSource = `
      attribute vec2 position;
      void main() {
        gl_Position = vec4(position, 0.0, 1.0);
      }
    `;

    const fsSource = `
      precision highp float;
      uniform float u_time;
      uniform vec2 u_resolution;

      float hash(vec2 p) {
        return fract(sin(dot(p, vec2(127.1, 311.7))) * 43758.5453123);
      }

      float noise(vec2 p) {
        vec2 i = floor(p);
        vec2 f = fract(p);
        vec2 u = f * f * (3.0 - 2.0 * f);
        return mix(mix(hash(i + vec2(0.0, 0.0)), hash(i + vec2(1.0, 0.0)), u.x),
                   mix(hash(i + vec2(0.0, 1.0)), hash(i + vec2(1.0, 1.0)), u.x), u.y);
      }

      void main() {
        vec2 uv = (gl_FragCoord.xy * 2.0 - u_resolution.xy) / min(u_resolution.x, u_resolution.y);
        
        // Ground Perspective Simulation
        float depth = 1.0 / (uv.y + 1.15);
        vec2 gridUv = vec2(uv.x * depth, depth + u_time * 0.15);
        
        // Layered Procedural Noise for Terrain
        float n = noise(gridUv * 3.5);
        float ripples = sin(gridUv.y * 18.0 + n * 8.0 + u_time * 0.5);
        
        // Neon Topographic Lines
        float topoLine = smoothstep(0.03, 0.0, abs(ripples));
        
        // Color Palette
        vec3 baseColor = vec3(0.04, 0.03, 0.12); // Deep Space
        vec3 accentColor = vec3(0.1, 0.3, 0.8);   // Electric Blue
        vec3 neonColor = vec3(0.6, 0.2, 1.0);     // Neon Purple
        
        // Composite
        vec3 finalColor = mix(baseColor, accentColor, n * 0.6);
        finalColor += topoLine * neonColor * depth * 0.4;
        
        // Horizon Fog / Fade
        float fade = smoothstep(0.1, -1.0, uv.y);
        finalColor *= (1.0 - length(uv) * 0.45) * (1.0 - fade);

        gl_FragColor = vec4(finalColor, 1.0);
      }
    `;

    const createShader = (gl: WebGLRenderingContext, type: number, source: string) => {
      const shader = gl.createShader(type)!;
      gl.shaderSource(shader, source);
      gl.compileShader(shader);
      return shader;
    };

    const program = gl.createProgram()!;
    gl.attachShader(program, createShader(gl, gl.VERTEX_SHADER, vsSource));
    gl.attachShader(program, createShader(gl, gl.FRAGMENT_SHADER, fsSource));
    gl.linkProgram(program);
    gl.useProgram(program);

    const buffer = gl.createBuffer();
    gl.bindBuffer(gl.ARRAY_BUFFER, buffer);
    gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([
      -1, -1,  1, -1, -1,  1,
      -1,  1,  1, -1,  1,  1
    ]), gl.STATIC_DRAW);

    const posAttrib = gl.getAttribLocation(program, "position");
    gl.enableVertexAttribArray(posAttrib);
    gl.vertexAttribPointer(posAttrib, 2, gl.FLOAT, false, 0, 0);

    const timeLoc = gl.getUniformLocation(program, "u_time");
    const resLoc = gl.getUniformLocation(program, "u_resolution");

    let animationFrameId: number;
    const render = (time: number) => {
      const { innerWidth: width, innerHeight: height } = window;
      if (canvas.width !== width || canvas.height !== height) {
        canvas.width = width;
        canvas.height = height;
        gl.viewport(0, 0, width, height);
      }

      gl.uniform1f(timeLoc, time * 0.001);
      gl.uniform2f(resLoc, width, height);
      gl.drawArrays(gl.TRIANGLES, 0, 6);
      animationFrameId = requestAnimationFrame(render);
    };

    animationFrameId = requestAnimationFrame(render);

    return () => {
      cancelAnimationFrame(animationFrameId);
    };
  }, []);

  return (
    <div className="fixed inset-0 w-full h-full bg-zinc-950 -z-10">
      <canvas
        ref={canvasRef}
        className="w-full h-full block touch-none"
        style={{ filter: 'contrast(1.1) brightness(0.9)' }}
      />
    </div>
  );
};

export default ProceduralGroundBackground;
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


## SpotlightBackground

**Author:** @dhileepkumargm | **Used:** 116x
**URL:** https://21st.dev/@dhileepkumargm/components/spotlight-background
**Install:** `npx shadcn@latest add "https://21st.dev/r/dhileepkumargm/spotlight-background?api_key=$API_KEY_21ST"`
**Description:** A dramatic, animated background composed of multiple soft “spotlight” blobs that glide and rotate to create depth and movement. Ideal for hero sections or immersive UI backdrops.

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
spotlight-background.tsx
// Full source available at: https://21st.dev/@dhileepkumargm/components/spotlight-background
// Or install via: npx shadcn@latest add "https://21st.dev/r/dhileepkumargm/spotlight-background?api_key=$API_KEY_21ST"

"use client";

import React from "react";
import { motion } from "framer-motion";
import SpotlightBackground from "@/components/ui/spotlight-background";

const DemoOne = () => {
  return (
    <SpotlightBackground>
      <motion.div
        initial={{ opacity: 0, y: 40 }}
        whileInView={{ opacity: 1, y: 0 }}
        transition={{
          delay: 0.3,
          duration: 0.8,
          ease: "easeInOut",
        }}
        className="spotlight-inner"
      >
        <h1 className="spotlight-title">
          Spotlight Background
        </h1>
        <p className="spotlight-description">
          A dramatic and eye-catching animated background effect.
        </p>
        <button className="spotlight-button">
          Get Started
        </button>
      </motion.div>
    </SpotlightBackground>
  );
};

export default DemoOne;

```

Install NPM dependencies:
```bash
framer-motion, motion
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


## Animated Search Bar

**Author:** @aghasisahakyan1 | **Used:** 114x
**URL:** https://21st.dev/@aghasisahakyan1/components/animated-search-bar
**Install:** `npx shadcn@latest add "https://21st.dev/r/aghasisahakyan1/animated-search-bar?api_key=$API_KEY_21ST"`
**Description:** Animated Search Bar with gooey effect  

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
animated-search-bar.tsx
// Full source available at: https://21st.dev/@aghasisahakyan1/components/animated-search-bar
// Or install via: npx shadcn@latest add "https://21st.dev/r/aghasisahakyan1/animated-search-bar?api_key=$API_KEY_21ST"

import React from 'react';
import { GooeySearchBar } from "@/components/ui/animated-search-bar";

const DemoOne = () => {
  return (
    <div style={{
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        minHeight: '100vh',
        backgroundColor: '#e5e7eb',
        padding: '20px',
        boxSizing: 'border-box',
        width: '100%',
        overflow: 'hidden'
    }}>
      <GooeySearchBar />
    </div>
  );
};

export default DemoOne;
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


## Background Shader

**Author:** @moazamtrade | **Used:** 108x
**URL:** https://21st.dev/@moazamtrade/components/background-shader
**Install:** `npx shadcn@latest add "https://21st.dev/r/moazamtrade/background-shader?api_key=$API_KEY_21ST"`
**Description:** Background Shader blur gredient paper design bg 

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
background-shader.tsx
// Full source available at: https://21st.dev/@moazamtrade/components/background-shader
// Or install via: npx shadcn@latest add "https://21st.dev/r/moazamtrade/background-shader?api_key=$API_KEY_21ST"

import  Waitlist  from "@/components/ui/background-shader";

export default function DemoOne() {
  return <Waitlist />;
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


## Animated Scroll

**Author:** @minhxthanh | **Used:** 106x
**URL:** https://21st.dev/@minhxthanh/components/animated-scroll
**Install:** `npx shadcn@latest add "https://21st.dev/r/minhxthanh/animated-scroll?api_key=$API_KEY_21ST"`
**Description:** An animated two-panel scroll adventure

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
animated-scroll.tsx
// Full source available at: https://21st.dev/@minhxthanh/components/animated-scroll
// Or install via: npx shadcn@latest add "https://21st.dev/r/minhxthanh/animated-scroll?api_key=$API_KEY_21ST"

import ScrollAdventure from "@/components/ui/animated-scroll";

const DemoOne = () => {
  return (
    <div className="w-full h-screen">
      <ScrollAdventure />
    </div>
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


## Images Scrolling Animation

**Author:** @minhxthanh | **Used:** 105x
**URL:** https://21st.dev/@minhxthanh/components/images-scrolling-animation
**Install:** `npx shadcn@latest add "https://21st.dev/r/minhxthanh/images-scrolling-animation?api_key=$API_KEY_21ST"`
**Description:** Images Scrolling Animation

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
images-scrolling-animation.tsx
// Full source available at: https://21st.dev/@minhxthanh/components/images-scrolling-animation
// Or install via: npx shadcn@latest add "https://21st.dev/r/minhxthanh/images-scrolling-animation?api_key=$API_KEY_21ST"

import { ImagesScrollingAnimation } from "@/components/ui/images-scrolling-animation";

export default function DemoOne() {
  return <ImagesScrollingAnimation />;
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


## background plus

**Author:** @reuno-ui | **Used:** 103x
**URL:** https://21st.dev/@reuno-ui/components/background-plus
**Install:** `npx shadcn@latest add "https://21st.dev/r/reuno-ui/background-plus?api_key=$API_KEY_21ST"`
**Description:** bg background 

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
background-plus.tsx
// Full source available at: https://21st.dev/@reuno-ui/components/background-plus
// Or install via: npx shadcn@latest add "https://21st.dev/r/reuno-ui/background-plus?api_key=$API_KEY_21ST"

import { BackgroundPlus } from "@/components/ui/background-plus";

export default function DemoOne() {
  return <BackgroundPlus />;
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


## Gradient Backgrounds

**Author:** @meghtrix | **Used:** 101x
**URL:** https://21st.dev/@meghtrix/components/gradient-backgrounds
**Install:** `npx shadcn@latest add "https://21st.dev/r/meghtrix/gradient-backgrounds?api_key=$API_KEY_21ST"`
**Description:** Here is Gradient Background Bottom Blue

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
gradient-backgrounds.tsx
// Full source available at: https://21st.dev/@meghtrix/components/gradient-backgrounds
// Or install via: npx shadcn@latest add "https://21st.dev/r/meghtrix/gradient-backgrounds?api_key=$API_KEY_21ST"

import { Component } from "@/components/ui/gradient-backgrounds";

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


## Scrolling animation

**Author:** @minhxthanh | **Used:** 98x
**URL:** https://21st.dev/@minhxthanh/components/scrolling-animation
**Install:** `npx shadcn@latest add "https://21st.dev/r/minhxthanh/scrolling-animation?api_key=$API_KEY_21ST"`
**Description:** Scrolling animation, Profile images

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
scrolling-animation.tsx
// Full source available at: https://21st.dev/@minhxthanh/components/scrolling-animation
// Or install via: npx shadcn@latest add "https://21st.dev/r/minhxthanh/scrolling-animation?api_key=$API_KEY_21ST"

import { HomePage } from "@/components/ui/scrolling-animation";

export default function DemoOne() {
  return (
    <div className="w-full">
      <HomePage />
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


## BlurTextAnimation

**Author:** @xubohuah | **Used:** 88x
**URL:** https://21st.dev/@xubohuah/components/blur-text-animation
**Install:** `npx shadcn@latest add "https://21st.dev/r/xubohuah/blur-text-animation?api_key=$API_KEY_21ST"`
**Description:** Elegant blur animation that brings your words to life with cinematic transitions.

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
blur-text-animation.tsx
// Full source available at: https://21st.dev/@xubohuah/components/blur-text-animation
// Or install via: npx shadcn@latest add "https://21st.dev/r/xubohuah/blur-text-animation?api_key=$API_KEY_21ST"

import { Component } from "@/components/ui/blur-text-animation";

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


## Gallery Animation

**Author:** @n38693842 | **Used:** 88x
**URL:** https://21st.dev/@n38693842/components/gallery-animation
**Install:** `npx shadcn@latest add "https://21st.dev/r/n38693842/gallery-animation?api_key=$API_KEY_21ST"`
**Description:** this is the gallery animation on hover pics are expended with smooth animation

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
gallery-animation.tsx
// Full source available at: https://21st.dev/@n38693842/components/gallery-animation
// Or install via: npx shadcn@latest add "https://21st.dev/r/n38693842/gallery-animation?api_key=$API_KEY_21ST"

import { Component } from "@/components/ui/gallery-animation";

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


## Onboard Card

**Author:** @amanshakya307 | **Used:** 87x
**URL:** https://21st.dev/@amanshakya307/components/onboard-card
**Install:** `npx shadcn@latest add "https://21st.dev/r/amanshakya307/onboard-card?api_key=$API_KEY_21ST"`
**Description:** Animated onboarding progress card showing three steps with visual loaders, transitions, and completion indicators.

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
onboard-card.tsx
// Full source available at: https://21st.dev/@amanshakya307/components/onboard-card
// Or install via: npx shadcn@latest add "https://21st.dev/r/amanshakya307/onboard-card?api_key=$API_KEY_21ST"

// visit https://forgeui.in for more such components

import OnboardCard from '@/components/ui/onboard-card';

const Demo = () => {
  return (
       <OnboardCard
      duration={3000} // 3sec
      step1="Welcome Aboard"
      step2="Verifying Details"
      step3="Account Created"
    />
  )
}

export default Demo

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

