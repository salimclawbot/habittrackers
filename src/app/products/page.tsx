import { Metadata } from "next";
import Link from "next/link";
import { products } from "@/lib/products";

const accent = "#7c3aed";

export const metadata: Metadata = {
  title: "ADHD Productivity Products",
  description: "Digital ADHD planners, focus trackers, and routines for adults.",
};

export default function ProductsPage() {
  return (
    <main className="mx-auto max-w-6xl px-4 py-12 sm:px-6">
      <section className="rounded-3xl bg-gradient-to-br from-violet-50 via-white to-purple-100 px-6 py-10 shadow-sm ring-1 ring-purple-100 sm:px-10">
        <p className="text-sm font-semibold uppercase tracking-[0.2em]" style={{ color: accent }}>
          Product Library
        </p>
        <h1 className="mt-3 text-4xl font-bold tracking-tight text-slate-900 sm:text-5xl">
          ADHD Productivity Systems for Adults
        </h1>
        <p className="mt-4 max-w-2xl text-lg text-slate-700">
          Printable and digital tools built to support focus, planning, and routines without adding more overwhelm.
        </p>
      </section>

      <section className="mt-10 grid gap-6 md:grid-cols-2 xl:grid-cols-4">
        {products.map((product) => (
          <Link
            key={product.slug}
            href={`/products/${product.slug}`}
            className="group flex h-full flex-col rounded-2xl border border-purple-100 bg-white p-6 shadow-sm transition-all hover:-translate-y-1 hover:border-purple-300 hover:shadow-lg"
          >
            <div className="flex items-start justify-between gap-4">
              <h2 className="text-xl font-semibold text-slate-900">{product.name}</h2>
              <span
                className="rounded-full px-3 py-1 text-sm font-semibold text-white"
                style={{ backgroundColor: accent }}
              >
                ${product.price}
              </span>
            </div>
            <p className="mt-4 flex-1 text-sm leading-6 text-slate-600">{product.description}</p>
            <span className="mt-5 text-sm font-semibold group-hover:translate-x-1 transition-transform" style={{ color: accent }}>
              View product →
            </span>
          </Link>
        ))}
      </section>
    </main>
  );
}
