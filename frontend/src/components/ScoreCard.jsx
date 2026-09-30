import {
  TrendingUp,
  AlertTriangle,
  CheckCircle2,
} from "lucide-react";

export default function ScoreCard({
  score = 0,
  opportunities = 0,
}) {
  const safeScore = Math.max(0, Math.min(100, Number(score) || 0));

  const circumference = 2 * Math.PI * 50;
  const progress =
    circumference - (safeScore / 100) * circumference;

  const getStatus = () => {
    if (safeScore >= 80) return "Good";
    if (safeScore >= 60) return "Needs Improvement";
    return "Needs Attention";
  };

  return (
    <div className="card score-card">

      <div className="section-heading">
        <div>
          <span className="eyebrow">
            SEO PERFORMANCE
          </span>

          <h2>Health Score</h2>
        </div>

        <TrendingUp size={20} />
      </div>

      <div className="score-main">

        <div className="score-ring">

          <svg width="140" height="140">

            <circle
              className="ring-bg"
              cx="70"
              cy="70"
              r="50"
            />

            <circle
              className="ring-progress"
              cx="70"
              cy="70"
              r="50"
              strokeDasharray={circumference}
              strokeDashoffset={progress}
            />

          </svg>

          <div className="score-number">

            <strong>{safeScore}</strong>

            <span>/100</span>

          </div>

        </div>

        <div className="score-description">

          <div className="score-badge">

            <CheckCircle2 size={15} />

            {getStatus()}

          </div>

          <p>
            Your website has been analyzed by the
            Multi-Agent SEO Team. The score is based
            on the technical SEO audit returned by
            the backend.
          </p>

        </div>

      </div>

      <div className="score-breakdown">

        <div>
          <span>Technical</span>
          <strong>{safeScore}</strong>
        </div>

        <div>
          <span>Keywords</span>
          <strong>AI</strong>
        </div>

        <div>
          <span>Content</span>
          <strong>AI</strong>
        </div>

        <div>
          <span>On-page</span>
          <strong>AI</strong>
        </div>

      </div>

      <div className="warning">

        <AlertTriangle size={17} />

        <span>
          {opportunities} optimization opportunities detected
        </span>

      </div>

    </div>
  );
}