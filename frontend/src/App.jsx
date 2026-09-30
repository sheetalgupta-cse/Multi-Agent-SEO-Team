import { useState } from "react";
import "./App.css";

const API_URL = "http://127.0.0.1:8000/api/seo/analyze";

function App() {
  const [website, setWebsite] = useState("");
  const [goal, setGoal] = useState("Increase organic traffic");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const analyzeSEO = async () => {
    if (!website.trim()) {
      setError("Please enter a website URL.");
      return;
    }

    setLoading(true);
    setError("");
    setResult(null);

    try {
      const response = await fetch(API_URL, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          website: website.trim(),
          goal: goal.trim(),
        }),
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.detail || "SEO analysis failed.");
      }

      setResult(data);
    } catch (err) {
      setError(
        err.message ||
          "Unable to connect with the SEO backend. Make sure FastAPI is running."
      );
    } finally {
      setLoading(false);
    }
  };

  const getPriorityClass = (priority) => {
    if (!priority) return "priority";
    return `priority ${priority.toLowerCase()}`;
  };

  const downloadJSON = () => {
    if (!result) return;

    const blob = new Blob([JSON.stringify(result, null, 2)], {
      type: "application/json",
    });

    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");

    a.href = url;
    a.download = "seo-analysis-report.json";
    a.click();

    URL.revokeObjectURL(url);
  };

  const keywords = result?.keywords?.keywords || [];
  const competitorGaps = result?.competitors?.competitor_gaps || [];
  const technicalIssues = result?.technical?.issues || [];
  const contentOpportunities =
    result?.content?.content_opportunities || [];
  const validated = result?.evaluation?.validated || [];
  const actionPlan = result?.action_plan?.action_plan || [];

  const allOpportunities = [
  ...keywords,
  ...competitorGaps,
  ...technicalIssues,
  ...contentOpportunities,
];

const highPriority = allOpportunities.filter(
  (item) =>
    item.priority?.toLowerCase() === "high"
).length;
  return (
    <div className="app">
      {/* HEADER */}
      <header className="header">
        <div>
          <h1>🤖 Multi-Agent SEO Team</h1>
          <p>
            AI-powered SEO analysis using multiple specialized agents
          </p>
        </div>

        {result && (
          <button className="download-btn" onClick={downloadJSON}>
            ↓ Download Report
          </button>
        )}
      </header>

      {/* INPUT */}
      <section className="hero">
        <div className="hero-content">
          <h2>Analyze Your Website with AI Agents</h2>
          <p>
            Our AI SEO team analyzes keywords, competitors, technical
            SEO, content opportunities and creates an actionable SEO plan.
          </p>

          <div className="input-box">
            <div className="input-group">
              <label>Website URL</label>
              <input
                type="url"
                placeholder="https://www.example.com/"
                value={website}
                onChange={(e) => setWebsite(e.target.value)}
              />
            </div>

            <div className="input-group">
              <label>SEO Goal</label>
              <input
                type="text"
                placeholder="Increase organic traffic"
                value={goal}
                onChange={(e) => setGoal(e.target.value)}
              />
            </div>

            <button
              className="analyze-btn"
              onClick={analyzeSEO}
              disabled={loading}
            >
              {loading ? "Analyzing..." : "🚀 Analyze SEO"}
            </button>
          </div>

          {error && <div className="error-box">⚠ {error}</div>}
        </div>
      </section>

      {/* AGENT STATUS */}
      {loading && (
        <section className="agent-status">
          <h3>🤖 AI Agents Working...</h3>

          <div className="agents">
            <div>⏳ SEO Planner</div>
            <div>⏳ Keyword Agent</div>
            <div>⏳ Competitor Agent</div>
            <div>⏳ Technical SEO Agent</div>
            <div>⏳ Content Agent</div>
            <div>⏳ AI Evaluator</div>
            <div>⏳ Action Planner</div>
          </div>
        </section>
      )}

      {/* RESULTS */}
      {result && !loading && (
        <main className="dashboard">

          {/* OVERVIEW */}
          <section className="section">
            <div className="section-title">
              <h2>📊 SEO Overview</h2>
              <span className="website-name">{result.website}</span>
            </div>

            <div className="stats-grid">
              <div className="stat-card score-card">
                <span>SEO Score</span>
                <strong>{result.technical?.technical_score ?? 0}</strong>
                <small>/ 100</small>
              </div>

              <div className="stat-card">
                <span>Keywords</span>
                <strong>{keywords.length}</strong>
                <small>opportunities</small>
              </div>

              <div className="stat-card">
                <span>Competitor Gaps</span>
                <strong>{competitorGaps.length}</strong>
                <small>identified</small>
              </div>

              <div className="stat-card">
                <span>Content Ideas</span>
                <strong>{contentOpportunities.length}</strong>
                <small>opportunities</small>
              </div>

              <div className="stat-card">
                <span>High Priority</span>
                <strong>{highPriority}</strong>
                <small>actions</small>
              </div>
            </div>
          </section>

          {/* KEYWORDS */}
          <section className="section">
            <h2>🔑 Keyword Research Agent</h2>

            {keywords.length === 0 ? (
              <div className="empty">No keyword opportunities found.</div>
            ) : (
              <div className="table-wrapper">
                <table>
                  <thead>
                    <tr>
                      <th>Keyword</th>
                      <th>Intent</th>
                      <th>Priority</th>
                      <th>Reason</th>
                    </tr>
                  </thead>

                  <tbody>
                    {keywords.map((item, index) => (
                      <tr key={index}>
                        <td>
                          <strong>{item.keyword}</strong>
                        </td>

                        <td>{item.intent}</td>

                        <td>
                          <span className={getPriorityClass(item.priority)}>
                            {item.priority}
                          </span>
                        </td>

                        <td>{item.reason}</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            )}
          </section>

          {/* COMPETITORS */}
          <section className="section">
            <h2>🔍 Competitor Analysis Agent</h2>

            <div className="card-grid">
              {competitorGaps.map((item, index) => (
                <div className="info-card" key={index}>
                  <div className="card-top">
                    <h3>{item.competitor}</h3>

                    <span
                      className={getPriorityClass(item.priority)}
                    >
                      {item.priority}
                    </span>
                  </div>

                  <p>
                    <strong>Gap:</strong> {item.gap}
                  </p>

                  <p>
                    <strong>Opportunity:</strong> {item.opportunity}
                  </p>
                </div>
              ))}
            </div>
          </section>

          {/* TECHNICAL */}
          <section className="section">
            <h2>🛠️ Technical SEO Audit</h2>

            <div className="technical-layout">
              <div className="seo-score">
                <div
                  className="score-circle"
                  style={{
                    "--score": `${result.technical?.technical_score || 0}%`,
                  }}
                >
                  <div>
                    <strong>
                      {result.technical?.technical_score || 0}
                    </strong>
                    <span>/100</span>
                  </div>
                </div>

                <h3>Technical SEO Score</h3>
              </div>

              <div className="technical-details">
                <div className="meta-card">
                  <h3>Page Title</h3>
                  <p>
                    {result.technical?.page_title || "Not detected"}
                  </p>
                </div>

                <div className="meta-card">
                  <h3>Meta Description</h3>
                  <p>
                    {result.technical?.meta_description ||
                      "Not detected"}
                  </p>
                </div>
              </div>
            </div>

            <h3 className="subheading">Issues Found</h3>

            {technicalIssues.length === 0 ? (
              <div className="success-box">
                ✓ No major technical issues found.
              </div>
            ) : (
              <div className="issues">
                {technicalIssues.map((issue, index) => (
                  <div className="issue-card" key={index}>
                    <div>
                      <strong>⚠ {issue.issue}</strong>
                    </div>

                    <span
                      className={getPriorityClass(issue.priority)}
                    >
                      {issue.priority}
                    </span>
                  </div>
                ))}
              </div>
            )}
          </section>

          {/* CONTENT */}
          <section className="section">
            <h2>📝 Content Strategy Agent</h2>

            <div className="card-grid">
              {contentOpportunities.map((item, index) => (
                <div className="content-card" key={index}>
                  <div className="card-top">
                    <span className="content-number">
                      #{index + 1}
                    </span>

                    <span
                      className={getPriorityClass(item.priority)}
                    >
                      {item.priority}
                    </span>
                  </div>

                  <h3>{item.topic}</h3>

                  <p>
                    <strong>Primary Keyword:</strong>{" "}
                    {item.primary_keyword}
                  </p>

                  <p>
                    <strong>Suggested Title:</strong>{" "}
                    {item.suggested_title}
                  </p>

                  {item.search_intent && (
                    <p>
                      <strong>Search Intent:</strong>{" "}
                      {item.search_intent}
                    </p>
                  )}
                </div>
              ))}
            </div>
          </section>

          {/* EVALUATION */}
          <section className="section">
            <h2>🧠 AI Evaluation</h2>

            <div className="evaluation-list">
              {validated.map((item, index) => (
                <div className="evaluation-card" key={index}>
                  <div>
                    <h3>{item.recommendation}</h3>
                    <p>{item.reason}</p>
                  </div>

                  <div className="confidence">
                    <strong>{item.confidence}%</strong>
                    <span>Confidence</span>
                  </div>

                  <span className="validated">
                    ✓ {item.status}
                  </span>
                </div>
              ))}
            </div>
          </section>

          {/* ACTION PLAN */}
          <section className="section action-section">
            <h2>📋 Final SEO Action Plan</h2>

            <div className="action-list">
              {actionPlan.map((item, index) => (
                <div className="action-card" key={index}>
                  <div className="action-number">
                    {index + 1}
                  </div>

                  <div className="action-content">
                    <div className="card-top">
                      <span
                        className={getPriorityClass(item.priority)}
                      >
                        {item.priority}
                      </span>

                      <span className="effort">
                        Effort: {item.effort}
                      </span>
                    </div>

                    <h3>{item.action}</h3>

                    <p>{item.reason}</p>
                  </div>
                </div>
              ))}
            </div>
          </section>

          {/* SUMMARY */}
          <section className="final-summary">
            <h2>🎯 SEO Analysis Complete</h2>

            <p>
              The Multi-Agent SEO Team analyzed the website using
              specialized AI agents and generated actionable SEO
              recommendations.
            </p>

            <button className="download-btn" onClick={downloadJSON}>
              ↓ Download JSON Report
            </button>
          </section>
        </main>
      )}
    </div>
  );
}

export default App;