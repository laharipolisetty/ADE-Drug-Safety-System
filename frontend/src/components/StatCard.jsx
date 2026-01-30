export default function StatCard({ title, value, color }) {
  return (
    <div className={`p-6 rounded-xl shadow bg-${color}-100`}>
      <h3 className="text-gray-600 text-sm">{title}</h3>
      <p className={`text-3xl font-bold text-${color}-700`}>
        {value}
      </p>
    </div>
  );
}
