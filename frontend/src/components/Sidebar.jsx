import {
  LayoutDashboard,
  Search,
  Users,
  FileText,
  BarChart3,
  Settings,
  Sparkles,
  ChevronLeft,
} from "lucide-react";

const menuItems = [
  {
    id: "overview",
    icon: LayoutDashboard,
    label: "Overview",
  },
  {
    id: "keywords",
    icon: Search,
    label: "Keyword Intelligence",
  },
  {
    id: "competitors",
    icon: Users,
    label: "Competitors",
  },
  {
    id: "content",
    icon: FileText,
    label: "Content Strategy",
  },
  {
    id: "analytics",
    icon: BarChart3,
    label: "SEO Analytics",
  },
];

export default function Sidebar({
 open,
 setOpen,
 activeSection,
 setActiveSection,
 onNavigate,

}) {
  const handleNavigation = (section) => {
  setActiveSection(section);

  if (onNavigate) {
    onNavigate(section);
  }

  setOpen(false);
};
 

  return (
    <>
      {/* Mobile overlay */}

      {open && (
        <div
          className="mobile-overlay"
          onClick={() => setOpen(false)}
        />
      )}

      <aside
        className={`sidebar ${
          open ? "sidebar-open" : ""
        }`}
      >

        {/* ================= BRAND ================= */}

        <div className="brand">

          <div className="brand-logo">
            <Sparkles size={19} />
          </div>

          <div>
            <div className="brand-name">
              Aurify
            </div>

            <div className="brand-subtitle">
              AI SEO TEAM
            </div>
          </div>

          <button
            className="mobile-close"
            onClick={() => setOpen(false)}
          >
            <ChevronLeft size={18} />
          </button>

        </div>


        {/* ================= WORKSPACE ================= */}

        <div className="workspace">

          <div className="workspace-label">
            WORKSPACE
          </div>

          <div className="workspace-box">

            <div className="workspace-avatar">
              A
            </div>

            <div>
              <strong>
                Aurify Marketing
              </strong>

              <span>
                SEO Workspace
              </span>
            </div>

          </div>

        </div>


        {/* ================= NAVIGATION ================= */}

        <nav className="nav">

          <div className="nav-label">
            MAIN
          </div>


          {menuItems.map((item) => {

            const Icon = item.icon;

            return (
              <button
                key={item.id}
                className={`nav-item ${
                  activeSection === item.id
                    ? "active"
                    : ""
                }`}
                onClick={() =>
                  handleNavigation(item.id)
                }
              >

                <Icon size={18} />

                <span>
                  {item.label}
                </span>

              </button>
            );

          })}


          {/* ================= SYSTEM ================= */}

          <div className="nav-label settings-label">
            SYSTEM
          </div>


          <button
            className={`nav-item ${
              activeSection === "settings"
                ? "active"
                : ""
            }`}
            onClick={() =>
              handleNavigation("settings")
            }
          >

            <Settings size={18} />

            <span>
              Settings
            </span>

          </button>

        </nav>


        {/* ================= BOTTOM ================= */}

        <div className="sidebar-bottom">

          <div className="ai-status">

            <div className="status-dot" />

            <div>

              <strong>
                AI Team Online
              </strong>

              <span>
                5 agents available
              </span>

            </div>

          </div>


          <div className="version">
            Aurify AI v1.0
          </div>

        </div>

      </aside>
    </>
  );
}