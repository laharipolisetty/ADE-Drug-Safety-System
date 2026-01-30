import { Link } from "react-router-dom";

export default function Home() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-600 to-indigo-700 text-white flex items-center">
      <div className="px-16">
        <h1 className="text-5xl font-bold mb-6">
          Adverse Drug Effect Detection
        </h1>

        <p className="text-xl max-w-xl mb-8">
          AI-powered pharmacovigilance system for real-time detection
          and safety analytics of adverse drug reactions.
        </p>

        <div className="flex gap-6">
          <Link
            to="/analyze"
            className="bg-white text-blue-700 px-6 py-3 rounded-lg font-semibold"
          >
            Start Analysis
          </Link>

          <Link
            to="/dashboard"
            className="border border-white px-6 py-3 rounded-lg"
          >
            View Dashboard
          </Link>
        </div>
      </div>
    </div>
  );
}
