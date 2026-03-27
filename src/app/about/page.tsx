export const metadata = { title: "About | Habit Tracker Spot", alternates: { canonical: "https://habittrackerspot.com/about" } };

export default function AboutPage() {
  return (
    <div className="max-w-3xl mx-auto px-4 sm:px-6 py-10 space-y-4">
      <h1 className="text-3xl font-bold">About Habit Tracker Spot</h1>
      <p>Habit Tracker Spot publishes practical guides and expert reviews to help readers with habit tracking, building consistent routines, and personal development. Our editorial team researches and tests products so you can make confident decisions.</p>
      <p>We focus on habit journals, tracking apps, accountability systems, and behaviour change strategies — cutting through the noise with honest, well-researched recommendations backed by real-world testing and expert input.</p>
      <p>Every article on Habit Tracker Spot is written to meet strict editorial standards: accurate information, clear explanations, and up-to-date guidance. We update our guides regularly to reflect the latest research and product releases.</p>
      <p><a href="/" className="text-blue-600 hover:underline">← Back to Habit Tracker Spot</a></p>
    </div>
  );
}
