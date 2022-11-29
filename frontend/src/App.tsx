import React from "react";
import logo from "./logo.svg";
import { Counter } from "./features/counter/Counter";
import "./App.css";
import LoginScreen from "./Components/login_screen";
import { Routes, Route } from "react-router-dom";
import MainScreen from "./Components/main_screen";
import BenchmarkScreen from "./Components/benchmark_screen";
function App() {
  return (
    <Routes>
      <Route path="/" element={<LoginScreen />} />
      <Route path="/main" element={<MainScreen />} />
      <Route path="/benchmark" element={<BenchmarkScreen />} />

      {/* <Route path="*" element={<NotFound />} /> */}
    </Routes>
    // <div className="App">
    //   <header className="App-header">{LoginScreen([])}</header>
    // </div>
  );
}

export default App;
