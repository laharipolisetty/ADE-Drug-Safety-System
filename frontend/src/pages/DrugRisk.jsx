import React, { useEffect, useState } from "react";
import axios from "axios";

export default function DrugRisk() {
  const [risks, setRisks] = useState([]);

  useEffect(() => {
    loadRisk();
    const interval = setInterval(loadRisk, 5000);
    return () => clearInterval(interval);
  }, []);

  const loadRisk = () => {
    axios.get("http://127.0.0.1:8000/drug-risk")
      .then(res => setRisks(res.data))
      .catch(err => console.log(err));
  };

  return (
    <div className="p-8">
      <h1 className="text-3xl font-bold text-purple-700 mb-6">
        Real-Time Drug Risk Monitoring
      </h1>

      <table className="w-full bg-white shadow rounded">
        <thead>
          <tr className="bg-gray-100">
            <th className="p-3">Drug</th>
            <th className="p-3">Risk Level</th>
            <th className="p-3">Score</th>
          </tr>
        </thead>
        <tbody>
          {risks.map((r, i) => (
            <tr key={i} className="border-b">
              <td className="p-3">{r.drug}</td>
              <td className="p-3">{r.level}</td>
              <td className="p-3">{r.score}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
