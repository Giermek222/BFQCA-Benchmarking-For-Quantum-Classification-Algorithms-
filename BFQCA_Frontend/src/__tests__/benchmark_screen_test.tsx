import { render, screen, fireEvent } from "@testing-library/react";
import axios from "axios";
import React from "react";
import * as router from "react-router-dom";
import BenchmarkScreen from "../Components/benchmarks/benchmark_screen";

describe("BenchmarkScreen", () => {
  const mockBenchmarks = [
    {
      algorithmName: "Algorithm 1",
      problemName: "Dataset 1",
      accuracyLearning: 0.8,
      accuracyTest: 0.9,
      lossTest: 0.1,
      time: 1000,
      maxLatency: 100,
      minLatency: 50,
      avgLatency: 75,
      latencyPercentile: 95,
    },
    {
      algorithmName: "Algorithm 2",
      problemName: "Dataset 2",
      accuracyLearning: 0.7,
      accuracyTest: 0.85,
      lossTest: 0.15,
      time: 2000,
      maxLatency: 200,
      minLatency: 100,
      avgLatency: 150,
      latencyPercentile: 90,
    },
  ];
  it("displays a table of benchmarks", () => {
    // Arrange

    jest.spyOn(axios, "post").mockResolvedValue({ data: mockBenchmarks });

    // Act
    render(<BenchmarkScreen />);

    // Assert
    expect(screen.getAllByRole("row").length).toBe(2); // 2 rows in the table (1 for each benchmark)
    expect(screen.getAllByRole("cell").length).toBe(18); // 2 rows * 9 columns
  });

  it("navigates to the main screen when the back button is clicked", () => {
    // Arrange
    jest.spyOn(axios, "post").mockResolvedValue({ data: mockBenchmarks });
    const navigate = jest.fn();
    jest.spyOn(router, "useNavigate").mockReturnValue(navigate);

    // Act
    render(<BenchmarkScreen />);
    fireEvent.click(screen.getByText("BACK"));

    // Assert
    expect(navigate).toHaveBeenCalledWith("/main");
  });
});
