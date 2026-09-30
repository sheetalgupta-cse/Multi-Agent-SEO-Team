import {
  Search,
  TrendingUp,
  Target,
} from "lucide-react";

function KeywordTable({ keywords = [] }) {

  return (
    <section className="keyword-section">

      <div className="section-header">

        <div>

          <div className="section-title">

            <Search size={18} />

            Keyword Opportunities

          </div>

          <p className="section-subtitle">
            High-potential keywords identified by
            the AI Keyword Agent
          </p>

        </div>

        <div className="keyword-badge">

          <TrendingUp size={15} />

          AI Generated

        </div>

      </div>

      {keywords.length === 0 ? (

        <div className="empty">
          No keyword opportunities found.
        </div>

      ) : (

        <div className="keyword-table-wrapper">

          <table className="keyword-table">

            <thead>

              <tr>

                <th>KEYWORD</th>
                <th>INTENT</th>
                <th>PRIORITY</th>
                <th>REASON</th>

              </tr>

            </thead>

            <tbody>

              {keywords.map((item, index) => (

                <tr key={index}>

                  <td>

                    <div className="keyword-name">

                      <Target size={15} />

                      {item.keyword}

                    </div>

                  </td>

                  <td>
                    {item.intent || "N/A"}
                  </td>

                  <td>

                    <span
                      className={`priority ${
                        item.priority
                          ? item.priority.toLowerCase()
                          : ""
                      }`}
                    >
                      {item.priority || "N/A"}
                    </span>

                  </td>

                  <td>
                    {item.reason || "No reason provided"}
                  </td>

                </tr>

              ))}

            </tbody>

          </table>

        </div>

      )}

    </section>
  );
}

export default KeywordTable;