export interface Product {
  slug: string;
  name: string;
  price: number;
  description: string;
  features: string[];
}

export const products: Product[] = [
  {
    slug: "adhd-daily-planner",
    name: "ADHD Daily Planner System",
    price: 27,
    description:
      "Time-blocked daily planner designed for ADHD. Visual schedule, task batching, and dopamine reward checkboxes.",
    features: [
      "Time-blocked visual schedule",
      "Task batching by energy level",
      "Dopamine reward checkboxes",
      "Evening review prompts",
      "Weekly reset template",
    ],
  },
  {
    slug: "focus-block-tracker",
    name: "Focus Block Tracker",
    price: 12,
    description:
      "Track your focus sessions and identify your peak productivity windows. Pomodoro-compatible.",
    features: [
      "Focus session logger",
      "Peak hour identifier",
      "Distraction tally",
      "Energy level tracker",
      "Weekly pattern report",
    ],
  },
  {
    slug: "brain-dump-system",
    name: "Brain Dump & Priority System",
    price: 17,
    description:
      "Get everything out of your head and into a system. Capture, sort, and prioritise without overwhelm.",
    features: [
      "Unlimited brain dump pages",
      "3-tier priority sorter",
      "Idea parking lot",
      "Daily transfer prompts",
      "Weekly brain dump review",
    ],
  },
  {
    slug: "routine-builder",
    name: "ADHD Routine Builder",
    price: 9,
    description:
      "Build morning, work, and evening routines that actually stick. Visual checklists with buffer time built in.",
    features: [
      "Morning/work/evening routines",
      "Visual checklist format",
      "Buffer time prompts",
      "Habit stacking guide",
      "Printable wall version",
    ],
  },
];

export function getProduct(slug: string): Product | undefined {
  return products.find((product) => product.slug === slug);
}
