export default function Export() {
  return (
    <div className="space-y-4">
      <div className="bg-white rounded-md border p-4">
        <div className="font-medium mb-2">Production Export</div>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          <div>
            <label className="text-sm text-gray-600">Format</label>
            <select className="w-full border rounded-md px-3 py-2 mt-1">
              <option>PDF</option>
              <option>Excel</option>
              <option>CSV</option>
              <option>EML</option>
            </select>
          </div>
          <div>
            <label className="text-sm text-gray-600">Bates Prefix</label>
            <input className="w-full border rounded-md px-3 py-2 mt-1" placeholder="ACME-" />
          </div>
          <div>
            <label className="text-sm text-gray-600">Start Number</label>
            <input type="number" className="w-full border rounded-md px-3 py-2 mt-1" defaultValue={1000} />
          </div>
        </div>
        <button className="mt-4 px-4 py-2 bg-primary-600 text-white rounded-md">Generate Export</button>
      </div>
    </div>
  );
}
