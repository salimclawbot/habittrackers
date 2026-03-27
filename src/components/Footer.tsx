import Link from "next/link";

export default function Footer() {
  return (
    <footer className="mt-16 border-t border-indigo-100 bg-indigo-50/40">
      <div className="mx-auto grid max-w-6xl gap-8 px-4 py-10 text-sm text-slate-700 sm:px-6 md:grid-cols-3">
        <div>
          <h3 className="font-semibold text-slate-900">Habit Tracker Spot</h3>
          <p className="mt-2">Expert ADHD habit guides, morning routine tips, and focus strategies for building better habits.</p>
        </div>
        <div>
          <h3 className="font-semibold text-slate-900">Guides</h3>
          <ul className="mt-2 space-y-1">
            <li><Link href="/adhd-morning-routine" className="hover:text-indigo-700">Morning Routine</Link></li>
            <li><Link href="/adhd-focus-techniques" className="hover:text-indigo-700">Focus Tips</Link></li>
            <li><Link href="/adhd-daily-planner-guide" className="hover:text-indigo-700">Daily Planner</Link></li>
          </ul>
        </div>
        <div>
          <h3 className="font-semibold text-slate-900">Contact</h3>
          <p className="mt-2">hello@habittrackerspot.com</p>
          <ul className="mt-2 space-y-1">
            <li><Link href="/privacy-policy" className="hover:text-indigo-700">Privacy Policy</Link></li>
            <li><Link href="/affiliate-disclosure" className="hover:text-indigo-700">Affiliate Disclosure</Link></li>
            <li><Link href="/about" className="hover:text-indigo-700">About</Link></li>
          </ul>
        </div>
      </div>
      <div className="border-t border-indigo-100 py-4 text-center text-xs text-slate-500">© {new Date().getFullYear()} Habit Tracker Spot</div>
    </footer>
  );
}
