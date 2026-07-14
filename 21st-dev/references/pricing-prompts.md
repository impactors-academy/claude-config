# 21st.dev — Pricing Sections — Full Integration Prompts

30 components sorted by popularity.
Each section is a copy-paste ready prompt for Claude or any AI coding tool.

---

## Pricing Section

**Author:** @aymanch-03 | **Used:** 1,196x
**URL:** https://21st.dev/@aymanch-03/components/pricing-section
**Install:** `npx shadcn@latest add "https://21st.dev/r/aymanch-03/pricing-section?api_key=$API_KEY_21ST"`
**Description:** A comprehensive pricing section component that combines animated tabs and pricing cards. Originally built for Dub.co's pricing page.

Features
- Monthly/yearly frequency toggle with discount badge
- Animated tab selection
- Four-tier pricing layout
- Highlighted and popular tier states
- Grid background pattern with mask effect
- Dark mode support
- Responsive grid layout (1 column on mobile, 2 on tablet, 4 on desktop)

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
pricing-section.tsx
// Full source available at: https://21st.dev/@aymanch-03/components/pricing-section
// Or install via: npx shadcn@latest add "https://21st.dev/r/aymanch-03/pricing-section?api_key=$API_KEY_21ST"

import { PricingSection } from "@/components/blocks/pricing-section"

export const PAYMENT_FREQUENCIES = ["monthly", "yearly"]

export const TIERS = [
  {
    id: "individuals",
    name: "Individuals",
    price: {
      monthly: "Free",
      yearly: "Free",
    },
    description: "For your hobby projects",
    features: [
      "Free email alerts",
      "3-minute checks",
      "Automatic data enrichment",
      "10 monitors",
      "Up to 3 seats",
    ],
    cta: "Get started",
  },
  {
    id: "teams",
    name: "Teams",
    price: {
      monthly: 90,
      yearly: 75,
    },
    description: "Great for small businesses",
    features: [
      "Unlimited phone calls",
      "30 second checks",
      "Single-user account",
      "20 monitors",
      "Up to 6 seats",
    ],
    cta: "Get started",
    popular: true,
  },
  {
    id: "organizations",
    name: "Organizations",
    price: {
      monthly: 120,
      yearly: 100,
    },
    description: "Great for large businesses",
    features: [
      "Unlimited phone calls",
      "15 second checks",
      "Single-user account",
      "50 monitors",
      "Up to 10 seats",
    ],
    cta: "Get started",
  },
  {
    id: "enterprise",
    name: "Enterprise",
    price: {
      monthly: "Custom",
      yearly: "Custom",
    },
    description: "For multiple teams",
    features: [
      "Everything in Organizations",
      "Up to 5 team members",
      "100 monitors",
      "15 status pages",
      "200+ integrations",
    ],
    cta: "Contact Us",
    highlighted: true,
  },
]

export function PricingSectionDemo() {
  return (
    <div className="relative flex justify-center items-center w-full mt-20 scale-90">
      <div className="absolute inset-0 -z-10">
        <div className="h-full w-full bg-[linear-gradient(to_right,#4f4f4f2e_1px,transparent_1px),linear-gradient(to_bottom,#4f4f4f2e_1px,transparent_1px)] bg-[size:35px_35px] opacity-30 [mask-image:radial-gradient(ellipse_80%_50%_at_50%_0%,#000_70%,transparent_110%)]" />
      </div>
        <PricingSection
          title="Simple Pricing"
          subtitle="Choose the best plan for your needs"
          frequencies={PAYMENT_FREQUENCIES}
          tiers={TIERS}
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


## Pricing Section

**Author:** @uilayout.contact | **Used:** 699x
**URL:** https://21st.dev/@uilayout.contact/components/pricing-section-4
**Install:** `npx shadcn@latest add "https://21st.dev/r/uilayout.contact/pricing-section-4?api_key=$API_KEY_21ST"`
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
pricing-section-4.tsx
// Full source available at: https://21st.dev/@uilayout.contact/components/pricing-section-4
// Or install via: npx shadcn@latest add "https://21st.dev/r/uilayout.contact/pricing-section-4?api_key=$API_KEY_21ST"


import Component from "@/components/ui/pricing-section-4";

export default function DemoOne() {
  return <div className="w-full"><Component /></div>;
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


## Pricing

**Author:** @sshahaider | **Used:** 411x
**URL:** https://21st.dev/@sshahaider/components/pricing
**Install:** `npx shadcn@latest add "https://21st.dev/r/sshahaider/pricing?api_key=$API_KEY_21ST"`
**Description:** a dynamic, responsive pricing table with animated monthly/yearly toggle, tooltips for feature descriptions, and an optional highlight effect for popular plans. Each card displays plan info, price, and a CTA button, making it perfect for showcasing product tiers in a modern SaaS landing page.


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
// Full source available at: https://21st.dev/@sshahaider/components/pricing
// Or install via: npx shadcn@latest add "https://21st.dev/r/sshahaider/pricing?api_key=$API_KEY_21ST"

import React from 'react';
import { PricingSection } from '@/components/ui/pricing';

export default function Demo() {
	return (
		<div className="flex min-h-screen items-center justify-center py-12">
			<PricingSection
				plans={PLANS}
				heading="Plans that Scale with You"
				description="Whether you're just starting out or growing fast, our flexible pricing has you covered — with no hidden costs."
			/>
		</div>
	);
}

const PLANS = [
	{
		id: 'basic',
		name: 'Basic',
		info: 'For most individuals',
		price: {
			monthly: 7,
			yearly: Math.round(7 * 12 * (1 - 0.12)),
		},
		features: [
			{ text: 'Up to 3 Blog posts', limit: '100 tags' },
			{ text: 'Up to 3 Transcriptions' },
			{ text: 'Up to 3 Posts stored' },
			{
				text: 'Markdown support',
				tooltip: 'Export content in Markdown format',
			},
			{
				text: 'Community support',
				tooltip: 'Get answers your questions on discord',
			},
			{
				text: 'AI powered suggestions',
				tooltip: 'Get up to 100 AI powered suggestions',
			},
		],
		btn: {
			text: 'Start Your Free Trial',
			href: '#',
		},
	},
	{
		highlighted: true,
		id: 'pro',
		name: 'Pro',
		info: 'For small businesses',
		price: {
			monthly: 17.99,
			yearly: Math.round(17.99 * 12 * (1 - 0.12)),
		},
		features: [
			{ text: 'Up to 500 Blog Posts', limit: '500 tags' },
			{ text: 'Up to 500 Transcriptions' },
			{ text: 'Up to 500 Posts stored' },
			{
				text: 'Unlimited Markdown support',
				tooltip: 'Export content in Markdown format',
			},
			{ text: 'SEO optimization tools' },
			{ text: 'Priority support', tooltip: 'Get 24/7 chat support' },
			{
				text: 'AI powered suggestions',
				tooltip: 'Get up to 500 AI powered suggestions',
			},
		],
		btn: {
			text: 'Get started',
			href: '#',
		},
	},
	{
		name: 'Business',
		info: 'For large organizations',
		price: {
			monthly: 69.99,
			yearly: Math.round(49.99 * 12 * (1 - 0.12)),
		},
		features: [
			{ text: 'Unlimited Blog Posts' },
			{ text: 'Unlimited Transcriptions' },
			{ text: 'Unlimited Posts stored' },
			{ text: 'Unlimited Markdown support' },
			{
				text: 'SEO optimization tools',
				tooltip: 'Advanced SEO optimization tools',
			},
			{ text: 'Priority support', tooltip: 'Get 24/7 chat support' },
			{
				text: 'AI powered suggestions',
				tooltip: 'Get up to 500 AI powered suggestions',
			},
		],
		btn: {
			text: 'Contact team',
			href: '#',
		},
	},
];

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


## Single Pricing Card

**Author:** @sshahaider | **Used:** 318x
**URL:** https://21st.dev/@sshahaider/components/single-pricing-card-1
**Install:** `npx shadcn@latest add "https://21st.dev/r/sshahaider/single-pricing-card-1?api_key=$API_KEY_21ST"`
**Description:** A modern, responsive single-plan pricing section built for SaaS apps. Easy to customize and integrate into any project.

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
single-pricing-card-1.tsx
// Full source available at: https://21st.dev/@sshahaider/components/single-pricing-card-1
// Or install via: npx shadcn@latest add "https://21st.dev/r/sshahaider/single-pricing-card-1?api_key=$API_KEY_21ST"

import { Pricing } from "@/components/ui/single-pricing-card-1";

export default function DemoOne() {
	return <Pricing />;
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


## Pricing Card

**Author:** @sshahaider | **Used:** 294x
**URL:** https://21st.dev/@sshahaider/components/pricing-card
**Install:** `npx shadcn@latest add "https://21st.dev/r/sshahaider/pricing-card?api_key=$API_KEY_21ST"`
**Description:** A sleek, component-based Card system with glass effects, pricing layouts, and flexible sections like header, body, and list items.
Perfect for modern SaaS pricing tables, feature lists, or product showcases with consistent, stylish UI.

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
pricing-card.tsx
// Full source available at: https://21st.dev/@sshahaider/components/pricing-card
// Or install via: npx shadcn@latest add "https://21st.dev/r/sshahaider/pricing-card?api_key=$API_KEY_21ST"

'use client';

import { cn } from '@/lib/utils';
import { Button } from '@/components/ui/button';
import * as PricingCard from '@/components/ui/pricing-card';
import {
	CheckCircle2,
	XCircleIcon,
	Users,
} from 'lucide-react';


function Default() {
	const handleClick = (plan: string) => {
		alert(`Selected ${plan} plan!`);
	};

	const features = [
		'Up to 3 projects',
		'Basic templates',
		'Community support',
		'1GB storage',
	];

	const lockedFeatures = [
		'Unlimited projects',
		'Premium templates',
		'Priority support',
	];

	return (
		<PricingCard.Card>
			<PricingCard.Header>
				<PricingCard.Plan>
					<PricingCard.PlanName>
						<Users aria-hidden="true" />
						<span className="text-muted-foreground">Starter</span>
					</PricingCard.PlanName>
					<PricingCard.Badge>For Individuals</PricingCard.Badge>
				</PricingCard.Plan>
				<PricingCard.Price>
					<PricingCard.MainPrice>$10</PricingCard.MainPrice>
					<PricingCard.Period>/ month</PricingCard.Period>
					<PricingCard.OriginalPrice className="ml-auto">
						$12
					</PricingCard.OriginalPrice>
				</PricingCard.Price>
				<Button
					className={cn(
						'w-full font-semibold text-white',
						'bg-gradient-to-b from-orange-500 to-orange-600 shadow-[0_10px_25px_rgba(255,115,0,0.3)]',
					)}
					onClick={() => handleClick('Starter')}
				>
					Get Started
				</Button>
			</PricingCard.Header>
			<PricingCard.Body>
				<PricingCard.List>
					{features.map((item) => (
						<PricingCard.ListItem>
							<span className="mt-0.5">
								<CheckCircle2
									className="h-4 w-4 text-green-500"
									aria-hidden="true"
								/>
							</span>
							<span>{item}</span>
						</PricingCard.ListItem>
					))}
				</PricingCard.List>
				<PricingCard.Separator>Pro features</PricingCard.Separator>
				<PricingCard.List>
					{lockedFeatures.map((item) => (
						<PricingCard.ListItem className="opacity-75">
							<span className="mt-0.5">
								<XCircleIcon
									className="text-destructive h-4 w-4"
									aria-hidden="true"
								/>
							</span>
							<span>{item}</span>
						</PricingCard.ListItem>
					))}
				</PricingCard.List>
			</PricingCard.Body>
		</PricingCard.Card>
	);
}


export default function Page() {
	return (
		<main
			className={cn(
				'relative min-h-svh w-full overflow-hidden',
				'flex items-center justify-center p-4',
			)}
		>
    
      {/* Subtle dotted grid */}
			<div
				aria-hidden="true"
				className="pointer-events-none absolute inset-0"
				style={{
					backgroundImage:
						'radial-gradient(rgba(255,255,255,0.08) 0.8px, transparent 0.8px)',
					backgroundSize: '14px 14px',
					maskImage:
						'radial-gradient( circle at 50% 10%, rgba(0,0,0,1), rgba(0,0,0,0.2) 40%, rgba(0,0,0,0) 70% )',
				}}
			/>

			{/* Radial spotlight */}
			<div
				aria-hidden="true"
				className={cn(
					'pointer-events-none absolute -top-1/2 left-1/2 h-[120vmin] w-[120vmin] -translate-x-1/2 rounded-full',
					'bg-[radial-gradient(ellipse_at_center,--theme(--color-foreground/.1),transparent_50%)]',
					'blur-[30px]',
				)}
			/>
			<Default />
		</main>
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


## Pricing Section

**Author:** @uilayout.contact | **Used:** 249x
**URL:** https://21st.dev/@uilayout.contact/components/pricing-section
**Install:** `npx shadcn@latest add "https://21st.dev/r/uilayout.contact/pricing-section?api_key=$API_KEY_21ST"`
**Description:** Professional pricing table components featuring subscription plans, pricing tiers, feature comparisons, and conversion-optimized layouts designed to showcase value and drive purchases

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
pricing-section.tsx
// Full source available at: https://21st.dev/@uilayout.contact/components/pricing-section
// Or install via: npx shadcn@latest add "https://21st.dev/r/uilayout.contact/pricing-section?api_key=$API_KEY_21ST"

import  PricingSection  from "@/components/ui/pricing-section";


export default function DemoOne() {
  return <PricingSection />;
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


## Pricing

**Author:** @ravikatiyar162 | **Used:** 186x
**URL:** https://21st.dev/@ravikatiyar162/components/pricing
**Install:** `npx shadcn@latest add "https://21st.dev/r/ravikatiyar162/pricing?api_key=$API_KEY_21ST"`
**Description:** A responsive, theme-adaptive pricing section with an interactive starfield background and a toggle for monthly/annual plans.
Animated pricing cards with Framer Motion
Interactive monthly/yearly pricing toggle with confetti effect
Responsive design with mobile-first approach
Dynamic price updates with NumberFlow animations
Popular plan highlighting
Dark mode compatible

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
// Full source available at: https://21st.dev/@ravikatiyar162/components/pricing
// Or install via: npx shadcn@latest add "https://21st.dev/r/ravikatiyar162/pricing?api_key=$API_KEY_21ST"

import { PricingSection } from "@/components/ui/pricing";

// Demo data for the pricing plans
const demoPlans = [
  {
    name: "Starter",
    price: "50",
    yearlyPrice: "40",
    period: "month",
    features: [
      "Up to 10 projects",
      "Basic analytics",
      "48-hour support response time",
      "Limited API access",
      "Community support",
    ],
    description: "Perfect for individuals and small projects.",
    buttonText: "Start Free Trial",
    href: "#",
  },
  {
    name: "Professional",
    price: "99",
    yearlyPrice: "79",
    period: "month",
    features: [
      "Unlimited projects",
      "Advanced analytics",
      "24-hour support response time",
      "Full API access",
      "Priority support & Team collaboration",
    ],
    description: "Ideal for growing teams and businesses.",
    buttonText: "Get Started",
    href: "#",
    isPopular: true,
  },
  {
    name: "Enterprise",
    price: "299",
    yearlyPrice: "239",
    period: "month",
    features: [
      "Everything in Professional",
      "Custom solutions & integrations",
      "Dedicated account manager",
      "SSO Authentication & Advanced security",
    ],
    description: "For large organizations with specific needs.",
    buttonText: "Contact Sales",
    href: "#",
  },
];

// Demo component to showcase the PricingSection
export default function PricingSectionDemo() {
  return (
    <PricingSection
      plans={demoPlans}
      title="Find the Perfect Plan"
      description="Select the ideal package for your needs and start building today."
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


## Pricing Base

**Author:** @meschacirung | **Used:** 153x
**URL:** https://21st.dev/@meschacirung/components/pricing-base
**Install:** `npx shadcn@latest add "https://21st.dev/r/meschacirung/pricing-base?api_key=$API_KEY_21ST"`
**Description:** Here is Pricing compoenent

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
pricing-base.tsx
// Full source available at: https://21st.dev/@meschacirung/components/pricing-base
// Or install via: npx shadcn@latest add "https://21st.dev/r/meschacirung/pricing-base?api_key=$API_KEY_21ST"

import Pricing  from "@/components/ui/pricing-base";

export default function DemoOne() {
  return <Pricing />;
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


## Pricing Section

**Author:** @brijr | **Used:** 143x
**URL:** https://21st.dev/@brijr/components/pricing-section
**Install:** `npx shadcn@latest add "https://21st.dev/r/brijr/pricing-section?api_key=$API_KEY_21ST"`
**Description:** Here is Pricing Section component

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
pricing-section.tsx
// Full source available at: https://21st.dev/@brijr/components/pricing-section
// Or install via: npx shadcn@latest add "https://21st.dev/r/brijr/pricing-section?api_key=$API_KEY_21ST"

import Pricing from "@/components/ui/pricing-section";

export default function DemoOne() {
  return <Pricing />;
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


## Pricing Section

**Author:** @uilayout.contact | **Used:** 133x
**URL:** https://21st.dev/@uilayout.contact/components/pricing-section-3
**Install:** `npx shadcn@latest add "https://21st.dev/r/uilayout.contact/pricing-section-3?api_key=$API_KEY_21ST"`
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
pricing-section-3.tsx
// Full source available at: https://21st.dev/@uilayout.contact/components/pricing-section-3
// Or install via: npx shadcn@latest add "https://21st.dev/r/uilayout.contact/pricing-section-3?api_key=$API_KEY_21ST"


import Component from "@/components/ui/pricing-section-3";


export default function DemoOne() {
  return <div className="bg-white w-full">
  <Component />;
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


## Pricing Module

**Author:** @ruixen.ui | **Used:** 132x
**URL:** https://21st.dev/@ruixen.ui/components/pricing-module
**Install:** `npx shadcn@latest add "https://21st.dev/r/ruixen.ui/pricing-module?api_key=$API_KEY_21ST"`
**Description:** The PricingModule component is a fully configurable, responsive pricing section built with shadcn/ui, Lucide icons, and Tailwind CSS. It allows users to easily toggle between monthly and yearly billing, updating prices instantly for a seamless and dynamic experience. Designed for modern SaaS and product websites, it combines clarity, flexibility, and style — giving teams the ability to showcase multiple pricing tiers with detailed features and highlights.

Each pricing card is modular, allowing you to define the name, description, icon, pricing options, user limits, and features through props. The component also includes a recommended plan highlight, making it easy to emphasize the most popular or valuable tier. With clean transitions, adaptive theming for light and dark modes, and accessible UI components, the PricingModule serves as a polished and production-ready pricing layout for any digital platform.

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
pricing-module.tsx
// Full source available at: https://21st.dev/@ruixen.ui/components/pricing-module
// Or install via: npx shadcn@latest add "https://21st.dev/r/ruixen.ui/pricing-module?api_key=$API_KEY_21ST"

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


## Pricing Table

**Author:** @sshahaider | **Used:** 119x
**URL:** https://21st.dev/@sshahaider/components/pricing-table
**Install:** `npx shadcn@latest add "https://21st.dev/r/sshahaider/pricing-table?api_key=$API_KEY_21ST"`
**Description:** A sleek, component-based Card system with glass effects, pricing layouts, and flexible sections like header, body, and list items.
Perfect for modern SaaS pricing tables, feature lists, or product showcases with consistent, stylish UI.

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
pricing-table.tsx
// Full source available at: https://21st.dev/@sshahaider/components/pricing-table
// Or install via: npx shadcn@latest add "https://21st.dev/r/sshahaider/pricing-table?api_key=$API_KEY_21ST"

import React from 'react';
import { cn } from '@/lib/utils';
import { Shield, Users, Rocket } from 'lucide-react';
import {
	type FeatureItem,
	PricingTable,
	PricingTableBody,
	PricingTableHeader,
	PricingTableHead,
	PricingTableRow,
	PricingTableCell,
	PricingTablePlan,
} from '@/components/ui/pricing-table';
import { Button } from '@/components/ui/button';

export default function Page() {
	return (
		<div className="relative min-h-screen overflow-hidden px-4 py-20">
			<div
				className={cn(
					'absolute inset-0 z-[-10] size-full max-h-102 opacity-50',
					'[mask-image:radial-gradient(ellipse_at_center,var(--background),transparent)]',
				)}
				style={{
					backgroundImage:
						'radial-gradient(var(--foreground) 1px, transparent 1px)',
					backgroundSize: '32px 32px',
				}}
			/>
			<div className="relative mx-auto flex max-w-4xl flex-col items-center text-center">
				<h1
					className={cn(
						'text-3xl leading-tight font-bold text-balance sm:text-5xl',
					)}
				>
					{'Lighting Fast '}
					<i className="bg-gradient-to-r from-violet-500 via-violet-400 to-fuchsia-400 bg-clip-text font-serif font-extrabold text-transparent drop-shadow-[0_0_18px_rgba(167,139,250,0.55)]">
						{'Design Systems'}
					</i>
					<br />
					{'with '}
					<i className="bg-gradient-to-r from-violet-500 via-fuchsia-400 to-indigo-400 bg-clip-text font-serif font-extrabold text-transparent drop-shadow-[0_0_22px_rgba(167,139,250,0.75)]">
						{'Figr Identity'}
					</i>
				</h1>
				<p className="text-muted-foreground mt-4 max-w-2xl text-pretty">
					Deploy Consistent Designs Faster With Figr’s AI solutions.
				</p>
			</div>
			<Default />
		</div>
	);
}

function Default() {
	return (
		<PricingTable className="mx-auto my-5 max-w-5xl">
			<PricingTableHeader>
				<PricingTableRow>
					<th />
					<th className="p-1">
						<PricingTablePlan
							name="Solo"
							badge="For Freelancers"
							price="$29"
							compareAt="$59"
							icon={Shield}
						>
							<Button variant="outline" className="w-full rounded-lg" size="lg">
								Get Started
							</Button>
						</PricingTablePlan>
					</th>
					<th className="p-1">
						<PricingTablePlan
							name="teams"
							badge="For Growing Teams"
							price="$99"
							compareAt="$139"
							icon={Users}
							className="after:pointer-events-none after:absolute after:-inset-0.5 after:rounded-[inherit] after:bg-gradient-to-b after:from-violet-500/15 after:to-transparent after:blur-[2px]"
						>
							<Button
								className="w-full rounded-lg border-violet-700/60 bg-violet-600/80 text-white hover:bg-violet-600"
								size="lg"
							>
								Get Started
							</Button>
						</PricingTablePlan>
					</th>
					<th className="p-1">
						<PricingTablePlan
							name="scale"
							badge="For Large Teams"
							price="$239"
							compareAt="$299"
							icon={Rocket}
						>
							<Button variant="outline" className="w-full rounded-lg" size="lg">
								Get Started
							</Button>
						</PricingTablePlan>
					</th>
				</PricingTableRow>
			</PricingTableHeader>
			<PricingTableBody>
				{FEATURES.map((feature, index) => (
					<PricingTableRow key={index}>
						<PricingTableHead>{feature.label}</PricingTableHead>
						{feature.values.map((value, index) => (
							<PricingTableCell key={index}>{value}</PricingTableCell>
						))}
					</PricingTableRow>
				))}
			</PricingTableBody>
		</PricingTable>
	);
}

export const FEATURES: FeatureItem[] = [
	{
		label: 'Members',
		values: ['1', 'Up to 5', 'Unlimited'],
	},
	{
		label: 'Workspaces',
		values: ['1', 'Up to 3', 'Unlimited'],
	},
	{
		label: 'Guests',
		values: [true, true, true],
	},
	{
		label: 'Live collaboration',
		values: [false, true, true],
	},
	{
		label: 'Integrations of sub-brands',
		values: [false, true, true],
	},
	{
		label: 'Asset library',
		values: ['50 assets', '500 assets', 'Unlimited assets'],
	},
	{
		label: 'Export files',
		values: ['PNG only', 'PNG, PDF, MP4', 'PNG, PDF, MP4, JPEG'],
	},
	{
		label: 'Multiple dimensions',
		values: ['1:1', '1:1 and 9:16', 'All ratios & custom sizes'],
	},
	{
		label: 'Integrations & planning tools',
		values: [false, true, true],
	},
	{
		label: 'Dedicated account manager',
		values: [false, false, true],
	},
	{
		label: 'Access to help center',
		values: [true, true, true],
	},
	{
		label: 'Priority support',
		values: [false, 'Business hours', '24/7 priority'],
	},
	{
		label: 'Brand kit & custom colors',
		values: [false, true, true],
	},
	{
		label: 'Advanced analytics',
		values: [false, true, true],
	},
	{
		label: 'Storage space',
		values: ['1 GB', '20 GB', '1 TB'],
	},
	{
		label: 'User roles & permissions',
		values: [false, true, true],
	},
	{
		label: 'Custom integrations (API access)',
		values: [false, false, true],
	},
	{
		label: 'White-label option',
		values: [false, false, true],
	},
	{
		label: 'Training & onboarding sessions',
		values: [false, '1 session', 'Unlimited sessions'],
	},
];

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


## Pricing Cards

**Author:** @lyanchouss | **Used:** 117x
**URL:** https://21st.dev/@lyanchouss/components/pricing-cards
**Install:** `npx shadcn@latest add "https://21st.dev/r/lyanchouss/pricing-cards?api_key=$API_KEY_21ST"`
**Description:** Here is Pricing Cards components

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
pricing-cards.tsx
// Full source available at: https://21st.dev/@lyanchouss/components/pricing-cards
// Or install via: npx shadcn@latest add "https://21st.dev/r/lyanchouss/pricing-cards?api_key=$API_KEY_21ST"

import { Pricing2 } from "@/components/ui/pricing-cards";

export default function DemoOne() {
  return <Pricing2 />;
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


## Modern Pricing Table 

**Author:** @chowlol202 | **Used:** 102x
**URL:** https://21st.dev/@chowlol202/components/modern-pricing-table
**Install:** `npx shadcn@latest add "https://21st.dev/r/chowlol202/modern-pricing-table?api_key=$API_KEY_21ST"`
**Description:** A clean, responsive pricing section with a segmented Monthly/Yearly toggle, animated price transitions, feature comparison table, and full dark mode support. Built with Tailwind, ShadCN UI, and Framer Motion — perfect for modern SaaS apps.

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
modern-pricing-table.tsx
// Full source available at: https://21st.dev/@chowlol202/components/modern-pricing-table
// Or install via: npx shadcn@latest add "https://21st.dev/r/chowlol202/modern-pricing-table?api_key=$API_KEY_21ST"

import PricingTable, { Plan } from '@/components/ui/modern-pricing-table'

// Sample pricing data
const samplePlans: Plan[] = [
  {
    title: "Starter",
    price: {
      monthly: 9,
      yearly: 96
    },
    description: "Perfect for individuals and small projects",
    features: [
      "Up to 5 projects",
      "5GB storage",
      "Basic support",
      "Standard analytics",
      "API access"
    ],
    ctaText: "Get Started",
    ctaHref: "#",
    isFeatured: false
  },
  {
    title: "Professional",
    price: {
      monthly: 29,
      yearly: 312
    },
    description: "Ideal for growing teams and businesses",
    features: [
      "Up to 25 projects",
      "50GB storage",
      "Priority support",
      "Advanced analytics",
      "API access",
      "Team collaboration",
      "Custom integrations",
    ],
    ctaText: "Start Free Trial",
    ctaHref: "#",
    isFeatured: true
  },
  {
    title: "Enterprise",
    price: {
      monthly: 99,
      yearly: 1068
    },
    description: "For large organizations with complex needs",
    features: [
      "Unlimited projects",
      "500GB storage",
      "24/7 dedicated support",
      "Advanced analytics",
      "API access",
      "Team collaboration",
      "Custom integrations",
      "Advanced security",
      "SSO authentication",
    ],
    ctaText: "Contact Sales",
    ctaHref: "#",
    isFeatured: false
  }
]

export default function Home() {
  return (
    <div className="min-h-screen bg-white dark:bg-neutral-950 p-4">
      <div className="w-full max-w-7xl mx-auto">
        
        {/* Pricing Table Component */}
        <PricingTable plans={samplePlans} />
      </div>
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

