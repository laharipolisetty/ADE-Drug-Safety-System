import { Link } from "react-router-dom";

export default function Navbar() {
  return (
    <nav className="bg-blue-900 text-white px-10 py-4 flex justify-between">
      <h1 className="font-bold text-xl">Drug Safety AI</h1>

      <div className="space-x-6">
        <Link to="/">Home</Link>
        <Link to="/analyze">Analyze</Link>
        <Link to="/dashboard">Dashboard</Link>
        <Link to="/reports">Reports</Link>
        <Link to="/risk">Drug Risk</Link>
      </div>
    </nav>
  );
}
