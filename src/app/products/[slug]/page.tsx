import { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import { getProduct, products } from "@/lib/products";

const accent = "#7c3aed";

interface PageProps {
  params: {
    slug: string;
  };
}

export function generateStaticParams() {
  return products.map((product) => ({ slug: product.slug }));
}

export function generateMetadata({ params }: PageProps): Metadata {
  const product = getProduct(params.slug);

  if (!product) {
    return { title: "Product Not Found" };
  }

  return {
    title: product.name,
    description: product.description,
  };
}

export default function ProductPage({ params }: PageProps) {
  const product = getProduct(params.slug);

  if (!product) {
    notFound();
  }

  return (
    <main className="mx-auto max-w-5xl px-4 py-12 sm:px-6">
      <Link href="/products" className="text-sm font-semibold" style={{ color: accent }}>
        ← Back to products
      </Link>

      <section className="mt-6 rounded-3xl bg-gradient-to-br from-violet-50 via-white to-purple-100 px-6 py-10 shadow-sm ring-1 ring-purple-100 sm:px-10">
        <p className="text-sm font-semibold uppercase tracking-[0.2em]" style={{ color: accent }}>
          ADHD Productivity Tool
        </p>
        <div className="mt-4 flex flex-col gap-4 sm:flex-row sm:items-start sm:justify-between">
          <div className="max-w-2xl">
            <h1 className="text-4xl font-bold tracking-tight text-slate-900">{product.name}</h1>
            <p className="mt-4 text-lg text-slate-700">{product.description}</p>
          </div>
          <div className="rounded-2xl px-5 py-4 text-white shadow-sm" style={{ backgroundColor: accent }}>
            <p className="text-sm uppercase tracking-[0.18em] text-purple-100">Price</p>
            <p className="mt-1 text-3xl font-bold">${product.price}</p>
          </div>
        </div>
      </section>

      <section className="mt-10 grid gap-8 lg:grid-cols-[1.3fr_0.7fr]">
        <div className="rounded-3xl border border-slate-200 bg-white p-8 shadow-sm">
          <h2 className="text-2xl font-semibold text-slate-900">What&apos;s included</h2>
          <ul className="mt-6 space-y-4">
            {product.features.map((feature) => (
              <li key={feature} className="flex items-start gap-3 text-slate-700">
                <span
                  className="mt-1 inline-flex h-6 w-6 flex-none items-center justify-center rounded-full text-sm font-bold text-white"
                  style={{ backgroundColor: accent }}
                >
                  ✓
                </span>
                <span>{feature}</span>
              </li>
            ))}
          </ul>
        </div>

        <aside className="rounded-3xl border border-purple-100 bg-violet-50 p-8">
          <h2 className="text-xl font-semibold text-slate-900">Designed for ADHD adults</h2>
          <p className="mt-4 text-slate-700">
            Short setup time, visual structure, and low-friction prompts make this easier to start and easier to keep
            using.
          </p>
          <Link
            href="/products"
            className="mt-6 inline-flex rounded-full px-5 py-3 text-sm font-semibold text-white transition-opacity hover:opacity-90"
            style={{ backgroundColor: accent }}
          >
            Browse more tools
          </Link>
        </aside>
      </section>
    </main>
  );
}
