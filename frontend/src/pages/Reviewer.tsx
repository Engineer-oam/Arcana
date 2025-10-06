import DocumentViewer from '../components/DocumentViewer';

export default function Reviewer() {
  return (
    <div className="grid grid-cols-12 gap-4 h-[calc(100vh-4rem)]">
      <div className="col-span-3 bg-white rounded-md border p-3 overflow-auto">
        <div className="font-medium mb-2">Documents</div>
        <ul className="space-y-2">
          {Array.from({ length: 20 }).map((_, i) => (
            <li key={i} className="p-2 border rounded hover:bg-gray-50 cursor-pointer">Document {i + 1}</li>
          ))}
        </ul>
      </div>
      <div className="col-span-6 h-full">
        <DocumentViewer />
      </div>
      <div className="col-span-3 bg-white rounded-md border p-3 overflow-auto">
        <div className="font-medium mb-2">Annotations</div>
        <div className="space-y-2 text-sm text-gray-600">No annotations.</div>
      </div>
    </div>
  );
}
