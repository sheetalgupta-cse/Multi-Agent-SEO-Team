import {
  CheckCircle2,
  Loader2,
  Circle,
  BrainCircuit,
  Search,
  Users,
  Globe,
  FileText,
} from "lucide-react";

const icons = {
  manager: BrainCircuit,
  keyword: Search,
  competitor: Users,
  audit: Globe,
  content: FileText,
};

export default function AgentPanel({ agents, running }) {
  return (
    <div className="card agent-card">
      <div className="section-heading">
        <div>
          <span className="eyebrow">MULTI-AGENT SYSTEM</span>
          <h2>AI SEO Team</h2>
        </div>

        <div className="online-pill">
          <span />
          {running ? "Running" : "Ready"}
        </div>
      </div>

      <div className="agent-list">
        {agents.map((agent) => {
          const Icon = icons[agent.id];

          return (
            <div className="agent-row" key={agent.id}>
              <div className={`agent-icon ${agent.status}`}>
                <Icon size={18} />
              </div>

              <div className="agent-info">
                <strong>{agent.name}</strong>
                <span>{agent.task}</span>
              </div>

              <div className="agent-status">
                {agent.status === "completed" && (
                  <>
                    <CheckCircle2 size={18} />
                    <span>Completed</span>
                  </>
                )}

                {agent.status === "running" && (
                  <>
                    <Loader2 className="spin" size={18} />
                    <span>Working</span>
                  </>
                )}

                {agent.status === "waiting" && (
                  <>
                    <Circle size={17} />
                    <span>Waiting</span>
                  </>
                )}
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}