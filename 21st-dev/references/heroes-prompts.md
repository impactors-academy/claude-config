# 21st.dev — Hero Sections — Full Integration Prompts

60 components sorted by popularity.
Each section is a copy-paste ready prompt for Claude or any AI coding tool.

---

## Hero 195

**Author:** @shadcnblockscom | **Used:** 980x
**URL:** https://21st.dev/@shadcnblockscom/components/hero-195-1
**Install:** `npx shadcn@latest add "https://21st.dev/r/shadcnblockscom/hero-195-1?api_key=$API_KEY_21ST"`
**Description:** A modern hero section with tabs, animated border and crisp fading background lines framing the hero images.

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
hero-195-1.tsx
// Full source available at: https://21st.dev/@shadcnblockscom/components/hero-195-1
// Or install via: npx shadcn@latest add "https://21st.dev/r/shadcnblockscom/hero-195-1?api_key=$API_KEY_21ST"

import { Hero195 } from "@/components/ui/hero-195";

const DemoOne = () => {
  return (
    <Hero195 />
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


## Hero

**Author:** @reuno-ui | **Used:** 720x
**URL:** https://21st.dev/@reuno-ui/components/hero
**Install:** `npx shadcn@latest add "https://21st.dev/r/reuno-ui/hero?api_key=$API_KEY_21ST"`
**Description:** sleek Hero section with background paper shaders 

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
hero.tsx
// Full source available at: https://21st.dev/@reuno-ui/components/hero
// Or install via: npx shadcn@latest add "https://21st.dev/r/reuno-ui/hero?api_key=$API_KEY_21ST"

import ShaderShowcase from "@/components/ui/hero";

export default function DemoOne() {
  return (
    <div className="min-h-screen h-full w-full">
    <ShaderShowcase/>
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


## Hero section with smooth bg Shader

**Author:** @moazamtrade | **Used:** 615x
**URL:** https://21st.dev/@moazamtrade/components/hero-section-with-smooth-bg-shader
**Install:** `npx shadcn@latest add "https://21st.dev/r/moazamtrade/hero-section-with-smooth-bg-shader?api_key=$API_KEY_21ST"`
**Description:** Hero section with smooth Shader and data passing using props 

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
hero-section-with-smooth-bg-shader.tsx
// Full source available at: https://21st.dev/@moazamtrade/components/hero-section-with-smooth-bg-shader
// Or install via: npx shadcn@latest add "https://21st.dev/r/moazamtrade/hero-section-with-smooth-bg-shader?api_key=$API_KEY_21ST"


import { HeroSection } from "@/components/ui/hero-section-with-smooth-bg-shader";

export default function DemoOne() {
  return <HeroSection 
  distortion={1.2}
  speed={0.8}
/>;
}

/*
Usage examples:

// Basic usage with defaults
<HeroSection />

// Custom content
<HeroSection 
  title="Revolutionary AI Solutions for"
  highlightText="Modern Business"
  description="Streamline operations with cutting-edge AI technology"
  buttonText="Get Started"
  onButtonClick={() => console.log('Button clicked!')}
/>

// Custom colors and animation
<HeroSection 
  colors={["#ff6b6b", "#4ecdc4", "#45b7d1"]}
  distortion={1.2}
  speed={0.8}
/>


*/
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


## Hero

**Author:** @beratberkayg | **Used:** 525x
**URL:** https://21st.dev/@beratberkayg/components/hero-1
**Install:** `npx shadcn@latest add "https://21st.dev/r/beratberkayg/hero-1?api_key=$API_KEY_21ST"`
**Description:** animated hero

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
hero-1.tsx
// Full source available at: https://21st.dev/@beratberkayg/components/hero-1
// Or install via: npx shadcn@latest add "https://21st.dev/r/beratberkayg/hero-1?api_key=$API_KEY_21ST"


import { Hero } from "@/components/ui/hero-1";

export default function DemoOne() {
  return (
    <Hero title="Build smarter tools for modern teams"
  subtitle="Streamline your workflow and boost productivity with intuitive solutions. Security, speed, and simplicity—all in one platform."
  eyebrow="Next-Gen Productivity"
  ctaLabel="Get Started"
  ctaHref="#"/>
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


## Hero Section

**Author:** @ravikatiyar162 | **Used:** 451x
**URL:** https://21st.dev/@ravikatiyar162/components/hero-section-2
**Install:** `npx shadcn@latest add "https://21st.dev/r/ravikatiyar162/hero-section-2?api_key=$API_KEY_21ST"`
**Description:** Clean, split-screen hero layout with bold headline, adventure call-to-action, and animated floral imagery for an engaging first impression.

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
hero-section-2.tsx
// Full source available at: https://21st.dev/@ravikatiyar162/components/hero-section-2
// Or install via: npx shadcn@latest add "https://21st.dev/r/ravikatiyar162/hero-section-2?api_key=$API_KEY_21ST"

import React from 'react';
import { HeroSection } from '@/components/ui/hero-section-2'; // Adjust the import path as needed

export default function HeroSectionDemo() {
  return (
    <div className="w-full">
      <HeroSection
        logo={{
            url: "https://vucvdpamtrjkzmubwlts.supabase.co/storage/v1/object/public/users/user_2zMtrqo9RMaaIn4f8F2z3oeY497/avatar.png",
            alt: "Company Logo",
            text: "Your Logo"
        }}
        slogan="ELEVATE YOUR PERSPECTIVE"
        title={
          <>
            Each Peak <br />
            <span className="text-primary">Teaches Something</span>
          </>
        }
        subtitle="Discover breathtaking landscapes and challenge yourself with our guided mountain expeditions. Join a community of adventurers."
        callToAction={{
          text: "JOIN US TO EXPLORE",
          href: "#explore",
        }}
        backgroundImage="https://plus.unsplash.com/premium_photo-1754738812660-11ca16e5b8bd?w=900&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxmZWF0dXJlZC1waG90b3MtZmVlZHwxN3x8fGVufDB8fHx8fA%3D%3D"
        contactInfo={{
            website: "yourwebsite.com",
            phone: "+1 (555) 123-4567",
            address: "20 Fieldstone Dr, Roswell, GA",
        }}
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


## Hero 2

**Author:** @preetsuthar17 | **Used:** 386x
**URL:** https://21st.dev/@preetsuthar17/components/hero-2-1
**Install:** `npx shadcn@latest add "https://21st.dev/r/preetsuthar17/hero-2-1?api_key=$API_KEY_21ST"`
**Description:** Beautiful, grainy hero component for an email-related website

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
hero-2-1.tsx
// Full source available at: https://21st.dev/@preetsuthar17/components/hero-2-1
// Or install via: npx shadcn@latest add "https://21st.dev/r/preetsuthar17/hero-2-1?api_key=$API_KEY_21ST"

import { Hero2 } from "@/components/ui/hero-2-1";

const DemoOne = () => {
  return (
    <div>
      <Hero2 />
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


## Hero Section

**Author:** @ravikatiyar162 | **Used:** 328x
**URL:** https://21st.dev/@ravikatiyar162/components/hero-section-9
**Install:** `npx shadcn@latest add "https://21st.dev/r/ravikatiyar162/hero-section-9?api_key=$API_KEY_21ST"`
**Description:** Hero Section Component
This component creates a dynamic and engaging hero section, perfect for landing pages. It features a two-column layout with animated text, actionable buttons, social proof statistics, and a visually appealing image collage.

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
hero-section-9.tsx
// Full source available at: https://21st.dev/@ravikatiyar162/components/hero-section-9
// Or install via: npx shadcn@latest add "https://21st.dev/r/ravikatiyar162/hero-section-9?api_key=$API_KEY_21ST"

import HeroSection from '@/components/ui/hero-section-9'; // Adjust the import path as needed
import { Users, Briefcase, Link as LinkIcon } from 'lucide-react';

const HeroSectionDemo = () => {
  // Sample data to be passed as props
  const heroData = {
    title: (
      <>
        A new way to learn <br /> & get knowledge
      </>
    ),
    subtitle: 'EduFlex is here for you with various courses & materials from skilled tutors all around the world.',
    actions: [
      {
        text: 'Join the Class',
        onClick: () => alert('Join the Class clicked!'),
        variant: 'default',
      },
      {
        text: 'Learn more',
        onClick: () => alert('Learn More clicked!'),
        variant: 'outline',
      },
    ],
    stats: [
      {
        value: '15,2K',
        label: 'Active students',
        icon: <Users className="h-5 w-5 text-muted-foreground" />,
      },
      {
        value: '4,5K',
        label: 'Tutors',
        icon: <Briefcase className="h-5 w-5 text-muted-foreground" />,
      },
      {
        value: 'Resources',
        label: '',
        icon: <LinkIcon className="h-5 w-5 text-muted-foreground" />,
      },
    ],
    images: [
      'https://images.unsplash.com/photo-1522202176988-66273c2fd55f?q=80&w=2071&auto=format&fit=crop',
      'https://images.unsplash.com/photo-1543269865-cbf427effbad?q=80&w=2070&auto=format&fit=crop',
      'https://plus.unsplash.com/premium_photo-1663054774427-55adfb2be76f?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8cGVvcGxlfGVufDB8fDB8fHww&auto=format&fit=crop&q=60&w=900?q=80&w=2070&auto=format&fit=crop',
    ],
  };

  return (
    <div className="w-full bg-background">
      <HeroSection
        title={heroData.title}
        subtitle={heroData.subtitle}
        actions={heroData.actions}
        stats={heroData.stats}
        images={heroData.images}
      />
    </div>
  );
};

export default HeroSectionDemo;
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


## Modern Hero

**Author:** @shadcnblockscom | **Used:** 313x
**URL:** https://21st.dev/@shadcnblockscom/components/modern-hero
**Install:** `npx shadcn@latest add "https://21st.dev/r/shadcnblockscom/modern-hero?api_key=$API_KEY_21ST"`
**Description:** Modern Hero

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
modern-hero.tsx
// Full source available at: https://21st.dev/@shadcnblockscom/components/modern-hero
// Or install via: npx shadcn@latest add "https://21st.dev/r/shadcnblockscom/modern-hero?api_key=$API_KEY_21ST"

import { Hero7 } from "@/components/blocks/modern-hero"

const demoData = {
  heading: "A Collection of Components Built With Shadcn & Tailwind",
  description:
    "Finely crafted components built with React, Tailwind and Shadcn UI. Developers can copy and paste these blocks directly into their project.",
  button: {
    text: "Discover all components",
    url: "https://www.shadcnblocks.com",
  },
  reviews: {
    count: 200,
    avatars: [
      {
        src: "https://www.shadcnblocks.com/images/block/avatar-1.webp",
        alt: "Avatar 1",
      },
      {
        src: "https://www.shadcnblocks.com/images/block/avatar-2.webp",
        alt: "Avatar 2",
      },
      {
        src: "https://www.shadcnblocks.com/images/block/avatar-3.webp",
        alt: "Avatar 3",
      },
      {
        src: "https://www.shadcnblocks.com/images/block/avatar-4.webp",
        alt: "Avatar 4",
      },
      {
        src: "https://www.shadcnblocks.com/images/block/avatar-5.webp",
        alt: "Avatar 5",
      },
    ],
  },
};

function Hero7Demo() {
  return <Hero7 {...demoData} />;
}

export { Hero7Demo };

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


## Hero Section

**Author:** @reuno-ui | **Used:** 297x
**URL:** https://21st.dev/@reuno-ui/components/hero-section
**Install:** `npx shadcn@latest add "https://21st.dev/r/reuno-ui/hero-section?api_key=$API_KEY_21ST"`
**Description:** Hero component with sleek animation 

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
hero-section.tsx
// Full source available at: https://21st.dev/@reuno-ui/components/hero-section
// Or install via: npx shadcn@latest add "https://21st.dev/r/reuno-ui/hero-section?api_key=$API_KEY_21ST"

import { Component } from "@/components/ui/hero-section";

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


## Shaders Hero Section

**Author:** @vaib215 | **Used:** 287x
**URL:** https://21st.dev/@vaib215/components/shaders-hero-section
**Install:** `npx shadcn@latest add "https://21st.dev/r/vaib215/shaders-hero-section?api_key=$API_KEY_21ST"`
**Description:** a modern sleek smooth shader gradient hero section

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
shaders-hero-section.tsx
// Full source available at: https://21st.dev/@vaib215/components/shaders-hero-section
// Or install via: npx shadcn@latest add "https://21st.dev/r/vaib215/shaders-hero-section?api_key=$API_KEY_21ST"

"use client"

import {Header, HeroContent, PulsingCircle, ShaderBackground} from "@/components/ui/shaders-hero-section"

export default function ShaderShowcase() {
  return (
    <ShaderBackground>
      <Header />
      <HeroContent />
      <PulsingCircle />
    </ShaderBackground>
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


## AnomalousMatterHero

**Author:** @dhileepkumargm | **Used:** 257x
**URL:** https://21st.dev/@dhileepkumargm/components/anomalous-matter-hero
**Install:** `npx shadcn@latest add "https://21st.dev/r/dhileepkumargm/anomalous-matter-hero?api_key=$API_KEY_21ST"`
**Description:** A full-screen hero section layered over a generative 3D shader background. Features animated Perlin-displaced geometry, dynamic lighting, and customizable overlay content. Ideal for immersive landing pages, sci-fi themes, or experimental UI.

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
anomalous-matter-hero.tsx
// Full source available at: https://21st.dev/@dhileepkumargm/components/anomalous-matter-hero
// Or install via: npx shadcn@latest add "https://21st.dev/r/dhileepkumargm/anomalous-matter-hero?api_key=$API_KEY_21ST"

import React from "react";
import { AnomalousMatterHero } from "@/components/ui/anomalous-matter-hero";

function App() {
  return (
    <AnomalousMatterHero
      title="Launch Sequence: Anomaly 12"
      subtitle="Energy dances along unseen frontiers."
      description="This demo shows how to override the default copy and integrate hero into a page layout."
    />
  );
}

export default App;
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


## Dynamic Hero

**Author:** @easemize | **Used:** 247x
**URL:** https://21st.dev/@easemize/components/dynamic-hero
**Install:** `npx shadcn@latest add "https://21st.dev/r/easemize/dynamic-hero?api_key=$API_KEY_21ST"`
**Description:** Elevate your landing page with this interactive React hero component. It captivates users with a unique arrow animation that tracks mouse movement, pointing towards the main call-to-action. Highly customizable, allowing you to define the heading, tagline, button text, and embed rich media (images or videos) in the designated card section. Seamlessly integrates with Tailwind CSS projects and follows modern React best practices for reusability.

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
dynamic-hero.tsx
// Full source available at: https://21st.dev/@easemize/components/dynamic-hero
// Or install via: npx shadcn@latest add "https://21st.dev/r/easemize/dynamic-hero?api_key=$API_KEY_21ST"

import { HeroSection } from "@/components/ui/dynamic-hero";

const DemoOne = () => {
   const myImage = (
    <img 
      src="https://images.unsplash.com/photo-1506744038136-46273834b3fb?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8bGFuZHNjYXBlfGVufDB8fDB8fHww&auto=format&fit=crop&w=800&q=60" 
      alt="Beautiful Landscape"
      className="w-full h-full object-cover"
    />
  );

  const myVideo = (
    <video 
      src="https://www.w3schools.com/html/mov_bbb.mp4" // Replace with your video URL
      autoPlay 
      loop 
      muted 
      playsInline
      className="w-full h-full object-cover"
    >
      Your browser does not support the video tag.
    </video>
  );

  return (
    <div>
      <HeroSection
        heading="Dynamic Design, Direct Action"
        tagline="Experience a hero section that not only looks great but actively leads your audience. Get started with a click."
        buttonText="Learn More"
        imageUrl="https://images.unsplash.com/photo-1506744038136-46273834b3fb?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8bGFuZHNjYXBlfGVufDB8fDB8fHww&auto=format&fit=crop&w=800&q=60"
        videoUrl="https://www.w3schools.com/html/mov_bbb.mp4" // A sample video
      />
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


## particle effect for hero

**Author:** @avanishverma4 | **Used:** 240x
**URL:** https://21st.dev/@avanishverma4/components/particle-effect-for-hero
**Install:** `npx shadcn@latest add "https://21st.dev/r/avanishverma4/particle-effect-for-hero?api_key=$API_KEY_21ST"`
**Description:** A reusable and responsive hero section with a background particle effect on hovering

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
particle-effect-for-hero.tsx
// Full source available at: https://21st.dev/@avanishverma4/components/particle-effect-for-hero
// Or install via: npx shadcn@latest add "https://21st.dev/r/avanishverma4/particle-effect-for-hero?api_key=$API_KEY_21ST"

import Component from "@/components/ui/particle-effect-for-hero";

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


## Hero ASCII 

**Author:** @larsen66 | **Used:** 235x
**URL:** https://21st.dev/@larsen66/components/hero-ascii
**Install:** `npx shadcn@latest add "https://21st.dev/r/larsen66/hero-ascii?api_key=$API_KEY_21ST"`
**Description:** Here is Hero ASCII  component

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
hero-ascii.tsx
// Full source available at: https://21st.dev/@larsen66/components/hero-ascii
// Or install via: npx shadcn@latest add "https://21st.dev/r/larsen66/hero-ascii?api_key=$API_KEY_21ST"

import Home from "@/components/ui/hero-ascii";

export default function DemoOne() {
  return (
    <div className="w-screen h-screen">
      <Home />
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


## Globe Hero

**Author:** @chowlol202 | **Used:** 234x
**URL:** https://21st.dev/@chowlol202/components/globe-hero
**Install:** `npx shadcn@latest add "https://21st.dev/r/chowlol202/globe-hero?api_key=$API_KEY_21ST"`
**Description:** Dot Globe Hero – A modern, interactive 3D globe hero section built with React Three Fiber and Tailwind CSS. Perfect for SaaS landing pages, dashboards, or portfolios, this component adds a visually striking, tech-forward centerpiece that’s fully responsive, themeable, and reusable.

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
globe-hero.tsx
// Full source available at: https://21st.dev/@chowlol202/components/globe-hero
// Or install via: npx shadcn@latest add "https://21st.dev/r/chowlol202/globe-hero?api_key=$API_KEY_21ST"

"use client";

import React from "react";
import { motion } from "framer-motion";
import { DotGlobeHero } from "@/components/ui/globe-hero";
import { ArrowRight, Zap } from "lucide-react";

export default function DotGlobeHeroDemo() {
  return (
    <DotGlobeHero
      rotationSpeed={0.004}
      className="bg-gradient-to-br from-background via-background/95 to-muted/10 relative overflow-hidden"
    >
      <div className="absolute inset-0 bg-gradient-to-t from-background/50 via-transparent to-background/30" />
      <div className="absolute top-1/4 left-1/4 w-96 h-96 bg-primary/5 rounded-full blur-3xl animate-pulse" />
      <div className="absolute bottom-1/4 right-1/4 w-64 h-64 bg-primary/3 rounded-full blur-3xl animate-pulse" />
      
      <div className="relative z-10 text-center space-y-12 max-w-5xl mx-auto px-6 py-12">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8 }}
          className="space-y-8"
        >
          <motion.div 
            initial={{ opacity: 0, scale: 0.9 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ duration: 0.6, delay: 0.2 }}
            className="relative inline-flex items-center gap-3 px-6 py-3 rounded-full bg-gradient-to-r from-primary/20 via-primary/10 to-primary/20 border border-primary/30 backdrop-blur-xl shadow-2xl"
          >
            <div className="absolute inset-0 rounded-full bg-gradient-to-r from-primary/10 via-transparent to-primary/10 animate-pulse" />
            <div className="w-2 h-2 bg-primary rounded-full animate-ping" />
            <span className="relative z-10 text-sm font-bold text-primary tracking-wider uppercase">GLOBAL NETWORK</span>
            <div className="w-2 h-2 bg-primary rounded-full animate-ping animation-delay-500" />
          </motion.div>
          
          <div className="space-y-6">
            <motion.h1 
              initial={{ opacity: 0, y: 30 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 1, delay: 0.3 }}
              className="text-5xl md:text-7xl lg:text-8xl xl:text-9xl font-black tracking-tighter leading-[0.85] select-none"
              style={{ fontFamily: 'Inter, system-ui, sans-serif' }}
            >
              <span className="block font-light text-foreground/70 mb-3 text-4xl md:text-6xl lg:text-7xl">
                Connect
              </span>
              <span className="block relative">
                <span className="bg-gradient-to-br from-primary via-primary to-primary/60 bg-clip-text text-transparent font-black relative z-10">
                  the World
                </span>
                <div className="absolute inset-0 bg-gradient-to-br from-primary via-primary to-primary/60 bg-clip-text text-transparent font-black blur-2xl opacity-50 scale-105" 
                     style={{ fontFamily: 'Inter, system-ui, sans-serif' }}>
                  the World
                </div>
                <motion.div
                  initial={{ width: 0 }}
                  animate={{ width: "100%" }}
                  transition={{ duration: 1.5, delay: 1.2, ease: "easeOut" }}
                  className="absolute -bottom-6 left-0 h-3 bg-gradient-to-r from-primary via-primary/80 to-transparent rounded-full shadow-lg shadow-primary/50"
                />
              </span>
            </motion.h1>
          </div>
          
          <motion.div 
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ duration: 0.8, delay: 0.8 }}
            className="max-w-3xl mx-auto space-y-4"
          >
            <p className="text-xl md:text-2xl text-muted-foreground leading-relaxed font-medium" 
               style={{ fontFamily: 'Inter, system-ui, sans-serif' }}>
              Experience real-time global connectivity with our{" "}
              <span className="text-foreground font-semibold bg-gradient-to-r from-primary/20 to-primary/10 px-2 py-1 rounded-md">
                distributed network infrastructure
              </span>
            </p>
            <p className="text-lg text-muted-foreground/80 leading-relaxed">
              Monitor data flows, track performance, and scale across continents with unprecedented reliability.
            </p>
          </motion.div>
        </motion.div>

        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8, delay: 1 }}
          className="flex flex-col sm:flex-row gap-6 justify-center items-center pt-4"
        >
          <motion.button
            whileHover={{ 
              scale: 1.05, 
              boxShadow: "0 20px 40px rgba(0,0,0,0.2), 0 0 25px hsl(var(--primary) / 0.3)",
              y: -2
            }}
            whileTap={{ scale: 0.98 }}
            className="group relative inline-flex items-center gap-3 px-8 py-4 bg-gradient-to-r from-primary via-primary to-primary/90 text-primary-foreground rounded-xl font-semibold text-lg shadow-xl hover:shadow-primary/30 transition-all duration-500 overflow-hidden border border-primary/20"
          >
            <div className="absolute inset-0 bg-gradient-to-r from-white/20 via-white/5 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500" />
            <motion.div
              className="absolute inset-0 bg-gradient-to-r from-transparent via-white/30 to-transparent"
              initial={{ x: "-100%" }}
              whileHover={{ x: "100%" }}
              transition={{ duration: 0.8 }}
            />
            <span className="relative z-10 tracking-wide">Start Exploring</span>
            <ArrowRight className="relative z-10 w-5 h-5 group-hover:translate-x-2 transition-transform duration-300" />
          </motion.button>
          
          <motion.button
            whileHover={{ 
              scale: 1.05,
              backgroundColor: "hsl(var(--accent))",
              borderColor: "hsl(var(--primary))",
              boxShadow: "0 15px 30px rgba(0,0,0,0.1), 0 0 15px hsl(var(--primary) / 0.1)",
              y: -2
            }}
            whileTap={{ scale: 0.98 }}
            className="group relative inline-flex items-center gap-3 px-8 py-4 border-2 border-border/40 rounded-xl font-semibold text-lg hover:border-primary/40 transition-all duration-500 backdrop-blur-xl bg-background/60 hover:bg-background/90 shadow-lg overflow-hidden"
          >
            <div className="absolute inset-0 bg-gradient-to-r from-primary/5 via-transparent to-primary/5 opacity-0 group-hover:opacity-100 transition-opacity duration-500" />
            <Zap className="relative z-10 w-5 h-5 group-hover:scale-110 group-hover:rotate-6 transition-all duration-300" />
            <span className="relative z-10 tracking-wide">View Live Demo</span>
          </motion.button>
        </motion.div>
      </div>
    </DotGlobeHero>
  );
}
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


## Hero Shader

**Author:** @designali-in | **Used:** 231x
**URL:** https://21st.dev/@designali-in/components/hero-shader
**Install:** `npx shadcn@latest add "https://21st.dev/r/designali-in/hero-shader?api_key=$API_KEY_21ST"`
**Description:** Discover the essence of creativity in our exquisite collection of top-tier abstract design assets. Each piece is a blend of beauty and utility, perfect for elevating any project.

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
hero-shader.tsx
// Full source available at: https://21st.dev/@designali-in/components/hero-shader
// Or install via: npx shadcn@latest add "https://21st.dev/r/designali-in/hero-shader?api_key=$API_KEY_21ST"

import { ShaderBackground } from "@/components/ui/hero-shader";

export default function DemoOne() {
  return (
    <div className="m-6 w-full">
    <ShaderBackground>
    <header className="relative z-20 flex items-center justify-between p-6">
      {/* Logo */}
      <div className="flex items-center">
        <svg width="24" height="24" viewBox="0 0 392.02 324.6" fill="currentColor" xmlns="http://www.w3.org/2000/svg"><path fill="#fff200" d="M268.08,0c-27.4,0-51.41,4.43-72.07,13.26C175.36,4.43,151.35,0,123.95,0H0v324.6h123.95c27.37,0,51.38-4.58,72.07-13.7,20.69,9.12,44.7,13.7,72.07,13.7h123.95V0h-123.95ZM324.09,268.36h-47.91c-20.25,0-37.3-4.05-51.18-12.15-12.28-7.17-21.94-17.41-28.99-30.7h0s0,0,0,0c0,0,0,0,0,0h0c-7.05,13.29-16.71,23.53-28.99,30.7-13.87,8.1-30.93,12.15-51.18,12.15h-47.91V56.24h47.91c19.8,0,36.67,4.01,50.61,12.04,12.51,7.2,22.35,17.47,29.55,30.77h0s0,0,0,0c0,0,0,0,0,0h0c7.2-13.3,17.04-23.57,29.55-30.77,13.95-8.02,30.82-12.04,50.61-12.04h47.91v212.13Z"></path></svg>
      </div>

      {/* Navigation */}
      <nav className="flex items-center space-x-2">
        <a
          href="#"
          className="text-white/80 hover:text-white text-xs font-light px-3 py-2 rounded-full hover:bg-white/10 transition-all duration-200"
        >
          Products
        </a>
        <a
          href="#"
          className="text-white/80 hover:text-white text-xs font-light px-3 py-2 rounded-full hover:bg-white/10 transition-all duration-200"
        >
          Pricing
        </a>
        <a
          href="#"
          className="text-white/80 hover:text-white text-xs font-light px-3 py-2 rounded-full hover:bg-white/10 transition-all duration-200"
        >
          Docs
        </a>
      </nav>

      {/* Login Button Group with Arrow */}
      <div id="gooey-btn" className="relative flex items-center group" style={{ filter: "url(#gooey-filter)" }}>
        <button className="absolute right-0 px-2.5 py-2 rounded-full bg-white text-black font-normal text-xs transition-all duration-300 hover:bg-white/90 cursor-pointer h-8 flex items-center justify-center -translate-x-10 group-hover:-translate-x-19 z-0">
          <svg className="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M7 17L17 7M17 7H7M17 7V17" />
          </svg>
        </button>
        <button className="px-6 py-2 rounded-full bg-white text-black font-normal text-xs transition-all duration-300 hover:bg-white/90 cursor-pointer h-8 flex items-center z-10">
          Login
        </button>
      </div>
    </header>
      <main className="absolute bottom-8 left-8 z-20 max-w-lg">
      <div className="text-left">
        <div
          className="inline-flex items-center px-3 py-1 rounded-full bg-white/5 backdrop-blur-sm mb-4 relative"
          style={{
            filter: "url(#glass-effect)",
          }}
        >
          <div className="absolute top-0 left-1 right-1 h-px bg-gradient-to-r from-transparent via-white/20 to-transparent rounded-full" />
          <span className="text-white/90 text-xs font-light relative z-10">✨ New Design Ideas</span>
        </div>

        {/* Main Heading */}
        <h1 className="text-5xl md:text-6xl leading-14 tracking-tight  text-white mb-4">
          <span className="italic instrument">Beautiful</span> Design
          <br />
          <span className="tracking-tight text-white font-bold">Experiences</span>
        </h1>

        {/* Description */}
        <p className="text-xs font-light text-white/70 mb-4 leading-relaxed">
          Discover the essence of creativity in our exquisite collection of top-tier abstract design assets. Each piece is a blend of beauty and utility, perfect for elevating any project.
        </p>

        {/* Buttons */}
        <div className="flex items-center gap-4 flex-wrap">
          <button className="px-8 py-3 rounded-full bg-transparent border border-white/30 text-white font-normal text-xs transition-all duration-200 hover:bg-white/10 hover:border-white/50 cursor-pointer">
            Pricing
          </button>
          <button className="px-8 py-3 rounded-full bg-white text-black font-normal text-xs transition-all duration-200 hover:bg-white/90 cursor-pointer">
            Get Started
          </button>
        </div>
      </div>
    </main>
    </ShaderBackground>
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


## Aether Flow Hero

**Author:** @dhileepkumargm | **Used:** 231x
**URL:** https://21st.dev/@dhileepkumargm/components/aether-flow-hero
**Install:** `npx shadcn@latest add "https://21st.dev/r/dhileepkumargm/aether-flow-hero?api_key=$API_KEY_21ST"`
**Description:** "Aether Flow" hero. It features a mesmerizing, interactive background of flowing light particles that weave and connect with each other. The entire particle system subtly reacts to your cursor, creating gentle swirls in the "aether" as you move your mouse.

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
aether-flow-hero.tsx
// Full source available at: https://21st.dev/@dhileepkumargm/components/aether-flow-hero
// Or install via: npx shadcn@latest add "https://21st.dev/r/dhileepkumargm/aether-flow-hero?api_key=$API_KEY_21ST"

import AetherFlowHero from "@/components/ui/aether-flow-hero";

export default function DemoOne() {
  return  <main className="App bg-black">
      <AetherFlowHero />
    </main>
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


## Smooth Scroll Hero

**Author:** @ishamsu | **Used:** 223x
**URL:** https://21st.dev/@ishamsu/components/smooth-scroll-hero
**Install:** `npx shadcn@latest add "https://21st.dev/r/ishamsu/smooth-scroll-hero?api_key=$API_KEY_21ST"`
**Description:** A React component that creates a smooth-scrolling hero section with parallax background effects. Features responsive images for mobile and desktop, with customizable scroll animations built using Framer Motion.

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
smooth-scroll-hero.tsx
// Full source available at: https://21st.dev/@ishamsu/components/smooth-scroll-hero
// Or install via: npx shadcn@latest add "https://21st.dev/r/ishamsu/smooth-scroll-hero?api_key=$API_KEY_21ST"

import SmoothScrollHero  from "@/components/ui/smooth-scroll-hero";

const DemoOne = () => {
  return (
    <div className="relative min-h-screen">
				<SmoothScrollHero
					scrollHeight={1500}
					desktopImage="https://images.unsplash.com/photo-1511884642898-4c92249e20b6"
					mobileImage="https://images.unsplash.com/photo-1511207538754-e8555f2bc187?q=80&w=2412&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
					initialClipPercentage={25}
					finalClipPercentage={75}
				/>
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


## IntegrationHero

**Author:** @ruixen.ui | **Used:** 222x
**URL:** https://21st.dev/@ruixen.ui/components/integration-hero
**Install:** `npx shadcn@latest add "https://21st.dev/r/ruixen.ui/integration-hero?api_key=$API_KEY_21ST"`
**Description:** The IntegrationHero component is a visually engaging section designed to showcase integrations with popular tools. It features two horizontal rows of app icons that continuously scroll in opposite directions, creating a dynamic carousel effect. The component includes a central call-to-action with a headline, description, and a “Get Started” button, encouraging users to explore integrations.

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
integration-hero.tsx
// Full source available at: https://21st.dev/@ruixen.ui/components/integration-hero
// Or install via: npx shadcn@latest add "https://21st.dev/r/ruixen.ui/integration-hero?api_key=$API_KEY_21ST"

import IntegrationHero from "@/components/ui/integration-hero";

export default function DemoOne() {
  return <IntegrationHero />;
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


## Hero ASCII one

**Author:** @larsen66 | **Used:** 221x
**URL:** https://21st.dev/@larsen66/components/hero-ascii-one
**Install:** `npx shadcn@latest add "https://21st.dev/r/larsen66/hero-ascii-one?api_key=$API_KEY_21ST"`
**Description:** Hero ASCII one

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
hero-ascii-one.tsx
// Full source available at: https://21st.dev/@larsen66/components/hero-ascii-one
// Or install via: npx shadcn@latest add "https://21st.dev/r/larsen66/hero-ascii-one?api_key=$API_KEY_21ST"

import Home from "@/components/ui/hero-ascii-one";

export default function DemoOne() {
  return (
    <div className="w-screen h-screen">
      <Home />
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


## Portfolio Hero

**Author:** @waleedkibhen | **Used:** 219x
**URL:** https://21st.dev/@waleedkibhen/components/portfolio-hero
**Install:** `npx shadcn@latest add "https://21st.dev/r/waleedkibhen/portfolio-hero?api_key=$API_KEY_21ST"`
**Description:** Animated Portfolio Hero Section - Bold Name with Profile Image Overlay
A striking, modern portfolio hero component featuring animated blur-in text effects and a profile image overlay. Perfect for developers, designers, and creatives who want to make a bold first impression.

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
portfolio-hero.tsx
// Full source available at: https://21st.dev/@waleedkibhen/components/portfolio-hero
// Or install via: npx shadcn@latest add "https://21st.dev/r/waleedkibhen/portfolio-hero?api_key=$API_KEY_21ST"

import React from "react";
import Component from "@/components/ui/portfolio-hero";

export default function Demo() {
  return (
    <>
      <link
        rel="stylesheet"
        href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@700&family=Antic&display=swap"
      />
      <div className="w-full">
        <Component />
      </div>
    </>
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


## Hero scroll animation

**Author:** @uilayout.contact | **Used:** 199x
**URL:** https://21st.dev/@uilayout.contact/components/hero-scroll-animation
**Install:** `npx shadcn@latest add "https://21st.dev/r/uilayout.contact/hero-scroll-animation?api_key=$API_KEY_21ST"`
**Description:** Here is scroll animation in hero section

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
hero-scroll-animation.tsx
// Full source available at: https://21st.dev/@uilayout.contact/components/hero-scroll-animation
// Or install via: npx shadcn@latest add "https://21st.dev/r/uilayout.contact/hero-scroll-animation?api_key=$API_KEY_21ST"

// demo.tsx
import React from 'react';
import Component from '@/components/ui/hero-scroll-animation';

function ComponentDemo() {
  return (
    <Component />
  );
}

export { ComponentDemo as DemoOne };
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


## Hero Section

**Author:** @prebuiltui | **Used:** 197x
**URL:** https://21st.dev/@prebuiltui/components/hero-section
**Install:** `npx shadcn@latest add "https://21st.dev/r/prebuiltui/hero-section?api_key=$API_KEY_21ST"`
**Description:** Here is Hero section components

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
hero-section.tsx
// Full source available at: https://21st.dev/@prebuiltui/components/hero-section
// Or install via: npx shadcn@latest add "https://21st.dev/r/prebuiltui/hero-section?api_key=$API_KEY_21ST"

import HeroSection from "@/components/ui/hero-section";

export default function DemoOne() {
  return <HeroSection />;
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


## Acme Hero

**Author:** @bankkroll | **Used:** 194x
**URL:** https://21st.dev/@bankkroll/components/acme-hero
**Install:** `npx shadcn@latest add "https://21st.dev/r/bankkroll/acme-hero?api_key=$API_KEY_21ST"`
**Description:** Animated hero section and nav

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
acme-hero.tsx
// Full source available at: https://21st.dev/@bankkroll/components/acme-hero
// Or install via: npx shadcn@latest add "https://21st.dev/r/bankkroll/acme-hero?api_key=$API_KEY_21ST"

import { AcmeHero } from "@/components/ui/acme-hero";

export default function DemoOne() {
  return <AcmeHero />;
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


## Glowy Waves Hero

**Author:** @moumensoliman | **Used:** 191x
**URL:** https://21st.dev/@moumensoliman/components/glowy-waves-hero-shadcnui
**Install:** `npx shadcn@latest add "https://21st.dev/r/moumensoliman/glowy-waves-hero-shadcnui?api_key=$API_KEY_21ST"`
**Description:** Hero section with glowy waves effect

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
glowy-waves-hero-shadcnui.tsx
// Full source available at: https://21st.dev/@moumensoliman/components/glowy-waves-hero-shadcnui
// Or install via: npx shadcn@latest add "https://21st.dev/r/moumensoliman/glowy-waves-hero-shadcnui?api_key=$API_KEY_21ST"

import { GlowyWavesHero } from "@/components/ui/glowy-waves-hero-shadcnui"

export default function Demo() {
  return (
    <div className="flex min-h-screen items-center justify-center bg-background p-8">
      <GlowyWavesHero />
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


## AI Image Generator Hero 

**Author:** @ravikatiyar162 | **Used:** 191x
**URL:** https://21st.dev/@ravikatiyar162/components/ai-image-generator-hero
**Install:** `npx shadcn@latest add "https://21st.dev/r/ravikatiyar162/ai-image-generator-hero?api_key=$API_KEY_21ST"`

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
ai-image-generator-hero.tsx
// Full source available at: https://21st.dev/@ravikatiyar162/components/ai-image-generator-hero
// Or install via: npx shadcn@latest add "https://21st.dev/r/ravikatiyar162/ai-image-generator-hero?api_key=$API_KEY_21ST"

"use client"

import { ImageCarouselHero } from "@/components/ui/ai-image-generator-hero"

export default function ImageCarouselHeroDemo() {
  const demoImages = [
    {
      id: "1",
      src: "https://images.unsplash.com/photo-1684369176170-463e84248b70?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTl8fGFpfGVufDB8MXwwfHx8MA%3D%3D&auto=format&fit=crop&q=60&w=900",
      alt: "Mountain landscape",
      rotation: -15,
    },
    {
      id: "2",
      src: "https://plus.unsplash.com/premium_photo-1677269465314-d5d2247a0b0c?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTN8fGFpfGVufDB8MXwwfHx8MA%3D%3D&auto=format&fit=crop&q=60&w=900",
      alt: "Abstract art",
      rotation: -8,
    },
    {
      id: "3",
      src: "https://images.unsplash.com/photo-1524673360092-e07b7ae58845?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MjR8fGFpfGVufDB8MXwwfHx8MA%3D%3D&auto=format&fit=crop&q=60&w=900",
      alt: "City skyline",
      rotation: 5,
    },
    {
      id: "4",
      src: "https://plus.unsplash.com/premium_photo-1680610653084-6e4886519caf?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MzN8fGFpfGVufDB8MXwwfHx8MA%3D%3D&auto=format&fit=crop&q=60&w=900",
      alt: "Nature photography",
      rotation: 12,
    },
    {
      id: "5",
      src: "https://plus.unsplash.com/premium_photo-1680608979589-e9349ed066d5?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OXx8QWl8ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&q=60&w=900",
      alt: "Digital art",
      rotation: -12,
    },
    {
      id: "6",
      src: "https://images.unsplash.com/photo-1562575214-da9fcf59b907?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MzV8fGFpfGVufDB8MXwwfHx8MA%3D%3D&auto=format&fit=crop&q=60&w=900",
      alt: "Tropical leaves",
      rotation: 8,
    },
    {
      id: "7",
      src: "https://plus.unsplash.com/premium_photo-1676637656210-390da73f4951?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mzd8fGFpfGVufDB8MXwwfHx8MA%3D%3D&auto=format&fit=crop&q=60&w=900",
      alt: "Tropical leaves",
      rotation: 8,
    },
    {
      id: "8",
      src: "https://images.unsplash.com/photo-1664448003794-2d446c53dcae?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NTV8fGFpfGVufDB8MXwwfHx8MA%3D%3D&auto=format&fit=crop&q=60&w=900",
      alt: "Tropical leaves",
      rotation: 8,
    },
  ]

  const demoFeatures = [
    {
      title: "Realistic Results",
      description: "Realistic Results Photos that look professionally crafted",
    },
    {
      title: "Fast Generation",
      description: "Turn ideas into images in seconds.",
    },
    {
      title: "Diverse Styles",
      description: "Choose from a wide range of artistic options.",
    },
  ]

  return (
    <ImageCarouselHero
      title="Create Stunning AI Generated Photos Instantly"
      subtitle="AI Photo Generation"
      description="Transform your ideas into breathtaking visuals with cutting-edge AI technology"
      ctaText="Start Generating Now"
      onCtaClick={() => console.log("CTA clicked!")}
      images={demoImages}
      features={demoFeatures}
    />
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


## Starfall portfolio landing

**Author:** @easemize | **Used:** 188x
**URL:** https://21st.dev/@easemize/components/starfall-portfolio-landing
**Install:** `npx shadcn@latest add "https://21st.dev/r/easemize/starfall-portfolio-landing?api_key=$API_KEY_21ST"`
**Description:** Starfall portfolio landing page hero

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
starfall-portfolio-landing.tsx
// Full source available at: https://21st.dev/@easemize/components/starfall-portfolio-landing
// Or install via: npx shadcn@latest add "https://21st.dev/r/easemize/starfall-portfolio-landing?api_key=$API_KEY_21ST"

import { PortfolioPage, PortfolioPageProps } from "@/components/ui/starfall-portfolio-landing";

const customPortfolioData: PortfolioPageProps = {
  logo: {
    initials: 'AT',
    name: 'Alex Thompson',
  },
  navLinks: [
    { label: 'Bio', href: '#about' },
    { label: 'Work', href: '#projects' },
    { label: 'Expertise', href: '#skills' },
  ],
  resume: {
    label: 'Download CV',
    onClick: () => alert('Downloading CV...'),
  },
  hero: {
    titleLine1: 'Full-Stack Engineer &',
    titleLine2Gradient: 'UX Architect',
    subtitle: 'I build robust and scalable web applications with a strong focus on user-centric design and performance.',
  },
  ctaButtons: {
    primary: {
      label: 'Explore My Work',
      onClick: () => { document.getElementById('projects')?.scrollIntoView({ behavior: 'smooth' }); },
    },
    secondary: {
      label: 'Contact Me',
      onClick: () => { window.location.href = 'mailto:alex.thompson@example.com'; },
    },
  },
  projects: [
    { 
      title: 'E-commerce Platform', 
      description: 'A scalable online store built with Next.js, TypeScript, and Stripe.',
      tags: ['Next.js', 'Stripe', 'Vercel'] 
    },
    { 
      title: 'SaaS Dashboard', 
      description: 'A real-time analytics dashboard for a B2B software-as-a-service product.',
      tags: ['React', 'Chart.js', 'Firebase'] 
    },
    { 
      title: 'AI Content Generator', 
      description: 'Leveraging OpenAI to generate marketing copy for businesses.',
      tags: ['SvelteKit', 'OpenAI', 'Tailwind CSS'],
      imageContent: <div className="text-2xl text-white/50">🤖</div>
    },
  ],
  stats: [
    { value: '7+', label: 'Years of Experience' },
    { value: '30+', label: 'Client Projects' },
    { value: '99%', label: 'Client Satisfaction' },
  ],
  showAnimatedBackground: true, // You can toggle the background
};

const DemoOne = () => {
  return <PortfolioPage {...customPortfolioData} />;
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


## Hero Minimalism

**Author:** @lyanchouss | **Used:** 180x
**URL:** https://21st.dev/@lyanchouss/components/hero-minimalism
**Install:** `npx shadcn@latest add "https://21st.dev/r/lyanchouss/hero-minimalism?api_key=$API_KEY_21ST"`
**Description:** Here is Hero section minimalism 

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
hero-minimalism.tsx
// Full source available at: https://21st.dev/@lyanchouss/components/hero-minimalism
// Or install via: npx shadcn@latest add "https://21st.dev/r/lyanchouss/hero-minimalism?api_key=$API_KEY_21ST"

import MinimalHero from "@/components/ui/hero-minimalism";

export default function DemoOne() {
  return <MinimalHero />;
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


## Modern Hero 

**Author:** @uniquesonu | **Used:** 177x
**URL:** https://21st.dev/@uniquesonu/components/modern-hero
**Install:** `npx shadcn@latest add "https://21st.dev/r/uniquesonu/modern-hero?api_key=$API_KEY_21ST"`
**Description:** Here's a description for your SmoothScrollHero component, tailored for 21st.dev:

SmoothScrollHero: Immersive Parallax & Scroll Effects in React
Elevate your web projects with SmoothScrollHero, a React component that delivers a captivating and highly performant smooth scrolling experience. Built with Lenis for silky-smooth scroll animations and Framer Motion for dynamic, interactive visuals, this component is designed to bring your content to life with stunning parallax effects and a responsive layout.

Features
Effortless Smooth Scrolling: Integrates ReactLenis for a truly fluid and customizable scroll feel, enhancing user engagement and content readability.
Dynamic Parallax Imagery: Showcases a large, central image that transforms its clip-path, background-size, and opacity based on scroll position, creating an eye-catching focal point.
Layered Parallax Images: Multiple smaller images animate independently with varying scroll speeds and fades, adding depth and a sense of movement to your hero section.
Interactive Navigation: A fixed navigation bar with a "Launch Schedule" button provides a smooth scroll-to-section functionality.
Animated Content Reveal: Individual schedule items gracefully animate into view as they enter the viewport, drawing attention to key information.
Responsive Design: Optimized to look great and perform well across various screen sizes.
How it Works
SmoothScrollHero combines several powerful libraries to achieve its effects:

react-lenis: Provides the core smooth scrolling functionality, ensuring a consistent and pleasant user experience.
framer-motion: Powers all the motion and animation, including useScroll, useTransform, and useMotionTemplate hooks to link scroll position to CSS properties like clipPath, backgroundSize, opacity, and translateY.
This component is perfect for creating impactful landing pages, portfolios, or any section where you want to create a visually rich and engaging introduction to your content.

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
modern-hero.tsx
// Full source available at: https://21st.dev/@uniquesonu/components/modern-hero
// Or install via: npx shadcn@latest add "https://21st.dev/r/uniquesonu/modern-hero?api_key=$API_KEY_21ST"

import { SmoothScrollHero } from "@/components/ui/modern-hero";

const DemoOne = () => {
  return <SmoothScrollHero />;
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


## Commerce Hero

**Author:** @bankkroll | **Used:** 174x
**URL:** https://21st.dev/@bankkroll/components/commerce-hero
**Install:** `npx shadcn@latest add "https://21st.dev/r/bankkroll/commerce-hero?api_key=$API_KEY_21ST"`
**Description:** Animated ecommerce hero and navbar.

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
commerce-hero.tsx
// Full source available at: https://21st.dev/@bankkroll/components/commerce-hero
// Or install via: npx shadcn@latest add "https://21st.dev/r/bankkroll/commerce-hero?api_key=$API_KEY_21ST"

import { CommerceHero } from "@/components/ui/commerce-hero";

export default function DemoOne() {
  return <CommerceHero />;
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


## Halide Topo Hero

**Author:** @shivendra9795kumar | **Used:** 173x
**URL:** https://21st.dev/@shivendra9795kumar/components/halide-topo-hero
**Install:** `npx shadcn@latest add "https://21st.dev/r/shivendra9795kumar/halide-topo-hero?api_key=$API_KEY_21ST"`
**Description:** A monochrome 3D hero component with topographical parallax layers and film grain effects.

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
halide-topo-hero.tsx
// Full source available at: https://21st.dev/@shivendra9795kumar/components/halide-topo-hero
// Or install via: npx shadcn@latest add "https://21st.dev/r/shivendra9795kumar/halide-topo-hero?api_key=$API_KEY_21ST"

import React, { useEffect, useRef } from 'react';

const HalideLanding: React.FC = () => {
  const canvasRef = useRef<HTMLDivElement>(null);
  const layersRef = useRef<HTMLDivElement[]>([]);

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;

    // Mouse Parallax Logic
    const handleMouseMove = (e: MouseEvent) => {
      const x = (window.innerWidth / 2 - e.pageX) / 25;
      const y = (window.innerHeight / 2 - e.pageY) / 25;

      // Rotate the 3D Canvas
      canvas.style.transform = `rotateX(${55 + y / 2}deg) rotateZ(${-25 + x / 2}deg)`;

      // Apply depth shift to layers
      layersRef.current.forEach((layer, index) => {
        if (!layer) return;
        const depth = (index + 1) * 15;
        const moveX = x * (index + 1) * 0.2;
        const moveY = y * (index + 1) * 0.2;
        layer.style.transform = `translateZ(${depth}px) translate(${moveX}px, ${moveY}px)`;
      });
    };

    // Entrance Animation
    canvas.style.opacity = '0';
    canvas.style.transform = 'rotateX(90deg) rotateZ(0deg) scale(0.8)';
    
    const timeout = setTimeout(() => {
      canvas.style.transition = 'all 2.5s cubic-bezier(0.16, 1, 0.3, 1)';
      canvas.style.opacity = '1';
      canvas.style.transform = 'rotateX(55deg) rotateZ(-25deg) scale(1)';
    }, 300);

    window.addEventListener('mousemove', handleMouseMove);

    return () => {
      window.removeEventListener('mousemove', handleMouseMove);
      clearTimeout(timeout);
    };
  }, []);

  return (
    <>
      <style>{`
        :root {
          --bg: #0a0a0a;
          --silver: #e0e0e0;
          --accent: #ff3c00;
          --grain-opacity: 0.15;
        }

        .halide-body {
          background-color: var(--bg);
          color: var(--silver);
          font-family: 'Syncopate', sans-serif;
          overflow: hidden;
          height: 100vh;
          width: 100vw;
          margin: 0;
          display: flex;
          align-items: center;
          justify-content: center;
        }

        .halide-grain {
          position: fixed;
          top: 0; left: 0; width: 100%; height: 100%;
          pointer-events: none;
          z-index: 100;
          opacity: var(--grain-opacity);
        }

        .viewport {
          perspective: 2000px;
          width: 100vw; height: 100vh;
          display: flex; align-items: center; justify-content: center;
          overflow: hidden;
        }

        .canvas-3d {
          position: relative;
          width: 800px; height: 500px;
          transform-style: preserve-3d;
          transition: transform 0.8s cubic-bezier(0.16, 1, 0.3, 1);
        }

        .layer {
          position: absolute;
          inset: 0;
          border: 1px solid rgba(224, 224, 224, 0.1);
          background-size: cover;
          background-position: center;
          transition: transform 0.5s ease;
        }

        .layer-1 { background-image: url('https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&q=80&w=1200'); filter: grayscale(1) contrast(1.2) brightness(0.5); }
        .layer-2 { background-image: url('https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&q=80&w=1200'); filter: grayscale(1) contrast(1.1) brightness(0.7); opacity: 0.6; mix-blend-mode: screen; }
        .layer-3 { background-image: url('https://images.unsplash.com/photo-1470770841072-f978cf4d019e?auto=format&fit=crop&q=80&w=1200'); filter: grayscale(1) contrast(1.3) brightness(0.8); opacity: 0.4; mix-blend-mode: overlay; }

        .contours {
          position: absolute;
          width: 200%; height: 200%;
          top: -50%; left: -50%;
          background-image: repeating-radial-gradient(circle at 50% 50%, transparent 0, transparent 40px, rgba(255,255,255,0.05) 41px, transparent 42px);
          transform: translateZ(120px);
          pointer-events: none;
        }

        .interface-grid {
          position: fixed;
          inset: 0;
          padding: 4rem;
          display: grid;
          grid-template-columns: 1fr 1fr;
          grid-template-rows: auto 1fr auto;
          z-index: 10;
          pointer-events: none;
        }

        .hero-title {
          grid-column: 1 / -1;
          align-self: center;
          font-size: clamp(3rem, 10vw, 10rem);
          line-height: 0.85;
          letter-spacing: -0.04em;
          mix-blend-mode: difference;
        }

        .cta-button {
          pointer-events: auto;
          background: var(--silver);
          color: var(--bg);
          padding: 1rem 2rem;
          text-decoration: none;
          font-weight: 700;
          clip-path: polygon(0 0, 100% 0, 100% 70%, 85% 100%, 0 100%);
          transition: 0.3s;
        }

        .cta-button:hover { background: var(--accent); transform: translateY(-5px); }

        .scroll-hint {
          position: absolute;
          bottom: 2rem; left: 50%;
          width: 1px; height: 60px;
          background: linear-gradient(to bottom, var(--silver), transparent);
          animation: flow 2s infinite ease-in-out;
        }

        @keyframes flow {
          0%, 100% { transform: scaleY(0); transform-origin: top; }
          50% { transform: scaleY(1); transform-origin: top; }
          51% { transform: scaleY(1); transform-origin: bottom; }
        }
      `}</style>

      <div className="halide-body">
        {/* SVG Filter for Grain */}
        <svg style={{ position: 'absolute', width: 0, height: 0 }}>
          <filter id="grain">
            <feTurbulence type="fractalNoise" baseFrequency="0.65" numOctaves="3" />
            <feColorMatrix type="saturate" values="0" />
          </filter>
        </svg>

        <div className="halide-grain" style={{ filter: 'url(#grain)' }}></div>

        <div className="interface-grid">
          <div style={{ fontWeight: 700 }}>HALIDE_CORE</div>
          <div style={{ textAlign: 'right', fontFamily: 'monospace', color: 'var(--accent)', fontSize: '0.7rem' }}>
            <div>LATITUDE: 34.0522° N</div>
            <div>FOCAL DEPTH: 80MM</div>
          </div>

          <h1 className="hero-title">SILVER<br />SULPHIDE</h1>

          <div style={{ gridColumn: '1 / -1', display: 'flex', justifyContent: 'space-between', alignItems: 'flex-end' }}>
            <div style={{ fontFamily: 'monospace', fontSize: '0.75rem' }}>
              <p>[ ARCHIVE 2024 ]</p>
              <p>SURFACE TENSION & TOPOGRAPHICAL LIGHT</p>
            </div>
            <a href="#" className="cta-button">EXPLORE DEPTH</a>
          </div>
        </div>

        <div className="viewport">
          <div className="canvas-3d" ref={canvasRef}>
            <div className="layer layer-1" ref={(el) => (layersRef.current[0] = el!)}></div>
            <div className="layer layer-2" ref={(el) => (layersRef.current[1] = el!)}></div>
            <div className="layer layer-3" ref={(el) => (layersRef.current[2] = el!)}></div>
            <div className="contours"></div>
          </div>
        </div>

        <div className="scroll-hint"></div>
      </div>
    </>
  );
};

export default HalideLanding;
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


## AI Input Hero

**Author:** @aghasisahakyan1 | **Used:** 173x
**URL:** https://21st.dev/@aghasisahakyan1/components/ai-input-hero
**Install:** `npx shadcn@latest add "https://21st.dev/r/aghasisahakyan1/ai-input-hero?api_key=$API_KEY_21ST"`
**Description:** AI Input hero section with animated shader background

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
ai-input-hero.tsx
// Full source available at: https://21st.dev/@aghasisahakyan1/components/ai-input-hero
// Or install via: npx shadcn@latest add "https://21st.dev/r/aghasisahakyan1/ai-input-hero?api_key=$API_KEY_21ST"

import { HeroWave } from "@/components/ui/ai-input-hero";

export default function DemoOne() {
  return <HeroWave />;
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


## Spatial Product Showcase

**Author:** @daiwiikharihar17147 | **Used:** 169x
**URL:** https://21st.dev/@daiwiikharihar17147/components/spatial-product-showcase
**Install:** `npx shadcn@latest add "https://21st.dev/r/daiwiikharihar17147/spatial-product-showcase?api_key=$API_KEY_21ST"`
**Description:** A high-fidelity hero section designed for displaying dual-state products or variations. Features fluid layout transitions powered by Framer Motion, reactive background gradients that adapt to the active item, and a sleek floating control dock. Fully responsive, accessible, and data-driven.

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
spatial-product-showcase.tsx
// Full source available at: https://21st.dev/@daiwiikharihar17147/components/spatial-product-showcase
// Or install via: npx shadcn@latest add "https://21st.dev/r/daiwiikharihar17147/spatial-product-showcase?api_key=$API_KEY_21ST"

import EarbudShowcase from "@/components/ui/spatial-product-showcase";

export default function DemoOne() {
  return <EarbudShowcase />;
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


## Woven Light Hero

**Author:** @dhileepkumargm | **Used:** 168x
**URL:** https://21st.dev/@dhileepkumargm/components/woven-light-hero
**Install:** `npx shadcn@latest add "https://21st.dev/r/dhileepkumargm/woven-light-hero?api_key=$API_KEY_21ST"`
**Description:** A fully interactive, theme-aware hero section featuring a 3D object woven from thousands of light particles that react to the user's cursor.

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
woven-light-hero.tsx
// Full source available at: https://21st.dev/@dhileepkumargm/components/woven-light-hero
// Or install via: npx shadcn@latest add "https://21st.dev/r/dhileepkumargm/woven-light-hero?api_key=$API_KEY_21ST"

import { WovenLightHero } from "@/components/ui/woven-light-hero";

export default function DemoOne() {
  return <WovenLightHero />;
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


## 3D Hero Section Boxes

**Author:** @aghasisahakyan1 | **Used:** 160x
**URL:** https://21st.dev/@aghasisahakyan1/components/3d-hero-section-boxes
**Install:** `npx shadcn@latest add "https://21st.dev/r/aghasisahakyan1/3d-hero-section-boxes?api_key=$API_KEY_21ST"`
**Description:** 3D Hero Section With Animated Boxes

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
3d-hero-section-boxes.tsx
// Full source available at: https://21st.dev/@aghasisahakyan1/components/3d-hero-section-boxes
// Or install via: npx shadcn@latest add "https://21st.dev/r/aghasisahakyan1/3d-hero-section-boxes?api_key=$API_KEY_21ST"

import React from 'react';
import { HeroSection } from "@/components/blocks/3d-hero-section-boxes"

// This is the main component for this specific page/route
export function HomePage() {
  return (
    // You might have a <main> tag or other wrappers provided by your layout.tsx
    // but the core usage is just rendering the component.
    <div>
      <HeroSection />

      {/* Optional: Add other sections of your page below the hero */}
      {/*
      <section className="py-16 bg-white text-black">
        <div className="container mx-auto text-center">
          <h2 className="text-3xl font-bold mb-4">Features Section</h2>
          <p>More content goes here...</p>
        </div>
      </section>
      */}
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


## Liquid Metal Hero

**Author:** @chowlol202 | **Used:** 157x
**URL:** https://21st.dev/@chowlol202/components/liquid-metal-hero
**Install:** `npx shadcn@latest add "https://21st.dev/r/chowlol202/liquid-metal-hero?api_key=$API_KEY_21ST"`
**Description:** Liquid metal hero section with nice animations and perfect for any website.

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
liquid-metal-hero.tsx
// Full source available at: https://21st.dev/@chowlol202/components/liquid-metal-hero
// Or install via: npx shadcn@latest add "https://21st.dev/r/chowlol202/liquid-metal-hero?api_key=$API_KEY_21ST"

"use client";

import LiquidMetalHero from '@/components/ui/liquid-metal-hero';

export default function LiquidMetalHeroDemo() {
  return (
    <LiquidMetalHero
      badge="✨ Next Generation UI"
      title="Fluid Design Excellence"
      subtitle="Experience the future of web interfaces with liquid metal aesthetics that adapt, flow, and captivate. Built for modern applications that demand both beauty and performance."
      primaryCtaLabel="Start Building"
      secondaryCtaLabel="View Examples"
      onPrimaryCtaClick={() => alert("Primary CTA clicked!")}
      onSecondaryCtaClick={() => alert("Secondary CTA clicked!")}
      features={[
        "Seamless Animations",
        "Responsive Excellence", 
        "Modern Architecture"
      ]}
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


## Hero Landing Page

**Author:** @minhxthanh | **Used:** 156x
**URL:** https://21st.dev/@minhxthanh/components/hero-landing-page
**Install:** `npx shadcn@latest add "https://21st.dev/r/minhxthanh/hero-landing-page?api_key=$API_KEY_21ST"`
**Description:** Hero Landing Page. Features a striking dark theme with video background

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
hero-landing-page.tsx
// Full source available at: https://21st.dev/@minhxthanh/components/hero-landing-page
// Or install via: npx shadcn@latest add "https://21st.dev/r/minhxthanh/hero-landing-page?api_key=$API_KEY_21ST"

import { TuringLanding } from "@/components/ui/hero-landing-page";

export default function DemoOne() {
  return (
    <div className="w-full">
      <TuringLanding />
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


## flow-gradient-heroSection

**Author:** @hardikkashiyani123456788 | **Used:** 156x
**URL:** https://21st.dev/@hardikkashiyani123456788/components/flow-gradient-hero-section
**Install:** `npx shadcn@latest add "https://21st.dev/r/hardikkashiyani123456788/flow-gradient-hero-section?api_key=$API_KEY_21ST"`
**Description:** An authoritative UI component featuring fluid liquid gradients and kinetic typography. Designed for premium dark-mode experiences, it combines a sophisticated grainy texture with bold messaging that commands attention. This section captures a modern, leadership-focused aesthetic, ideal for high-stakes tech brands or creative agencies looking for a "smart," professional edge.

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
flow-gradient-hero-section.tsx
// Full source available at: https://21st.dev/@hardikkashiyani123456788/components/flow-gradient-hero-section
// Or install via: npx shadcn@latest add "https://21st.dev/r/hardikkashiyani123456788/flow-gradient-hero-section?api_key=$API_KEY_21ST"

import { Component } from "@/components/ui/flow-gradient-hero-section";

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


## Artificial Hero

**Author:** @lovesickfromthe6ix | **Used:** 147x
**URL:** https://21st.dev/@lovesickfromthe6ix/components/artificial-hero
**Install:** `npx shadcn@latest add "https://21st.dev/r/lovesickfromthe6ix/artificial-hero?api_key=$API_KEY_21ST"`
**Description:** Animated 3d hero section with unique procedural glitch and ascii effects. Includes film  grain and bloom post processing and a navbar

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
artificial-hero.tsx
// Full source available at: https://21st.dev/@lovesickfromthe6ix/components/artificial-hero
// Or install via: npx shadcn@latest add "https://21st.dev/r/lovesickfromthe6ix/artificial-hero?api_key=$API_KEY_21ST"

import { Component } from "@/components/ui/artificial-hero";

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


## PulseFit hero

**Author:** @dhileepkumargm | **Used:** 145x
**URL:** https://21st.dev/@dhileepkumargm/components/pulse-fit-hero
**Install:** `npx shadcn@latest add "https://21st.dev/r/dhileepkumargm/pulse-fit-hero?api_key=$API_KEY_21ST"`
**Description:** A responsive, animated hero component with header, floating blurred gradient backgrounds, badge support, configurable navigation and auth buttons, gradient-styled title, description, and primary/secondary CTA buttons.

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
pulse-fit-hero.tsx
// Full source available at: https://21st.dev/@dhileepkumargm/components/pulse-fit-hero
// Or install via: npx shadcn@latest add "https://21st.dev/r/dhileepkumargm/pulse-fit-hero?api_key=$API_KEY_21ST"

import { PulseFitHero } from "@/components/ui/pulse-fit-hero";


export default function PulseFitHeroDemo() {
  return (
    <PulseFitHero
      logo="PulseFit"
      navigation={[
        { label: "Features", onClick: () => console.log("Features") },
        { label: "Programs", hasDropdown: true, onClick: () => console.log("Programs") },
        { label: "Testimonials", onClick: () => console.log("Testimonials") },
        { label: "Pricing", onClick: () => console.log("Pricing") },
        { label: "Contact", onClick: () => console.log("Contact") },
      ]}
      ctaButton={{
        label: "Get Free Trial",
        onClick: () => console.log("Get Free Trial"),
      }}
      title="Train smarter. Anywhere. Anytime."
      subtitle="Guided fitness sessions tailored to your goals - whether it's strength, endurance, or flexibility. Streamlined, motivating, and accessible 24/7."
      primaryAction={{
        label: "Start training",
        onClick: () => console.log("Start training"),
      }}
      secondaryAction={{
        label: "Browse programs",
        onClick: () => console.log("Browse programs"),
      }}
      disclaimer="*No credit card required"
      socialProof={{
        avatars: [
          "https://i.pravatar.cc/150?img=1",
          "https://i.pravatar.cc/150?img=2",
          "https://i.pravatar.cc/150?img=3",
          "https://i.pravatar.cc/150?img=4",
        ],
        text: "Join over 10,000+ people",
      }}
      programs={[
        {
          image: "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=400&h=500&fit=crop",
          category: "BEGINNER",
          title: "Jumping challenge",
          onClick: () => console.log("Jumping challenge"),
        },
        {
          image: "https://images.unsplash.com/photo-1518611012118-696072aa579a?w=400&h=500&fit=crop",
          category: "INTERMEDIATE",
          title: "Core stability flow",
          onClick: () => console.log("Core stability flow"),
        },
        {
          image: "https://images.unsplash.com/photo-1476480862126-209bfaa8edc8?w=400&h=500&fit=crop",
          category: "ADVANCED",
          title: "Trail sprint challenge",
          onClick: () => console.log("Trail sprint challenge"),
        },
        {
          image: "https://images.unsplash.com/photo-1534438327276-14e5300c3a48?w=400&h=500&fit=crop",
          category: "ALL LEVELS",
          title: "Full-body bootcamp",
          onClick: () => console.log("Full-body bootcamp"),
        },
        {
          image: "https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?w=400&h=500&fit=crop",
          category: "RECOVERY",
          title: "Mobility & Recovery",
          onClick: () => console.log("Mobility & Recovery"),
        },
      ]}
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


## Hero Button Expendable 

**Author:** @moazamtrade | **Used:** 144x
**URL:** https://21st.dev/@moazamtrade/components/hero-button-expendable
**Install:** `npx shadcn@latest add "https://21st.dev/r/moazamtrade/hero-button-expendable?api_key=$API_KEY_21ST"`
**Description:** Hero Button Expendable 

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
hero-button-expendable.tsx
// Full source available at: https://21st.dev/@moazamtrade/components/hero-button-expendable
// Or install via: npx shadcn@latest add "https://21st.dev/r/moazamtrade/hero-button-expendable?api_key=$API_KEY_21ST"

import Hero from "@/components/ui/hero-button-expendable";

export default function DemoOne() {
  return (
    <div className="h-full w-full">
    <Hero/>
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


## Illuminated Hero

**Author:** @sshahaider | **Used:** 143x
**URL:** https://21st.dev/@sshahaider/components/illuminated-hero
**Install:** `npx shadcn@latest add "https://21st.dev/r/sshahaider/illuminated-hero?api_key=$API_KEY_21ST"`
**Description:** A striking hero section with glowing animated text that instantly grabs attention.
Perfect for bold headlines, product launches, or landing pages with dramatic flair.

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
illuminated-hero.tsx
// Full source available at: https://21st.dev/@sshahaider/components/illuminated-hero
// Or install via: npx shadcn@latest add "https://21st.dev/r/sshahaider/illuminated-hero?api_key=$API_KEY_21ST"

import { IlluminatedHero } from "@/components/ui/illuminated-hero";

export default function DemoOne() {
  return <IlluminatedHero />;
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


## Digital Aurora

**Author:** @dhileepkumargm | **Used:** 136x
**URL:** https://21st.dev/@dhileepkumargm/components/digital-aurora
**Install:** `npx shadcn@latest add "https://21st.dev/r/dhileepkumargm/digital-aurora?api_key=$API_KEY_21ST"`
**Description:** A stunning, interactive hero section featuring a real-time volumetric aurora shader. Built with React and WebGL for a captivating user experience.

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
digital-aurora.tsx
// Full source available at: https://21st.dev/@dhileepkumargm/components/digital-aurora
// Or install via: npx shadcn@latest add "https://21st.dev/r/dhileepkumargm/digital-aurora?api_key=$API_KEY_21ST"

import AuroraHero from "@/components/ui/digital-aurora";

export default function DemoOne() {
  
  return <AuroraHero
      title="Experience the Digital Aurora."
      description="A stunning, interactive hero section featuring a real-time volumetric aurora shader. Built with React and WebGL for a captivating user experience."
      badgeText="Generative Art"
      badgeLabel="Live Demo"
      ctaButtons={[
        { text: "Explore Now", href: "#", primary: true },
        { text: "Learn More", href: "#" }
      ]}
      microDetails={["Real-time rendering", "Interactive mouse influence", "Volumetric light simulation"]}
    />
  ;
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

