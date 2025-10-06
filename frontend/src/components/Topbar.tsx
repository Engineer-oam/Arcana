export default function Topbar() {
  return (
    <header className="sticky top-0 z-10 bg-white border-b h-14 flex items-center px-4 shadow-soft">
      <div className="flex-1 font-medium">Case: ACME vs State</div>
      <div className="text-sm text-gray-500">Reviewer • John Doe</div>
    </header>
  );
}
