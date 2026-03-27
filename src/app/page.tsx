import { Metadata } from "next";
import Link from "next/link";
import { getAllSlugs, getArticle } from "@/lib/articles";
import { products } from "@/lib/products";

const accent = "#7c3aed";

export const metadata: Metadata = {
  title: "Best Habit Tracker Apps & Templates (2026)",
  description: "Build better habits with expert-reviewed trackers, planners and apps for 2026. ADHD-friendly systems and science-backed morning routines that actually work.",
  alternates: {
    canonical: "https://habittrackerspot.com",
  },
};

export default async function HomePage() {
  const articles = (await Promise.all(getAllSlugs().map((slug) => getArticle(slug)))).filter(Boolean);
      return (
    <main className="mx-auto max-w-6xl px-4 py-12 sm:px-6"><img src="/images/adhd/adhd-planner-hero.jpg" alt="ADHD productivity systems planners and focus tools 2026" style={{width:"100%",maxHeight:"380px",objectFit:"cover",borderRadius:"12px",marginBottom:"1.5rem"}} />
      <section className="rounded-3xl bg-gradient-to-br from-violet-50 via-white to-purple-100 px-6 py-10 shadow-sm ring-1 ring-purple-100 sm:px-10">
        <p className="text-sm font-semibold uppercase tracking-[0.2em]" style={{ color: accent }}>
          Adult ADHD Tools
        </p>
        <h1 className="mt-3 max-w-3xl text-4xl font-bold tracking-tight text-slate-900 sm:text-5xl">
          Best Habit Tracker Apps &amp; Templates (2026)
        </h1>
        <p className="mt-4 max-w-2xl text-lg text-slate-700 sm:text-xl">
          Build lasting habits with the right system. Expert-reviewed picks for every lifestyle.
        </p>
        <div className="mt-8">
          <Link
            href="/products"
            className="inline-flex items-center rounded-full px-5 py-3 text-sm font-semibold text-white transition-opacity hover:opacity-90"
            style={{ backgroundColor: accent }}
          >
            Explore Products
          </Link>
        </div>
      </section>

      <section className="mt-12">
        <div className="flex items-end justify-between gap-4">
          <div>
            <p className="text-sm font-semibold uppercase tracking-[0.2em]" style={{ color: accent }}>
              Products
            </p>
            <h2 className="mt-2 text-2xl font-semibold text-slate-900">Systems that reduce friction and overwhelm</h2>
          </div>
          <Link href="/products" className="text-sm font-semibold" style={{ color: accent }}>
            View all products
          </Link>
        </div>
        <div className="mt-6 grid gap-5 md:grid-cols-2 xl:grid-cols-4">
          {products.map((product) => (
            <Link
              key={product.slug}
              href={`/products/${product.slug}`}
              className="group rounded-2xl border border-purple-100 bg-white p-6 shadow-sm transition-all hover:-translate-y-1 hover:border-purple-300 hover:shadow-lg"
            >
              <p className="text-sm font-semibold uppercase tracking-[0.18em]" style={{ color: accent }}>
                ${product.price}
              </p>
              <h3 className="mt-3 text-xl font-semibold text-slate-900">{product.name}</h3>
              <p className="mt-3 text-sm leading-6 text-slate-600">{product.description}</p>
              <span className="mt-5 inline-flex text-sm font-semibold group-hover:translate-x-1 transition-transform" style={{ color: accent }}>
                View product →
              </span>
            </Link>
          ))}
        </div>
      </section>

      <section className="mt-16">
        <p className="text-sm font-semibold uppercase tracking-[0.2em]" style={{ color: accent }}>
          Articles
        </p>
        <h2 className="mt-2 text-2xl font-semibold text-slate-900">Free guides and printable inspiration</h2>
        <div className="mt-6 grid gap-6">
          {articles.map(
            (article) =>
              article && (
                <Link
                  key={article.slug}
                  href={`/${article.slug}`}
                  className="block rounded-2xl border border-slate-200 bg-white p-6 transition-all hover:border-purple-300 hover:shadow-md"
                >
                  <h3 className="text-xl font-semibold text-slate-900">{article.title}</h3>
                  <p className="mt-2 text-slate-600">{article.description}</p>
                  <span className="mt-4 inline-block text-sm font-medium" style={{ color: accent }}>
                    Read guide →
                  </span>
                </Link>
              ),
          )}
        </div>
      </section>
    
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{__html: JSON.stringify({
          "@context": "https://schema.org",
          "@type": "FAQPage",
          "mainEntity": [
            {"@type":"Question","name":"What is the best habit tracker app in 2026?","acceptedAnswer":{"@type":"Answer","text":"Habitica and Streaks are our top picks for 2026. Habitica gamifies habit building and works well for ADHD users, while Streaks is the best iOS option for simplicity."}},
            {"@type":"Question","name":"How long does it take to build a new habit?","acceptedAnswer":{"@type":"Answer","text":"Research from University College London found it takes an average of 66 days to form a new habit, though the range is 18 to 254 days depending on the person and habit complexity."}},
            {"@type":"Question","name":"Are paper or digital habit trackers better?","acceptedAnswer":{"@type":"Answer","text":"Both work well. Paper trackers have a tactile satisfaction factor that many people find motivating. Digital trackers offer reminders, streaks and analytics. Try both to see what works for you."}}
          ]
        })}}
      />
      </main>
  );
}
