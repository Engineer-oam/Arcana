export default function Activity() {
  return (
    <div className="space-y-4">
      <div className="bg-white rounded-md border p-4">
        <div className="font-medium mb-2">Activity Timeline</div>
        <div className="text-sm text-gray-500">No events yet.</div>
      </div>
      <div className="bg-white rounded-md border p-4">
        <div className="font-medium mb-2">Legal Hold</div>
        <div className="text-sm text-gray-500">No legal holds configured.</div>
      </div>
    </div>
  );
}
