import { ArrowUpRight, ShieldCheck } from "lucide-react";

export default function CompetitorCard() {
  const competitors = [
    {
      name: "Competitor Alpha",
      initials: "CA",
      strength: "Local SEO",
      gap: "Weak content depth",
    },
    {
      name: "Competitor Beta",
      initials: "CB",
      strength: "Content marketing",
      gap: "Poor technical SEO",
    },
    {
      name: "Competitor Gamma",
      initials: "CG",
      strength: "Service pages",
      gap: "Low topical authority",
    },
  ];

  return (
    <div className="card">
      <div className="section-heading">
        <div>
          <span className="eyebrow">COMPETITOR AGENT</span>
          <h2>Competitive Intelligence</h2>
        </div>

        <ArrowUpRight size={19} />
      </div>

      <div className="competitor-list">
        {competitors.map((competitor) => (
          <div className="competitor" key={competitor.name}>
            <div className="competitor-avatar">
              {competitor.initials}
            </div>

            <div className="competitor-info">
              <strong>{competitor.name}</strong>

              <span>
                Strength: <b>{competitor.strength}</b>
              </span>

              <span>
                Gap: <b>{competitor.gap}</b>
              </span>
            </div>

            <ShieldCheck size={18} />
          </div>
        ))}
      </div>
    </div>
  );
}