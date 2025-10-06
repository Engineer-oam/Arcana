import { useRef, useState } from 'react';

export default function Upload() {
  const inputRef = useRef<HTMLInputElement | null>(null);
  const [files, setFiles] = useState<File[]>([]);

  const onDrop = (e: React.DragEvent<HTMLDivElement>) => {
    e.preventDefault();
    const list = Array.from(e.dataTransfer.files);
    setFiles(list);
  };

  return (
    <div className="space-y-4">
      <div
        className="border-2 border-dashed rounded-md p-10 text-center bg-white"
        onDragOver={(e) => e.preventDefault()}
        onDrop={onDrop}
      >
        <div className="font-medium">Drag and drop files here</div>
        <div className="text-sm text-gray-500">PDF, DOCX, PNG, JPG</div>
        <button
          className="mt-4 px-4 py-2 bg-primary-600 text-white rounded-md"
          onClick={() => inputRef.current?.click()}
        >
          Browse Files
        </button>
        <input ref={inputRef} type="file" multiple className="hidden" onChange={(e) => setFiles(Array.from(e.target.files || []))} />
      </div>

      {files.length > 0 && (
        <div className="bg-white rounded-md border p-4">
          <div className="font-medium mb-2">Selected Files</div>
          <ul className="text-sm">
            {files.map((f) => (
              <li key={f.name} className="py-1">{f.name}</li>
            ))}
          </ul>
          <button className="mt-4 px-4 py-2 bg-primary-600 text-white rounded-md">Upload</button>
        </div>
      )}
    </div>
  );
}
