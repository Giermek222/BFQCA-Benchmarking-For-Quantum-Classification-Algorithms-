import * as React from "react";

import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import TableCell from "@mui/material/TableCell";
import TableContainer from "@mui/material/TableContainer";
import TableHead from "@mui/material/TableHead";
import TableRow from "@mui/material/TableRow";
import Paper from "@mui/material/Paper";
import Button from "@mui/material/Button";
import { useNavigate } from "react-router-dom";
import { useEffect, useState } from "react";
import axios from "axios";
import { benchmarkGetEndpoint } from "../constants";
function createData(
  algorithmName: string,
  dataset1: number,
  dataset2: number,
  dataset3: number
) {
  return { algorithmName, dataset1, dataset2, dataset3 };
}

const rows = [
  createData("Test Data - maybe GET didn't work", 78, 56, 90),
  createData("CNN with quantum layers", 34, 76, 78),
  createData("Quantum DNN", 12, 45, 32),
  createData("Quantum genetic algorithm", 43, 70, 67),
];
const ColumnsNames = new Map([
  ["algorithmName", "Algorithm"],
  ["problemName", "Dataset"],
  ["accuracyLearning", "Learning Accuracy"],
  ["accuracyTest", "Test Accuracy"],
  ["lossTest", "Test Loss"],
  ["time", "Time"],
  ["maxLatency", "Max Latency"],
  ["minLatency", "Min Latency"],
  ["avgLatency", "Avg Latency"],
  ["latencyPercentile", "Latency Percentile"],
]);
const ColumnArray = Array.from(ColumnsNames.values());
const BenchmarkNameDefinitons = Array.from(ColumnsNames.keys());
const BenchmarkScreen: React.FC = () => {
  const [benchmarks, setbenchmarks] = useState([]);
  const getBenchmarkdata = async () => {
    let benchmarksPromise = axios.post(
      benchmarkGetEndpoint + "?page=0&limit=5000",
      {
        headers: {
          "Content-Type": "application/json",
          Authorization: "---",
        },
      }
    );

    await benchmarksPromise.then((response) => {
      setbenchmarks(response.data);
    });
  };

  useEffect(() => {
    getBenchmarkdata();
  }, []);

  const navigate = useNavigate();
  return (
    <div>
      <TableContainer component={Paper}>
        <Table sx={{ minWidth: 650 }} aria-label="simple table">
          <TableHead>
            <TableRow>
              {ColumnArray.map((column) => (
                <TableCell>{column}</TableCell>
              ))}
            </TableRow>
          </TableHead>
          <TableBody>
            {benchmarks.map((row: any) => (
              <TableRow>
                {BenchmarkNameDefinitons.map((ColumnName) => {
                  console.info(ColumnName);

                  console.info(row);

                  if (row[ColumnName] != null) {
                    //has this parameter
                    return <TableCell>{row[ColumnName]}</TableCell>;
                  } else {
                    //this parameter is missing
                    return <TableCell>---</TableCell>;
                  }
                })}
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
      <Button
        variant="contained"
        onClick={() => {
          navigate("/main");
        }}
        sx={{ width: 300, margin: 2 }}
      >
        BACK
      </Button>
    </div>
  );
};

export default BenchmarkScreen;
