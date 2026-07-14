# 21st.dev — Backgrounds — Full Integration Prompts

Each section below is a **copy-paste ready integration prompt** for that component.
Use it directly with Claude or any AI coding tool to drop the component into your project.

---

## Shader R

**Author:** @ola.leandroaraujo
**URL:** https://21st.dev/@ola.leandroaraujo/components/shader-r

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
shader-r.tsx
// Full source: https://21st.dev/@ola.leandroaraujo/components/shader-r
// Install via: npx @21st-dev/magic add shader-r
// Or copy the component code from the 21st.dev page above.

import { ShaderBackground } from "@/components/ui/shader-r"

export default function ShaderBackgroundDemo() {
  return (
    <div className="relative h-[440px] w-full overflow-hidden rounded-xl">
      <ShaderBackground className="h-full w-full" />
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


## Silk Blend Gradient

**Author:** @amit.haski
**URL:** https://21st.dev/@amit.haski/components/silk-blend-gradient

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
silk-blend-gradient.tsx
// Full source: https://21st.dev/@amit.haski/components/silk-blend-gradient
// Install via: npx @21st-dev/magic add silk-blend-gradient
// Or copy the component code from the 21st.dev page above.

import { GradientBackground } from "@/components/ui/silk-blend-gradient"

export default function GradientBackgroundDemo() {
  return (
    <div className="relative h-[440px] w-full overflow-hidden rounded-xl">
      <GradientBackground className="h-full w-full" />
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


## Adisyon Shader

**Author:** @yaoztorun
**URL:** https://21st.dev/@yaoztorun/components/adisyon-shader

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
adisyon-shader.tsx
// Full source: https://21st.dev/@yaoztorun/components/adisyon-shader
// Install via: npx @21st-dev/magic add adisyon-shader
// Or copy the component code from the 21st.dev page above.

import { ShaderBackground } from "@/components/ui/adisyon-shader"

export default function ShaderBackgroundDemo() {
  return (
    <div className="relative h-[440px] w-full overflow-hidden rounded-xl">
      <ShaderBackground className="h-full w-full" />
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


## Waves Shader

**Author:** @notshekharsahu
**URL:** https://21st.dev/@notshekharsahu/components/waves-shader

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
waves-shader.tsx
// Full source: https://21st.dev/@notshekharsahu/components/waves-shader
// Install via: npx @21st-dev/magic add waves-shader
// Or copy the component code from the 21st.dev page above.

import { ShaderBackground } from "@/components/ui/waves-shader"

export default function ShaderBackgroundDemo() {
  return (
    <div className="relative h-[440px] w-full overflow-hidden rounded-xl">
      <ShaderBackground className="h-full w-full" />
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


## Violet Orbit

**Author:** @serafim
**URL:** https://21st.dev/@serafim/components/violet-orbit

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
violet-orbit.tsx
// Full source: https://21st.dev/@serafim/components/violet-orbit
// Install via: npx @21st-dev/magic add violet-orbit
// Or copy the component code from the 21st.dev page above.

import { GradientBackground } from "@/components/ui/violet-orbit"

export default function GradientBackgroundDemo() {
  return (
    <div className="relative h-[440px] w-full overflow-hidden rounded-xl">
      <GradientBackground className="h-full w-full" />
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


## Jade Orb

**Author:** @serafim
**URL:** https://21st.dev/@serafim/components/jade-orb

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
jade-orb.tsx
// Full source: https://21st.dev/@serafim/components/jade-orb
// Install via: npx @21st-dev/magic add jade-orb
// Or copy the component code from the 21st.dev page above.

import { GradientBackground } from "@/components/ui/jade-orb"

export default function GradientBackgroundDemo() {
  return (
    <div className="relative h-[440px] w-full overflow-hidden rounded-xl">
      <GradientBackground className="h-full w-full" />
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


## Sunset Orb

**Author:** @serafim
**URL:** https://21st.dev/@serafim/components/sunset-orb

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
sunset-orb.tsx
// Full source: https://21st.dev/@serafim/components/sunset-orb
// Install via: npx @21st-dev/magic add sunset-orb
// Or copy the component code from the 21st.dev page above.

import { GradientBackground } from "@/components/ui/sunset-orb"

export default function GradientBackgroundDemo() {
  return (
    <div className="relative h-[440px] w-full overflow-hidden rounded-xl">
      <GradientBackground className="h-full w-full" />
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


## Parallel Waves

**Author:** @serafim
**URL:** https://21st.dev/@serafim/components/parallel-waves

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
parallel-waves.tsx
// Full source: https://21st.dev/@serafim/components/parallel-waves
// Install via: npx @21st-dev/magic add parallel-waves
// Or copy the component code from the 21st.dev page above.

import { ShaderBackground } from "@/components/ui/parallel-waves"

export default function ShaderBackgroundDemo() {
  return (
    <div className="relative h-[440px] w-full overflow-hidden rounded-xl">
      <ShaderBackground className="h-full w-full" />
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


## Mirrorball

**Author:** @serafim
**URL:** https://21st.dev/@serafim/components/mirrorball

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
mirrorball.tsx
// Full source: https://21st.dev/@serafim/components/mirrorball
// Install via: npx @21st-dev/magic add mirrorball
// Or copy the component code from the 21st.dev page above.

import { AsciiArt } from "@/components/ui/mirrorball"

export default function AsciiArtDemo() {
  return (
    <div className="relative h-[440px] w-full overflow-hidden rounded-xl">
      <AsciiArt className="h-full w-full" />
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


## Gradient Animation Shadcnui

**Author:** @moumensoliman
**URL:** https://21st.dev/@moumensoliman/components/gradient-animation-shadcnui

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
gradient-animation-shadcnui.tsx
// Full source: https://21st.dev/@moumensoliman/components/gradient-animation-shadcnui
// Install via: npx @21st-dev/magic add gradient-animation-shadcnui
// Or copy the component code from the 21st.dev page above.

import GradientAnimation from "@/components/ui/gradient-animation-shadcnui";

export default function Demo() {
  return (
    <div className="flex min-h-[400px] w-full items-center justify-center">
      <GradientAnimation />
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


## Floating Gradient Shadcnui

**Author:** @moumensoliman
**URL:** https://21st.dev/@moumensoliman/components/floating-gradient-shadcnui

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
floating-gradient-shadcnui.tsx
// Full source: https://21st.dev/@moumensoliman/components/floating-gradient-shadcnui
// Install via: npx @21st-dev/magic add floating-gradient-shadcnui
// Or copy the component code from the 21st.dev page above.

import { FloatingGradient } from "@/components/ui/floating-gradient-shadcnui";

export default function Demo() {
  return (
    <div className="w-full p-8">
      <FloatingGradient />
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


## Orbit Footer

**Author:** @nexus-ui
**URL:** https://21st.dev/@nexus-ui/components/orbit-footer

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
orbit-footer.tsx
// Full source: https://21st.dev/@nexus-ui/components/orbit-footer
// Install via: npx @21st-dev/magic add orbit-footer
// Or copy the component code from the 21st.dev page above.

import OrbitFooter from "@/components/ui/orbit-footer";

export default function Demo() {
  return (
    <div className="w-full max-w-2xl p-6">
      <OrbitFooter />
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


## Mouse Wave Text

**Author:** @pacekit
**URL:** https://21st.dev/@pacekit/components/mouse-wave-text

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
mouse-wave-text.tsx
// Full source: https://21st.dev/@pacekit/components/mouse-wave-text
// Install via: npx @21st-dev/magic add mouse-wave-text
// Or copy the component code from the 21st.dev page above.

import { MouseWaveText } from "@/components/ui/mouse-wave-text";

export default function Demo() {
    return (
        <div className="flex min-h-[320px] w-full items-center justify-center">
            <MouseWaveText
                className="text-3xl font-semibold"
                textClassName="text-blue-500"
                shadowClassName="text-blue-500/20">
                Mouse Wave Text
            </MouseWaveText>
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


## Gradient Text Fill

**Author:** @grootstudio
**URL:** https://21st.dev/@grootstudio/components/gradient-text-fill

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
gradient-text-fill.tsx
// Full source: https://21st.dev/@grootstudio/components/gradient-text-fill
// Install via: npx @21st-dev/magic add gradient-text-fill
// Or copy the component code from the 21st.dev page above.

import { GradientText } from "@/components/ui/gradient-text-fill"

export default function Default() {
  return (
    <div className="flex min-h-[320px] w-full items-center justify-center p-8">
      <GradientText
        as="h1"
        className="text-6xl font-bold tracking-tight md:text-8xl"
      >
        Groot Studio
      </GradientText>
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


## Background Shapes

**Author:** @uicapsule
**URL:** https://21st.dev/@uicapsule/components/background-shapes

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
background-shapes.tsx
// Full source: https://21st.dev/@uicapsule/components/background-shapes
// Install via: npx @21st-dev/magic add background-shapes
// Or copy the component code from the 21st.dev page above.

import { BackgroundShapes } from "@/components/ui/background-shapes";

const Demo = () => {
  return (
    <div className="flex h-full min-h-[500px] w-full items-center justify-center bg-[#2164D6]">
      <BackgroundShapes width={800} height={500} colors={["white"]} />
    </div>
  );
};

export default Demo;

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


## Background Pixel Stars

**Author:** @uicapsule
**URL:** https://21st.dev/@uicapsule/components/background-pixel-stars

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
background-pixel-stars.tsx
// Full source: https://21st.dev/@uicapsule/components/background-pixel-stars
// Install via: npx @21st-dev/magic add background-pixel-stars
// Or copy the component code from the 21st.dev page above.

"use client";

import { BackgroundPixelStars } from "@/components/ui/background-pixel-stars";

const Default = () => {
  return (
    <div className="h-dvh w-dvw bg-black bg-[url('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAIAAACQkWg2AAAAIElEQVR42mIUEhJiwAbevXuHVZyJgUQwqmEUDB0AEGAADd8DEPTX6ksAAAAASUVORK5CYII=')] bg-[size:10px]">
      <BackgroundPixelStars />
    </div>
  );
};

export default Default;

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


## Waveform

**Author:** @thegridcn
**URL:** https://21st.dev/@thegridcn/components/waveform

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
waveform.tsx
// Full source: https://21st.dev/@thegridcn/components/waveform
// Install via: npx @21st-dev/magic add waveform
// Or copy the component code from the 21st.dev page above.

import { Waveform } from "@/components/ui/waveform"

export default function WaveformDemo() {
  return (
    <div className="flex min-h-[240px] items-center justify-center bg-background p-8">
      <Waveform
        label="Audio Signal"
        bars={28}
        playing
        intensity="medium"
        className="w-80"
      />
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


## Circuit Background

**Author:** @thegridcn
**URL:** https://21st.dev/@thegridcn/components/circuit-background

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
circuit-background.tsx
// Full source: https://21st.dev/@thegridcn/components/circuit-background
// Install via: npx @21st-dev/magic add circuit-background
// Or copy the component code from the 21st.dev page above.

import { CircuitBackground } from "@/components/ui/circuit-background"

export default function Default() {
  return (
    <CircuitBackground className="flex min-h-[400px] w-full items-center justify-center rounded-xl border bg-background">
      <div className="text-center">
        <h2 className="text-3xl font-bold tracking-tight">Circuit Background</h2>
        <p className="mt-2 text-muted-foreground">
          An animated circuit-board pattern behind your content.
        </p>
      </div>
    </CircuitBackground>
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


## Border Beam

**Author:** @gooseui
**URL:** https://21st.dev/@gooseui/components/border-beam

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
border-beam.tsx
// Full source: https://21st.dev/@gooseui/components/border-beam
// Install via: npx @21st-dev/magic add border-beam
// Or copy the component code from the 21st.dev page above.

import { BorderBeam } from "@/components/ui/border-beam"

export default function BorderBeamDemo() {
  return (
    <div className="flex min-h-[320px] w-full items-center justify-center p-8">
      <div className="relative w-full max-w-sm overflow-hidden rounded-xl border bg-background p-6">
        <h3 className="text-lg font-semibold text-foreground">Border Beam</h3>
        <p className="mt-1 text-sm font-medium text-muted-foreground">
          Animated border effect
        </p>
        <p className="mt-3 text-sm text-muted-foreground">
          A beam of light smoothly moves around the perimeter of the card,
          creating an impressive animation.
        </p>
        <BorderBeam />
      </div>
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


## Animated Gradient

**Author:** @componentry
**URL:** https://21st.dev/@componentry/components/animated-gradient

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
animated-gradient.tsx
// Full source: https://21st.dev/@componentry/components/animated-gradient
// Install via: npx @21st-dev/magic add animated-gradient
// Or copy the component code from the 21st.dev page above.

import { AnimatedGradient } from "@/components/ui/animated-gradient";

export default function AnimatedGradientDemo() {
  return (
    <div className="relative h-[420px] w-full max-w-2xl overflow-hidden rounded-xl">
      <AnimatedGradient config={{ preset: "Aurora" }} radius="12px" />
      <div className="relative z-10 flex h-full flex-col items-center justify-center px-6 text-center">
        <h1 className="text-5xl font-semibold leading-tight tracking-tight text-white">
          Animated
          <br />
          Gradient
        </h1>
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


## Beam Sweep Field

**Author:** @nexus-ui
**URL:** https://21st.dev/@nexus-ui/components/beam-sweep-field

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
beam-sweep-field.tsx
// Full source: https://21st.dev/@nexus-ui/components/beam-sweep-field
// Install via: npx @21st-dev/magic add beam-sweep-field
// Or copy the component code from the 21st.dev page above.

import BeamField from "@/components/ui/beam-sweep-field";

export default function Default() {
  return (
    <div className="h-96 w-full max-w-4xl p-6 [&>div]:h-full">
      <BeamField />
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


## Particles

**Author:** @scrollxui
**URL:** https://21st.dev/@scrollxui/components/particles

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
particles.tsx
// Full source: https://21st.dev/@scrollxui/components/particles
// Install via: npx @21st-dev/magic add particles
// Or copy the component code from the 21st.dev page above.

import { Particles } from "@/components/ui/particles";

export default function ParticlesDemo() {
  return (
    <div className="relative bg-black w-full h-100 overflow-hidden">
      <Particles
        color="#ffffff"
        particleCount={25000}
        particleSize={5}
        animate={false}
        className="z-0"
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


## Aurora Background

**Author:** @pulkitxm
**URL:** https://21st.dev/@pulkitxm/components/aurora-background

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
aurora-background.tsx
// Full source: https://21st.dev/@pulkitxm/components/aurora-background
// Install via: npx @21st-dev/magic add aurora-background
// Or copy the component code from the 21st.dev page above.

import { AuroraBackground } from "@/components/ui/aurora-background";

export default function AuroraBackgroundDemo() {
  return (
    <AuroraBackground
      variant="sunset"
      className="flex h-[400px] w-full items-center justify-center rounded-xl"
      childrenClassName="flex flex-col items-center justify-center gap-4 text-center px-6"
    >
      <h1 className="text-4xl font-bold text-white drop-shadow-lg md:text-6xl">
        Aurora Background
      </h1>
      <p className="max-w-md text-lg text-white/80">
        A living, animated canvas backdrop with multiple color variants.
      </p>
    </AuroraBackground>
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


## Perlin Noise

**Author:** @reshaped
**URL:** https://21st.dev/@reshaped/components/perlin-noise

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
perlin-noise.tsx
// Full source: https://21st.dev/@reshaped/components/perlin-noise
// Install via: npx @21st-dev/magic add perlin-noise
// Or copy the component code from the 21st.dev page above.

import { useCallback, useEffect, useRef, useState } from "react";
import PerlinNoise, { perlinNoisePresets } from "@/components/ui/perlin-noise";

const MONO = '"Paper Mono", ui-monospace, SFMono-Regular, Menlo, monospace';

type ControlDef = {
  kind: "color" | "slider" | "select" | "checkbox";
  key: string;
  min?: number;
  max?: number;
  step?: number;
  int?: boolean;
  options?: string[];
};

const CONTROLS: ControlDef[] = [
  {
    kind: "color",
    key: "colorBack"
  },
  {
    kind: "color",
    key: "colorFront"
  },
  {
    kind: "slider",
    key: "proportion",
    min: 0,
    max: 1,
    step: 0.01
  },
  {
    kind: "slider",
    key: "softness",
    min: 0,
    max: 1,
    step: 0.01
  },
  {
    kind: "slider",
    key: "octaveCount",
    min: 1,
    max: 8,
    step: 1,
    int: true
  },
  {
    kind: "slider",
    key: "persistence",
    min: 0.3,
    max: 1,
    step: 0.01
  },
  {
    kind: "slider",
    key: "lacunarity",
    min: 1.5,
    max: 10,
    step: 0.01
  },
  {
    kind: "slider",
    key: "speed",
    min: 0,
    max: 0.5,
    step: 0.01
  },
  {
    kind: "slider",
    key: "scale",
    min: 0.01,
    max: 4,
    step: 0.01
  },
  {
    kind: "slider",
    key: "rotation",
    min: 0,
    max: 360,
    step: 1,
    int: true
  }
];

const PARAM_KEYS = ["colorBack","colorFront","proportion","softness","octaveCount","persistence","lacunarity","speed","scale","rotation"];

type Params = Record<string, string | number | boolean>;

function pickParams(source: Record<string, unknown>): Params {
  const out: Params = {};
  for (const k of PARAM_KEYS) out[k] = source[k] as string | number | boolean;
  return out;
}

const DEFAULTS = pickParams(perlinNoisePresets[0].params as Record<string, unknown>);

function fmt(value: number, def: ControlDef) {
  return def.int ? String(Math.round(value)) : Number(value).toFixed(2);
}

function Row({ label, children }: { label: string; children: React.ReactNode }) {
  return (
    <div style={{ display: "flex", alignItems: "center", gap: 8, height: 26 }}>
      <div style={{ width: 104, flexShrink: 0, fontSize: 11, color: "#222" }}>{label}</div>
      <div style={{ flex: 1, display: "flex", alignItems: "center", gap: 8 }}>{children}</div>
    </div>
  );
}

function ValueBox({ children }: { children: React.ReactNode }) {
  return (
    <div
      style={{
        width: 58, flexShrink: 0, height: 24, borderRadius: 3,
        background: "rgba(0,0,0,0.055)", display: "flex", alignItems: "center",
        justifyContent: "flex-end", padding: "0 8px", fontSize: 11, color: "#222",
      }}
    >
      {children}
    </div>
  );
}

function Slider({ def, value, onChange }: { def: ControlDef; value: number; onChange: (v: number) => void }) {
  const min = def.min ?? 0;
  const max = def.max ?? 1;
  const pct = Math.min(100, Math.max(0, ((value - min) / (max - min)) * 100));
  return (
    <>
      <div style={{ position: "relative", flex: 1, height: 24, display: "flex", alignItems: "center" }}>
        <div style={{ position: "absolute", left: 0, right: 0, height: 2, borderRadius: 1, background: "rgba(0,0,0,0.14)" }} />
        <div style={{ position: "absolute", left: 0, width: `${pct}%`, height: 2, borderRadius: 1, background: "#999997" }} />
        <div style={{ position: "absolute", left: `calc(${pct}% - 2.5px)`, width: 5, height: 12, borderRadius: 1, background: "#77756f" }} />
        <input
          type="range"
          min={min}
          max={max}
          step={def.step ?? 0.01}
          value={value}
          onChange={(e) => onChange(Number(e.target.value))}
          aria-label={def.key}
          style={{ position: "absolute", inset: 0, width: "100%", opacity: 0, cursor: "ew-resize" }}
        />
      </div>
      <ValueBox>{fmt(value, def)}</ValueBox>
    </>
  );
}

function ColorRow({ label, value, onChange }: { label: string; value: string; onChange: (v: string) => void }) {
  const [text, setText] = useState(value);
  useEffect(() => setText(value), [value]);
  const commit = () => {
    if (/^#([0-9a-fA-F]{3,4}|[0-9a-fA-F]{6}|[0-9a-fA-F]{8})$/.test(text)) onChange(text);
    else setText(value);
  };
  return (
    <Row label={label}>
      <label
        style={{
          position: "relative", width: 24, height: 24, flexShrink: 0, borderRadius: 3,
          background: value, boxShadow: "inset 0 0 0 1px rgba(0,0,0,0.12)", cursor: "pointer",
        }}
      >
        <input
          type="color"
          value={/^#[0-9a-fA-F]{6}/.test(value) ? value.slice(0, 7) : "#000000"}
          onChange={(e) => onChange(e.target.value)}
          aria-label={`${label} color`}
          style={{ position: "absolute", inset: 0, width: "100%", height: "100%", opacity: 0, cursor: "pointer" }}
        />
      </label>
      <div style={{ flex: 1, height: 24, borderRadius: 3, background: "rgba(0,0,0,0.055)", display: "flex", alignItems: "center", padding: "0 8px" }}>
        <input
          value={text}
          onChange={(e) => setText(e.target.value)}
          onBlur={commit}
          onKeyDown={(e) => e.key === "Enter" && commit()}
          aria-label={`${label} value`}
          style={{ width: "100%", background: "transparent", border: 0, outline: "none", fontSize: 11, color: "#222", fontFamily: MONO }}
        />
      </div>
    </Row>
  );
}

function SelectRow({ label, value, options, onChange }: { label: string; value: string; options: string[]; onChange: (v: string) => void }) {
  return (
    <Row label={label}>
      <div style={{ position: "relative", flex: 1 }}>
        <select
          value={value}
          onChange={(e) => onChange(e.target.value)}
          aria-label={label}
          style={{
            width: "100%", height: 24, borderRadius: 3, border: 0,
            background: "rgba(0,0,0,0.055)", fontSize: 11, color: "#222",
            fontFamily: MONO, padding: "0 8px", appearance: "none", cursor: "pointer",
          }}
        >
          {options.map((o) => (
            <option key={o} value={o}>{o}</option>
          ))}
        </select>
        <div style={{ position: "absolute", right: 8, top: 9, pointerEvents: "none", borderLeft: "4px solid transparent", borderRight: "4px solid transparent", borderTop: "5px solid #222" }} />
      </div>
    </Row>
  );
}

function PanelButton({ children, onClick }: { children: React.ReactNode; onClick: () => void }) {
  const [hover, setHover] = useState(false);
  return (
    <button
      onClick={onClick}
      onMouseEnter={() => setHover(true)}
      onMouseLeave={() => setHover(false)}
      style={{
        height: 24, borderRadius: 3, border: 0, cursor: "pointer",
        background: hover ? "#8a8a88" : "#999997", color: "#fefefe",
        fontSize: 11, fontFamily: MONO, letterSpacing: "0.2px",
      }}
    >
      {children}
    </button>
  );
}

export default function PerlinNoiseDemo() {
  const [params, setParams] = useState<Params>({ ...DEFAULTS });


  const set = (key: string, value: string | number | boolean) => setParams((p) => ({ ...p, [key]: value }));

  const applyPreset = (presetParams: Record<string, unknown>) => {
    setParams(pickParams(presetParams));
  };

  return (
    <div
      style={{
        display: "flex", alignItems: "stretch", gap: 32, width: "100%", minHeight: "100vh",
        padding: 32, background: "#f8f8f6", fontFamily: MONO, boxSizing: "border-box",
      }}
    >
      <div style={{ flex: 1, minHeight: 480, display: "flex", minWidth: 0 }}>
        <PerlinNoise {...(params as object)} style={{ width: "100%", height: "100%" }} />
      </div>

      <div
        style={{
          width: 300, flexShrink: 0, alignSelf: "flex-start", borderRadius: 12,
          background: "#f4f3eb", padding: "12px 12px 14px",
          boxShadow:
            "0px 4px 40px -8px rgba(58,34,17,0.1), 0px 12px 20px -8px rgba(58,34,17,0.2), 0px 0px 0px 1px rgba(58,34,17,0.1)",
        }}
      >
        <div style={{ fontSize: 11, color: "#222", padding: "2px 0 8px" }}>Presets</div>
        <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 8 }}>
          {perlinNoisePresets.map((preset) => (
            <PanelButton key={preset.name} onClick={() => applyPreset(preset.params as Record<string, unknown>)}>
              {preset.name}
            </PanelButton>
          ))}
        </div>

        <div style={{ height: 1, background: "rgba(0,0,0,0.08)", margin: "12px 0" }} />

        <div style={{ display: "flex", flexDirection: "column", gap: 2 }}>
          {CONTROLS.map((def) => {
            if (def.kind === "color")
              return <ColorRow key={def.key} label={def.key} value={String(params[def.key])} onChange={(v) => set(def.key, v)} />;
            if (def.kind === "select")
              return <SelectRow key={def.key} label={def.key} value={String(params[def.key])} options={def.options ?? []} onChange={(v) => set(def.key, v)} />;
            return (
              <Row key={def.key} label={def.key}>
                <Slider def={def} value={Number(params[def.key])} onChange={(v) => set(def.key, v)} />
              </Row>
            );
          })}
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


## Neuro Noise

**Author:** @paper-design
**URL:** https://21st.dev/@paper-design/components/neuro-noise

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
neuro-noise.tsx
// Full source: https://21st.dev/@paper-design/components/neuro-noise
// Install via: npx @21st-dev/magic add neuro-noise
// Or copy the component code from the 21st.dev page above.

import { useCallback, useEffect, useRef, useState } from "react";
import NeuroNoise, { neuroNoisePresets } from "@/components/ui/neuro-noise";

const MONO = '"Paper Mono", ui-monospace, SFMono-Regular, Menlo, monospace';

type ControlDef = {
  kind: "color" | "slider" | "select" | "checkbox";
  key: string;
  min?: number;
  max?: number;
  step?: number;
  int?: boolean;
  options?: string[];
};

const CONTROLS: ControlDef[] = [
  {
    kind: "color",
    key: "colorFront"
  },
  {
    kind: "color",
    key: "colorMid"
  },
  {
    kind: "color",
    key: "colorBack"
  },
  {
    kind: "slider",
    key: "brightness",
    min: 0,
    max: 1,
    step: 0.01
  },
  {
    kind: "slider",
    key: "contrast",
    min: 0,
    max: 1,
    step: 0.01
  },
  {
    kind: "slider",
    key: "speed",
    min: 0,
    max: 2,
    step: 0.01
  },
  {
    kind: "slider",
    key: "scale",
    min: 0.01,
    max: 4,
    step: 0.01
  },
  {
    kind: "slider",
    key: "rotation",
    min: 0,
    max: 360,
    step: 1,
    int: true
  }
];

const PARAM_KEYS = ["colorFront","colorMid","colorBack","brightness","contrast","speed","scale","rotation"];

type Params = Record<string, string | number | boolean>;

function pickParams(source: Record<string, unknown>): Params {
  const out: Params = {};
  for (const k of PARAM_KEYS) out[k] = source[k] as string | number | boolean;
  return out;
}

const DEFAULTS = pickParams(neuroNoisePresets[0].params as Record<string, unknown>);

function fmt(value: number, def: ControlDef) {
  return def.int ? String(Math.round(value)) : Number(value).toFixed(2);
}

function Row({ label, children }: { label: string; children: React.ReactNode }) {
  return (
    <div style={{ display: "flex", alignItems: "center", gap: 8, height: 26 }}>
      <div style={{ width: 104, flexShrink: 0, fontSize: 11, color: "#222" }}>{label}</div>
      <div style={{ flex: 1, display: "flex", alignItems: "center", gap: 8 }}>{children}</div>
    </div>
  );
}

function ValueBox({ children }: { children: React.ReactNode }) {
  return (
    <div
      style={{
        width: 58, flexShrink: 0, height: 24, borderRadius: 3,
        background: "rgba(0,0,0,0.055)", display: "flex", alignItems: "center",
        justifyContent: "flex-end", padding: "0 8px", fontSize: 11, color: "#222",
      }}
    >
      {children}
    </div>
  );
}

function Slider({ def, value, onChange }: { def: ControlDef; value: number; onChange: (v: number) => void }) {
  const min = def.min ?? 0;
  const max = def.max ?? 1;
  const pct = Math.min(100, Math.max(0, ((value - min) / (max - min)) * 100));
  return (
    <>
      <div style={{ position: "relative", flex: 1, height: 24, display: "flex", alignItems: "center" }}>
        <div style={{ position: "absolute", left: 0, right: 0, height: 2, borderRadius: 1, background: "rgba(0,0,0,0.14)" }} />
        <div style={{ position: "absolute", left: 0, width: `${pct}%`, height: 2, borderRadius: 1, background: "#999997" }} />
        <div style={{ position: "absolute", left: `calc(${pct}% - 2.5px)`, width: 5, height: 12, borderRadius: 1, background: "#77756f" }} />
        <input
          type="range"
          min={min}
          max={max}
          step={def.step ?? 0.01}
          value={value}
          onChange={(e) => onChange(Number(e.target.value))}
          aria-label={def.key}
          style={{ position: "absolute", inset: 0, width: "100%", opacity: 0, cursor: "ew-resize" }}
        />
      </div>
      <ValueBox>{fmt(value, def)}</ValueBox>
    </>
  );
}

function ColorRow({ label, value, onChange }: { label: string; value: string; onChange: (v: string) => void }) {
  const [text, setText] = useState(value);
  useEffect(() => setText(value), [value]);
  const commit = () => {
    if (/^#([0-9a-fA-F]{3,4}|[0-9a-fA-F]{6}|[0-9a-fA-F]{8})$/.test(text)) onChange(text);
    else setText(value);
  };
  return (
    <Row label={label}>
      <label
        style={{
          position: "relative", width: 24, height: 24, flexShrink: 0, borderRadius: 3,
          background: value, boxShadow: "inset 0 0 0 1px rgba(0,0,0,0.12)", cursor: "pointer",
        }}
      >
        <input
          type="color"
          value={/^#[0-9a-fA-F]{6}/.test(value) ? value.slice(0, 7) : "#000000"}
          onChange={(e) => onChange(e.target.value)}
          aria-label={`${label} color`}
          style={{ position: "absolute", inset: 0, width: "100%", height: "100%", opacity: 0, cursor: "pointer" }}
        />
      </label>
      <div style={{ flex: 1, height: 24, borderRadius: 3, background: "rgba(0,0,0,0.055)", display: "flex", alignItems: "center", padding: "0 8px" }}>
        <input
          value={text}
          onChange={(e) => setText(e.target.value)}
          onBlur={commit}
          onKeyDown={(e) => e.key === "Enter" && commit()}
          aria-label={`${label} value`}
          style={{ width: "100%", background: "transparent", border: 0, outline: "none", fontSize: 11, color: "#222", fontFamily: MONO }}
        />
      </div>
    </Row>
  );
}

function SelectRow({ label, value, options, onChange }: { label: string; value: string; options: string[]; onChange: (v: string) => void }) {
  return (
    <Row label={label}>
      <div style={{ position: "relative", flex: 1 }}>
        <select
          value={value}
          onChange={(e) => onChange(e.target.value)}
          aria-label={label}
          style={{
            width: "100%", height: 24, borderRadius: 3, border: 0,
            background: "rgba(0,0,0,0.055)", fontSize: 11, color: "#222",
            fontFamily: MONO, padding: "0 8px", appearance: "none", cursor: "pointer",
          }}
        >
          {options.map((o) => (
            <option key={o} value={o}>{o}</option>
          ))}
        </select>
        <div style={{ position: "absolute", right: 8, top: 9, pointerEvents: "none", borderLeft: "4px solid transparent", borderRight: "4px solid transparent", borderTop: "5px solid #222" }} />
      </div>
    </Row>
  );
}

function PanelButton({ children, onClick }: { children: React.ReactNode; onClick: () => void }) {
  const [hover, setHover] = useState(false);
  return (
    <button
      onClick={onClick}
      onMouseEnter={() => setHover(true)}
      onMouseLeave={() => setHover(false)}
      style={{
        height: 24, borderRadius: 3, border: 0, cursor: "pointer",
        background: hover ? "#8a8a88" : "#999997", color: "#fefefe",
        fontSize: 11, fontFamily: MONO, letterSpacing: "0.2px",
      }}
    >
      {children}
    </button>
  );
}

export default function NeuroNoiseDemo() {
  const [params, setParams] = useState<Params>({ ...DEFAULTS });


  const set = (key: string, value: string | number | boolean) => setParams((p) => ({ ...p, [key]: value }));

  const applyPreset = (presetParams: Record<string, unknown>) => {
    setParams(pickParams(presetParams));
  };

  return (
    <div
      style={{
        display: "flex", alignItems: "stretch", gap: 32, width: "100%", minHeight: "100vh",
        padding: 32, background: "#f8f8f6", fontFamily: MONO, boxSizing: "border-box",
      }}
    >
      <div style={{ flex: 1, minHeight: 480, display: "flex", minWidth: 0 }}>
        <NeuroNoise {...(params as object)} style={{ width: "100%", height: "100%" }} />
      </div>

      <div
        style={{
          width: 300, flexShrink: 0, alignSelf: "flex-start", borderRadius: 12,
          background: "#f4f3eb", padding: "12px 12px 14px",
          boxShadow:
            "0px 4px 40px -8px rgba(58,34,17,0.1), 0px 12px 20px -8px rgba(58,34,17,0.2), 0px 0px 0px 1px rgba(58,34,17,0.1)",
        }}
      >
        <div style={{ fontSize: 11, color: "#222", padding: "2px 0 8px" }}>Presets</div>
        <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 8 }}>
          {neuroNoisePresets.map((preset) => (
            <PanelButton key={preset.name} onClick={() => applyPreset(preset.params as Record<string, unknown>)}>
              {preset.name}
            </PanelButton>
          ))}
        </div>

        <div style={{ height: 1, background: "rgba(0,0,0,0.08)", margin: "12px 0" }} />

        <div style={{ display: "flex", flexDirection: "column", gap: 2 }}>
          {CONTROLS.map((def) => {
            if (def.kind === "color")
              return <ColorRow key={def.key} label={def.key} value={String(params[def.key])} onChange={(v) => set(def.key, v)} />;
            if (def.kind === "select")
              return <SelectRow key={def.key} label={def.key} value={String(params[def.key])} options={def.options ?? []} onChange={(v) => set(def.key, v)} />;
            return (
              <Row key={def.key} label={def.key}>
                <Slider def={def} value={Number(params[def.key])} onChange={(v) => set(def.key, v)} />
              </Row>
            );
          })}
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


## Paper Waves

**Author:** @paper-design
**URL:** https://21st.dev/@paper-design/components/paper-waves

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
paper-waves.tsx
// Full source: https://21st.dev/@paper-design/components/paper-waves
// Install via: npx @21st-dev/magic add paper-waves
// Or copy the component code from the 21st.dev page above.

import { useCallback, useEffect, useRef, useState } from "react";
import Waves, { wavesPresets } from "@/components/ui/paper-waves";

const MONO = '"Paper Mono", ui-monospace, SFMono-Regular, Menlo, monospace';

type ControlDef = {
  kind: "color" | "slider" | "select" | "checkbox";
  key: string;
  min?: number;
  max?: number;
  step?: number;
  int?: boolean;
  options?: string[];
};

const CONTROLS: ControlDef[] = [
  {
    kind: "color",
    key: "colorBack"
  },
  {
    kind: "color",
    key: "colorFront"
  },
  {
    kind: "slider",
    key: "frequency",
    min: 0,
    max: 2,
    step: 0.01
  },
  {
    kind: "slider",
    key: "amplitude",
    min: 0,
    max: 1,
    step: 0.01
  },
  {
    kind: "slider",
    key: "spacing",
    min: 0,
    max: 2,
    step: 0.01
  },
  {
    kind: "slider",
    key: "proportion",
    min: 0,
    max: 1,
    step: 0.01
  },
  {
    kind: "slider",
    key: "softness",
    min: 0,
    max: 1,
    step: 0.01
  },
  {
    kind: "slider",
    key: "shape",
    min: 0,
    max: 3,
    step: 1,
    int: true
  },
  {
    kind: "slider",
    key: "scale",
    min: 0.01,
    max: 4,
    step: 0.01
  },
  {
    kind: "slider",
    key: "rotation",
    min: 0,
    max: 360,
    step: 1,
    int: true
  }
];

const PARAM_KEYS = ["colorBack","colorFront","frequency","amplitude","spacing","proportion","softness","shape","scale","rotation"];

type Params = Record<string, string | number | boolean>;

function pickParams(source: Record<string, unknown>): Params {
  const out: Params = {};
  for (const k of PARAM_KEYS) out[k] = source[k] as string | number | boolean;
  return out;
}

const DEFAULTS = pickParams(wavesPresets[0].params as Record<string, unknown>);

function fmt(value: number, def: ControlDef) {
  return def.int ? String(Math.round(value)) : Number(value).toFixed(2);
}

function Row({ label, children }: { label: string; children: React.ReactNode }) {
  return (
    <div style={{ display: "flex", alignItems: "center", gap: 8, height: 26 }}>
      <div style={{ width: 104, flexShrink: 0, fontSize: 11, color: "#222" }}>{label}</div>
      <div style={{ flex: 1, display: "flex", alignItems: "center", gap: 8 }}>{children}</div>
    </div>
  );
}

function ValueBox({ children }: { children: React.ReactNode }) {
  return (
    <div
      style={{
        width: 58, flexShrink: 0, height: 24, borderRadius: 3,
        background: "rgba(0,0,0,0.055)", display: "flex", alignItems: "center",
        justifyContent: "flex-end", padding: "0 8px", fontSize: 11, color: "#222",
      }}
    >
      {children}
    </div>
  );
}

function Slider({ def, value, onChange }: { def: ControlDef; value: number; onChange: (v: number) => void }) {
  const min = def.min ?? 0;
  const max = def.max ?? 1;
  const pct = Math.min(100, Math.max(0, ((value - min) / (max - min)) * 100));
  return (
    <>
      <div style={{ position: "relative", flex: 1, height: 24, display: "flex", alignItems: "center" }}>
        <div style={{ position: "absolute", left: 0, right: 0, height: 2, borderRadius: 1, background: "rgba(0,0,0,0.14)" }} />
        <div style={{ position: "absolute", left: 0, width: `${pct}%`, height: 2, borderRadius: 1, background: "#999997" }} />
        <div style={{ position: "absolute", left: `calc(${pct}% - 2.5px)`, width: 5, height: 12, borderRadius: 1, background: "#77756f" }} />
        <input
          type="range"
          min={min}
          max={max}
          step={def.step ?? 0.01}
          value={value}
          onChange={(e) => onChange(Number(e.target.value))}
          aria-label={def.key}
          style={{ position: "absolute", inset: 0, width: "100%", opacity: 0, cursor: "ew-resize" }}
        />
      </div>
      <ValueBox>{fmt(value, def)}</ValueBox>
    </>
  );
}

function ColorRow({ label, value, onChange }: { label: string; value: string; onChange: (v: string) => void }) {
  const [text, setText] = useState(value);
  useEffect(() => setText(value), [value]);
  const commit = () => {
    if (/^#([0-9a-fA-F]{3,4}|[0-9a-fA-F]{6}|[0-9a-fA-F]{8})$/.test(text)) onChange(text);
    else setText(value);
  };
  return (
    <Row label={label}>
      <label
        style={{
          position: "relative", width: 24, height: 24, flexShrink: 0, borderRadius: 3,
          background: value, boxShadow: "inset 0 0 0 1px rgba(0,0,0,0.12)", cursor: "pointer",
        }}
      >
        <input
          type="color"
          value={/^#[0-9a-fA-F]{6}/.test(value) ? value.slice(0, 7) : "#000000"}
          onChange={(e) => onChange(e.target.value)}
          aria-label={`${label} color`}
          style={{ position: "absolute", inset: 0, width: "100%", height: "100%", opacity: 0, cursor: "pointer" }}
        />
      </label>
      <div style={{ flex: 1, height: 24, borderRadius: 3, background: "rgba(0,0,0,0.055)", display: "flex", alignItems: "center", padding: "0 8px" }}>
        <input
          value={text}
          onChange={(e) => setText(e.target.value)}
          onBlur={commit}
          onKeyDown={(e) => e.key === "Enter" && commit()}
          aria-label={`${label} value`}
          style={{ width: "100%", background: "transparent", border: 0, outline: "none", fontSize: 11, color: "#222", fontFamily: MONO }}
        />
      </div>
    </Row>
  );
}

function SelectRow({ label, value, options, onChange }: { label: string; value: string; options: string[]; onChange: (v: string) => void }) {
  return (
    <Row label={label}>
      <div style={{ position: "relative", flex: 1 }}>
        <select
          value={value}
          onChange={(e) => onChange(e.target.value)}
          aria-label={label}
          style={{
            width: "100%", height: 24, borderRadius: 3, border: 0,
            background: "rgba(0,0,0,0.055)", fontSize: 11, color: "#222",
            fontFamily: MONO, padding: "0 8px", appearance: "none", cursor: "pointer",
          }}
        >
          {options.map((o) => (
            <option key={o} value={o}>{o}</option>
          ))}
        </select>
        <div style={{ position: "absolute", right: 8, top: 9, pointerEvents: "none", borderLeft: "4px solid transparent", borderRight: "4px solid transparent", borderTop: "5px solid #222" }} />
      </div>
    </Row>
  );
}

function PanelButton({ children, onClick }: { children: React.ReactNode; onClick: () => void }) {
  const [hover, setHover] = useState(false);
  return (
    <button
      onClick={onClick}
      onMouseEnter={() => setHover(true)}
      onMouseLeave={() => setHover(false)}
      style={{
        height: 24, borderRadius: 3, border: 0, cursor: "pointer",
        background: hover ? "#8a8a88" : "#999997", color: "#fefefe",
        fontSize: 11, fontFamily: MONO, letterSpacing: "0.2px",
      }}
    >
      {children}
    </button>
  );
}

export default function WavesDemo() {
  const [params, setParams] = useState<Params>({ ...DEFAULTS });


  const set = (key: string, value: string | number | boolean) => setParams((p) => ({ ...p, [key]: value }));

  const applyPreset = (presetParams: Record<string, unknown>) => {
    setParams(pickParams(presetParams));
  };

  return (
    <div
      style={{
        display: "flex", alignItems: "stretch", gap: 32, width: "100%", minHeight: "100vh",
        padding: 32, background: "#f8f8f6", fontFamily: MONO, boxSizing: "border-box",
      }}
    >
      <div style={{ flex: 1, minHeight: 480, display: "flex", minWidth: 0 }}>
        <Waves {...(params as object)} style={{ width: "100%", height: "100%" }} />
      </div>

      <div
        style={{
          width: 300, flexShrink: 0, alignSelf: "flex-start", borderRadius: 12,
          background: "#f4f3eb", padding: "12px 12px 14px",
          boxShadow:
            "0px 4px 40px -8px rgba(58,34,17,0.1), 0px 12px 20px -8px rgba(58,34,17,0.2), 0px 0px 0px 1px rgba(58,34,17,0.1)",
        }}
      >
        <div style={{ fontSize: 11, color: "#222", padding: "2px 0 8px" }}>Presets</div>
        <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 8 }}>
          {wavesPresets.map((preset) => (
            <PanelButton key={preset.name} onClick={() => applyPreset(preset.params as Record<string, unknown>)}>
              {preset.name}
            </PanelButton>
          ))}
        </div>

        <div style={{ height: 1, background: "rgba(0,0,0,0.08)", margin: "12px 0" }} />

        <div style={{ display: "flex", flexDirection: "column", gap: 2 }}>
          {CONTROLS.map((def) => {
            if (def.kind === "color")
              return <ColorRow key={def.key} label={def.key} value={String(params[def.key])} onChange={(v) => set(def.key, v)} />;
            if (def.kind === "select")
              return <SelectRow key={def.key} label={def.key} value={String(params[def.key])} options={def.options ?? []} onChange={(v) => set(def.key, v)} />;
            return (
              <Row key={def.key} label={def.key}>
                <Slider def={def} value={Number(params[def.key])} onChange={(v) => set(def.key, v)} />
              </Row>
            );
          })}
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


## Dot Orbit

**Author:** @paper-design
**URL:** https://21st.dev/@paper-design/components/dot-orbit

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
dot-orbit.tsx
// Full source: https://21st.dev/@paper-design/components/dot-orbit
// Install via: npx @21st-dev/magic add dot-orbit
// Or copy the component code from the 21st.dev page above.

import { useCallback, useEffect, useRef, useState } from "react";
import DotOrbit, { dotOrbitPresets } from "@/components/ui/dot-orbit";

const MONO = '"Paper Mono", ui-monospace, SFMono-Regular, Menlo, monospace';

type ControlDef = {
  kind: "color" | "slider" | "select" | "checkbox";
  key: string;
  min?: number;
  max?: number;
  step?: number;
  int?: boolean;
  options?: string[];
};

const CONTROLS: ControlDef[] = [
  {
    kind: "color",
    key: "colorBack"
  },
  {
    kind: "slider",
    key: "stepsPerColor",
    min: 1,
    max: 4,
    step: 1,
    int: true
  },
  {
    kind: "slider",
    key: "size",
    min: 0,
    max: 1,
    step: 0.01
  },
  {
    kind: "slider",
    key: "sizeRange",
    min: 0,
    max: 1,
    step: 0.01
  },
  {
    kind: "slider",
    key: "spreading",
    min: 0,
    max: 1,
    step: 0.01
  },
  {
    kind: "slider",
    key: "speed",
    min: 0,
    max: 20,
    step: 0.01
  },
  {
    kind: "slider",
    key: "scale",
    min: 0.01,
    max: 5,
    step: 0.01
  }
];

const PARAM_KEYS = ["colorBack","stepsPerColor","size","sizeRange","spreading","speed","scale"];

type Params = Record<string, string | number | boolean>;

function pickParams(source: Record<string, unknown>): Params {
  const out: Params = {};
  for (const k of PARAM_KEYS) out[k] = source[k] as string | number | boolean;
  return out;
}

const DEFAULTS = pickParams(dotOrbitPresets[0].params as Record<string, unknown>);

function fmt(value: number, def: ControlDef) {
  return def.int ? String(Math.round(value)) : Number(value).toFixed(2);
}

function Row({ label, children }: { label: string; children: React.ReactNode }) {
  return (
    <div style={{ display: "flex", alignItems: "center", gap: 8, height: 26 }}>
      <div style={{ width: 104, flexShrink: 0, fontSize: 11, color: "#222" }}>{label}</div>
      <div style={{ flex: 1, display: "flex", alignItems: "center", gap: 8 }}>{children}</div>
    </div>
  );
}

function ValueBox({ children }: { children: React.ReactNode }) {
  return (
    <div
      style={{
        width: 58, flexShrink: 0, height: 24, borderRadius: 3,
        background: "rgba(0,0,0,0.055)", display: "flex", alignItems: "center",
        justifyContent: "flex-end", padding: "0 8px", fontSize: 11, color: "#222",
      }}
    >
      {children}
    </div>
  );
}

function Slider({ def, value, onChange }: { def: ControlDef; value: number; onChange: (v: number) => void }) {
  const min = def.min ?? 0;
  const max = def.max ?? 1;
  const pct = Math.min(100, Math.max(0, ((value - min) / (max - min)) * 100));
  return (
    <>
      <div style={{ position: "relative", flex: 1, height: 24, display: "flex", alignItems: "center" }}>
        <div style={{ position: "absolute", left: 0, right: 0, height: 2, borderRadius: 1, background: "rgba(0,0,0,0.14)" }} />
        <div style={{ position: "absolute", left: 0, width: `${pct}%`, height: 2, borderRadius: 1, background: "#999997" }} />
        <div style={{ position: "absolute", left: `calc(${pct}% - 2.5px)`, width: 5, height: 12, borderRadius: 1, background: "#77756f" }} />
        <input
          type="range"
          min={min}
          max={max}
          step={def.step ?? 0.01}
          value={value}
          onChange={(e) => onChange(Number(e.target.value))}
          aria-label={def.key}
          style={{ position: "absolute", inset: 0, width: "100%", opacity: 0, cursor: "ew-resize" }}
        />
      </div>
      <ValueBox>{fmt(value, def)}</ValueBox>
    </>
  );
}

function ColorRow({ label, value, onChange }: { label: string; value: string; onChange: (v: string) => void }) {
  const [text, setText] = useState(value);
  useEffect(() => setText(value), [value]);
  const commit = () => {
    if (/^#([0-9a-fA-F]{3,4}|[0-9a-fA-F]{6}|[0-9a-fA-F]{8})$/.test(text)) onChange(text);
    else setText(value);
  };
  return (
    <Row label={label}>
      <label
        style={{
          position: "relative", width: 24, height: 24, flexShrink: 0, borderRadius: 3,
          background: value, boxShadow: "inset 0 0 0 1px rgba(0,0,0,0.12)", cursor: "pointer",
        }}
      >
        <input
          type="color"
          value={/^#[0-9a-fA-F]{6}/.test(value) ? value.slice(0, 7) : "#000000"}
          onChange={(e) => onChange(e.target.value)}
          aria-label={`${label} color`}
          style={{ position: "absolute", inset: 0, width: "100%", height: "100%", opacity: 0, cursor: "pointer" }}
        />
      </label>
      <div style={{ flex: 1, height: 24, borderRadius: 3, background: "rgba(0,0,0,0.055)", display: "flex", alignItems: "center", padding: "0 8px" }}>
        <input
          value={text}
          onChange={(e) => setText(e.target.value)}
          onBlur={commit}
          onKeyDown={(e) => e.key === "Enter" && commit()}
          aria-label={`${label} value`}
          style={{ width: "100%", background: "transparent", border: 0, outline: "none", fontSize: 11, color: "#222", fontFamily: MONO }}
        />
      </div>
    </Row>
  );
}

function SelectRow({ label, value, options, onChange }: { label: string; value: string; options: string[]; onChange: (v: string) => void }) {
  return (
    <Row label={label}>
      <div style={{ position: "relative", flex: 1 }}>
        <select
          value={value}
          onChange={(e) => onChange(e.target.value)}
          aria-label={label}
          style={{
            width: "100%", height: 24, borderRadius: 3, border: 0,
            background: "rgba(0,0,0,0.055)", fontSize: 11, color: "#222",
            fontFamily: MONO, padding: "0 8px", appearance: "none", cursor: "pointer",
          }}
        >
          {options.map((o) => (
            <option key={o} value={o}>{o}</option>
          ))}
        </select>
        <div style={{ position: "absolute", right: 8, top: 9, pointerEvents: "none", borderLeft: "4px solid transparent", borderRight: "4px solid transparent", borderTop: "5px solid #222" }} />
      </div>
    </Row>
  );
}

function PanelButton({ children, onClick }: { children: React.ReactNode; onClick: () => void }) {
  const [hover, setHover] = useState(false);
  return (
    <button
      onClick={onClick}
      onMouseEnter={() => setHover(true)}
      onMouseLeave={() => setHover(false)}
      style={{
        height: 24, borderRadius: 3, border: 0, cursor: "pointer",
        background: hover ? "#8a8a88" : "#999997", color: "#fefefe",
        fontSize: 11, fontFamily: MONO, letterSpacing: "0.2px",
      }}
    >
      {children}
    </button>
  );
}

export default function DotOrbitDemo() {
  const [params, setParams] = useState<Params>({ ...DEFAULTS });
  const [colors, setColors] = useState<string[]>(
    (dotOrbitPresets[0].params as Record<string, unknown>).colors as string[],
  );


  const set = (key: string, value: string | number | boolean) => setParams((p) => ({ ...p, [key]: value }));

  const applyPreset = (presetParams: Record<string, unknown>) => {
    setParams(pickParams(presetParams));
    const presetColors = (presetParams as Record<string, unknown>).colors as string[] | undefined;
    if (presetColors) setColors([...presetColors]);
  };

  return (
    <div
      style={{
        display: "flex", alignItems: "stretch", gap: 32, width: "100%", minHeight: "100vh",
        padding: 32, background: "#f8f8f6", fontFamily: MONO, boxSizing: "border-box",
      }}
    >
      <div style={{ flex: 1, minHeight: 480, display: "flex", minWidth: 0 }}>
        <DotOrbit {...(params as object)} colors={colors} style={{ width: "100%", height: "100%" }} />
      </div>

      <div
        style={{
          width: 300, flexShrink: 0, alignSelf: "flex-start", borderRadius: 12,
          background: "#f4f3eb", padding: "12px 12px 14px",
          boxShadow:
            "0px 4px 40px -8px rgba(58,34,17,0.1), 0px 12px 20px -8px rgba(58,34,17,0.2), 0px 0px 0px 1px rgba(58,34,17,0.1)",
        }}
      >
        <div style={{ fontSize: 11, color: "#222", padding: "2px 0 8px" }}>Presets</div>
        <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 8 }}>
          {dotOrbitPresets.map((preset) => (
            <PanelButton key={preset.name} onClick={() => applyPreset(preset.params as Record<string, unknown>)}>
              {preset.name}
            </PanelButton>
          ))}
        </div>

        <div style={{ height: 1, background: "rgba(0,0,0,0.08)", margin: "12px 0" }} />

        <div style={{ display: "flex", flexDirection: "column", gap: 2 }}>
          <Row label="colorCount">
            <Slider
              def={{ key: "colorCount", kind: "slider", min: 1, max: 10, step: 1, int: true }}
              value={colors.length}
              onChange={(v) => {
                const n = Math.round(v);
                setColors((c) =>
                  n > c.length
                    ? [...c, ...Array.from({ length: n - c.length }, (_, i) => `hsl(${(40 * (c.length + i)) % 360} 60% 50%)`)]
                    : c.slice(0, n),
                );
              }}
            />
          </Row>
          {colors.map((c, i) => (
            <ColorRow key={i} label={`color${i + 1}`} value={c} onChange={(v) => setColors((arr) => arr.map((x, j) => (j === i ? v : x)))} />
          ))}
          {CONTROLS.map((def) => {
            if (def.kind === "color")
              return <ColorRow key={def.key} label={def.key} value={String(params[def.key])} onChange={(v) => set(def.key, v)} />;
            if (def.kind === "select")
              return <SelectRow key={def.key} label={def.key} value={String(params[def.key])} options={def.options ?? []} onChange={(v) => set(def.key, v)} />;
            return (
              <Row key={def.key} label={def.key}>
                <Slider def={def} value={Number(params[def.key])} onChange={(v) => set(def.key, v)} />
              </Row>
            );
          })}
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


## Grain Gradient

**Author:** @paper-design
**URL:** https://21st.dev/@paper-design/components/grain-gradient

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
grain-gradient.tsx
// Full source: https://21st.dev/@paper-design/components/grain-gradient
// Install via: npx @21st-dev/magic add grain-gradient
// Or copy the component code from the 21st.dev page above.

import { useCallback, useEffect, useRef, useState } from "react";
import GrainGradient, { grainGradientPresets } from "@/components/ui/grain-gradient";

const MONO = '"Paper Mono", ui-monospace, SFMono-Regular, Menlo, monospace';

type ControlDef = {
  kind: "color" | "slider" | "select" | "checkbox";
  key: string;
  min?: number;
  max?: number;
  step?: number;
  int?: boolean;
  options?: string[];
};

const CONTROLS: ControlDef[] = [
  {
    kind: "color",
    key: "colorBack"
  },
  {
    kind: "slider",
    key: "softness",
    min: 0,
    max: 1,
    step: 0.01
  },
  {
    kind: "slider",
    key: "intensity",
    min: 0,
    max: 1,
    step: 0.01
  },
  {
    kind: "slider",
    key: "noise",
    min: 0,
    max: 1,
    step: 0.01
  },
  {
    kind: "select",
    key: "shape",
    options: [
      "wave",
      "dots",
      "truchet",
      "corners",
      "ripple",
      "blob",
      "sphere"
    ]
  },
  {
    kind: "slider",
    key: "speed",
    min: 0,
    max: 2,
    step: 0.01
  },
  {
    kind: "slider",
    key: "scale",
    min: 0.01,
    max: 4,
    step: 0.01
  },
  {
    kind: "slider",
    key: "rotation",
    min: 0,
    max: 360,
    step: 1,
    int: true
  },
  {
    kind: "slider",
    key: "offsetX",
    min: -1,
    max: 1,
    step: 0.01
  },
  {
    kind: "slider",
    key: "offsetY",
    min: -1,
    max: 1,
    step: 0.01
  }
];

const PARAM_KEYS = ["colorBack","softness","intensity","noise","shape","speed","scale","rotation","offsetX","offsetY"];

type Params = Record<string, string | number | boolean>;

function pickParams(source: Record<string, unknown>): Params {
  const out: Params = {};
  for (const k of PARAM_KEYS) out[k] = source[k] as string | number | boolean;
  return out;
}

const DEFAULTS = pickParams(grainGradientPresets[0].params as Record<string, unknown>);

function fmt(value: number, def: ControlDef) {
  return def.int ? String(Math.round(value)) : Number(value).toFixed(2);
}

function Row({ label, children }: { label: string; children: React.ReactNode }) {
  return (
    <div style={{ display: "flex", alignItems: "center", gap: 8, height: 26 }}>
      <div style={{ width: 104, flexShrink: 0, fontSize: 11, color: "#222" }}>{label}</div>
      <div style={{ flex: 1, display: "flex", alignItems: "center", gap: 8 }}>{children}</div>
    </div>
  );
}

function ValueBox({ children }: { children: React.ReactNode }) {
  return (
    <div
      style={{
        width: 58, flexShrink: 0, height: 24, borderRadius: 3,
        background: "rgba(0,0,0,0.055)", display: "flex", alignItems: "center",
        justifyContent: "flex-end", padding: "0 8px", fontSize: 11, color: "#222",
      }}
    >
      {children}
    </div>
  );
}

function Slider({ def, value, onChange }: { def: ControlDef; value: number; onChange: (v: number) => void }) {
  const min = def.min ?? 0;
  const max = def.max ?? 1;
  const pct = Math.min(100, Math.max(0, ((value - min) / (max - min)) * 100));
  return (
    <>
      <div style={{ position: "relative", flex: 1, height: 24, display: "flex", alignItems: "center" }}>
        <div style={{ position: "absolute", left: 0, right: 0, height: 2, borderRadius: 1, background: "rgba(0,0,0,0.14)" }} />
        <div style={{ position: "absolute", left: 0, width: `${pct}%`, height: 2, borderRadius: 1, background: "#999997" }} />
        <div style={{ position: "absolute", left: `calc(${pct}% - 2.5px)`, width: 5, height: 12, borderRadius: 1, background: "#77756f" }} />
        <input
          type="range"
          min={min}
          max={max}
          step={def.step ?? 0.01}
          value={value}
          onChange={(e) => onChange(Number(e.target.value))}
          aria-label={def.key}
          style={{ position: "absolute", inset: 0, width: "100%", opacity: 0, cursor: "ew-resize" }}
        />
      </div>
      <ValueBox>{fmt(value, def)}</ValueBox>
    </>
  );
}

function ColorRow({ label, value, onChange }: { label: string; value: string; onChange: (v: string) => void }) {
  const [text, setText] = useState(value);
  useEffect(() => setText(value), [value]);
  const commit = () => {
    if (/^#([0-9a-fA-F]{3,4}|[0-9a-fA-F]{6}|[0-9a-fA-F]{8})$/.test(text)) onChange(text);
    else setText(value);
  };
  return (
    <Row label={label}>
      <label
        style={{
          position: "relative", width: 24, height: 24, flexShrink: 0, borderRadius: 3,
          background: value, boxShadow: "inset 0 0 0 1px rgba(0,0,0,0.12)", cursor: "pointer",
        }}
      >
        <input
          type="color"
          value={/^#[0-9a-fA-F]{6}/.test(value) ? value.slice(0, 7) : "#000000"}
          onChange={(e) => onChange(e.target.value)}
          aria-label={`${label} color`}
          style={{ position: "absolute", inset: 0, width: "100%", height: "100%", opacity: 0, cursor: "pointer" }}
        />
      </label>
      <div style={{ flex: 1, height: 24, borderRadius: 3, background: "rgba(0,0,0,0.055)", display: "flex", alignItems: "center", padding: "0 8px" }}>
        <input
          value={text}
          onChange={(e) => setText(e.target.value)}
          onBlur={commit}
          onKeyDown={(e) => e.key === "Enter" && commit()}
          aria-label={`${label} value`}
          style={{ width: "100%", background: "transparent", border: 0, outline: "none", fontSize: 11, color: "#222", fontFamily: MONO }}
        />
      </div>
    </Row>
  );
}

function SelectRow({ label, value, options, onChange }: { label: string; value: string; options: string[]; onChange: (v: string) => void }) {
  return (
    <Row label={label}>
      <div style={{ position: "relative", flex: 1 }}>
        <select
          value={value}
          onChange={(e) => onChange(e.target.value)}
          aria-label={label}
          style={{
            width: "100%", height: 24, borderRadius: 3, border: 0,
            background: "rgba(0,0,0,0.055)", fontSize: 11, color: "#222",
            fontFamily: MONO, padding: "0 8px", appearance: "none", cursor: "pointer",
          }}
        >
          {options.map((o) => (
            <option key={o} value={o}>{o}</option>
          ))}
        </select>
        <div style={{ position: "absolute", right: 8, top: 9, pointerEvents: "none", borderLeft: "4px solid transparent", borderRight: "4px solid transparent", borderTop: "5px solid #222" }} />
      </div>
    </Row>
  );
}

function PanelButton({ children, onClick }: { children: React.ReactNode; onClick: () => void }) {
  const [hover, setHover] = useState(false);
  return (
    <button
      onClick={onClick}
      onMouseEnter={() => setHover(true)}
      onMouseLeave={() => setHover(false)}
      style={{
        height: 24, borderRadius: 3, border: 0, cursor: "pointer",
        background: hover ? "#8a8a88" : "#999997", color: "#fefefe",
        fontSize: 11, fontFamily: MONO, letterSpacing: "0.2px",
      }}
    >
      {children}
    </button>
  );
}

export default function GrainGradientDemo() {
  const [params, setParams] = useState<Params>({ ...DEFAULTS });
  const [colors, setColors] = useState<string[]>(
    (grainGradientPresets[0].params as Record<string, unknown>).colors as string[],
  );


  const set = (key: string, value: string | number | boolean) => setParams((p) => ({ ...p, [key]: value }));

  const applyPreset = (presetParams: Record<string, unknown>) => {
    setParams(pickParams(presetParams));
    const presetColors = (presetParams as Record<string, unknown>).colors as string[] | undefined;
    if (presetColors) setColors([...presetColors]);
  };

  return (
    <div
      style={{
        display: "flex", alignItems: "stretch", gap: 32, width: "100%", minHeight: "100vh",
        padding: 32, background: "#f8f8f6", fontFamily: MONO, boxSizing: "border-box",
      }}
    >
      <div style={{ flex: 1, minHeight: 480, display: "flex", minWidth: 0 }}>
        <GrainGradient {...(params as object)} colors={colors} style={{ width: "100%", height: "100%" }} />
      </div>

      <div
        style={{
          width: 300, flexShrink: 0, alignSelf: "flex-start", borderRadius: 12,
          background: "#f4f3eb", padding: "12px 12px 14px",
          boxShadow:
            "0px 4px 40px -8px rgba(58,34,17,0.1), 0px 12px 20px -8px rgba(58,34,17,0.2), 0px 0px 0px 1px rgba(58,34,17,0.1)",
        }}
      >
        <div style={{ fontSize: 11, color: "#222", padding: "2px 0 8px" }}>Presets</div>
        <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 8 }}>
          {grainGradientPresets.map((preset) => (
            <PanelButton key={preset.name} onClick={() => applyPreset(preset.params as Record<string, unknown>)}>
              {preset.name}
            </PanelButton>
          ))}
        </div>

        <div style={{ height: 1, background: "rgba(0,0,0,0.08)", margin: "12px 0" }} />

        <div style={{ display: "flex", flexDirection: "column", gap: 2 }}>
          <Row label="colorCount">
            <Slider
              def={{ key: "colorCount", kind: "slider", min: 1, max: 7, step: 1, int: true }}
              value={colors.length}
              onChange={(v) => {
                const n = Math.round(v);
                setColors((c) =>
                  n > c.length
                    ? [...c, ...Array.from({ length: n - c.length }, (_, i) => `hsl(${(40 * (c.length + i)) % 360} 60% 50%)`)]
                    : c.slice(0, n),
                );
              }}
            />
          </Row>
          {colors.map((c, i) => (
            <ColorRow key={i} label={`color${i + 1}`} value={c} onChange={(v) => setColors((arr) => arr.map((x, j) => (j === i ? v : x)))} />
          ))}
          {CONTROLS.map((def) => {
            if (def.kind === "color")
              return <ColorRow key={def.key} label={def.key} value={String(params[def.key])} onChange={(v) => set(def.key, v)} />;
            if (def.kind === "select")
              return <SelectRow key={def.key} label={def.key} value={String(params[def.key])} options={def.options ?? []} onChange={(v) => set(def.key, v)} />;
            return (
              <Row key={def.key} label={def.key}>
                <Slider def={def} value={Number(params[def.key])} onChange={(v) => set(def.key, v)} />
              </Row>
            );
          })}
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


## Static Radial Gradient

**Author:** @paper-design
**URL:** https://21st.dev/@paper-design/components/static-radial-gradient

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
static-radial-gradient.tsx
// Full source: https://21st.dev/@paper-design/components/static-radial-gradient
// Install via: npx @21st-dev/magic add static-radial-gradient
// Or copy the component code from the 21st.dev page above.

import { useCallback, useEffect, useRef, useState } from "react";
import StaticRadialGradient, { staticRadialGradientPresets } from "@/components/ui/static-radial-gradient";

const MONO = '"Paper Mono", ui-monospace, SFMono-Regular, Menlo, monospace';

type ControlDef = {
  kind: "color" | "slider" | "select" | "checkbox";
  key: string;
  min?: number;
  max?: number;
  step?: number;
  int?: boolean;
  options?: string[];
};

const CONTROLS: ControlDef[] = [
  {
    kind: "color",
    key: "colorBack"
  },
  {
    kind: "slider",
    key: "radius",
    min: 0,
    max: 3,
    step: 0.01
  },
  {
    kind: "slider",
    key: "focalDistance",
    min: 0,
    max: 3,
    step: 0.01
  },
  {
    kind: "slider",
    key: "focalAngle",
    min: 0,
    max: 360,
    step: 1,
    int: true
  },
  {
    kind: "slider",
    key: "falloff",
    min: -1,
    max: 1,
    step: 0.01
  },
  {
    kind: "slider",
    key: "mixing",
    min: 0,
    max: 1,
    step: 0.01
  },
  {
    kind: "slider",
    key: "distortion",
    min: 0,
    max: 1,
    step: 0.01
  },
  {
    kind: "slider",
    key: "distortionShift",
    min: -1,
    max: 1,
    step: 0.01
  },
  {
    kind: "slider",
    key: "distortionFreq",
    min: 0,
    max: 20,
    step: 1,
    int: true
  },
  {
    kind: "slider",
    key: "grainMixer",
    min: 0,
    max: 1,
    step: 0.01
  },
  {
    kind: "slider",
    key: "grainOverlay",
    min: 0,
    max: 1,
    step: 0.01
  },
  {
    kind: "slider",
    key: "offsetX",
    min: -1,
    max: 1,
    step: 0.01
  },
  {
    kind: "slider",
    key: "offsetY",
    min: -1,
    max: 1,
    step: 0.01
  }
];

const PARAM_KEYS = ["colorBack","radius","focalDistance","focalAngle","falloff","mixing","distortion","distortionShift","distortionFreq","grainMixer","grainOverlay","offsetX","offsetY"];

type Params = Record<string, string | number | boolean>;

function pickParams(source: Record<string, unknown>): Params {
  const out: Params = {};
  for (const k of PARAM_KEYS) out[k] = source[k] as string | number | boolean;
  return out;
}

const DEFAULTS = pickParams(staticRadialGradientPresets[0].params as Record<string, unknown>);

function fmt(value: number, def: ControlDef) {
  return def.int ? String(Math.round(value)) : Number(value).toFixed(2);
}

function Row({ label, children }: { label: string; children: React.ReactNode }) {
  return (
    <div style={{ display: "flex", alignItems: "center", gap: 8, height: 26 }}>
      <div style={{ width: 104, flexShrink: 0, fontSize: 11, color: "#222" }}>{label}</div>
      <div style={{ flex: 1, display: "flex", alignItems: "center", gap: 8 }}>{children}</div>
    </div>
  );
}

function ValueBox({ children }: { children: React.ReactNode }) {
  return (
    <div
      style={{
        width: 58, flexShrink: 0, height: 24, borderRadius: 3,
        background: "rgba(0,0,0,0.055)", display: "flex", alignItems: "center",
        justifyContent: "flex-end", padding: "0 8px", fontSize: 11, color: "#222",
      }}
    >
      {children}
    </div>
  );
}

function Slider({ def, value, onChange }: { def: ControlDef; value: number; onChange: (v: number) => void }) {
  const min = def.min ?? 0;
  const max = def.max ?? 1;
  const pct = Math.min(100, Math.max(0, ((value - min) / (max - min)) * 100));
  return (
    <>
      <div style={{ position: "relative", flex: 1, height: 24, display: "flex", alignItems: "center" }}>
        <div style={{ position: "absolute", left: 0, right: 0, height: 2, borderRadius: 1, background: "rgba(0,0,0,0.14)" }} />
        <div style={{ position: "absolute", left: 0, width: `${pct}%`, height: 2, borderRadius: 1, background: "#999997" }} />
        <div style={{ position: "absolute", left: `calc(${pct}% - 2.5px)`, width: 5, height: 12, borderRadius: 1, background: "#77756f" }} />
        <input
          type="range"
          min={min}
          max={max}
          step={def.step ?? 0.01}
          value={value}
          onChange={(e) => onChange(Number(e.target.value))}
          aria-label={def.key}
          style={{ position: "absolute", inset: 0, width: "100%", opacity: 0, cursor: "ew-resize" }}
        />
      </div>
      <ValueBox>{fmt(value, def)}</ValueBox>
    </>
  );
}

function ColorRow({ label, value, onChange }: { label: string; value: string; onChange: (v: string) => void }) {
  const [text, setText] = useState(value);
  useEffect(() => setText(value), [value]);
  const commit = () => {
    if (/^#([0-9a-fA-F]{3,4}|[0-9a-fA-F]{6}|[0-9a-fA-F]{8})$/.test(text)) onChange(text);
    else setText(value);
  };
  return (
    <Row label={label}>
      <label
        style={{
          position: "relative", width: 24, height: 24, flexShrink: 0, borderRadius: 3,
          background: value, boxShadow: "inset 0 0 0 1px rgba(0,0,0,0.12)", cursor: "pointer",
        }}
      >
        <input
          type="color"
          value={/^#[0-9a-fA-F]{6}/.test(value) ? value.slice(0, 7) : "#000000"}
          onChange={(e) => onChange(e.target.value)}
          aria-label={`${label} color`}
          style={{ position: "absolute", inset: 0, width: "100%", height: "100%", opacity: 0, cursor: "pointer" }}
        />
      </label>
      <div style={{ flex: 1, height: 24, borderRadius: 3, background: "rgba(0,0,0,0.055)", display: "flex", alignItems: "center", padding: "0 8px" }}>
        <input
          value={text}
          onChange={(e) => setText(e.target.value)}
          onBlur={commit}
          onKeyDown={(e) => e.key === "Enter" && commit()}
          aria-label={`${label} value`}
          style={{ width: "100%", background: "transparent", border: 0, outline: "none", fontSize: 11, color: "#222", fontFamily: MONO }}
        />
      </div>
    </Row>
  );
}

function SelectRow({ label, value, options, onChange }: { label: string; value: string; options: string[]; onChange: (v: string) => void }) {
  return (
    <Row label={label}>
      <div style={{ position: "relative", flex: 1 }}>
        <select
          value={value}
          onChange={(e) => onChange(e.target.value)}
          aria-label={label}
          style={{
            width: "100%", height: 24, borderRadius: 3, border: 0,
            background: "rgba(0,0,0,0.055)", fontSize: 11, color: "#222",
            fontFamily: MONO, padding: "0 8px", appearance: "none", cursor: "pointer",
          }}
        >
          {options.map((o) => (
            <option key={o} value={o}>{o}</option>
          ))}
        </select>
        <div style={{ position: "absolute", right: 8, top: 9, pointerEvents: "none", borderLeft: "4px solid transparent", borderRight: "4px solid transparent", borderTop: "5px solid #222" }} />
      </div>
    </Row>
  );
}

function PanelButton({ children, onClick }: { children: React.ReactNode; onClick: () => void }) {
  const [hover, setHover] = useState(false);
  return (
    <button
      onClick={onClick}
      onMouseEnter={() => setHover(true)}
      onMouseLeave={() => setHover(false)}
      style={{
        height: 24, borderRadius: 3, border: 0, cursor: "pointer",
        background: hover ? "#8a8a88" : "#999997", color: "#fefefe",
        fontSize: 11, fontFamily: MONO, letterSpacing: "0.2px",
      }}
    >
      {children}
    </button>
  );
}

export default function StaticRadialGradientDemo() {
  const [params, setParams] = useState<Params>({ ...DEFAULTS });
  const [colors, setColors] = useState<string[]>(
    (staticRadialGradientPresets[0].params as Record<string, unknown>).colors as string[],
  );


  const set = (key: string, value: string | number | boolean) => setParams((p) => ({ ...p, [key]: value }));

  const applyPreset = (presetParams: Record<string, unknown>) => {
    setParams(pickParams(presetParams));
    const presetColors = (presetParams as Record<string, unknown>).colors as string[] | undefined;
    if (presetColors) setColors([...presetColors]);
  };

  return (
    <div
      style={{
        display: "flex", alignItems: "stretch", gap: 32, width: "100%", minHeight: "100vh",
        padding: 32, background: "#f8f8f6", fontFamily: MONO, boxSizing: "border-box",
      }}
    >
      <div style={{ flex: 1, minHeight: 480, display: "flex", minWidth: 0 }}>
        <StaticRadialGradient {...(params as object)} colors={colors} style={{ width: "100%", height: "100%" }} />
      </div>

      <div
        style={{
          width: 300, flexShrink: 0, alignSelf: "flex-start", borderRadius: 12,
          background: "#f4f3eb", padding: "12px 12px 14px",
          boxShadow:
            "0px 4px 40px -8px rgba(58,34,17,0.1), 0px 12px 20px -8px rgba(58,34,17,0.2), 0px 0px 0px 1px rgba(58,34,17,0.1)",
        }}
      >
        <div style={{ fontSize: 11, color: "#222", padding: "2px 0 8px" }}>Presets</div>
        <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 8 }}>
          {staticRadialGradientPresets.map((preset) => (
            <PanelButton key={preset.name} onClick={() => applyPreset(preset.params as Record<string, unknown>)}>
              {preset.name}
            </PanelButton>
          ))}
        </div>

        <div style={{ height: 1, background: "rgba(0,0,0,0.08)", margin: "12px 0" }} />

        <div style={{ display: "flex", flexDirection: "column", gap: 2 }}>
          <Row label="colorCount">
            <Slider
              def={{ key: "colorCount", kind: "slider", min: 1, max: 10, step: 1, int: true }}
              value={colors.length}
              onChange={(v) => {
                const n = Math.round(v);
                setColors((c) =>
                  n > c.length
                    ? [...c, ...Array.from({ length: n - c.length }, (_, i) => `hsl(${(40 * (c.length + i)) % 360} 60% 50%)`)]
                    : c.slice(0, n),
                );
              }}
            />
          </Row>
          {colors.map((c, i) => (
            <ColorRow key={i} label={`color${i + 1}`} value={c} onChange={(v) => setColors((arr) => arr.map((x, j) => (j === i ? v : x)))} />
          ))}
          {CONTROLS.map((def) => {
            if (def.kind === "color")
              return <ColorRow key={def.key} label={def.key} value={String(params[def.key])} onChange={(v) => set(def.key, v)} />;
            if (def.kind === "select")
              return <SelectRow key={def.key} label={def.key} value={String(params[def.key])} options={def.options ?? []} onChange={(v) => set(def.key, v)} />;
            return (
              <Row key={def.key} label={def.key}>
                <Slider def={def} value={Number(params[def.key])} onChange={(v) => set(def.key, v)} />
              </Row>
            );
          })}
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


## Static Mesh Gradient

**Author:** @paper-design
**URL:** https://21st.dev/@paper-design/components/static-mesh-gradient

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
static-mesh-gradient.tsx
// Full source: https://21st.dev/@paper-design/components/static-mesh-gradient
// Install via: npx @21st-dev/magic add static-mesh-gradient
// Or copy the component code from the 21st.dev page above.

import { useCallback, useEffect, useRef, useState } from "react";
import StaticMeshGradient, { staticMeshGradientPresets } from "@/components/ui/static-mesh-gradient";

const MONO = '"Paper Mono", ui-monospace, SFMono-Regular, Menlo, monospace';

type ControlDef = {
  kind: "color" | "slider" | "select" | "checkbox";
  key: string;
  min?: number;
  max?: number;
  step?: number;
  int?: boolean;
  options?: string[];
};

const CONTROLS: ControlDef[] = [
  {
    kind: "slider",
    key: "positions",
    min: 0,
    max: 100,
    step: 0.01
  },
  {
    kind: "slider",
    key: "waveX",
    min: 0,
    max: 1,
    step: 0.01
  },
  {
    kind: "slider",
    key: "waveXShift",
    min: 0,
    max: 1,
    step: 0.01
  },
  {
    kind: "slider",
    key: "waveY",
    min: 0,
    max: 1,
    step: 0.01
  },
  {
    kind: "slider",
    key: "waveYShift",
    min: 0,
    max: 1,
    step: 0.01
  },
  {
    kind: "slider",
    key: "mixing",
    min: 0,
    max: 1,
    step: 0.01
  },
  {
    kind: "slider",
    key: "grainMixer",
    min: 0,
    max: 1,
    step: 0.01
  },
  {
    kind: "slider",
    key: "grainOverlay",
    min: 0,
    max: 1,
    step: 0.01
  },
  {
    kind: "slider",
    key: "scale",
    min: 0.01,
    max: 4,
    step: 0.01
  },
  {
    kind: "slider",
    key: "rotation",
    min: 0,
    max: 360,
    step: 1,
    int: true
  },
  {
    kind: "slider",
    key: "offsetX",
    min: -1,
    max: 1,
    step: 0.01
  },
  {
    kind: "slider",
    key: "offsetY",
    min: -1,
    max: 1,
    step: 0.01
  }
];

const PARAM_KEYS = ["positions","waveX","waveXShift","waveY","waveYShift","mixing","grainMixer","grainOverlay","scale","rotation","offsetX","offsetY"];

type Params = Record<string, string | number | boolean>;

function pickParams(source: Record<string, unknown>): Params {
  const out: Params = {};
  for (const k of PARAM_KEYS) out[k] = source[k] as string | number | boolean;
  return out;
}

const DEFAULTS = pickParams(staticMeshGradientPresets[0].params as Record<string, unknown>);

function fmt(value: number, def: ControlDef) {
  return def.int ? String(Math.round(value)) : Number(value).toFixed(2);
}

function Row({ label, children }: { label: string; children: React.ReactNode }) {
  return (
    <div style={{ display: "flex", alignItems: "center", gap: 8, height: 26 }}>
      <div style={{ width: 104, flexShrink: 0, fontSize: 11, color: "#222" }}>{label}</div>
      <div style={{ flex: 1, display: "flex", alignItems: "center", gap: 8 }}>{children}</div>
    </div>
  );
}

function ValueBox({ children }: { children: React.ReactNode }) {
  return (
    <div
      style={{
        width: 58, flexShrink: 0, height: 24, borderRadius: 3,
        background: "rgba(0,0,0,0.055)", display: "flex", alignItems: "center",
        justifyContent: "flex-end", padding: "0 8px", fontSize: 11, color: "#222",
      }}
    >
      {children}
    </div>
  );
}

function Slider({ def, value, onChange }: { def: ControlDef; value: number; onChange: (v: number) => void }) {
  const min = def.min ?? 0;
  const max = def.max ?? 1;
  const pct = Math.min(100, Math.max(0, ((value - min) / (max - min)) * 100));
  return (
    <>
      <div style={{ position: "relative", flex: 1, height: 24, display: "flex", alignItems: "center" }}>
        <div style={{ position: "absolute", left: 0, right: 0, height: 2, borderRadius: 1, background: "rgba(0,0,0,0.14)" }} />
        <div style={{ position: "absolute", left: 0, width: `${pct}%`, height: 2, borderRadius: 1, background: "#999997" }} />
        <div style={{ position: "absolute", left: `calc(${pct}% - 2.5px)`, width: 5, height: 12, borderRadius: 1, background: "#77756f" }} />
        <input
          type="range"
          min={min}
          max={max}
          step={def.step ?? 0.01}
          value={value}
          onChange={(e) => onChange(Number(e.target.value))}
          aria-label={def.key}
          style={{ position: "absolute", inset: 0, width: "100%", opacity: 0, cursor: "ew-resize" }}
        />
      </div>
      <ValueBox>{fmt(value, def)}</ValueBox>
    </>
  );
}

function ColorRow({ label, value, onChange }: { label: string; value: string; onChange: (v: string) => void }) {
  const [text, setText] = useState(value);
  useEffect(() => setText(value), [value]);
  const commit = () => {
    if (/^#([0-9a-fA-F]{3,4}|[0-9a-fA-F]{6}|[0-9a-fA-F]{8})$/.test(text)) onChange(text);
    else setText(value);
  };
  return (
    <Row label={label}>
      <label
        style={{
          position: "relative", width: 24, height: 24, flexShrink: 0, borderRadius: 3,
          background: value, boxShadow: "inset 0 0 0 1px rgba(0,0,0,0.12)", cursor: "pointer",
        }}
      >
        <input
          type="color"
          value={/^#[0-9a-fA-F]{6}/.test(value) ? value.slice(0, 7) : "#000000"}
          onChange={(e) => onChange(e.target.value)}
          aria-label={`${label} color`}
          style={{ position: "absolute", inset: 0, width: "100%", height: "100%", opacity: 0, cursor: "pointer" }}
        />
      </label>
      <div style={{ flex: 1, height: 24, borderRadius: 3, background: "rgba(0,0,0,0.055)", display: "flex", alignItems: "center", padding: "0 8px" }}>
        <input
          value={text}
          onChange={(e) => setText(e.target.value)}
          onBlur={commit}
          onKeyDown={(e) => e.key === "Enter" && commit()}
          aria-label={`${label} value`}
          style={{ width: "100%", background: "transparent", border: 0, outline: "none", fontSize: 11, color: "#222", fontFamily: MONO }}
        />
      </div>
    </Row>
  );
}

function SelectRow({ label, value, options, onChange }: { label: string; value: string; options: string[]; onChange: (v: string) => void }) {
  return (
    <Row label={label}>
      <div style={{ position: "relative", flex: 1 }}>
        <select
          value={value}
          onChange={(e) => onChange(e.target.value)}
          aria-label={label}
          style={{
            width: "100%", height: 24, borderRadius: 3, border: 0,
            background: "rgba(0,0,0,0.055)", fontSize: 11, color: "#222",
            fontFamily: MONO, padding: "0 8px", appearance: "none", cursor: "pointer",
          }}
        >
          {options.map((o) => (
            <option key={o} value={o}>{o}</option>
          ))}
        </select>
        <div style={{ position: "absolute", right: 8, top: 9, pointerEvents: "none", borderLeft: "4px solid transparent", borderRight: "4px solid transparent", borderTop: "5px solid #222" }} />
      </div>
    </Row>
  );
}

function PanelButton({ children, onClick }: { children: React.ReactNode; onClick: () => void }) {
  const [hover, setHover] = useState(false);
  return (
    <button
      onClick={onClick}
      onMouseEnter={() => setHover(true)}
      onMouseLeave={() => setHover(false)}
      style={{
        height: 24, borderRadius: 3, border: 0, cursor: "pointer",
        background: hover ? "#8a8a88" : "#999997", color: "#fefefe",
        fontSize: 11, fontFamily: MONO, letterSpacing: "0.2px",
      }}
    >
      {children}
    </button>
  );
}

export default function StaticMeshGradientDemo() {
  const [params, setParams] = useState<Params>({ ...DEFAULTS });
  const [colors, setColors] = useState<string[]>(
    (staticMeshGradientPresets[0].params as Record<string, unknown>).colors as string[],
  );


  const set = (key: string, value: string | number | boolean) => setParams((p) => ({ ...p, [key]: value }));

  const applyPreset = (presetParams: Record<string, unknown>) => {
    setParams(pickParams(presetParams));
    const presetColors = (presetParams as Record<string, unknown>).colors as string[] | undefined;
    if (presetColors) setColors([...presetColors]);
  };

  return (
    <div
      style={{
        display: "flex", alignItems: "stretch", gap: 32, width: "100%", minHeight: "100vh",
        padding: 32, background: "#f8f8f6", fontFamily: MONO, boxSizing: "border-box",
      }}
    >
      <div style={{ flex: 1, minHeight: 480, display: "flex", minWidth: 0 }}>
        <StaticMeshGradient {...(params as object)} colors={colors} style={{ width: "100%", height: "100%" }} />
      </div>

      <div
        style={{
          width: 300, flexShrink: 0, alignSelf: "flex-start", borderRadius: 12,
          background: "#f4f3eb", padding: "12px 12px 14px",
          boxShadow:
            "0px 4px 40px -8px rgba(58,34,17,0.1), 0px 12px 20px -8px rgba(58,34,17,0.2), 0px 0px 0px 1px rgba(58,34,17,0.1)",
        }}
      >
        <div style={{ fontSize: 11, color: "#222", padding: "2px 0 8px" }}>Presets</div>
        <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 8 }}>
          {staticMeshGradientPresets.map((preset) => (
            <PanelButton key={preset.name} onClick={() => applyPreset(preset.params as Record<string, unknown>)}>
              {preset.name}
            </PanelButton>
          ))}
        </div>

        <div style={{ height: 1, background: "rgba(0,0,0,0.08)", margin: "12px 0" }} />

        <div style={{ display: "flex", flexDirection: "column", gap: 2 }}>
          <Row label="colorCount">
            <Slider
              def={{ key: "colorCount", kind: "slider", min: 1, max: 10, step: 1, int: true }}
              value={colors.length}
              onChange={(v) => {
                const n = Math.round(v);
                setColors((c) =>
                  n > c.length
                    ? [...c, ...Array.from({ length: n - c.length }, (_, i) => `hsl(${(40 * (c.length + i)) % 360} 60% 50%)`)]
                    : c.slice(0, n),
                );
              }}
            />
          </Row>
          {colors.map((c, i) => (
            <ColorRow key={i} label={`color${i + 1}`} value={c} onChange={(v) => setColors((arr) => arr.map((x, j) => (j === i ? v : x)))} />
          ))}
          {CONTROLS.map((def) => {
            if (def.kind === "color")
              return <ColorRow key={def.key} label={def.key} value={String(params[def.key])} onChange={(v) => set(def.key, v)} />;
            if (def.kind === "select")
              return <SelectRow key={def.key} label={def.key} value={String(params[def.key])} options={def.options ?? []} onChange={(v) => set(def.key, v)} />;
            return (
              <Row key={def.key} label={def.key}>
                <Slider def={def} value={Number(params[def.key])} onChange={(v) => set(def.key, v)} />
              </Row>
            );
          })}
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


## Mesh Gradient

**Author:** @paper-design
**URL:** https://21st.dev/@paper-design/components/mesh-gradient

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
mesh-gradient.tsx
// Full source: https://21st.dev/@paper-design/components/mesh-gradient
// Install via: npx @21st-dev/magic add mesh-gradient
// Or copy the component code from the 21st.dev page above.

import { useCallback, useEffect, useRef, useState } from "react";
import MeshGradient, { meshGradientPresets } from "@/components/ui/mesh-gradient";

const MONO = '"Paper Mono", ui-monospace, SFMono-Regular, Menlo, monospace';

type ControlDef = {
  kind: "color" | "slider" | "select" | "checkbox";
  key: string;
  min?: number;
  max?: number;
  step?: number;
  int?: boolean;
  options?: string[];
};

const CONTROLS: ControlDef[] = [
  {
    kind: "slider",
    key: "distortion",
    min: 0,
    max: 1,
    step: 0.01
  },
  {
    kind: "slider",
    key: "swirl",
    min: 0,
    max: 1,
    step: 0.01
  },
  {
    kind: "slider",
    key: "grainMixer",
    min: 0,
    max: 1,
    step: 0.01
  },
  {
    kind: "slider",
    key: "grainOverlay",
    min: 0,
    max: 1,
    step: 0.01
  },
  {
    kind: "slider",
    key: "speed",
    min: 0,
    max: 2,
    step: 0.01
  },
  {
    kind: "slider",
    key: "scale",
    min: 0.01,
    max: 4,
    step: 0.01
  },
  {
    kind: "slider",
    key: "rotation",
    min: 0,
    max: 360,
    step: 1,
    int: true
  },
  {
    kind: "slider",
    key: "offsetX",
    min: -1,
    max: 1,
    step: 0.01
  },
  {
    kind: "slider",
    key: "offsetY",
    min: -1,
    max: 1,
    step: 0.01
  }
];

const PARAM_KEYS = ["distortion","swirl","grainMixer","grainOverlay","speed","scale","rotation","offsetX","offsetY"];

type Params = Record<string, string | number | boolean>;

function pickParams(source: Record<string, unknown>): Params {
  const out: Params = {};
  for (const k of PARAM_KEYS) out[k] = source[k] as string | number | boolean;
  return out;
}

const DEFAULTS = pickParams(meshGradientPresets[0].params as Record<string, unknown>);

function fmt(value: number, def: ControlDef) {
  return def.int ? String(Math.round(value)) : Number(value).toFixed(2);
}

function Row({ label, children }: { label: string; children: React.ReactNode }) {
  return (
    <div style={{ display: "flex", alignItems: "center", gap: 8, height: 26 }}>
      <div style={{ width: 104, flexShrink: 0, fontSize: 11, color: "#222" }}>{label}</div>
      <div style={{ flex: 1, display: "flex", alignItems: "center", gap: 8 }}>{children}</div>
    </div>
  );
}

function ValueBox({ children }: { children: React.ReactNode }) {
  return (
    <div
      style={{
        width: 58, flexShrink: 0, height: 24, borderRadius: 3,
        background: "rgba(0,0,0,0.055)", display: "flex", alignItems: "center",
        justifyContent: "flex-end", padding: "0 8px", fontSize: 11, color: "#222",
      }}
    >
      {children}
    </div>
  );
}

function Slider({ def, value, onChange }: { def: ControlDef; value: number; onChange: (v: number) => void }) {
  const min = def.min ?? 0;
  const max = def.max ?? 1;
  const pct = Math.min(100, Math.max(0, ((value - min) / (max - min)) * 100));
  return (
    <>
      <div style={{ position: "relative", flex: 1, height: 24, display: "flex", alignItems: "center" }}>
        <div style={{ position: "absolute", left: 0, right: 0, height: 2, borderRadius: 1, background: "rgba(0,0,0,0.14)" }} />
        <div style={{ position: "absolute", left: 0, width: `${pct}%`, height: 2, borderRadius: 1, background: "#999997" }} />
        <div style={{ position: "absolute", left: `calc(${pct}% - 2.5px)`, width: 5, height: 12, borderRadius: 1, background: "#77756f" }} />
        <input
          type="range"
          min={min}
          max={max}
          step={def.step ?? 0.01}
          value={value}
          onChange={(e) => onChange(Number(e.target.value))}
          aria-label={def.key}
          style={{ position: "absolute", inset: 0, width: "100%", opacity: 0, cursor: "ew-resize" }}
        />
      </div>
      <ValueBox>{fmt(value, def)}</ValueBox>
    </>
  );
}

function ColorRow({ label, value, onChange }: { label: string; value: string; onChange: (v: string) => void }) {
  const [text, setText] = useState(value);
  useEffect(() => setText(value), [value]);
  const commit = () => {
    if (/^#([0-9a-fA-F]{3,4}|[0-9a-fA-F]{6}|[0-9a-fA-F]{8})$/.test(text)) onChange(text);
    else setText(value);
  };
  return (
    <Row label={label}>
      <label
        style={{
          position: "relative", width: 24, height: 24, flexShrink: 0, borderRadius: 3,
          background: value, boxShadow: "inset 0 0 0 1px rgba(0,0,0,0.12)", cursor: "pointer",
        }}
      >
        <input
          type="color"
          value={/^#[0-9a-fA-F]{6}/.test(value) ? value.slice(0, 7) : "#000000"}
          onChange={(e) => onChange(e.target.value)}
          aria-label={`${label} color`}
          style={{ position: "absolute", inset: 0, width: "100%", height: "100%", opacity: 0, cursor: "pointer" }}
        />
      </label>
      <div style={{ flex: 1, height: 24, borderRadius: 3, background: "rgba(0,0,0,0.055)", display: "flex", alignItems: "center", padding: "0 8px" }}>
        <input
          value={text}
          onChange={(e) => setText(e.target.value)}
          onBlur={commit}
          onKeyDown={(e) => e.key === "Enter" && commit()}
          aria-label={`${label} value`}
          style={{ width: "100%", background: "transparent", border: 0, outline: "none", fontSize: 11, color: "#222", fontFamily: MONO }}
        />
      </div>
    </Row>
  );
}

function SelectRow({ label, value, options, onChange }: { label: string; value: string; options: string[]; onChange: (v: string) => void }) {
  return (
    <Row label={label}>
      <div style={{ position: "relative", flex: 1 }}>
        <select
          value={value}
          onChange={(e) => onChange(e.target.value)}
          aria-label={label}
          style={{
            width: "100%", height: 24, borderRadius: 3, border: 0,
            background: "rgba(0,0,0,0.055)", fontSize: 11, color: "#222",
            fontFamily: MONO, padding: "0 8px", appearance: "none", cursor: "pointer",
          }}
        >
          {options.map((o) => (
            <option key={o} value={o}>{o}</option>
          ))}
        </select>
        <div style={{ position: "absolute", right: 8, top: 9, pointerEvents: "none", borderLeft: "4px solid transparent", borderRight: "4px solid transparent", borderTop: "5px solid #222" }} />
      </div>
    </Row>
  );
}

function PanelButton({ children, onClick }: { children: React.ReactNode; onClick: () => void }) {
  const [hover, setHover] = useState(false);
  return (
    <button
      onClick={onClick}
      onMouseEnter={() => setHover(true)}
      onMouseLeave={() => setHover(false)}
      style={{
        height: 24, borderRadius: 3, border: 0, cursor: "pointer",
        background: hover ? "#8a8a88" : "#999997", color: "#fefefe",
        fontSize: 11, fontFamily: MONO, letterSpacing: "0.2px",
      }}
    >
      {children}
    </button>
  );
}

export default function MeshGradientDemo() {
  const [params, setParams] = useState<Params>({ ...DEFAULTS });
  const [colors, setColors] = useState<string[]>(
    (meshGradientPresets[0].params as Record<string, unknown>).colors as string[],
  );


  const set = (key: string, value: string | number | boolean) => setParams((p) => ({ ...p, [key]: value }));

  const applyPreset = (presetParams: Record<string, unknown>) => {
    setParams(pickParams(presetParams));
    const presetColors = (presetParams as Record<string, unknown>).colors as string[] | undefined;
    if (presetColors) setColors([...presetColors]);
  };

  return (
    <div
      style={{
        display: "flex", alignItems: "stretch", gap: 32, width: "100%", minHeight: "100vh",
        padding: 32, background: "#f8f8f6", fontFamily: MONO, boxSizing: "border-box",
      }}
    >
      <div style={{ flex: 1, minHeight: 480, display: "flex", minWidth: 0 }}>
        <MeshGradient {...(params as object)} colors={colors} style={{ width: "100%", height: "100%" }} />
      </div>

      <div
        style={{
          width: 300, flexShrink: 0, alignSelf: "flex-start", borderRadius: 12,
          background: "#f4f3eb", padding: "12px 12px 14px",
          boxShadow:
            "0px 4px 40px -8px rgba(58,34,17,0.1), 0px 12px 20px -8px rgba(58,34,17,0.2), 0px 0px 0px 1px rgba(58,34,17,0.1)",
        }}
      >
        <div style={{ fontSize: 11, color: "#222", padding: "2px 0 8px" }}>Presets</div>
        <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 8 }}>
          {meshGradientPresets.map((preset) => (
            <PanelButton key={preset.name} onClick={() => applyPreset(preset.params as Record<string, unknown>)}>
              {preset.name}
            </PanelButton>
          ))}
        </div>

        <div style={{ height: 1, background: "rgba(0,0,0,0.08)", margin: "12px 0" }} />

        <div style={{ display: "flex", flexDirection: "column", gap: 2 }}>
          <Row label="colorCount">
            <Slider
              def={{ key: "colorCount", kind: "slider", min: 1, max: 10, step: 1, int: true }}
              value={colors.length}
              onChange={(v) => {
                const n = Math.round(v);
                setColors((c) =>
                  n > c.length
                    ? [...c, ...Array.from({ length: n - c.length }, (_, i) => `hsl(${(40 * (c.length + i)) % 360} 60% 50%)`)]
                    : c.slice(0, n),
                );
              }}
            />
          </Row>
          {colors.map((c, i) => (
            <ColorRow key={i} label={`color${i + 1}`} value={c} onChange={(v) => setColors((arr) => arr.map((x, j) => (j === i ? v : x)))} />
          ))}
          {CONTROLS.map((def) => {
            if (def.kind === "color")
              return <ColorRow key={def.key} label={def.key} value={String(params[def.key])} onChange={(v) => set(def.key, v)} />;
            if (def.kind === "select")
              return <SelectRow key={def.key} label={def.key} value={String(params[def.key])} options={def.options ?? []} onChange={(v) => set(def.key, v)} />;
            return (
              <Row key={def.key} label={def.key}>
                <Slider def={def} value={Number(params[def.key])} onChange={(v) => set(def.key, v)} />
              </Row>
            );
          })}
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


## Magic Dust Shader

**Author:** @uithefactory
**URL:** https://21st.dev/@uithefactory/components/magic-dust-shader

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
magic-dust-shader.tsx
// Full source: https://21st.dev/@uithefactory/components/magic-dust-shader
// Install via: npx @21st-dev/magic add magic-dust-shader
// Or copy the component code from the 21st.dev page above.

import React from "react";
import { Canvas } from "@react-three/fiber";
import { MagicDust } from "../components/ui/magic-dust-shader";
import { Globe } from "lucide-react";

export default function MagicDustDemo() {
    return (
        <div className="relative w-full h-[600px] bg-black overflow-hidden font-sans rounded-xl border border-white/5 flex flex-col items-center justify-end group">

            <a 
                href="https://uithefactory.com/gallery" 
                target="_blank" 
                rel="noopener noreferrer"
                className="absolute top-5 right-5 z-20 pointer-events-auto flex items-center justify-center w-10 h-10 bg-white text-black rounded-full hover:scale-110 active:scale-95 transition-all duration-300 shadow-[0_0_20px_rgba(255,255,255,0.2)]"
                title="View more components on The UI Factory"
            >
                <Globe strokeWidth={2} className="w-5 h-5" />
            </a>
    
            <div className="absolute inset-0 z-0">
             <MagicDust />
            </div>
            
            <div className="absolute inset-0 z-5 pointer-events-none bg-gradient-to-t from-black via-black/50 to-transparent" />

            <div className="relative z-10 pointer-events-none pb-10 md:pb-12 px-6 flex flex-col items-center text-center">
                
                <h1 className="text-7xl md:text-[85px] font-bold tracking-tighter leading-[0.85] text-white">
                    Magic<br/>
                    <span className="bg-gradient-to-b from-white via-white/80 to-white/10 text-transparent bg-clip-text">
                        Dust.
                    </span>
                </h1>
                
                <p className="mt-6 text-zinc-400 font-medium max-w-sm text-sm md:text-base leading-relaxed">
                    100% editable via React Props. Pass any text array or 3D geometry and watch it materialize instantly.
                </p>
                
            </div>
        </div>
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


## Dia Gradient

**Author:** @arlanoska
**URL:** https://21st.dev/@arlanoska/components/dia-gradient

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
dia-gradient.tsx
// Full source: https://21st.dev/@arlanoska/components/dia-gradient
// Install via: npx @21st-dev/magic add dia-gradient
// Or copy the component code from the 21st.dev page above.

"use client"

import { useEffect, useRef, useState, type ReactNode } from "react"
import { DiaGradient } from "@/components/ui/dia-gradient"

// Palette ramps captured verbatim from the source playground (arlan.me).
const PALETTES: Record<string, { offset: number; color: string }[]> = {"Dia":[{"offset":0,"color":"#3B1115"},{"offset":0.0833,"color":"#303DA7"},{"offset":0.1667,"color":"#2055EB"},{"offset":0.25,"color":"#4782D8"},{"offset":0.3333,"color":"#9AB9DE"},{"offset":0.4167,"color":"#E2EBFB"},{"offset":0.5,"color":"#F0E0B5"},{"offset":0.5833,"color":"#FED42E"},{"offset":0.6667,"color":"#FA6A27"},{"offset":0.75,"color":"#FB2FB9"},{"offset":0.8333,"color":"#FD4FF6D8"},{"offset":0.9167,"color":"#FE94F96C"},{"offset":1,"color":"#FFC1FD00"}],"Ocean":[{"offset":0,"color":"#08122E"},{"offset":0.0833,"color":"#06389C"},{"offset":0.1667,"color":"#044DD8"},{"offset":0.25,"color":"#0C6CF3"},{"offset":0.3333,"color":"#1897E7"},{"offset":0.4167,"color":"#22B8DC"},{"offset":0.5,"color":"#61D1D9"},{"offset":0.5833,"color":"#97E7DD"},{"offset":0.6667,"color":"#9FD3E7"},{"offset":0.75,"color":"#8B96F6"},{"offset":0.8333,"color":"#8B81FFD4"},{"offset":0.9167,"color":"#A8BBFF6A"},{"offset":1,"color":"#C1E8FF00"}],"Sunset":[{"offset":0,"color":"#2A0A06"},{"offset":0.0833,"color":"#4F1410"},{"offset":0.1667,"color":"#681B15"},{"offset":0.25,"color":"#822219"},{"offset":0.3333,"color":"#BB2F1C"},{"offset":0.4167,"color":"#E63A1F"},{"offset":0.5,"color":"#FB721E"},{"offset":0.5833,"color":"#FDB316"},{"offset":0.6667,"color":"#FFC955"},{"offset":0.75,"color":"#FFA3AA"},{"offset":0.8333,"color":"#FF81DCEC"},{"offset":0.9167,"color":"#FFA3ED76"},{"offset":1,"color":"#FFC0FD00"}],"Aurora":[{"offset":0,"color":"#031018"},{"offset":0.0833,"color":"#094534"},{"offset":0.1667,"color":"#0C6046"},{"offset":0.25,"color":"#12805A"},{"offset":0.3333,"color":"#1BA874"},{"offset":0.4167,"color":"#21C888"},{"offset":0.5,"color":"#5BDCA1"},{"offset":0.5833,"color":"#86ECB9"},{"offset":0.6667,"color":"#94F1CD"},{"offset":0.75,"color":"#77E3DC"},{"offset":0.8333,"color":"#65D9E9EC"},{"offset":0.9167,"color":"#A3EAED76"},{"offset":1,"color":"#CFFAF200"}],"Candy":[{"offset":0,"color":"#FE7AB6"},{"offset":0.0833,"color":"#FE87BF"},{"offset":0.1667,"color":"#FE94C8"},{"offset":0.25,"color":"#FEA0D1"},{"offset":0.3333,"color":"#EFA3E0"},{"offset":0.4167,"color":"#DDA6F0"},{"offset":0.5,"color":"#C9A8FF"},{"offset":0.5833,"color":"#BBBEFF"},{"offset":0.6667,"color":"#ADD1FF"},{"offset":0.75,"color":"#C6E1E9"},{"offset":0.8333,"color":"#F2EFC0"},{"offset":0.9167,"color":"#FFF8D498"},{"offset":1,"color":"#FFFFFF00"}],"Ember":[{"offset":0,"color":"#1F090C"},{"offset":0.0833,"color":"#520F0D"},{"offset":0.1667,"color":"#70140E"},{"offset":0.25,"color":"#87170E"},{"offset":0.3333,"color":"#AE2B0F"},{"offset":0.4167,"color":"#D63D10"},{"offset":0.5,"color":"#F74B11"},{"offset":0.5833,"color":"#FF6E17"},{"offset":0.6667,"color":"#FF8D1D"},{"offset":0.75,"color":"#FFAE4C"},{"offset":0.8333,"color":"#FFD48A"},{"offset":0.9167,"color":"#FFECB8B1"},{"offset":1,"color":"#FFF6E000"}],"Mono":[{"offset":0,"color":"#0A1A4A"},{"offset":0.0833,"color":"#18328B"},{"offset":0.1667,"color":"#2141B7"},{"offset":0.25,"color":"#274EDA"},{"offset":0.3333,"color":"#2E59F8"},{"offset":0.4167,"color":"#466CFD"},{"offset":0.5,"color":"#5B7FFD"},{"offset":0.5833,"color":"#6B90FD"},{"offset":0.6667,"color":"#86A6FD"},{"offset":0.75,"color":"#A6BEFE"},{"offset":0.8333,"color":"#C0D3FEEC"},{"offset":0.9167,"color":"#D5E2FE77"},{"offset":1,"color":"#E8F0FF00"}]}
const PALETTE_NAMES = Object.keys(PALETTES)

const STYLE = `
.dgp { --page:#f4f4f5; --surface:#fff; --line:rgba(0,0,0,0.09); --ring:rgba(0,0,0,0.22);
  --t1:#1b1b1b; --t2:#6b6b6b; --sel:#fcfcfc;
  display:flex; min-height:100vh; width:100%; align-items:center; justify-content:center;
  background:var(--page); color:var(--t1); padding:36px 24px;
  font-family:-apple-system,BlinkMacSystemFont,"SF Pro Text",Inter,"Segoe UI",system-ui,sans-serif; }
.dgp-wrap { width:100%; max-width:680px; }
.dgp-preview { border:1px solid var(--line); border-radius:16px 16px 0 0; background:var(--surface);
  height:340px; overflow:hidden; position:relative; }
.dgp-panel { border:1px solid var(--line); border-top:0; border-radius:0 0 16px 16px; background:var(--surface);
  padding:16px 18px 18px; display:flex; flex-direction:column; gap:12px; }
.dgp-row { display:flex; align-items:center; gap:14px; }
.dgp-row > .lab { color:var(--t2); font-size:13px; width:84px; flex:0 0 auto; }
.dgp-slider { position:relative; margin-left:auto; flex:1; height:34px; border:1px solid var(--line);
  border-radius:9px; background:var(--surface); display:flex; align-items:center; }
.dgp-slider input { -webkit-appearance:none; appearance:none; width:100%; height:34px; margin:0; background:transparent; cursor:pointer; }
.dgp-slider input::-webkit-slider-thumb { -webkit-appearance:none; appearance:none; width:3px; height:16px; border-radius:2px; background:var(--t1); opacity:.5; }
.dgp-slider input::-moz-range-thumb { width:3px; height:16px; border:0; border-radius:2px; background:var(--t1); opacity:.5; }
.dgp-slider .cap { position:absolute; left:12px; font-size:13px; color:var(--t2); pointer-events:none; }
.dgp-slider .val { position:absolute; right:12px; font-size:13px; color:var(--t2); font-variant-numeric:tabular-nums; pointer-events:none; }
.dgp-dd { position:relative; margin-left:auto; }
.dgp-dd-btn { display:flex; align-items:center; justify-content:space-between; gap:6px; height:34px; min-width:118px;
  padding:0 10px 0 12px; border:1px solid var(--line); border-radius:9px; background:var(--surface); color:var(--t1);
  font:inherit; font-size:13px; font-weight:500; cursor:pointer; outline:none; transition:border-color .15s ease; }
.dgp-dd-btn:hover { border-color:var(--ring); }
.dgp-dd-btn svg { color:var(--t2); transition:transform .18s ease; }
.dgp-dd-btn[data-open="true"] svg { transform:rotate(180deg); }
.dgp-dd-menu { position:absolute; top:calc(100% + 6px); right:0; z-index:20; min-width:168px;
  background:var(--surface); border:1px solid var(--line); border-radius:12px; padding:4px;
  box-shadow:0 1px 2px rgba(17,24,39,0.06), 0 8px 24px rgba(17,24,39,0.08); display:flex; flex-direction:column; gap:2px; }
.dgp-dd-opt { display:flex; align-items:center; width:100%; text-align:left; padding:8px 10px; border:0; border-radius:6px;
  background:transparent; color:var(--t2); font:inherit; font-size:13px; cursor:pointer; transition:background .12s ease,color .12s ease; }
.dgp-dd-opt:hover { background:rgba(0,0,0,0.04); color:var(--t1); }
.dgp-dd-opt[data-selected="true"] { background:var(--sel); color:var(--t1); font-weight:500; }
`

function Chevron() {
  return (<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.2" strokeLinecap="round" strokeLinejoin="round"><polyline points="6 9 12 15 18 9" /></svg>)
}

function Dropdown({ value, options, onChange, ariaLabel }: {
  value: string; options: string[]; onChange: (v: string) => void; ariaLabel: string
}) {
  const [open, setOpen] = useState(false)
  const root = useRef<HTMLDivElement>(null)
  useEffect(() => {
    if (!open) return
    const onDown = (e: MouseEvent) => { if (root.current && !root.current.contains(e.target as Node)) setOpen(false) }
    document.addEventListener("mousedown", onDown)
    return () => document.removeEventListener("mousedown", onDown)
  }, [open])
  return (
    <div className="dgp-dd" ref={root}>
      <button type="button" className="dgp-dd-btn" data-open={open ? "true" : "false"} aria-label={ariaLabel}
        aria-expanded={open} role="combobox" onClick={() => setOpen((o) => !o)}>
        <span>{value}</span>
        <Chevron />
      </button>
      {open && (
        <div className="dgp-dd-menu" role="listbox">
          {options.map((o) => (
            <button key={o} type="button" className="dgp-dd-opt" role="option" aria-selected={o === value}
              data-selected={o === value ? "true" : "false"} onClick={() => { onChange(o); setOpen(false) }}>
              {o}
            </button>
          ))}
        </div>
      )}
    </div>
  )
}

function Slider({ label, value, min, max, step, format, onChange }: {
  label: string; value: number; min: number; max: number; step: number
  format: (v: number) => string; onChange: (v: number) => void
}) {
  return (
    <div className="dgp-row">
      <span className="lab">{label}</span>
      <div className="dgp-slider">
        <input type="range" min={min} max={max} step={step} value={value} aria-label={label}
          onChange={(e) => onChange(Number(e.target.value))} />
        <span className="val">{format(value)}</span>
      </div>
    </div>
  )
}

function RiseLoop({ children }: { children: ReactNode }) {
  // loop the aurora rise so the effect is always visible on the card
  const [up, setUp] = useState(false)
  useEffect(() => {
    const id = setInterval(() => setUp((u) => !u), 2100)
    const t = setTimeout(() => setUp(true), 120)
    return () => { clearInterval(id); clearTimeout(t) }
  }, [])
  return (
    <>
      <span data-ghost-open={up ? "true" : "false"} style={{ display: "none" }} />
      <div style={{ position: "absolute", inset: 0, transformOrigin: "bottom",
        transform: up ? "scaleY(1)" : "scaleY(0)",
        transition: "transform 1100ms cubic-bezier(0.16, 1, 0.3, 1)" }}>
        {children}
      </div>
    </>
  )
}

export default function Default() {
  const [palette, setPalette] = useState("Candy")
  const [bars, setBars] = useState(9)
  const [blur, setBlur] = useState(15)
  const [peak, setPeak] = useState(0.98)
  const [valley, setValley] = useState(0.55)

  return (
    <>
      <style>{STYLE}</style>
      <div className="dgp">
        <div className="dgp-wrap">
          <div className="dgp-preview">
            <RiseLoop>
              <DiaGradient stops={PALETTES[palette]} bars={bars} blur={blur} peak={peak} valley={valley} riseMs={0} />
            </RiseLoop>
          </div>
          <div className="dgp-panel">
            <div className="dgp-row">
              <span className="lab">Palette</span>
              <Dropdown ariaLabel="Palette" value={palette} options={PALETTE_NAMES} onChange={setPalette} />
            </div>
            <Slider label="Bars" value={bars} min={3} max={21} step={1} format={(v) => String(v)} onChange={setBars} />
            <Slider label="Blur" value={blur} min={2} max={40} step={1} format={(v) => String(v)} onChange={setBlur} />
            <Slider label="Peak" value={peak} min={0.4} max={1} step={0.01} format={(v) => Math.round(v * 100) + "%"} onChange={setPeak} />
            <Slider label="Valley" value={valley} min={0.1} max={1} step={0.01} format={(v) => Math.round(v * 100) + "%"} onChange={setValley} />
          </div>
        </div>
      </div>
    </>
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


## Gradient Shimmer

**Author:** @mona_biasia
**URL:** https://21st.dev/@mona_biasia/components/gradient-shimmer

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
gradient-shimmer.tsx
// Full source: https://21st.dev/@mona_biasia/components/gradient-shimmer
// Install via: npx @21st-dev/magic add gradient-shimmer
// Or copy the component code from the 21st.dev page above.

"use client"

import { useState } from "react"
import {
  GradientShimmer,
  gradientPresets,
  type EasingPreset,
  type GradientPresetName,
} from "@/components/ui/gradient-shimmer"

const PRESETS = Object.keys(gradientPresets) as GradientPresetName[]
const EASINGS: { value: EasingPreset; label: string }[] = [
  { value: "smooth", label: "Smooth" },
  { value: "gentle", label: "Gentle" },
  { value: "snappy", label: "Snappy" },
]

/** 180deg swatch preview of a preset's stops (matches the original site). */
function swatchGradient(name: GradientPresetName) {
  const stops = [...gradientPresets[name]].sort((a, b) => a.position - b.position)
  return `linear-gradient(180deg, ${stops
    .map((s) => `${s.color} ${Math.round(s.position * 100)}%`)
    .join(", ")})`
}

const STYLE = `
.gsp {
  --bg: #ffffff; --fg: #1c1c1e; --muted: #8a8a90;
  --border: rgba(0,0,0,.1); --bg-weak: #f5f5f3; --surface: #ffffff;
  --shadow: 0 1px 2px rgba(0,0,0,.05); --ring: #1c1c1e;
  --mono: ui-monospace, SFMono-Regular, "SF Mono", Menlo, monospace;
  display: flex; min-height: 100vh; width: 100%;
  align-items: center; justify-content: center;
  background: var(--bg); color: var(--fg);
  font-family: -apple-system, BlinkMacSystemFont, "SF Pro Text", Inter, "Segoe UI", system-ui, sans-serif;
  padding: 40px 24px;
}
@media (prefers-color-scheme: dark) {
  .gsp {
    --bg: #0b0b0d; --fg: #f1f1f4; --muted: #85858d;
    --border: rgba(255,255,255,.12); --bg-weak: #161619; --surface: #161619;
    --shadow: 0 1px 2px rgba(0,0,0,.4); --ring: #f1f1f4;
  }
}
.gsp-inner { width: 100%; max-width: 560px; display: flex; flex-direction: column; align-items: center; }
.gsp-title { min-height: 72px; display: flex; align-items: center; justify-content: center; text-align: center; }
.gsp-install {
  margin-top: 8px; display: inline-flex; align-items: center; justify-content: space-between; gap: 12px;
  width: 100%; max-width: 380px; padding: 12px 16px; border-radius: 14px;
  background: var(--surface); border: .5px solid var(--border); box-shadow: var(--shadow);
  font-family: var(--mono); font-size: 14px; color: var(--fg);
}
.gsp-install .muted { color: var(--muted); }
.gsp-copy { display: inline-flex; padding: 0; border: 0; background: transparent; color: var(--muted); cursor: pointer; }
.gsp-copy:hover { color: var(--fg); }
.gsp-swatches { margin-top: 20px; display: flex; gap: 14px; flex-wrap: wrap; justify-content: center; }
.gsp-swatch { width: 34px; height: 34px; border-radius: 999px; border: 0; padding: 0; cursor: pointer;
  box-shadow: 0 0 0 1px var(--border); transition: transform .2s cubic-bezier(.34,1.4,.5,1), box-shadow .2s ease; }
.gsp-swatch:hover { transform: scale(1.09); }
.gsp-swatch[data-active="true"] { box-shadow: 0 0 0 2px var(--bg), 0 0 0 4px var(--ring); }
.gsp-divider { width: 100%; height: 1px; background: var(--border); margin: 30px 0; }
.gsp-controls { width: 100%; display: flex; flex-direction: column; gap: 18px; }
.gsp-row { display: flex; align-items: center; gap: 16px; }
.gsp-label { color: var(--muted); font-size: 14px; }
.gsp-row > .gsp-label { width: 64px; flex: 0 0 auto; }
.gsp-input { flex: 1; padding: 9px 12px; border-radius: 10px; border: .5px solid var(--border);
  background: var(--surface); color: var(--fg); font: inherit; font-size: 14px; outline: none; }
.gsp-input:focus { border-color: var(--ring); }
.gsp-seg { margin-left: auto; display: inline-flex; gap: 2px; padding: 3px; border-radius: 12px;
  background: var(--bg-weak); }
.gsp-seg button { padding: 7px 16px; border-radius: 10px; border: 0; cursor: pointer;
  font-size: 14px; font-weight: 500; background: transparent; color: var(--muted); transition: all .2s ease; }
.gsp-seg button[data-active="true"] { background: var(--surface); color: var(--fg); box-shadow: var(--shadow); }
.gsp-slider { display: flex; flex-direction: column; gap: 8px; width: 100%; }
.gsp-slider-head { display: flex; justify-content: space-between; font-size: 14px; }
.gsp-slider-head .val { color: var(--fg); font-variant-numeric: tabular-nums; }
.gsp input[type=range] { -webkit-appearance: none; appearance: none; width: 100%; height: 16px;
  background: transparent; cursor: pointer; margin: 0; }
.gsp input[type=range]::-webkit-slider-runnable-track { height: 3px; border-radius: 3px; background: var(--bg-weak); }
.gsp input[type=range]::-moz-range-track { height: 3px; border-radius: 3px; background: var(--bg-weak); }
.gsp input[type=range]::-webkit-slider-thumb { -webkit-appearance: none; appearance: none; margin-top: -5px;
  width: 13px; height: 13px; border-radius: 50%; background: var(--fg); border: 2px solid var(--bg);
  box-shadow: 0 1px 2px rgba(0,0,0,.25); }
.gsp input[type=range]::-moz-range-thumb { width: 13px; height: 13px; border-radius: 50%; background: var(--fg);
  border: 2px solid var(--bg); box-shadow: 0 1px 2px rgba(0,0,0,.25); }
.gsp-section-title { margin: 4px 0 20px; font-size: 12px; font-weight: 600; letter-spacing: .12em;
  text-transform: uppercase; color: var(--muted); text-align: center; }
.gsp-sidebar { width: 100%; max-width: 320px; background: var(--surface); border: .5px solid var(--border);
  border-radius: 20px; box-shadow: var(--shadow); padding: 8px; display: flex; flex-direction: column; gap: 2px; }
.gsp-channel { display: flex; align-items: center; gap: 10px; padding: 10px 12px; border-radius: 12px;
  font-size: 16px; color: var(--muted); }
.gsp-channel[data-active="true"] { background: var(--bg-weak); color: var(--fg); }
.gsp-channel .hash { color: var(--muted); opacity: .8; }
`

function CopyIcon() {
  return (
    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
      <rect x="9" y="9" width="13" height="13" rx="2" ry="2" />
      <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1" />
    </svg>
  )
}

function Slider({
  label, value, min, max, step, format, onChange,
}: {
  label: string; value: number; min: number; max: number; step: number
  format: (v: number) => string; onChange: (v: number) => void
}) {
  return (
    <div className="gsp-slider">
      <div className="gsp-slider-head">
        <span className="gsp-label">{label}</span>
        <span className="val">{format(value)}</span>
      </div>
      <input type="range" min={min} max={max} step={step} value={value}
        onChange={(e) => onChange(Number(e.target.value))} />
    </div>
  )
}

export default function Default() {
  const [text, setText] = useState("gradient-shimmer")
  const [gradient, setGradient] = useState<GradientPresetName>("sunrise")
  const [easing, setEasing] = useState<EasingPreset>("smooth")
  const [duration, setDuration] = useState(1.45)
  const [spread, setSpread] = useState(3)
  const [angle, setAngle] = useState(105)
  const [pauseBetween, setPauseBetween] = useState(700)

  const label = text.trim() === "" ? "gradient-shimmer" : text
  // Every live control feeds both the hero and the sidebar channel, so the
  // sidebar is a continuation of the same component — not a separate example.
  const shimmerProps = {
    gradient,
    easing,
    duration,
    spread,
    angle,
    pauseBetween,
    pauseOnScroll: false,
  }

  return (
    <>
      <style>{STYLE}</style>
      <div className="gsp">
        <div className="gsp-inner">
          <div className="gsp-title">
            <GradientShimmer
              {...shimmerProps}
              style={{ fontSize: 56, fontWeight: 700, letterSpacing: "-0.03em", maxWidth: "100%" }}
            >
              {label}
            </GradientShimmer>
          </div>

          <div className="gsp-install">
            <span><span className="muted">$</span>&nbsp;&nbsp;npm i gradient-shimmer</span>
            <button
              type="button"
              className="gsp-copy"
              aria-label="Copy install command"
              onClick={() => navigator.clipboard?.writeText("npm i gradient-shimmer").catch(() => {})}
            >
              <CopyIcon />
            </button>
          </div>

          <div className="gsp-swatches">
            {PRESETS.map((name) => (
              <button
                key={name}
                type="button"
                className="gsp-swatch"
                data-active={gradient === name}
                aria-label={name}
                style={{ backgroundImage: swatchGradient(name) }}
                onClick={() => setGradient(name)}
              />
            ))}
          </div>

          <div className="gsp-divider" />

          <div className="gsp-controls">
            <div className="gsp-row">
              <span className="gsp-label">Text</span>
              <input
                className="gsp-input"
                type="text"
                value={text}
                onChange={(e) => setText(e.target.value)}
                placeholder="gradient-shimmer"
                spellCheck={false}
              />
            </div>

            <div className="gsp-row">
              <span className="gsp-label">Easing</span>
              <div className="gsp-seg">
                {EASINGS.map((e) => (
                  <button key={e.value} type="button" data-active={easing === e.value} onClick={() => setEasing(e.value)}>
                    {e.label}
                  </button>
                ))}
              </div>
            </div>

            <Slider label="Speed" value={duration} min={0.6} max={8} step={0.05}
              format={(v) => `${v.toFixed(2)}s`} onChange={setDuration} />
            <Slider label="Spread" value={spread} min={1} max={8} step={0.5}
              format={(v) => `${v}px/char`} onChange={setSpread} />
            <Slider label="Angle" value={angle} min={0} max={180} step={1}
              format={(v) => `${Math.round(v)}°`} onChange={setAngle} />
            <Slider label="Pause" value={pauseBetween} min={0} max={3000} step={50}
              format={(v) => `${Math.round(v)}ms`} onChange={setPauseBetween} />
          </div>

          <div className="gsp-divider" />

          {/* Continuation — the same shimmer, in context */}
          <div className="gsp-section-title">In the channel sidebar</div>
          <div className="gsp-sidebar">
            <div className="gsp-channel"><span className="hash">#</span><span>general</span></div>
            <div className="gsp-channel" data-active="true">
              <span className="hash">#</span>
              <GradientShimmer {...shimmerProps}>{label}</GradientShimmer>
            </div>
            <div className="gsp-channel"><span className="hash">#</span><span>design-sync</span></div>
            <div className="gsp-channel"><span className="hash">#</span><span>release-notes</span></div>
          </div>
        </div>
      </div>
    </>
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


## Gradient Chat Input

**Author:** @ruixenui
**URL:** https://21st.dev/@ruixenui/components/gradient-chat-input

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
gradient-chat-input.tsx
// Full source: https://21st.dev/@ruixenui/components/gradient-chat-input
// Install via: npx @21st-dev/magic add gradient-chat-input
// Or copy the component code from the 21st.dev page above.

import GradientChatInput from "@/components/ui/gradient-chat-input";

export default function DemoOne() {
  return (
    <div className="relative flex h-[600px] w-full items-center justify-center overflow-hidden p-8">
      <GradientChatInput
        placeholder="Send Message"
        autoReply="Got it — looking into that now ✨"
        onSend={(message) => console.log("sent:", message)}
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


## Liquid Gradient

**Author:** @aayush-duhan
**URL:** https://21st.dev/@aayush-duhan/components/liquid-gradient

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
liquid-gradient.tsx
// Full source: https://21st.dev/@aayush-duhan/components/liquid-gradient
// Install via: npx @21st-dev/magic add liquid-gradient
// Or copy the component code from the 21st.dev page above.

"use client";

import { useMemo, useState } from "react";
import {
  LiquidGradientCanvas,
  LIQUID_GRADIENT_PRESETS,
  type LiquidGradientPresetName,
} from "@/components/ui/liquid-gradient";

const PRESETS: { key: LiquidGradientPresetName; label: string }[] = [
  { key: "sunset", label: "Sunset" },
  { key: "aurora", label: "Aurora" },
  { key: "vibrant", label: "Vibrant" },
  { key: "magma", label: "Magma" },
  { key: "subtleDark", label: "Subtle" },
];

export default function LiquidGradientDemo() {
  const [preset, setPreset] = useState<LiquidGradientPresetName>("sunset");
  const [speed, setSpeed] = useState(0.6);
  const [paused, setPaused] = useState(false);

  const params = useMemo(() => LIQUID_GRADIENT_PRESETS[preset], [preset]);

  return (
    <div className="flex min-h-[600px] w-full items-center justify-center p-4 sm:p-8">
      <div className="relative h-[540px] w-full max-w-3xl overflow-hidden rounded-3xl border border-white/10 shadow-2xl">
        <LiquidGradientCanvas
          {...params}
          speed={speed}
          paused={paused}
          className="absolute inset-0 h-full w-full"
        />

        <div className="relative flex h-full flex-col justify-between p-6 sm:p-8">
          <div className="flex justify-end">
            <button
              type="button"
              onClick={() => setPaused((p) => !p)}
              className="rounded-full border border-white/20 bg-white/10 px-4 py-1.5 text-xs font-medium text-white backdrop-blur-md transition-colors hover:bg-white/20"
            >
              {paused ? "Play" : "Pause"}
            </button>
          </div>

          <div className="flex flex-col gap-4">
            <div className="flex flex-wrap gap-2">
              {PRESETS.map(({ key, label }) => (
                <button
                  key={key}
                  type="button"
                  onClick={() => setPreset(key)}
                  className={`rounded-full border px-3 py-1.5 text-xs font-medium backdrop-blur-md transition-colors ${
                    preset === key
                      ? "border-white/60 bg-white/25 text-white"
                      : "border-white/15 bg-white/5 text-white/70 hover:bg-white/15"
                  }`}
                >
                  {label}
                </button>
              ))}
            </div>

            <label className="flex items-center gap-3 text-xs font-medium text-white/80">
              <span className="w-12 shrink-0">Speed</span>
              <input
                type="range"
                min={0}
                max={2}
                step={0.05}
                value={speed}
                onChange={(e) => setSpeed(parseFloat(e.target.value))}
                className="h-1 flex-1 cursor-pointer appearance-none rounded-full bg-white/20 accent-white"
                aria-label="Animation speed"
              />
              <span className="w-10 shrink-0 text-right font-mono tabular-nums">
                {speed.toFixed(2)}
              </span>
            </label>
          </div>
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


## Mesh Gradient Shader

**Author:** @nlace-com
**URL:** https://21st.dev/@nlace-com/components/mesh-gradient-shader

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
mesh-gradient-shader.tsx
// Full source: https://21st.dev/@nlace-com/components/mesh-gradient-shader
// Install via: npx @21st-dev/magic add mesh-gradient-shader
// Or copy the component code from the 21st.dev page above.

// Demo for the NLACE Mesh Gradient background component
import { MeshGradient } from "@/components/ui/mesh-gradient-shader";

export default function DemoOne() {
  return (
    <div style={{ position: "relative", width: "100%", height: "100vh" }}>
      <MeshGradient speed={10} intensity={2} grain={0.75} />
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


## Siri Wave

**Author:** @40973894
**URL:** https://21st.dev/@40973894/components/siri-wave

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
siri-wave.tsx
// Full source: https://21st.dev/@40973894/components/siri-wave
// Install via: npx @21st-dev/magic add siri-wave
// Or copy the component code from the 21st.dev page above.

import { SiriWave } from "@/components/ui/siri-wave"

export default function SiriWaveDemo() {
  return (
    <div className="flex min-h-screen w-full items-center justify-center bg-[#0a0a0c] p-8">
      <SiriWave
        variant="wave"
        size={360}
        className="shadow-[0_20px_60px_rgba(0,0,0,0.6)]"
      />
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


## Flightcn Satellite Orbits

**Author:** @ridemountainpig
**URL:** https://21st.dev/@ridemountainpig/components/flightcn-satellite-orbits

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
flightcn-satellite-orbits.tsx
// Full source: https://21st.dev/@ridemountainpig/components/flightcn-satellite-orbits
// Install via: npx @21st-dev/magic add flightcn-satellite-orbits
// Or copy the component code from the 21st.dev page above.

"use client";

import { SatelliteOrbits, Map } from "@/components/ui/flightcn-satellite-orbits";

export default function DefaultSatelliteOrbitsDemo() {
  return (
    <div className="flex min-h-screen w-full items-center justify-center overflow-hidden bg-background p-8">
      <div className="h-[520px] w-full max-w-4xl overflow-hidden rounded-lg border bg-background shadow-sm">
        <Map projection={{ type: "globe" }} center={[8, 16]} zoom={1.05}>
          <SatelliteOrbits
            orbits={[
              {
                inclination: 51.6,
                ascendingNode: -28,
                name: "ISS",
                orbitColor: "#213448",
                groundTrackColor: "#213448",
              },
              {
                inclination: 97.4,
                ascendingNode: 38,
                name: "NOAA-20",
                orbitColor: "#547792",
                groundTrackColor: "#547792",
              },
              {
                inclination: 53,
                ascendingNode: -120,
                name: "Starlink",
                orbitColor: "#94B4C1",
                groundTrackColor: "#94B4C1",
              },
            ]}
            duration={12000}
            altitudePx={28}
            showGlow={true}
            showConnector={true}
            connectorLineStyle="dash"
            animate={{ duration: 12000 }}
            showLabel={true}
            labelPosition="right"
            satelliteIconRotationOffset={0}
          />
        </Map>
      </div>
    </div>
  );
}

export { DefaultSatelliteOrbitsDemo };

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


## Flightcn Satellite Orbit

**Author:** @ridemountainpig
**URL:** https://21st.dev/@ridemountainpig/components/flightcn-satellite-orbit

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
flightcn-satellite-orbit.tsx
// Full source: https://21st.dev/@ridemountainpig/components/flightcn-satellite-orbit
// Install via: npx @21st-dev/magic add flightcn-satellite-orbit
// Or copy the component code from the 21st.dev page above.

"use client";

import { SatelliteOrbit, Map } from "@/components/ui/flightcn-satellite-orbit";

export default function DefaultSatelliteOrbitDemo() {
  return (
    <div className="flex min-h-screen w-full items-center justify-center overflow-hidden bg-background p-8">
      <div className="h-[520px] w-full max-w-4xl overflow-hidden rounded-lg border bg-background shadow-sm">
        <Map projection={{ type: "globe" }} center={[8, 16]} zoom={1.05}>
          <SatelliteOrbit
            inclination={51.6}
            ascendingNode={-28}
            altitudePx={28}
            orbitWidth={2.2}
            groundTrackWidth={1.4}
            showGlow={true}
            showConnector={true}
            orbitLineStyle="solid"
            groundTrackLineStyle="dash"
            connectorLineStyle="dash"
            animate={{ duration: 12000 }}
            satelliteIconRotationOffset={0}
            name="ISS"
            showLabel={true}
            labelPosition="right"
          />
        </Map>
      </div>
    </div>
  );
}

export { DefaultSatelliteOrbitDemo };

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

