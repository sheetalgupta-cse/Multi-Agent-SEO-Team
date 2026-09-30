import {
  AlertCircle,
  CheckCircle2,
  AlertTriangle,
} from "lucide-react";

export default function AuditCard() {
  const issues = [
    {
      type: "critical",
      icon: AlertCircle,
      title: "Missing meta descriptions",
      count: "3 pages",
    },
    {
      type: "warning",
      icon: AlertTriangle,
      title: "Weak internal linking",
      count: "8 pages",
    },
    {
      type: "warning",
      icon: AlertTriangle,
      title: "Images missing alt text",
      count: "6 images",
    },
    {
      type: "success",
      icon: CheckCircle2,
      title: "Mobile responsive",
      count: "Passed",
    },
  ];

  return (
    <div className="card">
      <div className="section-heading">
        <div>
          <span className="eyebrow">AUDIT AGENT</span>
          <h2>Technical SEO</h2>
        </div>

        <span className="mini-score">82%</span>
      </div>

      <div className="audit-list">
        {issues.map((issue) => {
          const Icon = issue.icon;

          return (
            <div className="audit-item" key={issue.title}>
              <Icon className={issue.type} size={19} />

              <div>
                <strong>{issue.title}</strong>
                <span>{issue.count}</span>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}