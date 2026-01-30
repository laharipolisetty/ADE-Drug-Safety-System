import React, { useEffect, useState } from "react";
import axios from "axios";
import {
  BarChart, Bar, XAxis, YAxis, Tooltip,
  PieChart, Pie, Cell
} from "recharts";

export default function Dashboard() {

  // ✅ STATES (inside component)
  const [data, setData] = useState(null);
  const [filter, setFilter] = useState("ALL");
  const [records, setRecords] = useState([]);

  // ✅ DASHBOARD DATA
  const loadData = () => {
    axios.get("http://127.0.0.1:8000/dashboard")
      .then(res => setData(res.data))
      .catch(err => console.log(err));
  };

  // ✅ FILTERED RECORDS
  const loadRecords = () => {
    let url = "http://127.0.0.1:8000/predictions";

    if (filter !== "ALL") {
      url += "?type=" + filter;
    }

    axios.get(url)
      .then(res => setRecords(res.data))
      .catch(err => console.log(err));
  };

  // ✅ AUTO REFRESH
  useEffect(() => {
    loadData();
    loadRecords();

    const interval = setInterval(() => {
      loadData();
      loadRecords();
    }, 5000);

    return () => clearInterval(interval);
  }, [filter]);

  if (!data) return <p>Loading dashboard...</p>;

  const pieData = [
    { name: "ADE", value: data.ade_cases },
    { name: "SAFE", value: data.safe_cases }
  ];

  return (
    <div className="p-8 bg-gray-100 min-h-screen">

      {/* TITLE */}
      <h1 className="text-3xl font-bold text-blue-700 mb-6">
        Drug Safety Analytics Dashboard
      </h1>

      {/* KPI CARDS */}
      <div className="grid grid-cols-3 gap-6 mb-8">
        <div className="bg-white p-6 shadow rounded">
          Total: {data.total_predictions}
        </div>

        <div className="bg-white p-6 shadow rounded text-red-600">
          ADE: {data.ade_cases}
        </div>

        <div className="bg-white p-6 shadow rounded text-green-600">
          Safe: {data.safe_cases}
        </div>
      </div>

      {/* FILTER + EXPORT */}
      <div className="flex gap-4 mb-8">
        <select
          value={filter}
          onChange={(e) => setFilter(e.target.value)}
          className="border p-2 rounded"
        >
          <option value="ALL">All</option>
          <option value="ADE">Adverse</option>
          <option value="SAFE">Safe</option>
        </select>

        <a
          href="http://127.0.0.1:8000/export/csv"
          className="bg-blue-600 text-white px-4 py-2 rounded"
        >
          Export CSV
        </a>
      </div>

      {/* CHARTS */}
      <div className="flex gap-10 mb-10">

        <BarChart width={400} height={300} data={pieData}>
          <XAxis dataKey="name" />
          <YAxis />
          <Tooltip />
          <Bar dataKey="value" fill="#2563eb" />
        </BarChart>

        <PieChart width={400} height={300}>
          <Pie
            data={pieData}
            dataKey="value"
            cx="50%"
            cy="50%"
            outerRadius={100}
            label
          >
            <Cell fill="#ef4444" />
            <Cell fill="#22c55e" />
          </Pie>
          <Tooltip />
        </PieChart>

      </div>

      {/* RECORD TABLE */}
      <table className="w-full bg-white shadow rounded">
        <thead className="bg-gray-100">
          <tr>
            <th className="p-2">Text</th>
            <th className="p-2">Prediction</th>
            <th className="p-2">Confidence</th>
            <th className="p-2">Time</th>
          </tr>
        </thead>
        <tbody>
          {records.map((r, i) => (
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
