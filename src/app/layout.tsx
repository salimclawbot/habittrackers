import Script from 'next/script';
import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: { default: "Habit Tracker Spot — Free Printable & Digital Templates (2026)", template: "%s | Habit Tracker Spot" },
  description: "Build better habits with expert-reviewed trackers, planners and apps for 2026. ADHD-friendly systems and science-backed morning routines that actually work.",
  metadataBase: new URL("https://www.habittrackerspot.com"),
  alternates: { canonical: "https://habittrackerspot.com" },
  openGraph: {
    siteName: "Habit Tracker Spot",
    type: "website",
    title: "Habit Tracker Spot — Free Printable & Digital Templates (2026)",
    description: "Build better habits with expert-reviewed trackers, planners and apps for 2026. ADHD-friendly systems and morning routines backed by behavioural science.",
    url: "https://habittrackerspot.com",
    images: [{ url: "https://habittrackerspot.com/og-image.jpg", width: 1200, height: 630, alt: "Habit Tracker Spot — Free Printable & Digital Templates (2026)" }],
  },
  twitter: {
    card: "summary_large_image",
    title: "Habit Tracker Spot — Free Printable & Digital Templates (2026)",
    description: "Build better habits with expert-reviewed trackers, planners and apps for 2026. ADHD-friendly systems and morning routines backed by behavioural science.",
    images: ["https://habittrackerspot.com/og-image.jpg"],
  },
};

const websiteSchema = {
  "@context": "https://schema.org",
  "@type": "WebSite",
  "name": "Habit Tracker Spot",
  "url": "https://habittrackerspot.com",
  "description": "Habit tracker templates and productivity guides",
  "potentialAction": {
    "@type": "SearchAction",
    "target": "https://habittrackerspot.com/?s={{search_term_string}}",
    "query-input": "required name=search_term_string"
  }
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <head>
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{ __html: JSON.stringify(websiteSchema) }}
        />
      </head>
      <body className={`${inter.className} antialiased`}>
        <main >{children}</main>
        <Script
          src="https://www.googletagmanager.com/gtag/js?id=G-3TVXZ48DDG"
          strategy="afterInteractive"
        />
        <Script id="google-analytics" strategy="afterInteractive">
          {`
            window.dataLayer = window.dataLayer || [];
            function gtag(){dataLayer.push(arguments);}
            gtag('js', new Date());
            gtag('config', 'G-3TVXZ48DDG');
          `}
        </Script>
      </body>
    </html>
  );
}
