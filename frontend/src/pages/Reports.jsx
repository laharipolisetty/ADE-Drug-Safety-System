import React, { useEffect, useState } from "react";
import axios from "axios";

export default function Reports() {
  const [reports, setReports] = useState([]);

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/report/reports")
      .then(res => setReports(res.data))
      .catch(err => console.log(err));
  }, []);

  return (
    <div className="p-8">
      <h1 className="text-2xl font-bold mb-6">Uploaded Medical Reports</h1>

      <table className="w-full bg-white shadow rounded">
        <thead className="bg-gray-100">
          <tr>
            <th className="p-2">Report</th>
            <th className="p-2">Prediction</th>
            <th className="p-2">Confidence</th>
            <th className="p-2">Time</th>
          </tr>
        </thead>
        <tbody>
          {reports.map((r, i) => (
            <tr key={i} className="border-b">
              <td className="p-2">{r.text.slice(0, 60)}...</td>
              <td className="p-2">{r.prediction}</td>
              <td className="p-2">{r.confidence}</td>
              <td className="p-2">{r.time}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
