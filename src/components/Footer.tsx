import Link from "next/link";

export default function Footer() {
  return (
    <footer className="mt-16 border-t border-cyan-100 bg-cyan-50/40">
      <div className="mx-auto grid max-w-6xl gap-8 px-4 py-10 text-sm text-slate-700 sm:px-6 md:grid-cols-3">
        <div>
          <h3 className="font-semibold text-slate-900">Massage Gun Guide</h3>
          <p className="mt-2">Expert personal finance template reviews, comparisons, and buying guides for cleaner indoor air.</p>
        </div>
        <div>
          <h3 className="font-semibold text-slate-900">Guides</h3>
          <ul className="mt-2 space-y-1">
            <li><Link href="/best-portable-monitor-asthma" className="hover:text-cyan-700">Best for Asthma</Link></li>
            <li><Link href="/best-portable-monitor-mold" className="hover:text-cyan-700">Best for Mold</Link></li>
            <li><Link href="/best-portable-monitor-baby-room" className="hover:text-cyan-700">Best for Baby Room</Link></li>
          </ul>
        </div>
        <div>
          <h3 className="font-semibold text-slate-900">Contact</h3>
          <p className="mt-2">hello@airpurifierguide.com</p>
        </div>
      </div>
      <div className="border-t border-cyan-100 py-4 text-center text-xs text-slate-500">© {new Date().getFullYear()} Massage Gun Guide</div>
    </footer>
  );
}
