import React, { useState } from "react";
import logo from "./logo.svg";
import "./App.css";
import LoginScreen from "./Components/login/login_screen";
import { Routes, Route } from "react-router-dom";
import AlgorithmScreen from "./Components/algorithm/algorithm_screen";
import BenchmarkScreen from "./Components/benchmark/benchmark_screen";
import Header from "./Components/Other/Header";
import ProblemScreen from "./Components/Other/ProblemScreen";
function App() {
  const [logged, setLogged] = useState(false);
  return (
    
      <div>
        {logged ?
          <div>
            <Header/>
            <Routes>
              <Route path="/" element={<AlgorithmScreen />} />
              <Route path="/benchmark" element={<BenchmarkScreen />} />
              <Route path="/problems" element={<ProblemScreen />} />
            </Routes>
          </div>
        :
            <Routes>
              <Route path="*" element={<LoginScreen logged={setLogged}/>} />
            </Routes>
        }
      </div>

  );
}

export default App;
