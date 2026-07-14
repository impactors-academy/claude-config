# 21st.dev — Hero Section Inspiration

80 hand-crafted hero components from the community. All React + Tailwind + shadcn/ui.

> Browse live previews at: https://21st.dev/community/components/s/heroes

---

## Aurora / Glow

### Glowy Waves Hero | Community Components
- **Author:** @moumensoliman
- **Slug:** `glowy-waves-hero-shadcnui`
- **URL:** https://21st.dev/@moumensoliman/components/glowy-waves-hero-shadcnui
- **Code:** https://cdn.21st.dev/larsen66/glowy-waves-hero-shadcnui/default/code.demo.1773289758692.tsx

```tsx
import { GlowyWavesHero } from "@/components/ui/glowy-waves-hero-shadcnui"
export default function Demo() {
  return (
    <div className="flex min-h-screen items-center justify-center bg-background p-8">
      <GlowyWavesHero />
    </div>
  )
}
```

---

### Aurora Hero bg | Community Components
- **Author:** @dhiluxui
- **Slug:** `aurora-hero-bg-3`
- **URL:** https://21st.dev/@dhiluxui/components/aurora-hero-bg-3
- **Code:** https://cdn.21st.dev/dhileepkumargm/aurora-hero-bg-3/default/code.demo.1760434672634.tsx

```tsx
import { RainbowHero } from "@/components/ui/aurora-hero-bg-3";
export default function AuroraHeroDemo() {
  return (
    <RainbowHero
      title="Transform Your Vision"
      description="Create stunning digital experiences with modern design and smooth animations"
      primaryAction={{
        label: "Get Started",
```

---

### PulseFit hero | Community Components
- **Author:** @dhiluxui
- **Slug:** `pulse-fit-hero`
- **URL:** https://21st.dev/@dhiluxui/components/pulse-fit-hero
- **Code:** https://cdn.21st.dev/dhileepkumargm/pulse-fit-hero/default/code.demo.1760255122322.tsx

```tsx
import { PulseFitHero } from "@/components/ui/pulse-fit-hero";
export default function PulseFitHeroDemo() {
  return (
    <PulseFitHero
      logo="PulseFit"
      navigation={[
        { label: "Features", onClick: () => console.log("Features") },
        { label: "Programs", hasDropdown: true, onClick: () => console.log("Programs") },
```

---

### Aurora Hero bg | Community Components
- **Author:** @dhiluxui
- **Slug:** `aurora-hero-bg-2`
- **URL:** https://21st.dev/@dhiluxui/components/aurora-hero-bg-2
- **Code:** https://cdn.21st.dev/dhileepkumargm/aurora-hero-bg-2/default/code.demo.1760253042005.tsx

```tsx
import { OceanHero } from "@/components/ui/aurora-hero-bg-2";
export default function AuroraHeroDemo() {
  return (
    <OceanHero
      title="Transform Your Vision"
      description="Create stunning digital experiences with modern design and smooth animations"
      primaryAction={{
        label: "Get Started",
```

---

### Aurora Hero bg | Community Components
- **Author:** @dhiluxui
- **Slug:** `aurora-hero-bg-1`
- **URL:** https://21st.dev/@dhiluxui/components/aurora-hero-bg-1
- **Code:** https://cdn.21st.dev/dhileepkumargm/aurora-hero-bg-1/default/code.demo.1760252956586.tsx

```tsx
import { SunsetHero } from "@/components/ui/aurora-hero-bg-1";
export default function AuroraHeroDemo() {
  return (
    <SunsetHero
      title="Transform Your Vision"
      description="Create stunning digital experiences with modern design and smooth animations"
      primaryAction={{
        label: "Get Started",
```

---

### Aurora Hero bg | Community Components
- **Author:** @dhiluxui
- **Slug:** `aurora-hero-bg`
- **URL:** https://21st.dev/@dhiluxui/components/aurora-hero-bg
- **Code:** https://cdn.21st.dev/dhileepkumargm/aurora-hero-bg/default/code.demo.1759933614605.tsx

```tsx
import { AuroraHero } from "@/components/ui/aurora-hero-bg";
export default function AuroraHeroDemo() {
  return (
    <AuroraHero
      title="Transform Your Vision"
      description="Create stunning digital experiences with modern design and smooth animations"
      primaryAction={{
        label: "Get Started",
```

---

### AuroraHero | Community Components
- **Author:** @dhiluxui
- **Slug:** `aurora-hero`
- **URL:** https://21st.dev/@dhiluxui/components/aurora-hero
- **Code:** https://cdn.21st.dev/dhileepkumargm/aurora-hero/default/code.demo.1759248426627.tsx

```tsx
import React, { useState, useEffect } from "react";
import AuroraHero from "@/components/ui/aurora-hero";
function DemoOne() {
  const [panelOpen, setPanelOpen] = useState(false);
  const [theme, setTheme] = useState<"dark" | "light">("dark");
  const [cfg, setCfg] = useState({
    ribbonCount: 4,
    speed: 0.006,
```

---

### Aurora voice Hero | Community Components
- **Author:** @dhiluxui
- **Slug:** `aurora-voice-hero`
- **URL:** https://21st.dev/@dhiluxui/components/aurora-voice-hero
- **Code:** https://cdn.21st.dev/dhileepkumargm/aurora-voice-hero/default/code.demo.1759247600271.tsx

```tsx
import AuroraHero from "@/components/ui/aurora-voice-hero";
export default function DemoOne() {
  return <AuroraHero  />;
}
```

---

### Aurora Section hero | Community Components
- **Author:** @dhiluxui
- **Slug:** `aurora-section-hero`
- **URL:** https://21st.dev/@dhiluxui/components/aurora-section-hero
- **Code:** https://cdn.21st.dev/dhileepkumargm/aurora-section-hero/default/code.demo.1759140631928.tsx

```tsx
import React from 'react'
import BackgroundScene from '@/components/ui/aurora-section-hero'
const App: React.FC = () => {
  return (
    <>
      <BackgroundScene beamCount={60} />
      <div className="content-wrapper">
        <header className="main-header">
```

---

## Glass / Blur

### Glass Video Hero | Community Components
- **Author:** @rahil1202
- **Slug:** `glass-video-hero`
- **URL:** https://21st.dev/@rahil1202/components/glass-video-hero
- **Code:** https://cdn.21st.dev/rahil1202/glass-video-hero/default/code.demo.1775887842155.tsx

```tsx
import { HeroSection } from "@/components/ui/glass-video-hero";
export default function DemoOne() {
  return <HeroSection />;
}
```

---

### Glassmorphism Trust Hero | Community Components
- **Author:** @easemize
- **Slug:** `glassmorphism-trust-hero`
- **URL:** https://21st.dev/@easemize/components/glassmorphism-trust-hero
- **Code:** https://cdn.21st.dev/easemize/glassmorphism-trust-hero/default/code.demo.1769356434569.tsx

```tsx
import React from 'react';
import HeroSection from '@/components/ui/glassmorphism-trust-hero';
export default function HeroDemo() {
  return (
    <div className="w-full h-screen overflow-y-auto bg-zinc-950">
      <HeroSection />
    </div>
  );
```

---

### GlassRefractionHero | Community Components
- **Author:** @dhiluxui
- **Slug:** `glass-refraction-hero`
- **URL:** https://21st.dev/@dhiluxui/components/glass-refraction-hero
- **Code:** https://cdn.21st.dev/dhileepkumargm/glass-refraction-hero/default/code.demo.1760254567388.tsx

```tsx
import { GlassRefractionHero } from "@/components/ui/glass-refraction-hero";
export default function GlassRefractionHeroDemo() {
  return (
    <GlassRefractionHero
      title="Glass Refraction Design"
      description="Experience the beauty of light refraction through glass with animated blue gradient blobs"
      primaryAction={{
        label: "Explore Now",
```

---

## Gradient / Mesh

### flow-gradient-heroSection | Community Components
- **Author:** @haik-kashiyani
- **Slug:** `flow-gradient-hero-section`
- **URL:** https://21st.dev/@haik-kashiyani/components/flow-gradient-hero-section
- **Code:** https://cdn.21st.dev/hardikkashiyani123456788/flow-gradient-hero-section/default/code.demo.1769358696285.tsx

```tsx
import { Component } from "@/components/ui/flow-gradient-hero-section";
export default function DemoOne() {
  return <Component />;
}
```

---

## 3D / Shader / WebGL

### Halide Topo Hero | Community Components
- **Author:** @shivendra9795kumar
- **Slug:** `halide-topo-hero`
- **URL:** https://21st.dev/@shivendra9795kumar/components/halide-topo-hero
- **Code:** https://cdn.21st.dev/shivendra9795kumar/halide-topo-hero/default/code.demo.1770239804676.tsx

```tsx
import React, { useEffect, useRef } from 'react';
const HalideLanding: React.FC = () => {
  const canvasRef = useRef<HTMLDivElement>(null);
  const layersRef = useRef<HTMLDivElement[]>([]);
  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    // Mouse Parallax Logic
```

---

### Animated Hero with WebGL Glitter | Community Components
- **Author:** @cinquinandy
- **Slug:** `animated-hero-with-web-gl-glitter`
- **URL:** https://21st.dev/@cinquinandy/components/animated-hero-with-web-gl-glitter
- **Code:** https://cdn.21st.dev/cinquinandy/animated-hero-with-web-gl-glitter/default/code.demo.1762441678672.tsx

```tsx
/**
 * WebGL Glitter Background Demo
 *
 * Showcases the WebGL glitter background effect.
 * Customize the speed and intensity of the sparkle animation.
 */
import { Component } from '@/components/ui/animated-hero-with-web-gl-glitter'
export default function DemoOne() {
```

---

### Shaders Hero Section | Community Components
- **Author:** @vaib215
- **Slug:** `shaders-hero-section`
- **URL:** https://21st.dev/@vaib215/components/shaders-hero-section
- **Code:** https://cdn.21st.dev/vaib215/shaders-hero-section/default/code.demo.1760818379697.tsx

```tsx
"use client"
import {Header, HeroContent, PulsingCircle, ShaderBackground} from "@/components/ui/shaders-hero-section"
export default function ShaderShowcase() {
  return (
    <ShaderBackground>
      <Header />
      <HeroContent />
      <PulsingCircle />
```

---

### PsychedelicVortexHero | Community Components
- **Author:** @dhiluxui
- **Slug:** `psychedelic-vortex-hero`
- **URL:** https://21st.dev/@dhiluxui/components/psychedelic-vortex-hero
- **Code:** https://cdn.21st.dev/dhileepkumargm/psychedelic-vortex-hero/default/code.demo.1760433575923.tsx

```tsx
import React from 'react';
import PsychedelicVortexHero from "@/components/ui/psychedelic-vortex-hero";
export default function PsychedelicVortexHeroDemo() {
  return (
    <div className="w-screen h-screen">
      <PsychedelicVortexHero/>
    </div>
  );
```

---

### Web3MediaHero | Community Components
- **Author:** @dhiluxui
- **Slug:** `web3media-hero`
- **URL:** https://21st.dev/@dhiluxui/components/web3media-hero
- **Code:** https://cdn.21st.dev/dhileepkumargm/web3media-hero/default/code.demo.1760257342701.tsx

```tsx
import { Web3MediaHero } from "@/components/ui/web3media-hero";
export default function Web3MediaHeroDemo() {
  return (
    <Web3MediaHero
      logo="Web3 Media"
      navigation={[
        { label: "Home", onClick: () => console.log("Home") },
        { label: "Gallery", onClick: () => console.log("Gallery") },
```

---

### Crypto hero | Community Components
- **Author:** @dhiluxui
- **Slug:** `crypto-hero`
- **URL:** https://21st.dev/@dhiluxui/components/crypto-hero
- **Code:** https://cdn.21st.dev/dhileepkumargm/crypto-hero/default/code.demo.1760257091939.tsx

```tsx
import VaultoryHero from "@/components/ui/crypto-hero";
export default function VaultoryHeroDemo() {
  return (
    <VaultoryHero
      logo={
        <div className="text-2xl font-bold text-white">Vaultory</div>
      }
      title="All-in-One Crypto Wallet for a"
```

---

### AnomalousMatterHero | Community Components
- **Author:** @dhiluxui
- **Slug:** `anomalous-matter-hero`
- **URL:** https://21st.dev/@dhiluxui/components/anomalous-matter-hero
- **Code:** https://cdn.21st.dev/dhileepkumargm/anomalous-matter-hero/default/code.demo.1759377025249.tsx

```tsx
import React from "react";
import { AnomalousMatterHero } from "@/components/ui/anomalous-matter-hero";
function App() {
  return (
    <AnomalousMatterHero
      title="Launch Sequence: Anomaly 12"
      subtitle="Energy dances along unseen frontiers."
      description="This demo shows how to override the default copy and integrate hero into a page layout."
```

---

### CyberpunkTerminalHero | Community Components
- **Author:** @dhiluxui
- **Slug:** `cyberpunk-terminal-hero`
- **URL:** https://21st.dev/@dhiluxui/components/cyberpunk-terminal-hero
- **Code:** https://cdn.21st.dev/dhileepkumargm/cyberpunk-terminal-hero/default/code.demo.1759378165783.tsx

```tsx
import React from "react";
import { CyberpunkTerminalHero } from "@/components/ui/cyberpunk-terminal-hero";
export default function CyberpunkTerminalHeroDemo() {
  return (
    <CyberpunkTerminalHero
      title="BOOT SEQUENCE: Welcome Aboard"
      subtitle={{ regular: "Enter the ", glitch: "Next Frontier" }}
      description="This demo overrides text and demonstrates theming with CSS variables."
```

---

### DataGridHero | Community Components
- **Author:** @dhiluxui
- **Slug:** `data-grid-hero`
- **URL:** https://21st.dev/@dhiluxui/components/data-grid-hero
- **Code:** https://cdn.21st.dev/dhileepkumargm/data-grid-hero/default/code.demo.1759246130283.tsx

```tsx
import React, { useState, useEffect, useCallback } from "react";
import DataGridHero from "@/components/ui/data-grid-hero";
export default function DemoOne() {
  const [cfg, setCfg] = useState({
    rows: 25,
    cols: 35,
    spacing: 4,
    duration: 5.0,
```

---

### Cybercore Section hero | Community Components
- **Author:** @dhiluxui
- **Slug:** `cybercore-section-hero`
- **URL:** https://21st.dev/@dhiluxui/components/cybercore-section-hero
- **Code:** https://cdn.21st.dev/dhileepkumargm/cybercore-section-hero/default/code.demo.1759141063173.tsx

```tsx
import React from 'react'
import CybercoreBackground from '@/components/ui/cybercore-section-hero'
const App: React.FC = () => (
  <>
    <CybercoreBackground beamCount={70} />
    <div className="content-wrapper">
      <header className="main-header">
        <div className="logo">CYBERCORE</div>
```

---

## Animated Text

### Hero Shutter Text | Community Components
- **Author:** @daiv09
- **Slug:** `hero-shutter-text`
- **URL:** https://21st.dev/@daiv09/components/hero-shutter-text
- **Code:** https://cdn.21st.dev/daiwiikharihar17147/hero-shutter-text/default/code.demo.1770201375306.tsx

```tsx
import HeroText from "@/components/ui/hero-shutter-text";
export default function DemoOne() {
  return (
    <main className="h-screen w-screen overflow-hidden bg-white dark:bg-zinc-950">
      <HeroText />
    </main>
  );
}
```

---

## Scroll / Parallax

### Hero Scrub | Community Components
- **Author:** @duthiljean
- **Slug:** `hero-scrub`
- **URL:** https://21st.dev/@duthiljean/components/hero-scrub
- **Code:** https://cdn.21st.dev/jean.duthil13/hero-scrub/default/code.demo.1776866303070.tsx

```tsx
import { HeroScrub } from "@/components/ui/hero-scrub";
export default function Demo() {
  return (
    <HeroScrub
      frameCount={300}
      frameUrl={(i) =>
        `https://raw.githubusercontent.com/duthiljean/ferrari-hero-demo/main/${String(i + 1).padStart(4, "0")}.webp`
      }
```

---

### Scroll Morph Hero | Community Components
- **Author:** @prashantsom75
- **Slug:** `scroll-morph-hero`
- **URL:** https://21st.dev/@prashantsom75/components/scroll-morph-hero
- **Code:** https://cdn.21st.dev/prashantsom75/scroll-morph-hero/default/code.demo.1765164297799.tsx

```tsx
"use client";
import IntroAnimation from "../components/ui/scroll-morph-hero";
export default function Demo() {
    return (
        <div className="w-full h-[800px] border rounded-lg overflow-hidden relative">
            <IntroAnimation />
        </div>
    );
```

---

### Scroll Hero Section | Community Components
- **Author:** @rahil1202
- **Slug:** `scroll-hero-section`
- **URL:** https://21st.dev/@rahil1202/components/scroll-hero-section
- **Code:** https://cdn.21st.dev/rahil1202/scroll-hero-section/default/code.demo.1759683737911.tsx

```tsx
import { WordHeroPage } from "@/components/ui/scroll-hero-section";
export default function DemoOne() {
  return <WordHeroPage
   items={['design.', 'prototype.', 'solve.', 'build.', 'develop.', 'cook.', 'ship.']}
      theme="system"
      animate
      hue={280}
      startVh={50}
```

---

### Layer Parallax Hero | Community Components
- **Author:** @rubenerik
- **Slug:** `layer-parallax-hero`
- **URL:** https://21st.dev/@rubenerik/components/layer-parallax-hero
- **Code:** https://cdn.21st.dev/erikvalencia1/layer-parallax-hero/default/code.demo.1759612080133.tsx

```tsx
import { LayeredParallaxHero } from "@/components/ui/layer-parallax-hero";
export default function DemoOne() {
  return <LayeredParallaxHero />;
}
```

---

## Minimal / Clean

### Hero - Personal Website | Community Components
- **Author:** @mara.stefana.ilie
- **Slug:** `hero-personal-website`
- **URL:** https://21st.dev/@mara.stefana.ilie/components/hero-personal-website
- **Code:** https://cdn.21st.dev/mara.stefana.ilie/hero-personal-website/default/code.demo.1783765993831.tsx

```tsx
import { AsciiArt } from "@/components/ui/hero-personal-website"
export default function AsciiArtDemo() {
  return (
    <div className="relative h-[440px] w-full overflow-hidden rounded-xl">
      <AsciiArt className="h-full w-full" />
    </div>
  )
}
```

---

### Waitlist Hero | Community Components
- **Author:** @thanh
- **Slug:** `waitlist-hero`
- **URL:** https://21st.dev/@thanh/components/waitlist-hero
- **Code:** https://cdn.21st.dev/minhxthanh/waitlist-hero/default/code.demo.1764083294693.tsx

```tsx
import { WaitlistHero } from "@/components/ui/waitlist-hero";
export default function DemoOne() {
  return <WaitlistHero />;
}
```

---

### Portfolio Hero | Community Components
- **Author:** @wisedev
- **Slug:** `portfolio-hero`
- **URL:** https://21st.dev/@wisedev/components/portfolio-hero
- **Code:** https://cdn.21st.dev/waleedkibhen/portfolio-hero/default/code.demo.1760684411020.tsx

```tsx
import React from "react";
import Component from "@/components/ui/portfolio-hero";
export default function Demo() {
  return (
    <>
      <link
        rel="stylesheet"
        href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@700&family=Antic&display=swap"
```

---

### Underline Hero Section | Community Components
- **Author:** @wisedev
- **Slug:** `underline-hero-section`
- **URL:** https://21st.dev/@wisedev/components/underline-hero-section
- **Code:** https://cdn.21st.dev/waleedkibhen/underline-hero-section/default/code.demo.1759825734513.tsx

```tsx
import React, { useState } from "react";
 import Component from "@/components/ui/underline-hero-section";
export default function Demo() {
  const [message, setMessage] = useState<string>("");
  const onSignIn = () => {
    setMessage("Sign In clicked");
    setTimeout(() => setMessage(""), 3000);
  };
```

---

## Particle / Noise

### Hero Dithering Card | Community Components
- **Author:** @shadway
- **Slug:** `hero-dithering-card`
- **URL:** https://21st.dev/@shadway/components/hero-dithering-card
- **Code:** https://cdn.21st.dev/moazamtrade/hero-dithering-card/default/code.demo.1769113686729.tsx

```tsx
import { CTASection } from "@/components/ui/hero-dithering-card";
export default function DemoOne() {
  return <CTASection />;
}
```

---

### particle effect for hero | Community Components
- **Author:** @avanishverma4
- **Slug:** `particle-effect-for-hero`
- **URL:** https://21st.dev/@avanishverma4/components/particle-effect-for-hero
- **Code:** https://cdn.21st.dev/avanishverma4/particle-effect-for-hero/default/code.demo.1765266057134.tsx

```tsx
import Component from "@/components/ui/particle-effect-for-hero";
export default function DemoOne() {
  return <Component />;
}
```

---

### Comet Hero | Community Components
- **Author:** @tonyzebastian
- **Slug:** `comet-hero`
- **URL:** https://21st.dev/@tonyzebastian/components/comet-hero
- **Code:** https://cdn.21st.dev/tonyzebastian/comet-hero/default/code.demo.1759509986723.tsx

```tsx
import React from 'react';
import CometHero from "@/components/ui/comet-hero";
import { Download } from 'lucide-react';
// Custom Button Component
interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  children: React.ReactNode;
}
const Button: React.FC<ButtonProps> = ({ children, className = '', ...props }) => {
```

---

## AI / Tech

### Robot Hero | Community Components
- **Author:** @uithefactory
- **Slug:** `robot-hero`
- **URL:** https://21st.dev/@uithefactory/components/robot-hero
- **Code:** https://cdn.21st.dev/alexperezcedeno/robot-hero/default/code.demo.1783341620795.tsx

```tsx
"use client";
import { RobotHero } from "@/components/ui/robot-hero";
export default function RobotHeroDemo() {
  const myUrl = "https://uithefactory.com/gallery";
  return (
    <div className="w-full min-h-screen bg-black overflow-hidden relative">
      <RobotHero 
        navItemsLeft={[
```

---

### Arc Preloader Hero | Community Components
- **Author:** @ruixenui
- **Slug:** `arc-preloader-hero`
- **URL:** https://21st.dev/@ruixenui/components/arc-preloader-hero
- **Code:** https://cdn.21st.dev/ruixen.ui/arc-preloader-hero/default/code.demo.1781853955195.tsx

```tsx
import { ArcRevealHero } from "@/components/ui/arc-preloader-hero";
export default function DemoOne() {
return (
    <ArcRevealHero>
      <div className="flex min-h-screen w-full flex-col items-center justify-center gap-5 px-6 text-center">
        <h1 className="max-w-2xl text-balance text-4xl font-semibold tracking-tight text-foreground sm:text-5xl md:text-6xl">
          First we listen. Then we ship.
        </h1>
```

---

### Pixel perfect Hero | Community Components
- **Author:** @easemize
- **Slug:** `pixel-perfect-hero`
- **URL:** https://21st.dev/@easemize/components/pixel-perfect-hero
- **Code:** https://cdn.21st.dev/easemize/pixel-perfect-hero/default/code.demo.1781185553155.tsx

```tsx
import React from "react";
import { PixelHero } from "@/components/ui/pixel-perfect-hero";
export default function Demo() {
  return (
    <div className="w-full min-h-screen bg-background">
      <PixelHero
        word1="Silent"
        word2="Precision."
```

---

### PrismaHero | Community Components
- **Author:** @rahil1202
- **Slug:** `prisma-hero`
- **URL:** https://21st.dev/@rahil1202/components/prisma-hero
- **Code:** https://cdn.21st.dev/rahil1202/prisma-hero/default/code.demo.1776747545948.tsx

```tsx
import { PrismaHero } from "@/components/ui/prisma-hero";
export default function DemoOne() {
  return <PrismaHero />;
}
```

---

### AI Image Generator Hero  | Community Components
- **Author:** @ravikatiyar
- **Slug:** `ai-image-generator-hero`
- **URL:** https://21st.dev/@ravikatiyar/components/ai-image-generator-hero
- **Code:** https://cdn.21st.dev/ravikatiyar162/ai-image-generator-hero/default/code.demo.1760853925745.tsx

```tsx
"use client"
import { ImageCarouselHero } from "@/components/ui/ai-image-generator-hero"
export default function ImageCarouselHeroDemo() {
  const demoImages = [
    {
      id: "1",
      src: "https://images.unsplash.com/photo-1684369176170-463e84248b70?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTl8fGFpfGVufDB8MXwwfHx8MA%3D%3D&auto=format&fit=crop&q=60&w=900",
      alt: "Mountain landscape",
```

---

### AetherHero | Community Components
- **Author:** @rahil1202
- **Slug:** `aether-hero`
- **URL:** https://21st.dev/@rahil1202/components/aether-hero
- **Code:** https://cdn.21st.dev/rahil1202/aether-hero/default/code.demo.1760174440789.tsx

```tsx
import { AetherHero } from "@/components/ui/aether-hero";
export default function DemoOne() {
  return (
    <AetherHero
      title="Build launch-grade UI in hours."
      subtitle="Animated WebGL backdrop, crisp type, and accessible CTAs. Drop it into any Next.js page."
      ctaLabel="Explore Docs"
      ctaHref="#docs"
```

---

### AI Input Hero | Community Components
- **Author:** @erikx
- **Slug:** `ai-input-hero`
- **URL:** https://21st.dev/@erikx/components/ai-input-hero
- **Code:** https://cdn.21st.dev/aghasisahakyan1/ai-input-hero/default/code.demo.1759262464978.tsx

```tsx
import { HeroWave } from "@/components/ui/ai-input-hero";
export default function DemoOne() {
  return <HeroWave />;
}
```

---

### Tech Solutions Hero Section | Community Components
- **Author:** @dhiluxui
- **Slug:** `tech-solutions-hero-section`
- **URL:** https://21st.dev/@dhiluxui/components/tech-solutions-hero-section
- **Code:** https://cdn.21st.dev/dhileepkumargm/tech-solutions-hero-section/default/code.demo.1759148358120.tsx

```tsx
import React from 'react';
import HaosShowcase from '@/components/ui/tech-solutions-hero-section';
import { Component } from '@/components/ui/raycast-animated-blue-background';
export default function App() {
  const handleAction = () => console.log('Action icon clicked');
  return (
    <HaosShowcase
      bg={<Component />}
```

---

## Video / Media

### Cinematic landing Hero | Community Components
- **Author:** @easemize
- **Slug:** `cinematic-landing-hero`
- **URL:** https://21st.dev/@easemize/components/cinematic-landing-hero
- **Code:** https://cdn.21st.dev/easemize/cinematic-landing-hero/default/code.demo.1774169408294.tsx

```tsx
import { CinematicHero } from "@/components/ui/cinematic-landing-hero";
export default function CinematicHeroDemo() {
  return (
    <div className="overflow-x-hidden w-[100%] min-h-screen">
      <CinematicHero />
    </div>
  );
}
```

---

## Other

### Modern Landing Hero | Community Components
- **Author:** @mokshithcodez
- **Slug:** `modern-landing-hero`
- **URL:** https://21st.dev/@mokshithcodez/components/modern-landing-hero
- **Code:** https://cdn.21st.dev/mokshithcodez/modern-landing-hero/default/code.demo.1783617372063.tsx

```tsx
import { Component } from "@/components/ui/modern-landing-hero";
export default function DemoOne() {
  return <Component />;
}
```

---

### Hero Component | Community Components
- **Author:** @pulseawan
- **Slug:** `hero-component`
- **URL:** https://21st.dev/@pulseawan/components/hero-component
- **Code:** https://cdn.21st.dev/pulseawan/hero-component/default/code.demo.1782907528638.tsx

```tsx
import BrandingHero from "@/components/ui/hero-component";
export default function Demo() {
  return <BrandingHero />;
}
```

---

### Focus Hero | Community Components
- **Author:** @arunjdass
- **Slug:** `focus-hero`
- **URL:** https://21st.dev/@arunjdass/components/focus-hero
- **Code:** https://cdn.21st.dev/arunjdass/focus-hero/default/code.demo.1782151566139.tsx

```tsx
import React, { useEffect, useState } from "react";
import { motion, useMotionValue, useSpring, useMotionValueEvent } from "framer-motion";
interface ArrowData {
  id: string;
  x: number;
  y: number;
  initialAngle: number;
}
```

---

### Preview Switch Hero | Community Components
- **Author:** @ruixenui
- **Slug:** `preview-switch-hero`
- **URL:** https://21st.dev/@ruixenui/components/preview-switch-hero
- **Code:** https://cdn.21st.dev/ruixen.ui/preview-switch-hero/default/code.demo.1780070410938.tsx

```tsx
import { PreviewSwitchHero } from "@/components/ui/preview-switch-hero";
import {
  Battery,
  Boxes,
  Gem,
  Hexagon,
  Orbit,
  Signal,
```

---

### Flow Hero-1 | Community Components
- **Author:** @cnippet_dev
- **Slug:** `flow-hero-1`
- **URL:** https://21st.dev/@cnippet_dev/components/flow-hero-1
- **Code:** https://cdn.21st.dev/cnippet.dev/flow-hero-1/default/code.demo.1774869569009.tsx

```tsx
"use client";
import Autoplay from "embla-carousel-autoplay";
import gsap from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import { ArrowRight } from "lucide-react";
import Image from "next/image";
import { useCallback, useEffect, useRef, useState } from "react";
import { Button } from "@/components/ui/button";
```

---

### Davincho Hero-1 | Community Components
- **Author:** @cnippet_dev
- **Slug:** `davincho-hero-1`
- **URL:** https://21st.dev/@cnippet_dev/components/davincho-hero-1
- **Code:** https://cdn.21st.dev/cnippet.dev/davincho-hero-1/default/code.demo.1774291019712.tsx

```tsx
"use client";
import { motion, useScroll, useTransform } from "motion/react";
import Image from "next/image";
import { useRef } from "react";
export default function Hero() {
  const container = useRef();
  const { scrollYProgress } = useScroll({
    offset: ["start end", "end start"],
```

---

### Hero 3 | Community Components
- **Author:** @efferd
- **Slug:** `hero-3`
- **URL:** https://21st.dev/@efferd/components/hero-3
- **Code:** https://cdn.21st.dev/sshahaider/hero-3/default/code.demo.1774009232270.tsx

```tsx
import { HeroSection } from "@/components/ui/hero-3";
import { Header } from "@/components/ui/header-3"; // @efferd/header-3
export default function DemoOne() {
	return (
		<div className="flex w-full flex-col">
		<Header />
		  <main className="grow" >
			<HeroSection />
```

---

### Hero | Community Components
- **Author:** @Samurai-ai-api
- **Slug:** `hero`
- **URL:** https://21st.dev/@Samurai-ai-api/components/hero
- **Code:** https://cdn.21st.dev/sam344334/hero/default/code.demo.1773995251378.tsx

```tsx
import { Component } from "@/components/ui/hero";
export default function Page() {
  return (
    <div className="w-full h-full min-h-screen">
      <Component />
    </div>
  );
}
```

---

### Aero Hero-2 | Community Components
- **Author:** @cnippet_dev
- **Slug:** `aero-hero-2`
- **URL:** https://21st.dev/@cnippet_dev/components/aero-hero-2
- **Code:** https://cdn.21st.dev/cnippet.dev/aero-hero-2/default/code.demo.1773482131300.tsx

```tsx
import { ArrowUpRight } from "lucide-react";
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar";
import { Button } from "@/components/ui/button";
export default function Hero() {
  return (
    <section className="relative flex h-screen w-full items-end justify-center">
      <div
        className="absolute inset-0 h-full bg-cover"
```

---

### Aero Hero-3 | Community Components
- **Author:** @cnippet_dev
- **Slug:** `aero-hero-3`
- **URL:** https://21st.dev/@cnippet_dev/components/aero-hero-3
- **Code:** https://cdn.21st.dev/cnippet.dev/aero-hero-3/default/code.demo.1773257562627.tsx

```tsx
import { ArrowUpRight } from "lucide-react";
import { Button } from "@/components/ui/button";
export default function Hero() {
  return (
    <section className="relative flex h-screen w-full items-center justify-center">
      <div className="absolute inset-0 z-10 size-full">
        <div className="grid w-full grid-cols-12 divide-x divide-white/20">
          <div className="col-span-1 h-screen" />
```

---

### Hero Section | Community Components
- **Author:** @moumensoliman
- **Slug:** `hero-section-shadcnui`
- **URL:** https://21st.dev/@moumensoliman/components/hero-section-shadcnui
- **Code:** https://cdn.21st.dev/larsen66/hero-section-shadcnui/demos/default/code.demo.1773289749167.tsx

```tsx
import { HeroSection } from "@/components/ui/hero-section-shadcnui"
export default function Demo() {
  return (
    <div className="flex min-h-screen items-center justify-center bg-background p-8">
      <HeroSection />
    </div>
  )
}
```

---

### Hero Block | Community Components
- **Author:** @moumensoliman
- **Slug:** `hero-block-shadcnui`
- **URL:** https://21st.dev/@moumensoliman/components/hero-block-shadcnui
- **Code:** https://cdn.21st.dev/larsen66/hero-block-shadcnui/demos/default/code.demo.1773289680899.tsx

```tsx
import { HeroBlock } from "@/components/ui/hero-block-shadcnui"
export default function Demo() {
  return (
    <div className="flex min-h-screen items-center justify-center bg-background p-8">
      <HeroBlock />
    </div>
  )
}
```

---

### Aero Hero-1 | Community Components
- **Author:** @cnippet_dev
- **Slug:** `aero-hero-1`
- **URL:** https://21st.dev/@cnippet_dev/components/aero-hero-1
- **Code:** https://cdn.21st.dev/cnippet.dev/aero-hero-1/default/code.demo.1772825419229.tsx

```tsx
import { ArrowUpRight } from "lucide-react";
import Image from "next/image";
import { Avatar, AvatarFallback, AvatarImage } from "@/demos/ui/avatar";
import { Button } from "@/components/ui/button";
import { Marquee } from "@/demos/ui/marquee";
export default function Hero() {
  return (
    <section className="relative w-full overflow-hidden pt-0 text-black dark:bg-white">
```

---

### Vercep Hero-1 | Community Components
- **Author:** @cnippet_dev
- **Slug:** `hero`
- **URL:** https://21st.dev/@cnippet_dev/components/hero
- **Code:** https://cdn.21st.dev/cnippet.dev/hero/default/code.demo.1771564649859.tsx

```tsx
"use client";
import { ArrowRight } from "lucide-react";
import { Avatar, AvatarFallback, AvatarImage } from "@/demos/ui/avatar";
import { Button } from "@/demos/ui/button";
import { Marquee } from "@/demos/ui/marquee";
const teamAvatars = [
  {
    initials: "JD",
```

---

### Hero 1 | Community Components
- **Author:** @efferd
- **Slug:** `hero-1`
- **URL:** https://21st.dev/@efferd/components/hero-1
- **Code:** https://cdn.21st.dev/sshahaider/hero-1/default/code.demo.1770851081525.tsx

```tsx
import { HeroSection, LogosSection } from "@/components/ui/hero-1";
import { Header } from "@/components/ui/header-1";
export default function DemoOne() {
	return (
		<div className= "flex w-full flex-col" >
		<Header />
		< main className = "grow" >
			<HeroSection />
```

---

### Responsive Hero Banner | Community Components
- **Author:** @saifyxpro
- **Slug:** `responsive-hero-banner`
- **URL:** https://21st.dev/@saifyxpro/components/responsive-hero-banner
- **Code:** https://cdn.21st.dev/sensewood8/responsive-hero-banner/default/code.demo.1768644363826.tsx

```tsx
import React from 'react';
import ResponsiveHeroBanner from '../components/ui/responsive-hero-banner';
const HeroDemo = () => {
    return (
        <ResponsiveHeroBanner
            badgeLabel="New"
            badgeText="First Commercial Flight to Mars 2026"
            title="Journey Beyond Earth"
```

---

### Experience Hero | Community Components
- **Author:** @haik-kashiyani
- **Slug:** `experience-hero`
- **URL:** https://21st.dev/@haik-kashiyani/components/experience-hero
- **Code:** N/A

```tsx

```

---

### HeroGridSection | Community Components
- **Author:** @Abuhuraira
- **Slug:** `hero-grid-section`
- **URL:** https://21st.dev/@Abuhuraira/components/hero-grid-section
- **Code:** https://cdn.21st.dev/hurerag24/hero-grid-section/default/code.demo.1767456252680.tsx

```tsx
import { HeroGridSection } from "@/components/ui/hero-grid-section";
export default function DemoOne() {
  return <HeroGridSection />;
}
```

---

### Hero Button Expendable  | Community Components
- **Author:** @shadway
- **Slug:** `hero-button-expendable`
- **URL:** https://21st.dev/@shadway/components/hero-button-expendable
- **Code:** https://cdn.21st.dev/moazamtrade/hero-button-expendable/default/code.demo.1765526195036.tsx

```tsx
import Hero from "@/components/ui/hero-button-expendable";
export default function DemoOne() {
  return (
    <div className="h-full w-full">
    <Hero/>
    </div>
  );
}
```

---

### Hero Preview Walls | Community Components
- **Author:** @ruixenui
- **Slug:** `hero-preview-walls`
- **URL:** https://21st.dev/@ruixenui/components/hero-preview-walls
- **Code:** https://cdn.21st.dev/ruixen.ui/hero-preview-walls/default/code.demo.1760965497667.tsx

```tsx
import { HeroPreviewWalls } from "@/components/ui/hero-preview-walls";
export default function Page() {
  return (
    <main>
      <HeroPreviewWalls />
    </main>
  );
}
```

---

### Hero | Community Components
- **Author:** @ravikatiyar
- **Slug:** `hero-5`
- **URL:** https://21st.dev/@ravikatiyar/components/hero-5
- **Code:** https://cdn.21st.dev/ravikatiyar162/hero-5/default/code.demo.1760864964235.tsx

```tsx
import * as React from 'react';
import { EthicalHero } from '@/components/ui/hero-5'; // Adjust path as needed
// --- Demo Data ---
const heroData = {
  title: (
    <>
      Invest in companies
      <br />
```

---

### Vercel Hero | Community Components
- **Author:** @aliimam
- **Slug:** `vercel-hero`
- **URL:** https://21st.dev/@aliimam/components/vercel-hero
- **Code:** https://cdn.21st.dev/designali-in/vercel-hero/default/code.demo.1760627333213.tsx

```tsx
import { Hero } from "@/components/ui/vercel-hero";
export default function DemoOne() {
  return <Hero />;
}
```

---

### Hero-Section | Community Components
- **Author:** @n38693842
- **Slug:** `hero-section-1`
- **URL:** https://21st.dev/@n38693842/components/hero-section-1
- **Code:** https://cdn.21st.dev/n38693842/hero-section-1/default/code.demo.1760291009178.tsx

```tsx
import { HeroSection } from "@/components/ui/hero-section-1";
export default function DemoOne() {
  return <HeroSection />;
}
```

---

### Hero Section | Community Components
- **Author:** @lavikatiyar
- **Slug:** `hero-section`
- **URL:** https://21st.dev/@lavikatiyar/components/hero-section
- **Code:** https://cdn.21st.dev/lavikatiyar/hero-section/default/code.demo.1760260926492.tsx

```tsx
import React from 'react';
import { FinancialHero } from '@/components/ui/hero-section'; // Adjust the import path as needed
// Demo component to showcase the FinancialHero
const FinancialHeroDemo = () => {
  return (
    <div className="w-full bg-background">
      <FinancialHero
        title={
```

---

### FoxyHero | Community Components
- **Author:** @dhiluxui
- **Slug:** `foxy-hero`
- **URL:** https://21st.dev/@dhiluxui/components/foxy-hero
- **Code:** https://cdn.21st.dev/dhileepkumargm/foxy-hero/default/code.demo.1760254328034.tsx

```tsx
import { FoxyHero } from "@/components/ui/foxy-hero";
export default function FoxyHeroDemo() {
  return (
    <FoxyHero
      logo={{
        icon: (
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
            <path
```

---

### FoxifyHero | Community Components
- **Author:** @dhiluxui
- **Slug:** `foxify-hero`
- **URL:** https://21st.dev/@dhiluxui/components/foxify-hero
- **Code:** https://cdn.21st.dev/dhileepkumargm/foxify-hero/default/code.demo.1760254231741.tsx

```tsx
import { FoxifyHero } from "@/components/ui/foxify-hero";
export default function FoxifyHeroDemo() {
  return (
    <FoxifyHero
      logo={{ initial: "F", text: "oxify" }}
      navigation={[
        { label: "Features", hasDropdown: true, onClick: () => console.log("Features") },
        { label: "Pricing", onClick: () => console.log("Pricing") },
```

---

### Hero Section | Community Components
- **Author:** @ravikatiyar
- **Slug:** `hero-section-9`
- **URL:** https://21st.dev/@ravikatiyar/components/hero-section-9
- **Code:** https://cdn.21st.dev/ravikatiyar162/hero-section-9/default/code.demo.1760172786727.tsx

```tsx
import HeroSection from '@/components/ui/hero-section-9'; // Adjust the import path as needed
import { Users, Briefcase, Link as LinkIcon } from 'lucide-react';
const HeroSectionDemo = () => {
  // Sample data to be passed as props
  const heroData = {
    title: (
      <>
        A new way to learn <br /> & get knowledge
```

---

### Hero 01 | Community Components
- **Author:** @aliimam
- **Slug:** `hero-01`
- **URL:** https://21st.dev/@aliimam/components/hero-01
- **Code:** https://cdn.21st.dev/designali-in/hero-01/default/code.demo.1760022303685.tsx

```tsx
import { HeroSection01 } from "@/components/ui/hero-01";
export default function DemoOne() {
  return <HeroSection01 />;
}
```

---

### Hero 02 | Community Components
- **Author:** @aliimam
- **Slug:** `hero-02`
- **URL:** https://21st.dev/@aliimam/components/hero-02
- **Code:** https://cdn.21st.dev/designali-in/hero-02/default/code.demo.1760021924615.tsx

```tsx
import { HeroSection02 } from "@/components/ui/hero-02";
export default function DemoOne() {
  return <HeroSection02 />;
}
```

---

### Hero 03 | Community Components
- **Author:** @aliimam
- **Slug:** `hero-03`
- **URL:** https://21st.dev/@aliimam/components/hero-03
- **Code:** https://cdn.21st.dev/designali-in/hero-03/default/code.demo.1760021284525.tsx

```tsx
import { HeroSection03 } from "@/components/ui/hero-03";
export default function DemoOne() {
  return <HeroSection03 />;
}
```

---

### Hero 04 | Community Components
- **Author:** @aliimam
- **Slug:** `hero-04`
- **URL:** https://21st.dev/@aliimam/components/hero-04
- **Code:** https://cdn.21st.dev/designali-in/hero-04/default/code.demo.1760021092785.tsx

```tsx
import { HeroSection04 } from "@/components/ui/hero-04";
export default function DemoOne() {
  return <HeroSection04 />;
}
```

---

### Hero Section | Community Components
- **Author:** @ravikatiyar
- **Slug:** `hero-section-7`
- **URL:** https://21st.dev/@ravikatiyar/components/hero-section-7
- **Code:** https://cdn.21st.dev/ravikatiyar162/hero-section-7/default/code.demo.1759479221395.tsx

```tsx
import { FloatingFoodHero } from '@/components/ui/hero-section-7'; // Adjust the import path
export default function FloatingFoodHeroDemo() {
  const heroImages = [
    {
      src: 'https://b.zmtcdn.com/data/o2_assets/110a09a9d81f0e5305041c1b507d0f391743058910.png',
      alt: 'A delicious cheeseburger',
      className: 'w-40 sm:w-56 md:w-64 lg:w-72 top-10 left-4 sm:left-10 md:top-20 md:left-20 animate-float',
    },
```

---

### Hero Section | Community Components
- **Author:** @ravikatiyar
- **Slug:** `hero-section-8`
- **URL:** https://21st.dev/@ravikatiyar/components/hero-section-8
- **Code:** https://cdn.21st.dev/ravikatiyar162/hero-section-8/default/code.demo.1759488919081.tsx

```tsx
import { FormBuilderHero } from "@/components/ui/hero-section-8"; // Adjust the import path
export default function HeroDemo() {
  return (
    <FormBuilderHero
      illustrationSrc="https://tally.so/images/demo/v2/roll-up-sleeves.png"
      illustrationAlt="A creative sketch of a person using a computer"
      title="Build stunning forms for free"
      description="It's as simple as one-two-three, and guess what? You don't even need an account to try it out!"
```

---

### Credit Card Hero | Community Components
- **Author:** @ruixenui
- **Slug:** `credit-card-hero`
- **URL:** https://21st.dev/@ruixenui/components/credit-card-hero
- **Code:** https://cdn.21st.dev/ruixen.ui/credit-card-hero/default/code.demo.1759045447239.tsx

```tsx
"use client";
import * as React from "react";
import { CreditCardHero } from "@/components/ui/credit-card-hero";
export default function CreditCardHeroDemo() {
  return (
    <div className="flex h-screen w-full items-center justify-center bg-muted/20 p-8">
      <CreditCardHero
        headline="The Future of Digital Banking"
```

---

### Hero Page | Community Components
- **Author:** @ruixenui
- **Slug:** `hero-page`
- **URL:** https://21st.dev/@ruixenui/components/hero-page
- **Code:** https://cdn.21st.dev/ruixen.ui/hero-page/default/code.demo.1758874356322.tsx

```tsx
import HeroPage from "@/components/ui/hero-page";
export default function DemoOne() {
  return <HeroPage />;
}
```

---

### HeroSection – Enterprise-Ready Landing Page Hero with Dual CTAs | Community Components
- **Author:** @uniquesonu
- **Slug:** `hero-section-enterprise-ready-landing-page-hero-with-dual-ctas`
- **URL:** https://21st.dev/@uniquesonu/components/hero-section-enterprise-ready-landing-page-hero-with-dual-ctas
- **Code:** https://cdn.21st.dev/uniquesonu/hero-section-enterprise-ready-landing-page-hero-with-dual-ctas/default/code.demo.1758876408461.tsx

```tsx
import ExampleUsage from "@/components/ui/hero-section-enterprise-ready-landing-page-hero-with-dual-ctas";
export default function DemoOne() {
  return <ExampleUsage />;
}
```

---

