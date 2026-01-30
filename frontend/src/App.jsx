import { BrowserRouter, Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";

import Home from "./pages/Home";
import Analyze from "./pages/Analyze";
import Reports from "./pages/Reports";
import DrugRisk from "./pages/DrugRisk";
import Dashboard from "./pages/Dashboard";

function App() {
  return (
    <BrowserRouter>
      <Navbar />

      <Routes>
        {/* HOME */}
        <Route path="/" element={<Home />} />

        {/* FEATURES */}
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/analyze" element={<Analyze />} />
        <Route path="/reports" element={<Reports />} />
        <Route path="/risk" element={<DrugRisk />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
