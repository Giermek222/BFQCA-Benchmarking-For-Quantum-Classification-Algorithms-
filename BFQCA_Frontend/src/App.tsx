import { useState } from "react";
import "./App.css";
import LoginScreen from "./Components/login/login_screen";
import { Routes, Route } from "react-router-dom";
import AlgorithmScreen from "./Components/algorithm/algorithm_logic";
import BenchmarkScreen from "./Components/benchmark/benchmark_logic";
import Header from "./Components/Other/Header";
import ProblemScreen from "./Components/datasets/ProblemScreen";
import ContributeScreen from "./Components/Other/ContributeScreen";
import AddAlgorithmScreen from "./Components/algorithm/add_algorithm_logic";
import AddDatasetScreen from "./Components/datasets/add_dataset_logic";
function App() {
  const [logged, setLogged] = useState(false);
  const [username, setUserName] = useState("");
  return (
    //TODO::add authorization checks on routes
    <div>
      {logged ? (
        <div>
          <Header logged={setLogged} userName={username} />
          <Routes>
            <Route path="/" element={<AlgorithmScreen userName={username} />} />
            <Route path="/benchmark" element={<BenchmarkScreen />} />
            <Route path="/problems" element={<ProblemScreen />} />
            <Route path="/contribute" element={<ContributeScreen />} />
            <Route
              path="/addAlgorithm"
              element={<AddAlgorithmScreen userName={username} />}
            />
            <Route
              path="/addDataset"
              element={<AddDatasetScreen userName={username} />}
            />
          </Routes>
        </div>
      ) : (
        <Routes>
          <Route
            path="*"
            element={
              <LoginScreen logged={setLogged} setUserName={setUserName} />
            }
          />
        </Routes>
      )}
    </div>
  );
}

export default App;
