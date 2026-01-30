import { useState } from "react";
import axios from "axios";

export default function Analyze() {
  const [text, setText] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [file, setFile] = useState(null);

  // TEXT ANALYSIS
  const analyzeText = async () => {
    if (!text.trim()) return alert("Enter clinical text");

    setLoading(true);
    try {
      const res = await axios.post(
        "http://127.0.0.1:8000/predict",
        { text }
      );
      setResult(res.data);
    } catch {
      alert("Backend not running");
    }
    setLoading(false);
  };

  // PDF ANALYSIS
  const analyzePDF = async () => {
    if (!file) return alert("Select PDF");

    const formData = new FormData();
    formData.append("file", file);

    setLoading(true);
    try {
      const res = await axios.post(
        "http://127.0.0.1:8000/report/upload",
        formData,
        { headers: { "Content-Type": "multipart/form-data" } }
      );
      setResult(res.data);
    } catch {
      alert("PDF analysis failed");
    }
    setLoading(false);
  };

  return (
    <div className="p-10 bg-gray-100 min-h-screen">

      <h1 className="text-3xl font-bold mb-6">
        Adverse Drug Effect Analysis
      </h1>

      {/* TEXT INPUT */}
      <div className="bg-white p-6 rounded-xl shadow mb-8">
        <h2 className="text-xl font-semibold mb-4">
          Analyze Clinical Text
        </h2>

        <textarea
          className="w-full border p-3 rounded h-32"
          placeholder="Enter patient symptoms, drugs, observations..."
          value={text}
          onChange={(e) => setText(e.target.value)}
        />

        <button
          onClick={analyzeText}
          className="mt-4 bg-blue-600 text-white px-6 py-2 rounded"
        >
          Analyze Text
        </button>
      </div>

      {/* PDF INPUT */}
      <div className="bg-white p-6 rounded-xl shadow mb-8">
        <h2 className="text-xl font-semibold mb-4">
          Upload Medical Report (PDF)
        </h2>

        <input
          type="file"
          accept=".pdf"
          onChange={(e) => setFile(e.target.files[0])}
        />

        <button
          onClick={analyzePDF}
          className="ml-4 bg-indigo-600 text-white px-6 py-2 rounded"
        >
          Upload & Analyze
        </button>
      </div>

      {/* RESULT */}
      {loading && (
        <p className="text-lg font-semibold">Analyzing...</p>
      )}

      {result && (
        <div className="bg-white p-6 rounded-xl shadow">
          <h2 className="text-xl font-semibold mb-2">
            Analysis Result
          </h2>

          <p className="text-lg">
            <b>Prediction:</b>{" "}
            <span
              className={
                result.prediction.includes("Adverse")
                  ? "text-red-600 font-bold"
                  : "text-green-600 font-bold"
              }
            >
              {result.prediction}
            </span>
          </p>

          {result.confidence && (
            <p className="mt-2">
              <b>Confidence:</b> {result.confidence}
            </p>
          )}
        </div>
      )}
    </div>
  );
}
