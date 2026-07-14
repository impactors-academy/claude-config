# 21st.dev — Pricing — Full Integration Prompts

Each section below is a **copy-paste ready integration prompt** for that component.
Use it directly with Claude or any AI coding tool to drop the component into your project.

---

## Pricing Section

**Author:** @mokshithcodez
**URL:** https://21st.dev/@mokshithcodez/components/pricing-section

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
pricing-section.tsx
// Full source: https://21st.dev/@mokshithcodez/components/pricing-section
// Install via: npx @21st-dev/magic add pricing-section
// Or copy the component code from the 21st.dev page above.

import { Component } from "@/components/ui/pricing-section";

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


## Pricing Glass

**Author:** @uithefactory
**URL:** https://21st.dev/@uithefactory/components/pricing-glass

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
pricing-glass.tsx
// Full source: https://21st.dev/@uithefactory/components/pricing-glass
// Install via: npx @21st-dev/magic add pricing-glass
// Or copy the component code from the 21st.dev page above.

"use client";

import React, { useState } from "react";
import { PricingGlass } from "@/components/ui/pricing-glass";


type BgOption = {
  name: string;
  tw: string;
  buttonClass: string;
};

const BG_COLORS: BgOption[] = [
  { name: "Obsidian", tw: "bg-[#050505]", buttonClass: "bg-[#050505]" },
  { name: "Midnight Cosmos", tw: "bg-[#0D0B14]", buttonClass: "bg-[#0D0B14]" },
  { name: "Mariana Trench", tw: "bg-[#06101E]", buttonClass: "bg-[#06101E]" },
  { name: "Dark Moss", tw: "bg-[#0A120D]", buttonClass: "bg-[#0A120D]" },
  { name: "Volcanic Ash", tw: "bg-[#1A0B0B]", buttonClass: "bg-[#1A0B0B]" }
];

const DEMO_TIERS = [
  {
    name: "Basic",
    priceMonthly: "9",
    priceAnnual: "7",
    description: "Perfect for individuals and side projects.",
    features: ["1 Workspace", "Basic Analytics", "Community Support"]
  },
  {
    name: "Pro",
    priceMonthly: "29",
    priceAnnual: "24",
    description: "For professionals and growing teams.",
    isPopular: true,
    features: ["Unlimited Workspaces", "Advanced Analytics", "Priority Support", "Custom Domains"]
  },
  {
    name: "Ultra",
    priceMonthly: "99",
    priceAnnual: "79",
    description: "Maximum power for massive scale.",
    features: ["Unlimited Everything", "Predictive AI Insights", "24/7 Dedicated Support", "Custom Domains", "Biometric Security"]
  }
];

export default function PricingGlassDemo() {
  const [bgIndex, setBgIndex] = useState(0);

  return (
    <div
      className={`relative w-full min-h-[900px] overflow-hidden ${BG_COLORS[bgIndex].tw} transition-colors duration-1000`}
    >

      {/* Background Selector */}
      <div className="absolute top-6 right-6 flex items-center gap-3 z-50 bg-black/40 backdrop-blur-xl p-2 rounded-full border border-white/10 shadow-2xl">
        <span className="text-white/60 text-[11px] font-bold tracking-wider uppercase px-2 pointer-events-none">Test Backgrounds</span>
        <div className="flex gap-2">
          {BG_COLORS.map((color, i) => (
            <button
              key={color.name}
              onClick={() => setBgIndex(i)}
              title={color.name}
              className={`w-6 h-6 rounded-full transition-all duration-300 shadow-[inset_0_2px_4px_rgba(0,0,0,0.5)] ${
                bgIndex === i ? "scale-110 ring-2 ring-white ring-offset-2 ring-offset-black" : "hover:scale-110 border border-white/20"
              } ${color.buttonClass}`}
            />
          ))}
        </div>
      </div>
      
      {/* Component Wrapper */}
      <div className="w-full max-w-7xl mx-auto py-24 relative z-20">
        <PricingGlass tiers={DEMO_TIERS} />
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


## Boxly Pricing 1

**Author:** @cnippet_dev
**URL:** https://21st.dev/@cnippet_dev/components/boxly-pricing-1

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
boxly-pricing-1.tsx
// Full source: https://21st.dev/@cnippet_dev/components/boxly-pricing-1
// Install via: npx @21st-dev/magic add boxly-pricing-1
// Or copy the component code from the 21st.dev page above.

"use client";

import { AlertCircle, ArrowRight, Check } from "lucide-react";
import { Button } from "@/components/ui/button";

const pricingTiers = [
  {
    cta: "GET STARTED FREE",
    description: "Perfect for individuals getting started",
    featured: false,
    features: [
      "Access to 50+ Templates",
      "Basic AI Writer",
      "Limited Word Count",
      "Email Support",
      "Brand Voice Customization",
      "SEO Optimization Tools",
    ],
    name: "FREE",
    price: "$0",
  },
  {
    cta: "START 7-DAY FREE TRIAL",
    description: "Best for solo creators and marketers",
    featured: true,
    features: [
      "Everything in Free",
      "Unlimited Words",
      "Export to WordPress & Notion",
      "Long-Form Assistant",
      "Brand Voice Customization",
      "SEO Optimization Tools",
    ],
    name: "PRO",
    price: "$299",
  },
  {
    cta: "CONTACT SALES",
    description: "For the growing teams and businesses",
    featured: false,
    features: [
      "Everything in Pro",
      "5 User Seats",
      "Shared Workspaces",
      "Team Performance Analytics",
      "Priority Support",
      "SEO Optimization Tools",
    ],
    name: "ENTERPRISE",
    price: "Contact us",
  },
];

export default function PricingSection() {
  return (
    <div className="min-h-screen bg-black px-4 text-white">
      <div className="mx-auto max-w-5xl border-neutral-700 border-x py-20">
        <div className="mb-10 grid grid-cols-1 items-center gap-6 px-4 md:grid-cols-12 md:px-10">
          <div className="md:col-span-8">
            <p className="mb-4 w-fit rounded-full border border-neutral-700 px-2 py-0.5 text-red-400 text-xs tracking-wide">
              SIMPLE, SCALABLE PRICING
            </p>
            <h1 className="font-normal text-3xl tracking-tight md:text-5xl">
              Plans that fit your{" "}
              <span className="text-gray-500">writing needs</span>
            </h1>
          </div>
          <div className="md:col-span-4 md:mt-auto">
            <p className="text-gray-500">
              <span className="text-white">Simple pricing</span> with powerful
              tools to help you write faster
            </p>
          </div>
        </div>

        <div className="mb-8 grid md:grid-cols-3">
          {pricingTiers.map((tier) => (
            <div
              className={`relative flex h-full flex-col ${
                tier.featured ? "" : ""
              }`}
              key={tier.name}
            >
              <div
                className={`relative flex h-full flex-col ${
                  tier.featured
                    ? "border-2 border-red-500 bg-neutral-900"
                    : "border border-neutral-700 bg-black md:border-x-0 md:border-y"
                }`}
              >
                <div className="relative mb-6 border-neutral-700 border-b p-6">
                  <h3
                    className={`mb-2 font-medium text-xl ${
                      tier.featured ? "text-red-500" : "text-white"
                    }`}
                  >
                    {tier.name}
                  </h3>
                  <p className="text-gray-400 text-sm">{tier.description}</p>
                  {!tier.featured && (
                    <div className="absolute inset-0 z-10 flex flex-col justify-between">
                      <div className="absolute -top-0.5 -left-0.5">
                        <div className="size-1.5 border-neutral-400 border-t-2 border-l-2" />
                      </div>
                      <div className="absolute -top-0.5 -right-0.5">
                        <div className="size-1.5 border-neutral-400 border-t-2 border-r-2" />
                      </div>
                      <div className="absolute -right-0.5 -bottom-0.5">
                        <div className="size-1.5 border-neutral-400 border-r-2 border-b-2" />
                      </div>
                      <div className="absolute -bottom-0.5 -left-0.5">
                        <div className="size-1.5 border-neutral-400 border-b-2 border-l-2" />
                      </div>
                    </div>
                  )}
                </div>

                <div className="mb-6 px-6">
                  <div className="flex items-baseline gap-2">
                    <span className="font-medium text-4xl text-white">
                      {tier.price}
                    </span>
                    {tier.price !== "Contact us" && (
                      <span className="text-gray-400">/month</span>
                    )}
                  </div>
                </div>

                <div className="mb-8 flex-1 px-6">
                  <p className="mb-4 font-bold text-gray-300 text-xs tracking-wide">
                    WHAT&apos;S INCLUDED:
                  </p>
                  <ul className="mb-6 space-y-3">
                    {tier.features.map((feature, idx) => (
                      <li className="flex items-start gap-3" key={idx}>
                        {tier.featured ? (
                          <AlertCircle className="mt-0.5 h-5 w-5 shrink-0 text-red-500" />
                        ) : (
                          <Check className="mt-0.5 h-5 w-5 shrink-0 text-gray-500" />
                        )}
                        <span className="text-gray-300 text-sm">{feature}</span>
                      </li>
                    ))}
                  </ul>
                  <Button
                    className={`w-full gap-2 rounded-sm py-2 ${
                      tier.featured
                        ? "bg-red-500 text-white hover:bg-red-600"
                        : "bg-white text-black hover:bg-gray-100"
                    }`}
                  >
                    {tier.cta}
                    <ArrowRight className="h-4 w-4" />
                  </Button>
                </div>
                {!tier.featured && (
                  <div className="absolute inset-0 z-10 flex flex-col justify-between">
                    <div className="absolute -right-0.5 -bottom-0.5">
                      <div className="size-1.5 border-neutral-400 border-r-2 border-b-2" />
                    </div>
                    <div className="absolute -bottom-0.5 -left-0.5">
                      <div className="size-1.5 border-neutral-400 border-b-2 border-l-2" />
                    </div>
                  </div>
                )}
              </div>
            </div>
          ))}
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


## Pricing Card

**Author:** @0xUrvish
**URL:** https://21st.dev/@0xUrvish/components/pricing-card

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
pricing-card.tsx
// Full source: https://21st.dev/@0xUrvish/components/pricing-card
// Install via: npx @21st-dev/magic add pricing-card
// Or copy the component code from the 21st.dev page above.

"use client";
import PricingCard from "@/components/ui/pricing-card";

export default function Demo() {
  return (
    <div className="flex items-center justify-center w-full min-h-screen bg-background p-8">
      <PricingCard />
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


## Pricing Tiers

**Author:** @dhiluxui
**URL:** https://21st.dev/@dhiluxui/components/pricing-tiers

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
pricing-tiers.tsx
// Full source: https://21st.dev/@dhiluxui/components/pricing-tiers
// Install via: npx @21st-dev/magic add pricing-tiers
// Or copy the component code from the 21st.dev page above.

import PricingSection from "@/components/ui/pricing-tiers";

export default function DemoOne() {
  const pricingData = {
    title: "Simple, transparent pricing",
    subtitle: "Get the features you need, without the clutter. Choose the plan that's right for you.",
    plans: [
      {
        id: 'free',
        name: 'Free',
        price: '$0',
        frequency: '/ month',
        description: 'For individuals just getting started.',
        features: [
          'Track 3 habits',
          'Basic progress reports',
          'Community access'
        ],
        buttonText: 'Get started for free',
        buttonLink: '#free',
        isFeatured: false
      },
      {
        id: 'pro',
        name: 'Pro',
        price: '$9',
        frequency: '/ month',
        description: 'For power users who want more.',
        features: [
          'Track unlimited habits',
          'Detailed analytics',
          'Priority support',
          'Data export'
        ],
        buttonText: 'Start your trial',
        buttonLink: '#pro',
        isFeatured: true
      },
      {
        id: 'team',
        name: 'Team',
        price: '$25',
        frequency: '/ user / month',
        description: 'For teams to collaborate.',
        features: [
          'All Pro features',
          'Team dashboards',
          'Shared habit tracking',
          'Admin controls'
        ],
        buttonText: 'Contact sales',
        buttonLink: '#team',
        isFeatured: false
      }
    ]
  };

  return (
    <div className="app-wrapper">
      <PricingSection data={pricingData} />
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


## Pricing Module

**Author:** @ruixenui
**URL:** https://21st.dev/@ruixenui/components/pricing-module

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
pricing-module.tsx
// Full source: https://21st.dev/@ruixenui/components/pricing-module
// Install via: npx @21st-dev/magic add pricing-module
// Or copy the component code from the 21st.dev page above.

"use client";

import { PricingModule } from "@/components/ui/pricing-module";
import { Layers, Monitor, Users, Building2 } from "lucide-react";

export default function PricingPage() {
  const plans = [
    {
      id: "free",
      name: "Free",
      description: "For individuals and small projects",
      icon: <Layers className="w-8 h-8 text-primary" />,
      priceMonthly: 9,
      priceYearly: 90,
      users: "Up to 3 users",
      features: [
        { label: "Basic analytics", included: true },
        { label: "Community access", included: true },
        { label: "Priority support", included: false },
      ],
    },
    {
      id: "basic",
      name: "Basic",
      description: "For small teams getting started",
      icon: <Monitor className="w-8 h-8 text-primary" />,
      priceMonthly: 29,
      priceYearly: 290,
      users: "Up to 10 users",
      features: [
        { label: "Advanced analytics", included: true },
        { label: "Priority support", included: true },
        { label: "Team collaboration tools", included: false },
      ],
    },
    {
      id: "team",
      name: "Team",
      description: "For growing startups and agencies",
      icon: <Users className="w-8 h-8 text-primary" />,
      priceMonthly: 99,
      priceYearly: 990,
      users: "Up to 50 users",
      features: [
        { label: "Dedicated success manager", included: true },
        { label: "Custom integrations", included: true },
        { label: "AI-powered insights", included: true },
      ],
      recommended: true,
    },
    {
      id: "enterprise",
      name: "Enterprise",
      description: "For large organizations with custom needs",
      icon: <Building2 className="w-8 h-8 text-primary" />,
      priceMonthly: 199,
      priceYearly: 1990,
      users: "Unlimited users",
      features: [
        { label: "24/7 priority support", included: true },
        { label: "Custom SLAs", included: true },
        { label: "Private cloud hosting", included: true },
      ],
    },
  ];

  return (
    <main className="min-h-screen bg-background text-foreground">
      <PricingModule
        title="Simple, Transparent Pricing"
        subtitle="Switch between monthly and yearly billing anytime."
        annualBillingLabel="Pay annually and save 20%"
        buttonLabel="Start Now"
        plans={plans}
        defaultAnnual={false}
      />
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


## Pricing Table

**Author:** @vaib215
**URL:** https://21st.dev/@vaib215/components/pricing-table

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
pricing-table.tsx
// Full source: https://21st.dev/@vaib215/components/pricing-table
// Install via: npx @21st-dev/magic add pricing-table
// Or copy the component code from the 21st.dev page above.

import { Pricing } from "@/components/ui/pricing-table"

export default function PricingDemo() {
  const gradientHeartIcon = (
    <div className="w-12 h-12 relative">
      <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" className="w-full h-full">
        <defs>
          <linearGradient id="heartGradient" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stopColor="#ff6b35" />
            <stop offset="100%" stopColor="#f72585" />
          </linearGradient>
        </defs>
        <path
          d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"
          fill="url(#heartGradient)"
        />
      </svg>
    </div>
  )

  return (
    <Pricing
      icon={gradientHeartIcon}
      title="Pricing"
      subtitle="Start for free. Upgrade to get the capacity that exactly matches your team's needs."
      tiers={[
        {
          name: "Free",
          description: "Discover what Lovable can do for you",
          price: 0,
          billingPeriod: "per month",
          buttonText: "Get Started",
          features: [
            { text: "5 daily credits (up to 30/month)" },
            { text: "Public projects" },
            { text: "Unlimited collaborators" },
          ],
          featuresTitle: "Free for everyone",
        },
        {
          name: "Pro",
          description: "Designed for fast-moving teams building together in real time.",
          price: 25,
          billingPeriod: "per month",
          buttonText: "Get Started",
          isPrimary: true,
          hasAnnualToggle: true,
          creditOptions: ["100 credits / month", "200 credits / month", "500 credits / month"],
          defaultCredits: "100 credits / month",
          featuresTitle: "Everything in Free, plus:",
          features: [
            { text: "100 monthly credits", hasInfo: true },
            { text: "5 daily credits (up to 150/month)" },
            { text: "Credit rollovers", hasInfo: true },
            { text: "Custom domains" },
            { text: "Remove the Lovable badge" },
            { text: "Private projects" },
            { text: "User roles & permissions" },
          ],
        },
        {
          name: "Business",
          description: "Advanced controls and power features for growing departments",
          price: 50,
          billingPeriod: "per month",
          buttonText: "Get Started",
          hasAnnualToggle: true,
          creditOptions: ["100 credits / month", "200 credits / month", "500 credits / month"],
          defaultCredits: "100 credits / month",
          featuresTitle: "All features in Pro, plus:",
          features: [
            { text: "100 monthly credits", hasInfo: true },
            { text: "SSO" },
            { text: "Personal Projects" },
            { text: "Opt out of data training" },
            { text: "Design templates" },
          ],
        },
        {
          name: "Enterprise",
          description: "Built for large orgs needing flexibility, scale, and governance.",
          priceLabel: "Flexible billing",
          buttonText: "Book a demo",
          featuresTitle: "Everything in Business, plus:",
          features: [
            { text: "Dedicated support" },
            { text: "Onboarding services" },
            { text: "Custom connections" },
            { text: "Group-based access control" },
            { text: "Custom design systems" },
          ],
        },
      ]}
      footerTitle="Student discount"
      footerDescription="Verify student status and get access to up to 50% off Lovable Pro."
      footerButtonText="Learn more"
    />
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


## Pricing Card With Features

**Author:** @rubenerik
**URL:** https://21st.dev/@rubenerik/components/pricing-card-with-features

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
pricing-card-with-features.tsx
// Full source: https://21st.dev/@rubenerik/components/pricing-card-with-features
// Install via: npx @21st-dev/magic add pricing-card-with-features
// Or copy the component code from the 21st.dev page above.

import { Box } from "@/components/ui/pricing-card-with-features";

export default function DemoOne() {
  return <Box />;
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


## Pricing Card Component

**Author:** @rubenerik
**URL:** https://21st.dev/@rubenerik/components/pricing-card-component

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
pricing-card-component.tsx
// Full source: https://21st.dev/@rubenerik/components/pricing-card-component
// Install via: npx @21st-dev/magic add pricing-card-component
// Or copy the component code from the 21st.dev page above.

// demo.tsx
import { Component } from "@/components/ui/pricing-card-component";

export default function DemoPricing() {
  return (
    <Component
      plans={[
        {
          name: "Starter",
          price: "19",
          yearlyPrice: "15",
          period: "month",
          features: ["Basic analytics", "100 leads", "Email support"],
          description: "Great for small teams getting started.",
          buttonText: "Get Started",
          href: "#",
          isPopular: false,
        },
        {
          name: "Pro",
          price: "49",
          yearlyPrice: "39",
          period: "month",
          features: ["Advanced analytics", "1000 leads", "Priority support"],
          description: "Perfect for growing businesses.",
          buttonText: "Upgrade",
          href: "#",
          isPopular: true,
        },
        {
          name: "Enterprise",
          price: "99",
          yearlyPrice: "79",
          period: "month",
          features: ["Unlimited leads", "Dedicated account manager"],
          description: "Best for large organizations.",
          buttonText: "Contact Sales",
          href: "#",
          isPopular: false,
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


## Pricing Section

**Author:** @bigbogiballer
**URL:** https://21st.dev/@bigbogiballer/components/pricing-section

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
pricing-section.tsx
// Full source: https://21st.dev/@bigbogiballer/components/pricing-section
// Install via: npx @21st-dev/magic add pricing-section
// Or copy the component code from the 21st.dev page above.

import * as React from "react";
import { motion } from "framer-motion";
import { cva, type VariantProps } from "class-variance-authority";
import { Slot } from "@radix-ui/react-slot";
import { Diamond, Sparkles } from "lucide-react";

// cn function
function cn(...inputs: (string | undefined | null | false)[]) {
  return inputs.filter(Boolean).join(" ");
}

// Button
const buttonVariants = cva(
  "inline-flex items-center justify-center whitespace-nowrap rounded-md text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50",
  {
    variants: {
      variant: {
        default: "bg-primary text-primary-foreground hover:bg-primary/90",
        destructive:
          "bg-destructive text-destructive-foreground hover:bg-destructive/90",
        outline:
          "border border-input bg-background hover:bg-accent hover:text-accent-foreground",
        secondary:
          "bg-secondary text-secondary-foreground hover:bg-secondary/80",
        ghost: "hover:bg-accent hover:text-accent-foreground",
        link: "text-primary underline-offset-4 hover:underline",
      },
      size: {
        default: "h-10 px-4 py-2",
        sm: "h-9 rounded-md px-3",
        lg: "h-11 rounded-md px-8",
        icon: "h-10 w-10",
      },
    },
    defaultVariants: {
      variant: "default",
      size: "default",
    },
  }
);

export interface ButtonProps
  extends React.ButtonHTMLAttributes<HTMLButtonElement>,
    VariantProps<typeof buttonVariants> {
  asChild?: boolean;
}

const Button = React.forwardRef<HTMLButtonElement, ButtonProps>(
  ({ className, variant, size, asChild = false, ...props }, ref) => {
    const Comp = asChild ? Slot : "button";
    return (
      <Comp
        className={cn(buttonVariants({ variant, size, className }))}
        ref={ref}
        {...props}
      />
    );
  }
);
Button.displayName = "Button";

// Define the props for the PricingCard component
interface PricingCardProps {
  title: string;
  price?: string;
  priceDescription?: string;
  description: string;
  features?: string[];
  buttonText: string;
  imageSrc?: string;
  imageAlt?: string;
  isUnique?: boolean; // A prop to handle the unique request card style
  className?: string;
  useSparkles?: boolean;
}

// Framer Motion variants for animations
const cardVariants = {
  initial: { scale: 1, y: 0 },
  hover: {
    scale: 1.03,
    y: -5,
    boxShadow: "0px 15px 30px -5px hsl(var(--foreground) / 0.1)",
    transition: { type: "spring", stiffness: 300, damping: 20 },
  },
};

const imageVariants = {
  initial: { scale: 1, rotate: 0 },
  hover: {
    scale: 1.1,
    rotate: -5,
    transition: { type: "spring", stiffness: 300, damping: 20 },
  },
};

const PricingCard = React.forwardRef<HTMLDivElement, PricingCardProps>(
  (
    {
      className,
      title,
      price,
      priceDescription,
      description,
      features,
      buttonText,
      imageSrc,
      imageAlt,
      isUnique = false,
      useSparkles = false,
      ...props
    },
    ref
  ) => {
    return (
      <motion.div
        ref={ref}
        variants={cardVariants}
        initial="initial"
        whileHover="hover"
        className={cn(
          "relative flex flex-col justify-between rounded-lg border bg-card p-6 text-card-foreground shadow-sm transition-shadow duration-300",
          className
        )}
        {...props}
      >
        <div className="flex flex-col space-y-4">
          {/* Card Header with optional image */}
          <div className="flex justify-between items-start">
            <div>
              <h3 className="text-xl font-semibold">{title}</h3>
              {price && (
                <div className="mt-2">
                  <span className="text-4xl font-bold">{price}</span>
                  <p className="text-sm text-muted-foreground">
                    {priceDescription}
                  </p>
                </div>
              )}
            </div>
            {imageSrc && (
              <motion.img
                src={imageSrc}
                alt={imageAlt || title}
                width={80}
                height={80}
                className="select-none"
                variants={imageVariants}
              />
            )}
          </div>

          {/* Card Description */}
          <p className="text-muted-foreground">{description}</p>

          {/* Feature List */}
          {features && (
            <ul className="space-y-2 pt-4">
              {features.map((feature, index) => (
                <li key={index} className="flex items-center gap-2">
                  {useSparkles ? (
                    <Sparkles className="h-4 w-4 text-primary" />
                  ) : (
                    <Diamond className="h-4 w-4 text-primary" />
                  )}
                  <span className="text-sm">{feature}</span>
                </li>
              ))}
            </ul>
          )}
        </div>

        {/* Card Footer with Button */}
        <div className="mt-6">
          <Button className="w-full">{buttonText}</Button>
        </div>
      </motion.div>
    );
  }
);
PricingCard.displayName = "PricingCard";

export default function PricingDemo() {
  const plans = [
    {
      title: "Starter",
      price: "€500",
      priceDescription: "Starting from",
      description:
        "Perfect for small projects and simple websites that need a professional touch.",
      features: [
        "Experienced Designer",
        "Fast Delivery",
        "Responsive Design",
        "Basic SEO Setup",
      ],
      buttonText: "Let's Talk",
      imageSrc: "https://www.thiings.co/_next/image?url=https%3A%2F%2Flftz25oez4aqbxpq.public.blob.vercel-storage.com%2Fimage-gyoxLFpXzRRzVsgPJOKvB2r4tvzpcy.png&w=320&q=75",
      imageAlt: "Pink cherry blossom tree",
    },
    {
      title: "Professional",
      price: "€1000",
      priceDescription: "Starting from",
      description:
        "Ideal for businesses that need a complete website with advanced features and functionality.",
      features: [
        "Experienced Designer",
        "Fast Delivery",
        "Conversion Focused",
        "Advanced Animations",
      ],
      buttonText: "Let's Talk",
      imageSrc: "https://www.thiings.co/_next/image?url=https%3A%2F%2Flftz25oez4aqbxpq.public.blob.vercel-storage.com%2Fimage-v98BP3EQdx0Yd0NkjHPnWx33WvzwGP.png&w=320&q=75",
      imageAlt: "Yellow autumn tree",
    },
    {
      title: "Enterprise",
      price: "€1500+",
      priceDescription: "Starting from",
      description:
        "For complex projects requiring custom development, integrations, and ongoing support.",
      features: [
        "Dedicated Design Team",
        "Priority Support",
        "Custom Development",
        "Full Design System",
      ],
      buttonText: "Let's Talk",
      imageSrc: "https://www.thiings.co/_next/image?url=https%3A%2F%2Flftz25oez4aqbxpq.public.blob.vercel-storage.com%2Fimage-gyoxLFpXzRRzVsgPJOKvB2r4tvzpcy.png&w=320&q=75",
      imageAlt: "Premium design",
      useSparkles: true,
    },
  ];

  return (
    <div className="flex min-h-screen w-full items-center justify-center bg-background px-4 py-12">
      <div className="w-full max-w-5xl space-y-8">
        {/* Title Section */}
        <div className="text-center">
          <p className="text-sm font-semibold uppercase tracking-wider text-primary">
            Pricing Plans
          </p>
          <h1 className="mt-2 text-3xl font-bold tracking-tight sm:text-4xl">
            Transparent Pricing, No Surprises
          </h1>
        </div>

        {/* Pricing Cards Grid */}
        <div className="grid grid-cols-1 gap-8 md:grid-cols-2 lg:grid-cols-3">
          {plans.map((plan) => (
            <PricingCard key={plan.title} {...plan} />
          ))}
        </div>

        {/* Unique Request Card */}
        <div className="rounded-lg border bg-card p-6 text-card-foreground shadow-sm">
           <h3 className="text-xl font-semibold">Unique Request</h3>
           <p className="mt-2 text-muted-foreground">Are you looking for something custom? Don't hesitate to contact us, and we'll help brainstorm your product to success.</p>
           <div className="mt-6">
                <Button className="w-full md:w-auto">Let's Talk</Button>
           </div>
        </div>
      </div>
    </div>
  );
}
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


## Pricing Table

**Author:** @dgearsonu1
**URL:** https://21st.dev/@dgearsonu1/components/pricing-table

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
pricing-table.tsx
// Full source: https://21st.dev/@dgearsonu1/components/pricing-table
// Install via: npx @21st-dev/magic add pricing-table
// Or copy the component code from the 21st.dev page above.

import ExamplePricingTable from "@/components/ui/pricing-table";

export default function DemoOne() {
  return <ExamplePricingTable />;
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


## Pricing Card

**Author:** @dgearsonu1
**URL:** https://21st.dev/@dgearsonu1/components/pricing-card

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
pricing-card.tsx
// Full source: https://21st.dev/@dgearsonu1/components/pricing-card
// Install via: npx @21st-dev/magic add pricing-card
// Or copy the component code from the 21st.dev page above.

import ExampleComp from "@/components/ui/pricing-card";

export default function DemoOne() {
  return <ExampleComp />;
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


## Interactive Pricing Component

**Author:** @uniquesonu
**URL:** https://21st.dev/@uniquesonu/components/interactive-pricing-component

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
interactive-pricing-component.tsx
// Full source: https://21st.dev/@uniquesonu/components/interactive-pricing-component
// Install via: npx @21st-dev/magic add interactive-pricing-component
// Or copy the component code from the 21st.dev page above.

import ExampleUsage from "@/components/ui/interactive-pricing-component";

export default function DemoOne() {
  return <ExampleUsage />;
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


## Pricing With Chart

**Author:** @efferd
**URL:** https://21st.dev/@efferd/components/pricing-with-chart

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
pricing-with-chart.tsx
// Full source: https://21st.dev/@efferd/components/pricing-with-chart
// Install via: npx @21st-dev/magic add pricing-with-chart
// Or copy the component code from the 21st.dev page above.

import { PricingWithChart } from "@/components/ui/pricing-with-chart";
import { cn } from '@/lib/utils';

export default function DemoOne() {
 return (
		<div className="relative flex min-h-screen w-full items-center justify-center px-4 py-10 bg-[radial-gradient(35%_80%_at_50%_0%,--theme(--color-foreground/.1),transparent)]">
			<PricingWithChart />


			{/* Dots */}
			<div
				aria-hidden="true"
				className={cn(
					'absolute inset-0 -z-10 size-full',
					'bg-[radial-gradient(color-mix(in_oklab,--theme(--color-foreground/.1)30%,transparent)_2px,transparent_2px)]',
					'bg-[size:12px_12px]',
				)}
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


## Pricing Card 1

**Author:** @ravikatiyar
**URL:** https://21st.dev/@ravikatiyar/components/pricing-card-1

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
pricing-card-1.tsx
// Full source: https://21st.dev/@ravikatiyar/components/pricing-card-1
// Install via: npx @21st-dev/magic add pricing-card-1
// Or copy the component code from the 21st.dev page above.

import { PricingCard } from "@/components/ui/pricing-card-1";
import { Button } from "@/components/ui/button"; 

export default function PricingDemo() {
  const plans = [
    {
      title: "Web Design",
      price: "€1500",
      priceDescription: "Starting from",
      description:
        "If you're looking to build a website that not only looks great but performs flawlessly.",
      features: [
        "Experienced Designer",
        "Fast Delivery",
        "Conversion Focused",
        "Framer Development (add-on)",
      ],
      buttonText: "Let's Talk",
      imageSrc: "https://www.thiings.co/_next/image?url=https%3A%2F%2Flftz25oez4aqbxpq.public.blob.vercel-storage.com%2Fimage-gyoxLFpXzRRzVsgPJOKvB2r4tvzpcy.png&w=320&q=75",
      imageAlt: "Pink cherry blossom tree",
    },
    {
      title: "Product Design",
      price: "€75",
      priceDescription: "Hourly rate",
      description:
        "Perfect if you're looking to build a dashboard, app, etc... and get it 'done-right' the first time.",
      features: [
        "Experienced Designer",
        "Fast Delivery",
        "Conversion Focused",
        "Tailored Design System",
      ],
      buttonText: "Let's Talk",
      imageSrc: "https://www.thiings.co/_next/image?url=https%3A%2F%2Flftz25oez4aqbxpq.public.blob.vercel-storage.com%2Fimage-v98BP3EQdx0Yd0NkjHPnWx33WvzwGP.png&w=320&q=75",
      imageAlt: "Yellow autumn tree",
    },
  ];

  return (
    <div className="flex min-h-screen w-full items-center justify-center bg-background px-4 py-12">
      <div className="w-full max-w-5xl space-y-8">
        {/* Title Section */}
        <div className="text-center">
          <p className="text-sm font-semibold uppercase tracking-wider text-primary">
            Pricing Plans
          </p>
          <h1 className="mt-2 text-3xl font-bold tracking-tight sm:text-4xl">
            Transparent Pricing, No Surprises
          </h1>
        </div>

        {/* Pricing Cards Grid */}
        <div className="grid grid-cols-1 gap-8 md:grid-cols-2">
          {plans.map((plan) => (
            <PricingCard key={plan.title} {...plan} />
          ))}
        </div>

        {/* Unique Request Card */}
        <div className="rounded-lg border bg-card p-6 text-card-foreground shadow-sm">
           <h3 className="text-xl font-semibold">Unique Request</h3>
           <p className="mt-2 text-muted-foreground">Are you looking for something custom? Don't hesitate to contact us, and we'll help brainstorm your product to success.</p>
           <div className="mt-6">
                <Button className="w-full md:w-auto">Let's Talk</Button>
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


## Pricing Component

**Author:** @shadway
**URL:** https://21st.dev/@shadway/components/pricing-component

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
pricing-component.tsx
// Full source: https://21st.dev/@shadway/components/pricing-component
// Install via: npx @21st-dev/magic add pricing-component
// Or copy the component code from the 21st.dev page above.

import PricingCards from "@/components/ui/pricing-component";

export default function DemoOne() {
  return <PricingCards />;
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


## Pricing

**Author:** @lavikatiyar
**URL:** https://21st.dev/@lavikatiyar/components/pricing

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
pricing.tsx
// Full source: https://21st.dev/@lavikatiyar/components/pricing
// Install via: npx @21st-dev/magic add pricing
// Or copy the component code from the 21st.dev page above.

import { InteractivePricingCard } from '@/components/ui/pricing'; // Adjust path as needed

export default function InteractivePricingCardDemo() {
  const proPlanFeatures = [
    'Unlimited Projects',
    'Team Collaboration',
    'Priority Support',
    'Advanced Analytics',
    '10GB Storage',
  ];

  const basicPlanFeatures = [
    '5 Projects',
    'Basic Collaboration',
    'Email Support',
    'Basic Analytics',
    '2GB Storage',
  ];

  return (
    <div className="flex min-h-screen w-full flex-col items-center justify-center gap-8 bg-background p-4 md:flex-row">
      {/* Standard Plan */}
      <InteractivePricingCard
        planName="Basic"
        planDescription="For individuals and small teams starting out."
        pricePerUnit={10}
        unitName="user"
        minUnits={1}
        maxUnits={10}
        initialUnits={3}
        features={basicPlanFeatures}
        ctaText="Get Started with Basic"
      />

      {/* Highlighted Plan */}
      <InteractivePricingCard
        planName="Pro"
        planDescription="For growing teams that need collaboration and power."
        pricePerUnit={15}
        unitName="user"
        minUnits={5}
        maxUnits={25}
        initialUnits={10}
        features={proPlanFeatures}
        ctaText="Subscribe to Pro"
        highlighted={true} // This prop makes the card stand out
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


## Pricing Section

**Author:** @brijr
**URL:** https://21st.dev/@brijr/components/pricing-section

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
pricing-section.tsx
// Full source: https://21st.dev/@brijr/components/pricing-section
// Install via: npx @21st-dev/magic add pricing-section
// Or copy the component code from the 21st.dev page above.

import Pricing from "@/components/ui/pricing-section";

export default function DemoOne() {
  return <Pricing />;
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


## Pricing Cards

**Author:** @prebuiltui
**URL:** https://21st.dev/@prebuiltui/components/pricing-cards

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
pricing-cards.tsx
// Full source: https://21st.dev/@prebuiltui/components/pricing-cards
// Install via: npx @21st-dev/magic add pricing-cards
// Or copy the component code from the 21st.dev page above.

import Example from "@/components/ui/pricing-cards";

export default function DemoOne() {
  return <Example />;
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


## Pricing Cards

**Author:** @lyanchouss
**URL:** https://21st.dev/@lyanchouss/components/pricing-cards

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
pricing-cards.tsx
// Full source: https://21st.dev/@lyanchouss/components/pricing-cards
// Install via: npx @21st-dev/magic add pricing-cards
// Or copy the component code from the 21st.dev page above.

import { Pricing2 } from "@/components/ui/pricing-cards";

export default function DemoOne() {
  return <Pricing2 />;
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


## Pricing For Teams

**Author:** @dhiluxui
**URL:** https://21st.dev/@dhiluxui/components/pricing-for-teams

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
pricing-for-teams.tsx
// Full source: https://21st.dev/@dhiluxui/components/pricing-for-teams
// Install via: npx @21st-dev/magic add pricing-for-teams
// Or copy the component code from the 21st.dev page above.

import PricingCard from "@/components/ui/pricing-for-teams";

export default function DemoOne() {
  const pricingPlans = [
    {
      planName: "Starter",
      price: "29",
      priceFrequency: "/month",
      description: "For individuals and small teams getting started.",
      features: [
        "10 Projects",
        "5 GB Storage",
        "Basic Analytics",
        "Community Support",
      ],
      ctaText: "Choose Starter",
      href: "#starter",
    },
    {
      planName: "Pro",
      price: "99",
      priceFrequency: "/month",
      description: "For growing businesses that need more power.",
      features: [
        "Unlimited Projects",
        "100 GB Storage",
        "Advanced Analytics",
        "Priority Email Support",
        "API Access",
      ],
      ctaText: "Choose Pro",
      href: "#pro",
      isFeatured: true,
    },
    {
      planName: "Enterprise",
      price: "Custom",
      priceFrequency: "",
      description: "For large organizations with custom needs.",
      features: [
        "Everything in Pro",
        "Dedicated Account Manager",
        "Custom Integrations",
        "24/7 Phone Support",
        "SLA Guarantee",
      ],
      ctaText: "Contact Sales",
      href: "#enterprise",
    },
  ];

  return (
    <div className="min-h-screen w-full bg-gray-50 font-sans text-gray-900 antialiased dark:bg-gray-900">
      <div className="container mx-auto px-4 py-16 sm:py-24">
        <header className="mb-16 text-center">
          <h1 className="text-4xl font-extrabold tracking-tight text-gray-900 sm:text-5xl dark:text-white">
            Flexible Pricing for Teams of Any Size
          </h1>
          <p className="mx-auto mt-4 max-w-2xl text-lg text-gray-500 dark:text-gray-400">
            Choose the plan that's right for you. All plans come with a 14-day free trial, no credit card required.
          </p>
        </header>

        <div className="mx-auto grid max-w-7xl grid-cols-1 gap-10 lg:grid-cols-3">
          {pricingPlans.map((plan, index) => (
            <PricingCard key={index} {...plan} />
          ))}
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


## Colorful Pricing

**Author:** @kinfe123
**URL:** https://21st.dev/@kinfe123/components/colorful-pricing

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
colorful-pricing.tsx
// Full source: https://21st.dev/@kinfe123/components/colorful-pricing
// Install via: npx @21st-dev/magic add colorful-pricing
// Or copy the component code from the 21st.dev page above.

import FUIPricingSectionWithOnePlan from "@/components/ui/colorful-pricing";


export default function FUIPricingSectionWithOnePlanDemo() {
  return <FUIPricingSectionWithOnePlan />;
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


## Pricing Section

**Author:** @kinfe123
**URL:** https://21st.dev/@kinfe123/components/pricing-section

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
pricing-section.tsx
// Full source: https://21st.dev/@kinfe123/components/pricing-section
// Install via: npx @21st-dev/magic add pricing-section
// Or copy the component code from the 21st.dev page above.

import FUIPricingSectionWithBadge from "@/components/ui/pricing-section";

export default function FUIPricingSectionWithBadgeDemo() {
  return <FUIPricingSectionWithBadge />;
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


## Aniamted Pricing Cards

**Author:** @erikx
**URL:** https://21st.dev/@erikx/components/aniamted-pricing-cards

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
aniamted-pricing-cards.tsx
// Full source: https://21st.dev/@erikx/components/aniamted-pricing-cards
// Install via: npx @21st-dev/magic add aniamted-pricing-cards
// Or copy the component code from the 21st.dev page above.

import { Heading, PricingWrapper, Price, Paragraph } from "@/components/ui/aniamted-pricing-cards";


export default function DemoOne() {
  return <div className={' h-[600px] w-full flex gap-12 items-center justify-center'}>

    <PricingWrapper contactHref={'/'} type={'waves'}>

      <Heading>component</Heading>

      <Price>

        $2000

        <br />

        /mo

      </Price>

      <Paragraph>

        Special UI component for your website made with React.js, TailwindCSS and FramerMotion.

      </Paragraph>

    </PricingWrapper>

  </div>

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


## Pricing Blocks

**Author:** @educalvolpz
**URL:** https://21st.dev/@educalvolpz/components/pricing-blocks

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
pricing-blocks.tsx
// Full source: https://21st.dev/@educalvolpz/components/pricing-blocks
// Install via: npx @21st-dev/magic add pricing-blocks
// Or copy the component code from the 21st.dev page above.

import PricingSimple from "@/components/ui/pricing-blocks";

export default function DemoOne() {
  return <PricingSimple />;
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


## Pricing Card Triple

**Author:** @nayan_radadiya6
**URL:** https://21st.dev/@nayan_radadiya6/components/pricing-card-triple

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
pricing-card-triple.tsx
// Full source: https://21st.dev/@nayan_radadiya6/components/pricing-card-triple
// Install via: npx @21st-dev/magic add pricing-card-triple
// Or copy the component code from the 21st.dev page above.

import PricingCardTwo from '@/components/ui/pricing-card-triple';
import { User, Users, Briefcase } from 'lucide-react';

export default function Pc2Basic() {
  return (
    <div className='mx-auto grid max-w-6xl gap-8 md:grid-cols-3'>
      <PricingCardTwo
        tone='pink'
        icon={<User />}
        name='Personal'
        subtitle='the starter choise'
        price={5}
        periodLabel='/month'
        features={[
          { label: 'Lorem ipsum' },
          { label: 'Lorem set' },
          { label: 'Lorem ipsum dolor.' },
          {
            label: 'Lorem ipsum dolor sit amet, consectetur.',
            included: false,
          },
          { label: 'Only lorem', included: false },
          { label: 'Lorem ipsum dolor.', included: false },
          { label: 'Lorem ipsum.', included: false },
        ]}
        cta={{ href: '#', label: 'Choose Plan' }}
      />

      <PricingCardTwo
        tone='blue'
        icon={<Users />}
        name='Team'
        subtitle='the starter choise'
        price={15}
        periodLabel='/month'
        features={[
          { label: 'Lorem ipsum' },
          { label: 'Lorem set' },
          { label: 'Lorem ipsum dolor.' },
          { label: 'Lorem ipsum dolor sit amet, consectetur.' },
          { label: 'Only lorem' },
          { label: 'Lorem ipsum dolor.', included: false },
          { label: 'Lorem ipsum.', included: false },
        ]}
        cta={{ href: '#', label: 'Choose Plan' }}
      />

      <PricingCardTwo
        tone='amber'
        icon={<Briefcase />}
        name='Business'
        subtitle='the starter choise'
        price={25}
        periodLabel='/month'
        features={[
          { label: 'Lorem ipsum' },
          { label: 'Lorem set' },
          { label: 'Lorem ipsum dolor.' },
          { label: 'Lorem ipsum dolor sit amet, consectetur.' },
          { label: 'Only lorem' },
          { label: 'Lorem ipsum dolor.' },
          { label: 'Lorem ipsum.' },
        ]}
        cta={{ href: '#', label: 'Choose Plan' }}
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


## Pricing Cart Duo

**Author:** @nayan_radadiya6
**URL:** https://21st.dev/@nayan_radadiya6/components/pricing-cart-duo

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
pricing-cart-duo.tsx
// Full source: https://21st.dev/@nayan_radadiya6/components/pricing-cart-duo
// Install via: npx @21st-dev/magic add pricing-cart-duo
// Or copy the component code from the 21st.dev page above.

import PricingCardOne from '@/components/ui/pricing-cart-duo';
import { Car, Plane } from 'lucide-react';

export default function Pc1Basic() {
  return (
    <div className='grid gap-8 sm:grid-cols-2'>
      <PricingCardOne
        icon={<Car />}
        name='Basic'
        subtitle='the starter choise'
        price={5}
        periodLabel='/month'
        tone='blue'
        features={[
          { label: 'Lorem ipsum' },
          { label: 'Lorem set' },
          { label: 'Lorem ipsum dolor.' },
          {
            label: 'Lorem ipsum dolor sit amet, consectetur.',
            included: false,
          },
          { label: 'Only lorem', included: false },
          { label: 'Lorem ipsum dolor.', included: false },
          { label: 'Lorem ipsum.', included: false },
        ]}
        cta={{ href: '#', label: 'Choose Plan' }}
        variant='outline'
      />

      <PricingCardOne
        icon={<Plane />}
        name='Pro'
        subtitle='the starter choise'
        price={15}
        periodLabel='/month'
        recommended
        tone='blue'
        features={[
          { label: 'Lorem ipsum' },
          { label: 'Lorem set' },
          { label: 'Lorem ipsum dolor.' },
          { label: 'Lorem ipsum dolor sit amet, consectetur.' },
          { label: 'Only lorem' },
          { label: 'Lorem ipsum dolor.', included: false },
          { label: 'Lorem ipsum.', included: false },
        ]}
        cta={{ href: '#', label: 'Choose Plan' }}
        variant='outline'
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


## Adaptive Pricing Section

**Author:** @vaib215
**URL:** https://21st.dev/@vaib215/components/adaptive-pricing-section

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
adaptive-pricing-section.tsx
// Full source: https://21st.dev/@vaib215/components/adaptive-pricing-section
// Install via: npx @21st-dev/magic add adaptive-pricing-section
// Or copy the component code from the 21st.dev page above.

import React from 'react'
import PricingComponent from '@/components/ui/adaptive-pricing-section'

const Demo = () => {
  const pricingTiers = [
    {
      name: "Free",
      subtitle: "COMMUNITY",
      description: "Perfect for getting started with essential features.",
      features: [
        { text: "Up to 10 user messages", included: true, hasInfo: true },
        { text: "Context Engine", included: true },
        { text: "MCP & Native Tools", included: false },
        { text: "Unlimited Next Edits & Completions", included: true },
        { text: "Community support", included: true }
      ],
      buttonText: "Install now"
    },
    {
      name: "$50",
      subtitle: "DEVELOPER",
      price: "$50",
      period: "/month",
      description: "For individuals or small teams that want to ship to production, fast.",
      badge: {
        text: "7 DAY FREE TRIAL"
      },
      features: [
        { text: "Everything in community", included: true },
        { text: "Up to 600 user messages", included: true, hasInfo: true },
        { text: "Team management, up to 100 users", included: true },
        { text: "SOC 2 type II", included: true }
      ],
      buttonText: "Install now",
      highlighted: true,
      footerText: "Need more messages?",
      footerLink: "See plans below."
    },
    {
      name: "Enterprise",
      subtitle: "ENTERPRISE", 
      description: "For enterprise teams with high volume, security, or support needs.",
      features: [
        { text: "Custom user pricing", included: true },
        { text: "Bespoke user message limit", included: true, hasInfo: true },
        { text: "Slack integration", included: true },
        { text: "Volume based annual discounts", included: true },
        { text: "SSO, OIDC, & SCIM support", included: true },
        { text: "SOC 2 & Security Reports", included: true }
      ],
      buttonText: "Contact sales"
    }
  ]

  return (
    <div className="w-full">
      <PricingComponent 
        tiers={pricingTiers}
      />
    </div>
  )
}

export default Demo
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


## Pricing Section 4

**Author:** @ui-layouts
**URL:** https://21st.dev/@ui-layouts/components/pricing-section-4

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
pricing-section-4.tsx
// Full source: https://21st.dev/@ui-layouts/components/pricing-section-4
// Install via: npx @21st-dev/magic add pricing-section-4
// Or copy the component code from the 21st.dev page above.


import Component from "@/components/ui/pricing-section-4";

export default function DemoOne() {
  return <div className="w-full"><Component /></div>;
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

