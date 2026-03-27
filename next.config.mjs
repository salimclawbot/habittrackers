/** @type {import('next').NextConfig} */
const nextConfig = {
  images: {
    remotePatterns: [
      {
        protocol: "https",
        hostname: "m.media-amazon.com",
        pathname: "/images/**",
      },
    ],
  },
  async redirects() {
    return [
      // DUPLICATE URL FIX (2026-03-23): 301 redirect old slug → canonical 2026 version
      {
        source: "/best-habit-tracker-apps",
        destination: "/best-habit-tracker-apps-2026",
        permanent: true,
      },
    ];
  },
};

export default nextConfig;
