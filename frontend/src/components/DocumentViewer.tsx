import { useState } from 'react';

type Props = {
  src?: string;
  type?: 'pdf' | 'image' | 'text';
  textContent?: string;
};

export default function DocumentViewer({ src, type = 'pdf', textContent }: Props) {
  const [scale, setScale] = useState(1);

  if (type === 'text' && textContent) {
    return (
      <pre className="p-4 whitespace-pre-wrap bg-white rounded-md border h-full overflow-auto">
        {textContent}
      </pre>
    );
  }

  if (type === 'image' && src) {
    return (
      <div className="flex items-center justify-center bg-gray-100 h-full">
        <img src={src} style={{ transform: `scale(${scale})` }} className="max-h-full" />
      </div>
    );
  }

  return (
    <div className="h-full">
      {src ? (
        <iframe src={src} className="w-full h-full bg-white rounded-md border" />
      ) : (
        <div className="h-full flex items-center justify-center text-gray-500">Select a document to view</div>
      )}
    </div>
  );
}
