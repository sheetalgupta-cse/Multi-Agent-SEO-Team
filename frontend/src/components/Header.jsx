import { Bell, Menu, Sparkles } from "lucide-react";

export default function Header({ setOpen }) {
  return (
    <header className="topbar">
      <button className="menu-button" onClick={() => setOpen(true)}>
        <Menu size={21} />
      </button>

      <div className="mobile-title">
        <Sparkles size={17} />
        Aurify AI SEO
      </div>

      <div className="topbar-right">
        <div className="notification">
          <Bell size={18} />
          <span />
        </div>

        <div className="user">
          <div className="user-avatar">SM</div>

          <div className="user-info">
            <strong>SEO Manager</strong>
            <span>Aurify Marketing</span>
          </div>
        </div>
      </div>
    </header>
  );
}