import type { Metadata } from "next"; import { Inter } from "next/font/google"; import "./globals.css";
const inter = Inter({ subsets: ["latin"] });
export const metadata: Metadata = {
  title: { default: "Habit Tracker Templates — Free Printable & Digital (2026)", template: "%s | Habit Tracker Templates" },
  description: "Free habit tracker templates for 2026: printable monthly habit trackers, daily routines, Google Sheets and Notion templates to build any habit in 30 days.",
  metadataBase: new URL("https://habittrackers.com"),
  openGraph: { siteName: "Habit Tracker Templates", type: "website" },
};
export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (<html lang="en"><body className={inter.className}>{children}</body></html>);
}
