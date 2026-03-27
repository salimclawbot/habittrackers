import { MetadataRoute } from "next"; import { getAllSlugs } from "@/lib/articles";
export default function sitemap(): MetadataRoute.Sitemap {
  const b = "https://habittrackerspot.com";
  return [...["","about","contact","privacy","affiliate-disclosure"].map(p=>({url:`${b}/${p}`,lastModified:new Date("2026-03-23"),changeFrequency:"monthly" as const,priority:p===""?1:.5})),...getAllSlugs().map(s=>({url:`${b}/${s}`,lastModified:new Date("2026-03-23"),changeFrequency:"weekly" as const,priority:.8}))];
}
