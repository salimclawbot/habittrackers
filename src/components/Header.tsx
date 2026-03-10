"use client";

import Link from "next/link";

export default function Header() {
  return (
    <header className="border-b border-cyan-100 bg-white/90 backdrop-blur">
      <div className="mx-auto flex max-w-6xl items-center justify-between px-4 py-4 sm:px-6">
        <Link href="/" className="text-xl font-bold text-cyan-800">Massage Gun Guide</Link>
        <nav className="hidden gap-6 text-sm font-medium text-slate-700 md:flex">
          <Link href="/best-portable-monitor-asthma" className="hover:text-cyan-700">Asthma</Link>
          <Link href="/best-portable-monitor-mold" className="hover:text-cyan-700">Mold</Link>
          <Link href="/best-portable-monitor-baby-room" className="hover:text-cyan-700">Baby Room</Link>
          <Link href="/about" className="hover:text-cyan-700">About</Link>
        </nav>
      </div>
    </header>
  );
}
