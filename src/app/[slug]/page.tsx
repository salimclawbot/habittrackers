import { Metadata } from "next";
import { notFound } from "next/navigation";
import { getArticle, getAllSlugs } from "@/lib/articles";

interface PageProps { params: { slug: string } }

export async function generateStaticParams() {
  return getAllSlugs().map((slug) => ({ slug }));
}

export async function generateMetadata({ params }: PageProps): Promise<Metadata> {
  const article = await getArticle(params.slug);
  if (!article) return { title: "Not Found" };
  return {
    title: { absolute: article.title },
    description: article.description,
    alternates: { canonical: `https://habittrackerspot.com/${article.slug}` },
    openGraph: {
      title: article.title,
      description: article.description,
      url: `https://habittrackerspot.com/${article.slug}`,
      images: [{ url: `https://habittrackerspot.com/og-image.jpg`, width: 1200, height: 630, alt: article.title }],
      type: "article",
      siteName: "Habit Tracker Spot",
    },
  };
}

export default async function ArticlePage({ params }: PageProps) {
  const article = await getArticle(params.slug);
  if (!article) notFound();

  const articleSchema =
    article.articleSchema ??
    {
      "@context": "https://schema.org",
      "@type": "Article",
      headline: article.title,
      description: article.description,
      author: { "@type": "Person", name: article.author || "Habit Tracker Spot" },
      publisher: {
        "@type": "Organization",
        name: "Habit Tracker Spot",
        logo: { "@type": "ImageObject", url: "https://habittracker-site.vercel.app/icon.svg" },
      },
      datePublished: article.date,
      dateModified: article.dateModified,
      mainEntityOfPage: { "@type": "WebPage", "@id": `https://habittracker-site.vercel.app/${article.slug}` },
    };

  return (
    <article className="max-w-4xl mx-auto px-4 sm:px-6 py-10">
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(articleSchema) }} />
      {article.faqSchema && (
        <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(article.faqSchema) }} />
      )}
      <p className="text-xs font-semibold uppercase tracking-wide text-cyan-700">{article.category}</p>
      <h1 className="mt-2 text-3xl sm:text-4xl font-extrabold text-slate-900">{article.title}</h1>
      <p className="mt-3 text-slate-600">By Habit Tracker Spot · Updated {article.dateModified}</p>
      <div className="prose prose-slate max-w-none mt-8" dangerouslySetInnerHTML={{ __html: article.htmlContent }} />
    </article>
  );
}
