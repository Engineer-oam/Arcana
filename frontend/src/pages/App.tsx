import { Route, Routes } from 'react-router-dom';
import Sidebar from '../components/Sidebar';
import Topbar from '../components/Topbar';
import Dashboard from './Dashboard';
import Reviewer from './Reviewer';
import Upload from './Upload';
import Activity from './Activity';
import Export from './Export';

export default function App() {
  return (
    <div className="min-h-screen grid grid-cols-12">
      <div className="col-span-12 md:col-span-2">
        <Sidebar />
      </div>
      <div className="col-span-12 md:col-span-10 flex flex-col">
        <Topbar />
        <main className="p-4 flex-1">
          <Routes>
            <Route path="/" element={<Dashboard />} />
            <Route path="/review" element={<Reviewer />} />
            <Route path="/upload" element={<Upload />} />
            <Route path="/activity" element={<Activity />} />
            <Route path="/export" element={<Export />} />
          </Routes>
        </main>
      </div>
    </div>
  );
}
