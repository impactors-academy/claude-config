# 21st.dev — Buttons & CTAs — Full Integration Prompts

20 components sorted by popularity.
Each section is a copy-paste ready prompt for Claude or any AI coding tool.

---

## Button

**Author:** @sean0205 | **Used:** 1,231x
**URL:** https://21st.dev/@sean0205/components/button-1
**Install:** `npx shadcn@latest add "https://21st.dev/r/sean0205/button-1?api_key=$API_KEY_21ST"`
**Description:** Renders a clickable button or an element styled as a button with advance options

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
button-1.tsx
// Full source available at: https://21st.dev/@sean0205/components/button-1
// Or install via: npx shadcn@latest add "https://21st.dev/r/sean0205/button-1?api_key=$API_KEY_21ST"

import { Button } from '@/components/ui/button-1';

export default function ButtonDemo() {
  return <Button>Button</Button>;
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


## Button

**Author:** @shugar | **Used:** 356x
**URL:** https://21st.dev/@shugar/components/button-1
**Install:** `npx shadcn@latest add "https://21st.dev/r/shugar/button-1?api_key=$API_KEY_21ST"`
**Description:** Trigger an action or event, such as submitting a form or displaying a dialog.

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
button-1.tsx
// Full source available at: https://21st.dev/@shugar/components/button-1
// Or install via: npx shadcn@latest add "https://21st.dev/r/shugar/button-1?api_key=$API_KEY_21ST"

import { Button } from "@/components/ui/button-1";

export default function DefaultDemo() {
  return (
        <div className="flex justify-between items-center gap-2">
          <Button size="small">Upload</Button>
          <Button>Upload</Button>
          <Button size="large">Upload</Button>
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


## Liquid Metal Button

**Author:** @johuniq | **Used:** 235x
**URL:** https://21st.dev/@johuniq/components/liquid-metal-button
**Install:** `npx shadcn@latest add "https://21st.dev/r/johuniq/liquid-metal-button?api_key=$API_KEY_21ST"`
**Description:** A button with liquid metal animation, metallic glowing borders, and fluid hover effects.

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
liquid-metal-button.tsx
// Full source available at: https://21st.dev/@johuniq/components/liquid-metal-button
// Or install via: npx shadcn@latest add "https://21st.dev/r/johuniq/liquid-metal-button?api_key=$API_KEY_21ST"

import { LiquidMetalButton } from "@/components/ui/liquid-metal-button";

export default function LiquidMetalButtonDemo() {
  return (
    <div className="flex flex-col items-center justify-center gap-8 p-8">
      <div className="flex items-center gap-8">
        <LiquidMetalButton label="Get Started" />
        <LiquidMetalButton viewMode="icon" />
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


## Animated Generate Button (shadcn + Tailwind)

**Author:** @moazamtrade | **Used:** 175x
**URL:** https://21st.dev/@moazamtrade/components/animated-generate-button-shadcn-tailwind
**Install:** `npx shadcn@latest add "https://21st.dev/r/moazamtrade/animated-generate-button-shadcn-tailwind?api_key=$API_KEY_21ST"`
**Description:** A reusable, accessible React button that mirrors the Uiverse “dexter-st” glow/flicker animation using Tailwind utilities and scoped CSS. It integrates with shadcn theme tokens, supports idle/active labels, a controllable generating state, and a customizable highlight hue for easy theming.

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
animated-generate-button-shadcn-tailwind.tsx
// Full source available at: https://21st.dev/@moazamtrade/components/animated-generate-button-shadcn-tailwind
// Or install via: npx shadcn@latest add "https://21st.dev/r/moazamtrade/animated-generate-button-shadcn-tailwind?api_key=$API_KEY_21ST"

import AnimatedGenerateButton from "@/components/ui/animated-generate-button-shadcn-tailwind";

export default function DemoOne() {
  return <AnimatedGenerateButton
  labelIdle="Generate"
  labelActive="Building"
  highlightHueDeg={5000} 
/>;
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


## Button

**Author:** @uilayout.contact | **Used:** 167x
**URL:** https://21st.dev/@uilayout.contact/components/button-1
**Install:** `npx shadcn@latest add "https://21st.dev/r/uilayout.contact/button-1?api_key=$API_KEY_21ST"`
**Description:** Here is modern liquid animated button component

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
button-1.tsx
// Full source available at: https://21st.dev/@uilayout.contact/components/button-1
// Or install via: npx shadcn@latest add "https://21st.dev/r/uilayout.contact/button-1?api_key=$API_KEY_21ST"

'use client';
import React, { useState } from 'react';
import { Github, Star } from 'lucide-react';
import { Liquid } from '@/components/ui/button-1';
const COLORS = {
  color1: '#FFFFFF',
  color2: '#1E10C5',
  color3: '#9089E2',
  color4: '#FCFCFE',
  color5: '#F9F9FD',
  color6: '#B2B8E7',
  color7: '#0E2DCB',
  color8: '#0017E9',
  color9: '#4743EF',
  color10: '#7D7BF4',
  color11: '#0B06FC',
  color12: '#C5C1EA',
  color13: '#1403DE',
  color14: '#B6BAF6',
  color15: '#C1BEEB',
  color16: '#290ECB',
  color17: '#3F4CC0',
};
const GitHubButton = () => {
  const [isHovered, setIsHovered] = useState(false);
  return (
    <div className="flex justify-center">
      <a
        href="https://github.com/ui-layouts/uilayouts"
        target="_blank"
        className="relative inline-block  sm:w-36 w-14 h-[2.7em] mx-auto group dark:bg-black bg-white dark:border-white border-black border-2 rounded-lg">
        <div className="absolute w-[112.81%] h-[128.57%] top-[8.57%] left-1/2 -translate-x-1/2 filter blur-[19px] opacity-70">
          <span className="absolute inset-0 rounded-lg bg-[#d9d9d9] filter blur-[6.5px]"></span>
          <div className="relative w-full h-full overflow-hidden rounded-lg">
            <Liquid isHovered={isHovered} colors={COLORS} />
          </div>
        </div>
        <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-[40%] w-[92.23%] h-[112.85%] rounded-lg bg-[#010128] filter blur-[7.3px]"></div>
        <div className="relative w-full h-full overflow-hidden rounded-lg">
          <span className="absolute inset-0 rounded-lg bg-[#d9d9d9]"></span>
          <span className="absolute inset-0 rounded-lg bg-black"></span>
          <Liquid isHovered={isHovered} colors={COLORS} />
          {[1, 2, 3, 4, 5].map((i) => (
            <span
              key={i}
              className={`absolute inset-0 rounded-lg border-solid border-[3px] border-gradient-to-b from-transparent to-white mix-blend-overlay filter ${i <= 2 ? 'blur-[3px]' : i === 3 ? 'blur-[5px]' : 'blur-[4px]'}`}></span>
          ))}
          <span className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-[40%] w-[70.8%] h-[42.85%] rounded-lg filter blur-[15px] bg-[#006]"></span>
        </div>
        <button
          className="absolute inset-0 rounded-lg bg-transparent cursor-pointer"
          aria-label="Get Starteqwed"
          type="button"
          onMouseEnter={() => setIsHovered(true)}
          onMouseLeave={() => setIsHovered(false)}>
          <span className=" flex  items-center justify-between px-4 gap-2   rounded-lg group-hover:text-yellow-400 text-white text-xl font-semibold tracking-wide whitespace-nowrap">
            <Star className="group-hover:fill-yellow-400 fill-white w-6 h-6 flex-shrink-0 sm:inline-block hidden" />
            <Github className="sm:hidden inline-block group-hover:fill-yellow-400 fill-white w-6 h-6 flex-shrink-0" />
            <span className="sm:inline-block hidden">Github</span>
          </span>
        </button>
      </a>
    </div>
  );
};
export default GitHubButton;

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


## Button

**Author:** @abishek1512 | **Used:** 161x
**URL:** https://21st.dev/@abishek1512/components/button-1
**Install:** `npx shadcn@latest add "https://21st.dev/r/abishek1512/button-1?api_key=$API_KEY_21ST"`
**Description:** Animated button

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
button-1.tsx
// Full source available at: https://21st.dev/@abishek1512/components/button-1
// Or install via: npx shadcn@latest add "https://21st.dev/r/abishek1512/button-1?api_key=$API_KEY_21ST"

import GradientButton from "@/components/ui/button-1";

const DemoOne = () => {
  return (
    <div className="flex w-full h-screen justify-center items-center">
      <GradientButton
        onClick={() => console.log('clicked')}
        width="300px"
        height="60px"
        disabled={false}
      >
        Button
      </GradientButton>
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


## 3d button

**Author:** @theutkarshmail | **Used:** 157x
**URL:** https://21st.dev/@theutkarshmail/components/3d-button
**Install:** `npx shadcn@latest add "https://21st.dev/r/theutkarshmail/3d-button?api_key=$API_KEY_21ST"`
**Description:** A 3D button with animated text is a visually dynamic UI element designed to mimic real-world depth and provide interactive feedback through both its structure and the movement of its text.



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
3d-button.tsx
// Full source available at: https://21st.dev/@theutkarshmail/components/3d-button
// Or install via: npx shadcn@latest add "https://21st.dev/r/theutkarshmail/3d-button?api_key=$API_KEY_21ST"

import { Component } from "@/components/ui/3d-button";

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


## lever-switch

**Author:** @theutkarshmail | **Used:** 124x
**URL:** https://21st.dev/@theutkarshmail/components/lever-switch
**Install:** `npx shadcn@latest add "https://21st.dev/r/theutkarshmail/lever-switch?api_key=$API_KEY_21ST"`
**Description:** this a animated lever switch can be toggled on and off just like a lever or gear of a machine

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
lever-switch.tsx
// Full source available at: https://21st.dev/@theutkarshmail/components/lever-switch
// Or install via: npx shadcn@latest add "https://21st.dev/r/theutkarshmail/lever-switch?api_key=$API_KEY_21ST"

import { Component } from "@/components/ui/lever-switch";

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

