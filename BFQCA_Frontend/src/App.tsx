import { useState } from "react";
import "./App.css";
import LoginScreen from "./Components/login/login_screen";
import { Routes, Route } from "react-router-dom";
import AlgorithmScreen from "./Components/algorithm/algorithm_logic";
import BenchmarkScreen from "./Components/benchmark/benchmark_logic";
import Header from "./Components/Other/Header";
import ProblemScreen from "./Components/Other/ProblemScreen";
import ContributeScreen from "./Components/Other/ContributeScreen";
function App() {
  const [logged, setLogged] = useState(false);
  const [username, setUserName] = useState("");
  return (
    
      <div>
        {logged ?
          <div>
            <Header logged={setLogged} userName={username}/>
            <Routes>
              <Route path="/" element={<AlgorithmScreen userName = {username} />} />
              <Route path="/benchmark" element={<BenchmarkScreen />} />
              <Route path="/problems" element={<ProblemScreen />} />
              <Route path="/contribute" element={<ContributeScreen/>} />
            </Routes>
          </div>
        :
            <Routes>
              <Route path="*" element={<LoginScreen logged={setLogged} setUserName={setUserName}/>} />
            </Routes>
        }
      </div>

  );
}

export default App;
