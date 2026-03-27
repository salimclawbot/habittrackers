"use client";

import Link from "next/link";

export default function Header() {
  return (
    <header className="border-b border-indigo-100 bg-white/90 backdrop-blur">
      <div className="mx-auto flex max-w-6xl items-center justify-between px-4 py-4 sm:px-6">
        <Link href="/" className="text-xl font-bold text-indigo-800">Habit Tracker Spot</Link>
        <nav className="hidden gap-6 text-sm font-medium text-slate-700 md:flex">
          <Link href="/adhd-morning-routine" className="hover:text-indigo-700">Morning Routine</Link>
          <Link href="/adhd-focus-techniques" className="hover:text-indigo-700">Focus Tips</Link>
          <Link href="/adhd-daily-planner-guide" className="hover:text-indigo-700">Daily Planner</Link>
          <Link href="/about" className="hover:text-indigo-700">About</Link>
        </nav>
      </div>
    </header>
  );
}
