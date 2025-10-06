export default function Dashboard() {
  return (
    <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
      <div className="p-4 bg-white rounded-md border shadow-soft">
        <div className="text-sm text-gray-500">Total Documents</div>
        <div className="text-3xl font-semibold">12,480</div>
      </div>
      <div className="p-4 bg-white rounded-md border shadow-soft">
        <div className="text-sm text-gray-500">Legal Holds</div>
        <div className="text-3xl font-semibold">3</div>
      </div>
      <div className="p-4 bg-white rounded-md border shadow-soft">
        <div className="text-sm text-gray-500">Active Reviewers</div>
        <div className="text-3xl font-semibold">8</div>
      </div>
      <div className="p-4 bg-white rounded-md border shadow-soft md:col-span-2 h-72">
        <div className="font-medium mb-2">Recent Activity</div>
        <div className="text-gray-500">No recent events.</div>
      </div>
      <div className="p-4 bg-white rounded-md border shadow-soft h-72">
        <div className="font-medium mb-2">Search</div>
        <input className="w-full border rounded-md px-3 py-2" placeholder="Search documents, tags, custodians..." />
      </div>
    </div>
  );
}
