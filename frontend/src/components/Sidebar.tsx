import { NavLink } from 'react-router-dom';
import { HomeIcon, DocumentMagnifyingGlassIcon, ArrowUpTrayIcon, ArchiveBoxIcon, Cog6ToothIcon } from '@heroicons/react/24/outline';

export default function Sidebar() {
  const linkClass = ({ isActive }: { isActive: boolean }) =>
    `flex items-center gap-3 px-3 py-2 rounded-md hover:bg-primary-50 ${isActive ? 'bg-primary-100 text-primary-800' : 'text-gray-700'}`;

  return (
    <aside className="h-screen w-64 border-r bg-white p-4 hidden md:block">
      <div className="text-xl font-semibold mb-6">e-Discovery</div>
      <nav className="space-y-1">
        <NavLink to="/" className={linkClass} end>
          <HomeIcon className="h-5 w-5" /> Dashboard
        </NavLink>
        <NavLink to="/review" className={linkClass}>
          <DocumentMagnifyingGlassIcon className="h-5 w-5" /> Review
        </NavLink>
        <NavLink to="/upload" className={linkClass}>
          <ArrowUpTrayIcon className="h-5 w-5" /> Upload
        </NavLink>
        <NavLink to="/activity" className={linkClass}>
          <ArchiveBoxIcon className="h-5 w-5" /> Activity & Legal Hold
        </NavLink>
        <NavLink to="/export" className={linkClass}>
          <Cog6ToothIcon className="h-5 w-5" /> Export
        </NavLink>
      </nav>
    </aside>
  );
}
