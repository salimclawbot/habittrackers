"use client";

import { useEffect, useMemo, useState } from "react";

const LOOP_SECONDS = 30;
const SLIDE_SECONDS = 5;

const slides = [
  {
    title: "Walking Pad vs Treadmill",
    subtitle: "30-second comparison",
    icon: "VS",
    bgClass: "from-teal-500 via-cyan-500 to-sky-500",
  },
  {
    title: "Size: Walking pads are 40% smaller",
    subtitle: "Easier to fit under desks and furniture",
    icon: "SZ",
    bgClass: "from-teal-600 to-emerald-500",
  },
  {
    title: "Speed: Treadmills go up to 7.5 mph",
    subtitle: "Better for users who want jogging options",
    icon: "SPD",
    bgClass: "from-sky-600 to-blue-500",
  },
  {
    title: "Price: Walking pads start at $150",
    subtitle: "Low-cost entry point for desk walking",
    icon: "$",
    bgClass: "from-emerald-600 to-lime-500",
  },
  {
    title: "Noise: Walking pads under 50 dB",
    subtitle: "Quieter choice for calls and shared spaces",
    icon: "DB",
    bgClass: "from-cyan-600 to-teal-500",
  },
  {
    title: "Which is right for you? Read the full guide",
    subtitle: "Use the comparison table and buyer tips below",
    icon: "GO",
    bgClass: "from-teal-700 to-slate-700",
  },
];

export default function ComparisonVideo() {
  const [elapsed, setElapsed] = useState(0);
  const [isPlaying, setIsPlaying] = useState(true);

  useEffect(() => {
    if (!isPlaying) return;

    const timer = window.setInterval(() => {
      setElapsed((prev) => {
        const next = prev + 0.1;
        return next >= LOOP_SECONDS ? 0 : next;
      });
    }, 100);

    return () => window.clearInterval(timer);
  }, [isPlaying]);

  const slideIndex = Math.floor(elapsed / SLIDE_SECONDS) % slides.length;
  const progress = (elapsed / LOOP_SECONDS) * 100;
  const currentSlide = useMemo(() => slides[slideIndex], [slideIndex]);

  return (
    <section className="my-8 rounded-xl border border-slate-200 bg-slate-950 p-3 sm:p-4 shadow-lg">
      <div className="aspect-video w-full overflow-hidden rounded-lg border border-slate-800 bg-slate-900 relative">
        <div
          className={`absolute inset-0 bg-gradient-to-br ${currentSlide.bgClass} transition-colors duration-700`}
        />
        <div className="absolute inset-0 bg-[radial-gradient(circle_at_top_right,rgba(255,255,255,0.28),transparent_45%)]" />

        <div className="relative z-10 flex h-full flex-col items-center justify-center px-6 text-center text-white">
          <div className="mb-4 h-12 w-12 rounded-full bg-white/20 backdrop-blur flex items-center justify-center text-xl font-bold">
            {currentSlide.icon}
          </div>
          <p className="text-xl sm:text-3xl font-extrabold leading-tight max-w-2xl">{currentSlide.title}</p>
          <p className="mt-2 text-sm sm:text-base text-white/90">{currentSlide.subtitle}</p>
        </div>
      </div>

      <div className="mt-3 flex items-center gap-3">
        <button
          type="button"
          onClick={() => setIsPlaying((prev) => !prev)}
          className="rounded-md bg-teal-600 px-3 py-1.5 text-xs font-semibold text-white hover:bg-teal-500"
          aria-label={isPlaying ? "Pause comparison video" : "Play comparison video"}
        >
          {isPlaying ? "Pause" : "Play"}
        </button>

        <div className="h-2 flex-1 overflow-hidden rounded-full bg-slate-700" aria-hidden="true">
          <div
            className="h-full rounded-full bg-teal-400 transition-[width] duration-100 linear"
            style={{ width: `${progress}%` }}
          />
        </div>
        <span className="text-xs text-slate-300 tabular-nums">{Math.floor(elapsed)}s / 30s</span>
      </div>
    </section>
  );
}
