# 21st.dev — Testimonials & Reviews — Full Integration Prompts

25 components sorted by popularity.
Each section is a copy-paste ready prompt for Claude or any AI coding tool.

---

## Stagger Testimonials

**Author:** @vaib215 | **Used:** 856x
**URL:** https://21st.dev/@vaib215/components/stagger-testimonials
**Install:** `npx shadcn@latest add "https://21st.dev/r/vaib215/stagger-testimonials?api_key=$API_KEY_21ST"`
**Description:** Testimonial Component that stands apart from the boring boxes of quotes. Dark mode compatible, no frame motion used.

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
stagger-testimonials.tsx
// Full source available at: https://21st.dev/@vaib215/components/stagger-testimonials
// Or install via: npx shadcn@latest add "https://21st.dev/r/vaib215/stagger-testimonials?api_key=$API_KEY_21ST"

import { StaggerTestimonials } from "@/components/ui/stagger-testimonials";

const DemoOne = () => {
  return (
    <div className="flex w-full h-screen justify-center items-center">
      <StaggerTestimonials />
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


## Circular Testimonials

**Author:** @maxim.bort.devel | **Used:** 767x
**URL:** https://21st.dev/@maxim.bort.devel/components/circular-testimonials
**Install:** `npx shadcn@latest add "https://21st.dev/r/maxim.bort.devel/circular-testimonials?api_key=$API_KEY_21ST"`
**Description:** An animated testimonial section that displays user feedback in a visually engaging way.

For the disclaimer, credit information, and the Vanilla HTML/CSS/JS version, please visit https://codepen.io/Northstrix/pen/QwWoYzZ

Vue Version https://namer-ui-for-vue.netlify.app/components/circular-testimonials


This component (Next.js version) is also available on Namer UI https://namer-ui.netlify.app

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
circular-testimonials.tsx
// Full source available at: https://21st.dev/@maxim.bort.devel/components/circular-testimonials
// Or install via: npx shadcn@latest add "https://21st.dev/r/maxim.bort.devel/circular-testimonials?api_key=$API_KEY_21ST"

import React from "react";
import { CircularTestimonials } from '@/components/ui/circular-testimonials';

const testimonials = [
  {
    quote:
      "I was impressed by the food! And I could really tell that they use high-quality ingredients. The staff was friendly and attentive. I'll definitely be back for more!",
    name: "Tamar Mendelson",
    designation: "Restaurant Critic",
    src:
      "https://images.unsplash.com/photo-1512316609839-ce289d3eba0a?q=80&w=1368&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
  },
  {
    quote:
      "This place exceeded all expectations! The atmosphere is inviting, and the staff truly goes above and beyond. I'll keep returning for more exceptional dining experience.",
    name: "Joe Charlescraft",
    designation: "Frequent Visitor",
    src:
      "https://images.unsplash.com/photo-1628749528992-f5702133b686?q=80&w=1368&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fA%3D%3D",
  },
  {
    quote:
      "Shining Yam is a hidden gem! The impeccable service and overall attention to detail created a memorable experience. I highly recommend it!",
    name: "Martina Edelweist",
    designation: "Satisfied Customer",
    src:
      "https://images.unsplash.com/photo-1524267213992-b76e8577d046?q=80&w=1368&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fA%3D%3D",
  },
];

export const CircularTestimonialsDemo = () => (
  <section>
    {/* Light testimonials section */}
    <div className="bg-[#f7f7fa] p-20 rounded-lg min-h-[300px] flex flex-wrap gap-6 items-center justify-center relative">
      <div
        className="items-center justify-center relative flex"
        style={{ maxWidth: "1456px" }}
      >
        <CircularTestimonials
          testimonials={testimonials}
          autoplay={true}
          colors={{
            name: "#0a0a0a",
            designation: "#454545",
            testimony: "#171717",
            arrowBackground: "#141414",
            arrowForeground: "#f1f1f7",
            arrowHoverBackground: "#00A6FB",
          }}
          fontSizes={{
            name: "28px",
            designation: "20px",
            quote: "20px",
          }}
        />
      </div>
    </div>

    {/* Dark testimonials section */}
    <div className="bg-[#060507] p-16 rounded-lg min-h-[300px] flex flex-wrap gap-6 items-center justify-center relative">
      <div
        className="items-center justify-center relative flex"
        style={{ maxWidth: "1024px" }}
      >
        <CircularTestimonials
          testimonials={testimonials}
          autoplay={true}
          colors={{
            name: "#f7f7ff",
            designation: "#e1e1e1",
            testimony: "#f1f1f7",
            arrowBackground: "#0582CA",
            arrowForeground: "#141414",
            arrowHoverBackground: "#f7f7ff",
          }}
          fontSizes={{
            name: "28px",
            designation: "20px",
            quote: "20px",
          }}
        />
      </div>
    </div>
  </section>
);

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


## Testimonial-v2

**Author:** @avanishverma4 | **Used:** 428x
**URL:** https://21st.dev/@avanishverma4/components/testimonial-v2
**Install:** `npx shadcn@latest add "https://21st.dev/r/avanishverma4/testimonial-v2?api_key=$API_KEY_21ST"`
**Description:** A reusable testimonial component block

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
testimonial-v2.tsx
// Full source available at: https://21st.dev/@avanishverma4/components/testimonial-v2
// Or install via: npx shadcn@latest add "https://21st.dev/r/avanishverma4/testimonial-v2?api_key=$API_KEY_21ST"

import Component from "@/components/ui/testimonial-v2";

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


## Testimonials

**Author:** @meschacirung | **Used:** 332x
**URL:** https://21st.dev/@meschacirung/components/testimonials
**Install:** `npx shadcn@latest add "https://21st.dev/r/meschacirung/testimonials?api_key=$API_KEY_21ST"`
**Description:** Here is Testimonials components

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
testimonials.tsx
// Full source available at: https://21st.dev/@meschacirung/components/testimonials
// Or install via: npx shadcn@latest add "https://21st.dev/r/meschacirung/testimonials?api_key=$API_KEY_21ST"

import Testimonials from "@/components/ui/testimonials";

export default function DemoOne() {
  return <Testimonials />;
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


## testimonial

**Author:** @uilayout.contact | **Used:** 281x
**URL:** https://21st.dev/@uilayout.contact/components/testimonial
**Install:** `npx shadcn@latest add "https://21st.dev/r/uilayout.contact/testimonial?api_key=$API_KEY_21ST"`
**Description:** Professional testimonial components featuring customer reviews, client feedback, social proof displays, and trust-building layouts designed to showcase credibility and increase customer confidence

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
testimonial.tsx
// Full source available at: https://21st.dev/@uilayout.contact/components/testimonial
// Or install via: npx shadcn@latest add "https://21st.dev/r/uilayout.contact/testimonial?api_key=$API_KEY_21ST"

import  Component  from "@/components/ui/testimonial";

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


## Design Testimonial

**Author:** @jatin-yadav05 | **Used:** 265x
**URL:** https://21st.dev/@jatin-yadav05/components/design-testimonial
**Install:** `npx shadcn@latest add "https://21st.dev/r/jatin-yadav05/design-testimonial?api_key=$API_KEY_21ST"`
**Description:** A completely unique asymmetric layout testimonial. Features include a vertical left column with rotated "Testimonials" text and an animated progress bar.

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
design-testimonial.tsx
// Full source available at: https://21st.dev/@jatin-yadav05/components/design-testimonial
// Or install via: npx shadcn@latest add "https://21st.dev/r/jatin-yadav05/design-testimonial?api_key=$API_KEY_21ST"

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


## pricing

**Author:** @uilayout.contact | **Used:** 251x
**URL:** https://21st.dev/@uilayout.contact/components/pricing
**Install:** `npx shadcn@latest add "https://21st.dev/r/uilayout.contact/pricing?api_key=$API_KEY_21ST"`
**Description:** Professional pricing components featuring subscription plans, pricing tiers, feature comparisons, and conversion-optimized layouts designed to showcase value and drive purchases

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
pricing.tsx
// Full source available at: https://21st.dev/@uilayout.contact/components/pricing
// Or install via: npx shadcn@latest add "https://21st.dev/r/uilayout.contact/pricing?api_key=$API_KEY_21ST"


import Component  from "@/components/ui/pricing";

export default function DemoOne() {
  return <div className="w-full bg-neutral-100"><Component /></div>;
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


## Profile Card Testimonial Carousel

**Author:** @arunachalam0606 | **Used:** 244x
**URL:** https://21st.dev/@arunachalam0606/components/profile-card-testimonial-carousel
**Install:** `npx shadcn@latest add "https://21st.dev/r/arunachalam0606/profile-card-testimonial-carousel?api_key=$API_KEY_21ST"`
**Description:** A responsive testimonial carousel component featuring profile cards with avatars, descriptions, and social links. Built with smooth fade animations, bottom navigation controls, and supports both light and dark themes for seamless integration.

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
profile-card-testimonial-carousel.tsx
// Full source available at: https://21st.dev/@arunachalam0606/components/profile-card-testimonial-carousel
// Or install via: npx shadcn@latest add "https://21st.dev/r/arunachalam0606/profile-card-testimonial-carousel?api_key=$API_KEY_21ST"

import { TestimonialCarousel } from "@/components/ui/profile-card-testimonial-carousel";

export default function TestimonialCarouselDemo() {
  return (
    <div className="min-h-screen flex items-center justify-center">
      <TestimonialCarousel />
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


## about section 2

**Author:** @uilayout.contact | **Used:** 207x
**URL:** https://21st.dev/@uilayout.contact/components/about-section-2
**Install:** `npx shadcn@latest add "https://21st.dev/r/uilayout.contact/about-section-2?api_key=$API_KEY_21ST"`
**Description:** Professional about section components featuring company stories, team showcases, mission statements, and brand narratives with elegant animations and responsive layouts

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
about-section-2.tsx
// Full source available at: https://21st.dev/@uilayout.contact/components/about-section-2
// Or install via: npx shadcn@latest add "https://21st.dev/r/uilayout.contact/about-section-2?api_key=$API_KEY_21ST"

import AboutSection2  from "@/components/ui/about-section-2";

export default function DemoOne() {
  return <AboutSection2 />;
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


## Retro Testimonial Carousel

**Author:** @ishamsu | **Used:** 194x
**URL:** https://21st.dev/@ishamsu/components/retro-testimonial
**Install:** `npx shadcn@latest add "https://21st.dev/r/ishamsu/retro-testimonial?api_key=$API_KEY_21ST"`
**Description:** Retro Animated Testimonial is a sleek carousel of vintage-inspired cards, each featuring a user’s photo, name, role, and feedback over a stylish background. Perfect for adding trust and a nostalgic touch to your site.



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
retro-testimonial.tsx
// Full source available at: https://21st.dev/@ishamsu/components/retro-testimonial
// Or install via: npx shadcn@latest add "https://21st.dev/r/ishamsu/retro-testimonial?api_key=$API_KEY_21ST"

import {Carousel, TestimonialCard} from "@/components/ui/retro-testimonial";
import {iTestimonial} from "@/components/ui/retro-testimonial";
type TestimonialDetails = {
	[key: string]: iTestimonial & {id: string};
};

const testimonialData = {
	ids: [
		"e60aa346-f6da-11ed-b67e-0242ac120002",
		"e60aa346-f6da-11ed-b67e-0242ac120003",
		"e60aa346-f6da-11ed-b67e-0242ac120004",
		"e60aa346-f6da-11ed-b67e-0242ac120005",
		"e60aa346-f6da-11ed-b67e-0242ac120006",
		"e60aa346-f6da-11ed-b67e-0242ac120007",
	],
	details: {
		"e60aa346-f6da-11ed-b67e-0242ac120002": {
			id: "e60aa346-f6da-11ed-b67e-0242ac120002",
			description:
				"The component library has revolutionized our development workflow. The pre-built components are not only beautiful but also highly customizable. It's saved us countless hours of development time.",
			profileImage:
				"https://images.unsplash.com/photo-1506794778202-cad84cf45f1d",
			name: "Sarah Chen",
			designation: "Senior Frontend Developer",
		},
		"e60aa346-f6da-11ed-b67e-0242ac120003": {
			id: "e60aa346-f6da-11ed-b67e-0242ac120003",
			description:
				"As a startup founder, I needed a quick way to build a professional-looking product. This component library was exactly what I needed. The documentation is clear, and the components are production-ready.",
			profileImage:
				"https://images.unsplash.com/photo-1506794778202-cad84cf45f1d",
			name: "Michael Rodriguez",
			designation: "Founder, TechStart",
		},
		"e60aa346-f6da-11ed-b67e-0242ac120004": {
			id: "e60aa346-f6da-11ed-b67e-0242ac120004",
			description:
				"The attention to detail in these components is impressive. From accessibility features to responsive design, everything is well thought out. It's become an essential part of our tech stack.",
			profileImage:
				"https://images.unsplash.com/photo-1500648767791-00dcc994a43e",
			name: "David Kim",
			designation: "UI/UX Lead",
		},
		"e60aa346-f6da-11ed-b67e-0242ac120005": {
			id: "e60aa346-f6da-11ed-b67e-0242ac120005",
			description:
				"What sets this component library apart is its flexibility. We've been able to maintain consistency across our applications while still customizing components to match our brand identity perfectly.",
			profileImage:
				"https://images.unsplash.com/photo-1494790108377-be9c29b29330",
			name: "Emily Thompson",
			designation: "Product Designer",
		},
		"e60aa346-f6da-11ed-b67e-0242ac120006": {
			id: "e60aa346-f6da-11ed-b67e-0242ac120006",
			description:
				"The performance optimization in these components is outstanding. We've seen significant improvements in our application's load times and overall user experience since implementing them.",
			profileImage:
				"https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d",
			name: "James Wilson",
			designation: "Performance Engineer",
		},
		"e60aa346-f6da-11ed-b67e-0242ac120007": {
			id: "e60aa346-f6da-11ed-b67e-0242ac120007",
			description:
				"The community support and regular updates make this component library a reliable choice for our projects. It's clear that the team behind it is committed to maintaining high quality and adding new features.",
			profileImage:
				"https://images.unsplash.com/photo-1534528741775-53994a69daeb",
			name: "Sophia Martinez",
			designation: "Full Stack Developer",
		},
	},
};

// Example 1: Basic Carousel with Testimonials
const cards = testimonialData.ids.map((cardId: string, index: number) => {
	const details = testimonialData.details as TestimonialDetails;
	return (
		<TestimonialCard
			key={cardId}
			testimonial={details[cardId]}
			index={index}
			backgroundImage="https://images.unsplash.com/photo-1528458965990-428de4b1cb0d?q=80&w=3129&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
		/>
	);
});

const DemoOne = () => {
  return (
    <div className="min-h-screen">
			{/* Example 1: Basic Carousel */}
			<section className="py-12 bg-white">
				<div className="max-w-5xl mx-auto px-4">
					<Carousel items={cards} />
				</div>
			</section>

			{/* Example 2: Vintage Style */}
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


## CaseStudies

**Author:** @ruixen.ui | **Used:** 151x
**URL:** https://21st.dev/@ruixen.ui/components/case-studies
**Install:** `npx shadcn@latest add "https://21st.dev/r/ruixen.ui/case-studies?api_key=$API_KEY_21ST"`
**Description:** This component is a pricing plan selector built with React and ShadCN UI. It displays three subscription options—Free, Pro, and Enterprise—each inside a styled card. The plans include a title, price, base units, and a list of features. A toggle button allows switching between showing the base units included in each plan or the per-unit pricing. The design ensures clarity by neatly aligning text, removing decimals

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
case-studies.tsx
// Full source available at: https://21st.dev/@ruixen.ui/components/case-studies
// Or install via: npx shadcn@latest add "https://21st.dev/r/ruixen.ui/case-studies?api_key=$API_KEY_21ST"

import Casestudies from "@/components/ui/case-studies";

export default function DemoOne() {
  return <Casestudies />;
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


## Testimonial Slider

**Author:** @rf-rifat | **Used:** 145x
**URL:** https://21st.dev/@rf-rifat/components/testimonial-slider
**Install:** `npx shadcn@latest add "https://21st.dev/r/rf-rifat/testimonial-slider?api_key=$API_KEY_21ST"`
**Description:** Adaptive Layout: Automatically adjusts visible testimonials (1-3) based on screen size

Smooth Animations: Spring-based transitions with drag-and-drop functionality

Auto-Play: Rotates testimonials every 4 seconds with pause on interaction

Interactive Controls: Navigation buttons and dot indicators with hover effects

Mobile Optimized: Touch-friendly swipe gestures with reduced swipe threshold

Visual Feedback: Animated user avatars and active slide indicators

Accessible: ARIA labels and keyboard-navigable controls

Modern Design: Gradient accents, card shadows, and clean typography

Performance: Optimized image loading with error fallbacks

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
testimonial-slider.tsx
// Full source available at: https://21st.dev/@rf-rifat/components/testimonial-slider
// Or install via: npx shadcn@latest add "https://21st.dev/r/rf-rifat/testimonial-slider?api_key=$API_KEY_21ST"

"use client"
import React, { useState, useEffect, useRef } from 'react';
import { motion } from 'framer-motion';
import { ChevronLeft, ChevronRight, Quote } from 'lucide-react';
import Image from 'next/image';

interface Testimonial {
  id: number;
  quote: string;
  name: string;
  username: string;
  avatar: string;
}

const testimonials: Testimonial[] = [
  { id: 1, quote: "Impressed by the professionalism and attention to detail.", name: "Guy Hawkins", username: "@guyhawkins", avatar: "https://images.unsplash.com/photo-1633332755192-727a05c4013d?fm=jpg&q=60&w=3000&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8dXNlcnxlbnwwfHwwfHx8MA%3D%3D" },
  { id: 2, quote: "A seamless experience from start to finish. Highly recommend!", name: "Karla Lynn", username: "@karlalynn8", avatar: "https://images.unsplash.com/photo-1633332755192-727a05c4013d?fm=jpg&q=60&w=3000&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8dXNlcnxlbnwwfHwwfHx8MA%3D%3D" },
  { id: 3, quote: "Reliable and trustworthy. Made my life so much easier!", name: "Jane Cooper", username: "@janecooper", avatar: "https://images.unsplash.com/photo-1633332755192-727a05c4013d?fm=jpg&q=60&w=3000&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8dXNlcnxlbnwwfHwwfHx8MA%3D%3D" },
  { id: 4, quote: "The level of service exceeded my expectations. Will definitely come back.", name: "Robert Chen", username: "@robertchen", avatar: "https://images.unsplash.com/photo-1633332755192-727a05c4013d?fm=jpg&q=60&w=3000&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8dXNlcnxlbnwwfHwwfHx8MA%3D%3D" },
  { id: 5, quote: "An innovative approach that truly solved my problems.", name: "Sarah Miller", username: "@sarahmiller", avatar: "https://images.unsplash.com/photo-1633332755192-727a05c4013d?fm=jpg&q=60&w=3000&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8dXNlcnxlbnwwfHwwfHx8MA%3D%3D" },
];

const getVisibleCount = (width: number): number => {
  if (width >= 1280) return 3;
  if (width >= 768) return 2;
  return 1;
};

const TestimonialSlider: React.FC = () => {
  const [currentIndex, setCurrentIndex] = useState(0);
  const [windowWidth, setWindowWidth] = useState(typeof window !== 'undefined' ? window.innerWidth : 1024);
  const [isAutoPlaying, setIsAutoPlaying] = useState(true);
  const autoPlayRef = useRef<NodeJS.Timeout | null>(null);
  const [direction, setDirection] = useState(0);
  const containerRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (typeof window === 'undefined') return;
    
    const handleResize = () => {
      const newWidth = window.innerWidth;
      setWindowWidth(newWidth);
      
      const oldVisibleCount = getVisibleCount(windowWidth);
      const newVisibleCount = getVisibleCount(newWidth);
      
      if (oldVisibleCount !== newVisibleCount) {
        const maxIndexForNewWidth = testimonials.length - newVisibleCount;
        if (currentIndex > maxIndexForNewWidth) {
          setCurrentIndex(Math.max(0, maxIndexForNewWidth));
        }
      }
    };
    
    window.addEventListener('resize', handleResize);
    return () => window.removeEventListener('resize', handleResize);
  }, [windowWidth, currentIndex]);

  useEffect(() => {
    if (!isAutoPlaying) return;

    const startAutoPlay = () => {
      autoPlayRef.current = setInterval(() => {
        const visibleCount = getVisibleCount(windowWidth);
        const maxIndex = testimonials.length - visibleCount;

        if (currentIndex >= maxIndex) {
          setDirection(-1);
          setCurrentIndex((prev) => prev - 1);
        } else if (currentIndex <= 0) {
          setDirection(1);
          setCurrentIndex((prev) => prev + 1);
        } else {
          setCurrentIndex((prev) => prev + direction);
        }
      }, 4000);
    };

    startAutoPlay();

    return () => {
      if (autoPlayRef.current) {
        clearInterval(autoPlayRef.current);
      }
    };
  }, [isAutoPlaying, currentIndex, windowWidth, direction]);

  const visibleCount = getVisibleCount(windowWidth);
  const maxIndex = testimonials.length - visibleCount;
  const canGoNext = currentIndex < maxIndex;
  const canGoPrev = currentIndex > 0;

  const goNext = () => {
    if (canGoNext) {
      setDirection(1);
      setCurrentIndex((prev) => Math.min(prev + 1, maxIndex));
      pauseAutoPlay();
    }
  };

  const goPrev = () => {
    if (canGoPrev) {
      setDirection(-1);
      setCurrentIndex((prev) => Math.max(prev - 1, 0));
      pauseAutoPlay();
    }
  };

  const pauseAutoPlay = () => {
    setIsAutoPlaying(false);
    setTimeout(() => setIsAutoPlaying(true), 8000);
  };

  const handleDragEnd = (event: any, info: any) => {
    const { offset } = info;
    const swipeThreshold = 30;

    if (offset.x < -swipeThreshold && canGoNext) {
      goNext();
    } else if (offset.x > swipeThreshold && canGoPrev) {
      goPrev();
    }
  };

  const goToSlide = (index: number) => {
    setCurrentIndex(index);
    pauseAutoPlay();
  };

  return (
    <div className="px-4 py-8 sm:py-16 bg-gradient-to-b from-gray-50 to-white dark:from-gray-900 dark:to-gray-800 overflow-hidden">
      <div className="max-w-6xl mx-auto">
        <motion.div 
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6 }}
          className="text-center mb-8 sm:mb-12 md:mb-16"
        >
          <span className="inline-block py-1 px-3 rounded-full bg-primary/10 dark:bg-primary/20 text-primary dark:text-primary-light font-medium text-xs sm:text-sm uppercase tracking-wider">
            Testimonials
          </span>
          <h3 className="text-2xl sm:text-3xl md:text-4xl font-bold bg-gradient-to-r from-primary to-primary/70 dark:from-primary-light dark:to-primary bg-clip-text text-transparent mt-3 sm:mt-4 px-4">
            Transformative Student Experiences
          </h3>
          <div className="w-16 sm:w-24 h-1 bg-gradient-to-r from-primary to-primary/70 dark:from-primary-light dark:to-primary mx-auto mt-4 sm:mt-6"></div>
        </motion.div>

        <div className="relative" ref={containerRef}>
          <div className="flex justify-center sm:justify-end sm:absolute sm:-top-16 right-0 space-x-2 mb-4 sm:mb-0">
            <motion.button
              whileHover={{ scale: 1.1 }}
              whileTap={{ scale: 0.95 }}
              onClick={goPrev}
              disabled={!canGoPrev}
              className={`p-2 rounded-full ${
                canGoPrev 
                  ? 'bg-white dark:bg-gray-700 shadow-md hover:bg-gray-50 dark:hover:bg-gray-600 text-primary dark:text-primary-light' 
                  : 'bg-gray-100 dark:bg-gray-800 text-gray-400 cursor-not-allowed'
              } transition-all duration-300`}
              aria-label="Previous testimonial"
            >
              <ChevronLeft size={20} className="w-4 h-4 sm:w-5 sm:h-5" />
            </motion.button>
            <motion.button
              whileHover={{ scale: 1.1 }}
              whileTap={{ scale: 0.95 }}
              onClick={goNext}
              disabled={!canGoNext}
              className={`p-2 rounded-full ${
                canGoNext 
                  ? 'bg-white dark:bg-gray-700 shadow-md hover:bg-gray-50 dark:hover:bg-gray-600 text-primary dark:text-primary-light' 
                  : 'bg-gray-100 dark:bg-gray-800 text-gray-400 cursor-not-allowed'
              } transition-all duration-300`}
              aria-label="Next testimonial"
            >
              <ChevronRight size={20} className="w-4 h-4 sm:w-5 sm:h-5" />
            </motion.button>
          </div>

          <div className="overflow-hidden relative px-2 sm:px-0">
            <motion.div
              className="flex"
              animate={{ x: `-${currentIndex * (100 / visibleCount)}%` }}
              transition={{ 
                type: 'spring', 
                stiffness: 70, 
                damping: 20 
              }}
            >
              {testimonials.map((testimonial) => (
                <motion.div
                  key={testimonial.id}
                  className={`flex-shrink-0 w-full ${
                    visibleCount === 3 ? 'md:w-1/3' : 
                    visibleCount === 2 ? 'md:w-1/2' : 'w-full'
                  } p-2`}
                  initial={{ opacity: 0.5, scale: 0.95 }}
                  animate={{ opacity: 1, scale: 1 }}
                  transition={{ duration: 0.4 }}
                  drag="x"
                  dragConstraints={{ left: 0, right: 0 }}
                  dragElastic={0.2}
                  onDragEnd={handleDragEnd}
                  whileHover={{ y: -5 }}
                  whileTap={{ scale: 0.98, cursor: 'grabbing' }}
                  style={{ cursor: 'grab' }}
                >
                  <motion.div 
                    className="relative overflow-hidden rounded-xl sm:rounded-2xl p-4 sm:p-6 h-full bg-white dark:bg-gray-800 border border-gray-100 dark:border-gray-700 shadow-lg shadow-primary/5 dark:shadow-primary-light/5"
                    whileHover={{
                      boxShadow: "0 10px 15px -3px rgba(79, 70, 229, 0.1), 0 4px 6px -2px rgba(79, 70, 229, 0.05)"
                    }}
                  >
                    <div className="absolute -top-4 -left-4 opacity-10 dark:opacity-20">
                      <Quote size={windowWidth < 640 ? 40 : 60} className="text-primary dark:text-primary-light" />
                    </div>
                    
                    <div className="relative z-10 h-full flex flex-col">
                      <p className="text-sm sm:text-base text-gray-700 dark:text-gray-300 font-medium mb-4 sm:mb-6 leading-relaxed">
                        &ldquo;{testimonial.quote}&rdquo;
                      </p>
                      
                      <div className="mt-auto pt-3 sm:pt-4 border-t border-gray-100 dark:border-gray-700">
                        <div className="flex items-center">
                          <div className="relative flex-shrink-0">
                            <Image
                              width={48}
                              height={48}
                              src={testimonial.avatar}
                              alt={testimonial.name}
                              className="w-8 h-8 sm:w-10 sm:h-10 rounded-full object-cover border-2 border-white dark:border-gray-800 shadow-sm"
                              onError={(e) => {
                                (e.target as HTMLImageElement).src = '/api/placeholder/48/48';
                              }}
                            />
                            <motion.div 
                              className="absolute inset-0 rounded-full bg-primary/20 dark:bg-primary-light/20"
                              animate={{ 
                                scale: [1, 1.2, 1],
                                opacity: [0, 0.3, 0] 
                              }}
                              transition={{ 
                                duration: 2,
                                repeat: Infinity,
                                repeatDelay: 1
                              }}
                            />
                          </div>
                          <div className="ml-3">
                            <h4 className="font-bold text-sm sm:text-base text-gray-900 dark:text-white">{testimonial.name}</h4>
                            <p className="text-gray-600 dark:text-gray-400 text-xs sm:text-sm">{testimonial.username}</p>
                          </div>
                        </div>
                      </div>
                    </div>
                  </motion.div>
                </motion.div>
              ))}
            </motion.div>
          </div>
              
          <div className="flex justify-center mt-6 sm:mt-8">
            {Array.from({ length: testimonials.length - visibleCount + 1 }, (_: any, index: any) => (
              <motion.button
                key={index}
                onClick={() => goToSlide(index)}
                className="relative mx-1 focus:outline-none"
                whileHover={{ scale: 1.2 }}
                whileTap={{ scale: 0.9 }}
                aria-label={`Go to testimonial ${index + 1}`}
              >
                <motion.div
                  className={`w-2 h-2 rounded-full ${
                    index === currentIndex 
                      ? 'bg-primary dark:bg-primary-light' 
                      : 'bg-gray-300 dark:bg-gray-600'
                  }`}
                  animate={{ 
                    scale: index === currentIndex ? [1, 1.2, 1] : 1
                  }}
                  transition={{ 
                    duration: 1.5, 
                    repeat: index === currentIndex ? Infinity : 0,
                    repeatDelay: 1
                  }}
                />
                {index === currentIndex && (
                  <motion.div
                    className="absolute inset-0 rounded-full bg-primary/30 dark:bg-primary-light/30"
                    animate={{ 
                      scale: [1, 1.8],
                      opacity: [1, 0] 
                    }}
                    transition={{ 
                      duration: 1.5,
                      repeat: Infinity,
                    }}
                  />
                )}
              </motion.button>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};

export default TestimonialSlider;
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


## Image Testimonial Grid

**Author:** @ravikatiyar162 | **Used:** 142x
**URL:** https://21st.dev/@ravikatiyar162/components/image-testimonial-grid
**Install:** `npx shadcn@latest add "https://21st.dev/r/ravikatiyar162/image-testimonial-grid?api_key=$API_KEY_21ST"`
**Description:** Pinterest-style testimonial cards featuring user profile images, names, and quotes over scenic backgrounds. Ideal for showcasing customer stories, social proof, or community highlights in a visually engaging way.

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
image-testimonial-grid.tsx
// Full source available at: https://21st.dev/@ravikatiyar162/components/image-testimonial-grid
// Or install via: npx shadcn@latest add "https://21st.dev/r/ravikatiyar162/image-testimonial-grid?api_key=$API_KEY_21ST"

import * as React from 'react';
import { MasonryGrid } from '@/components/ui/image-testimonial-grid'; // Adjust the import path as needed

// --- Data for the cards ---
const testimonials = [
    {
        profileImage: 'https://randomuser.me/api/portraits/men/32.jpg',
        name: 'Anaam Farooq',
        feedback: "Kashmir's Hidden Winter Wonderland",
        mainImage: 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4?auto=format&fit=crop&w=800&h=1200&q=80',
    },
    {
        profileImage: 'https://randomuser.me/api/portraits/women/44.jpg',
        name: 'neophyte_clicker',
        feedback: 'Celebrating Diwali Through The Lens',
        mainImage: 'https://images.unsplash.com/photo-1605292356183-a77d0a9c9d1d?w=900&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8RGl3YWxpfGVufDB8fDB8fHww',
    },
    {
        profileImage: 'https://randomuser.me/api/portraits/men/56.jpg',
        name: 'Badshah1341',
        feedback: 'A Sunset Symphony in Gold',
        mainImage: 'https://images.unsplash.com/photo-1494500764479-0c8f2919a3d8?auto=format&fit=crop&w=800&h=1000&q=80',
    },
    {
        profileImage: 'https://randomuser.me/api/portraits/men/78.jpg',
        name: 'mohsinsyasin_',
        feedback: 'realme Insider Event Kashmir',
        mainImage: 'https://images.unsplash.com/photo-1617396900799-f4ec2b43c7ae?w=900&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTh8fHdhbGxwYXBlciUyMDRrfGVufDB8fDB8fHww',
    },
    {
        profileImage: 'https://randomuser.me/api/portraits/women/68.jpg',
        name: 'Naaz khan',
        feedback: 'Illuminate the Night with the P3 Pro',
        mainImage: 'https://images.unsplash.com/photo-1542273917363-3b1817f69a2d?w=900&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NTF8fG5hdHVyZXxlbnwwfHwwfHx8MA%3D%3D',
    },
    {
        profileImage: 'https://randomuser.me/api/portraits/women/88.jpg',
        name: 'Venky_smile',
        feedback: 'Highlights from realme',
        mainImage: 'https://images.unsplash.com/photo-1444464666168-49d633b86797?w=900&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OTh8fG5hdHVyZXxlbnwwfHwwfHx8MA%3D%3D',
    },
    {
        profileImage: 'https://randomuser.me/api/portraits/men/21.jpg',
        name: 'LoserAnant',
        feedback: '14 Pro Series Launch Event Recap',
        mainImage: 'https://images.unsplash.com/photo-1497436072909-60f360e1d4b1?w=900&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Njh8fG5hdHVyZXxlbnwwfHwwfHx8MA%3D%3D',
    },
    {
        profileImage: 'https://randomuser.me/api/portraits/women/11.jpg',
        name: 'Isabella',
        feedback: 'The mountains are calling me.',
        mainImage: 'https://images.unsplash.com/photo-1531366936337-7c912a4589a7?auto=format&fit=crop&w=800&h=1200&q=80',
    },
];

// --- Reusable Card Component ---
const TestimonialCard = ({ profileImage, name, feedback, mainImage }: (typeof testimonials)[0]) => (
  <div className="relative rounded-2xl overflow-hidden group transition-transform duration-300 ease-in-out hover:scale-105">
    <img
      src={mainImage}
      alt={feedback}
      className="w-full h-auto object-cover"
      onError={(e) => {
        e.currentTarget.src = 'https://placehold.co/800x600/1a1a1a/ffffff?text=Image';
      }}
    />
    <div className="absolute inset-0 bg-gradient-to-b from-black/60 via-black/20 to-transparent" />
    <div className="absolute top-0 left-0 p-4 text-white">
      <div className="flex items-center gap-3 mb-2">
        <img
          src={profileImage}
          className="w-8 h-8 rounded-full border-2 border-white/80"
          alt={name}
          onError={(e) => {
            e.currentTarget.src = 'https://placehold.co/40x40/EFEFEF/333333?text=A';
          }}
        />
        <span className="font-semibold text-sm drop-shadow-md">{name}</span>
      </div>
      <p className="text-sm font-medium leading-tight drop-shadow-md">{feedback}</p>
    </div>
  </div>
);


// --- Demo Component ---
const MasonryGridDemo = () => {
  const [columns, setColumns] = React.useState(4);

  // Function to determine columns based on screen width
  const getColumns = (width: number) => {
    if (width < 640) return 1;    // sm
    if (width < 1024) return 2;   // lg
    if (width < 1280) return 3;   // xl
    return 4;                     // 2xl and up
  };

  React.useEffect(() => {
    const handleResize = () => {
      setColumns(getColumns(window.innerWidth));
    };

    handleResize(); // Set initial columns on mount

    window.addEventListener('resize', handleResize);
    return () => window.removeEventListener('resize', handleResize);
  }, []);

  return (
    <div className="w-full min-h-screen p-4 sm:p-6 lg:p-8 bg-background text-foreground">
      <div className="max-w-7xl mx-auto">
        <h1 className="text-3xl md:text-4xl font-bold mb-8 text-center">What People Are Saying</h1>
        <MasonryGrid columns={columns} gap={4}>
          {testimonials.map((card, index) => (
            <TestimonialCard key={index} {...card} />
          ))}
        </MasonryGrid>
      </div>
    </div>
  );
};

export default MasonryGridDemo;

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


## Unique Testimonial

**Author:** @jatin-yadav05 | **Used:** 140x
**URL:** https://21st.dev/@jatin-yadav05/components/unique-testimonial
**Install:** `npx shadcn@latest add "https://21st.dev/r/jatin-yadav05/unique-testimonial?api_key=$API_KEY_21ST"`
**Description:** A minimal testimonial component featuring a centered quote with smooth fade/blur transitions when switching between testimonials.

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
unique-testimonial.tsx
// Full source available at: https://21st.dev/@jatin-yadav05/components/unique-testimonial
// Or install via: npx shadcn@latest add "https://21st.dev/r/jatin-yadav05/unique-testimonial?api_key=$API_KEY_21ST"

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


## Testimonials

**Author:** @ravikatiyar162 | **Used:** 130x
**URL:** https://21st.dev/@ravikatiyar162/components/testimonials
**Install:** `npx shadcn@latest add "https://21st.dev/r/ravikatiyar162/testimonials?api_key=$API_KEY_21ST"`
**Description:** Testimonials Section
A responsive and animated component to showcase customer testimonials in a clean, grid-based layout.

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
testimonials.tsx
// Full source available at: https://21st.dev/@ravikatiyar162/components/testimonials
// Or install via: npx shadcn@latest add "https://21st.dev/r/ravikatiyar162/testimonials?api_key=$API_KEY_21ST"

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


## Testimonials Section

**Author:** @sshahaider | **Used:** 127x
**URL:** https://21st.dev/@sshahaider/components/testimonials-section
**Install:** `npx shadcn@latest add "https://21st.dev/r/sshahaider/testimonials-section?api_key=$API_KEY_21ST"`
**Description:** A modern testimonial grid with animations, customer photos, and quotes — perfect for SaaS, startups, and business websites to showcase client success stories and build trust.

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
testimonials-section.tsx
// Full source available at: https://21st.dev/@sshahaider/components/testimonials-section
// Or install via: npx shadcn@latest add "https://21st.dev/r/sshahaider/testimonials-section?api_key=$API_KEY_21ST"

import { TestimonialsSection } from "@/components/ui/testimonials-section";

export default function DemoOne() {
  return <TestimonialsSection />;
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


## Testimonial Slider

**Author:** @kavikatiyar | **Used:** 126x
**URL:** https://21st.dev/@kavikatiyar/components/testimonial-slider-1
**Install:** `npx shadcn@latest add "https://21st.dev/r/kavikatiyar/testimonial-slider-1?api_key=$API_KEY_21ST"`

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
testimonial-slider-1.tsx
// Full source available at: https://21st.dev/@kavikatiyar/components/testimonial-slider-1
// Or install via: npx shadcn@latest add "https://21st.dev/r/kavikatiyar/testimonial-slider-1?api_key=$API_KEY_21ST"

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


## Clean Testimonial

**Author:** @jatin-yadav05 | **Used:** 125x
**URL:** https://21st.dev/@jatin-yadav05/components/clean-testimonial
**Install:** `npx shadcn@latest add "https://21st.dev/r/jatin-yadav05/clean-testimonial?api_key=$API_KEY_21ST"`
**Description:** Clean testimonial component with unique features.

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
clean-testimonial.tsx
// Full source available at: https://21st.dev/@jatin-yadav05/components/clean-testimonial
// Or install via: npx shadcn@latest add "https://21st.dev/r/jatin-yadav05/clean-testimonial?api_key=$API_KEY_21ST"

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


## Testimonial

**Author:** @ravikatiyar162 | **Used:** 118x
**URL:** https://21st.dev/@ravikatiyar162/components/testimonial
**Install:** `npx shadcn@latest add "https://21st.dev/r/ravikatiyar162/testimonial?api_key=$API_KEY_21ST"`
**Description:** An animated testimonials slider, pairing a person's image on the left with their quote, name, and title on the right. Users can navigate through entries with arrow controls, and the component features a subtle animated grid background with both light and dark modes.

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
testimonial.tsx
// Full source available at: https://21st.dev/@ravikatiyar162/components/testimonial
// Or install via: npx shadcn@latest add "https://21st.dev/r/ravikatiyar162/testimonial?api_key=$API_KEY_21ST"

import { Component } from "@/components/ui/testimonial";

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


## Team Showcase

**Author:** @makviesainte | **Used:** 110x
**URL:** https://21st.dev/@makviesainte/components/team-showcase
**Install:** `npx shadcn@latest add "https://21st.dev/r/makviesainte/team-showcase?api_key=$API_KEY_21ST"`
**Description:** A magazine-style team section featuring a three-column staggered photo grid paired with an interactive member list. Photos default to grayscale; hovering a photo or a name entry simultaneously reveals the portrait in full color and highlights the corresponding name row. Includes social link icons (X, LinkedIn) that animate in on row hover.

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
team-showcase.tsx
// Full source available at: https://21st.dev/@makviesainte/components/team-showcase
// Or install via: npx shadcn@latest add "https://21st.dev/r/makviesainte/team-showcase?api_key=$API_KEY_21ST"

import TeamShowcase from "@/components/ui/team-showcase";

export default function TeamShowcaseDemo() {
  return (
    <div className="min-h-screen flex items-center justify-center p-8">
      <TeamShowcase />
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

