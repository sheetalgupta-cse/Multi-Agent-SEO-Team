import {
  CheckCircle2,
  Circle,
  CalendarDays,
  ArrowRight,
} from "lucide-react";

export default function ActionPlan() {
  const actions = [
    {
      priority: "HIGH",
      title: 'Create "SEO Services in Lucknow" landing page',
      description:
        "Target high-intent local commercial keywords.",
    },
    {
      priority: "HIGH",
      title: "Fix missing meta descriptions",
      description:
        "Optimize 3 pages with relevant keywords and CTAs.",
    },
    {
      priority: "MEDIUM",
      title: "Build internal linking structure",
      description:
        "Connect service pages with relevant content clusters.",
    },
    {
      priority: "MEDIUM",
      title: "Publish local SEO content cluster",
      description:
        "Create 4 supporting articles over the next month.",
    },
  ];

  return (
    <div className="card action-card">
      <div className="section-heading">
        <div>
          <span className="eyebrow">SEO STRATEGIST</span>
          <h2>Priority Action Plan</h2>
        </div>

        <CalendarDays size={19} />
      </div>

      <div className="timeline">
        {actions.map((action, index) => (
          <div className="timeline-item" key={action.title}>
            <div className="timeline-marker">
              {index === 0 ? (
                <CheckCircle2 size={19} />
              ) : (
                <Circle size={18} />
              )}
            </div>

            <div className="timeline-content">
              <div className="action-top">
                <span
                  className={`priority ${action.priority.toLowerCase()}`}
                >
                  {action.priority}
                </span>

                <span>Week {index + 1}</span>
              </div>

              <h3>{action.title}</h3>
              <p>{action.description}</p>
            </div>
          </div>
        ))}
      </div>

      <button className="generate-plan">
        Generate full 30-day plan
        <ArrowRight size={17} />
      </button>
    </div>
  );
}