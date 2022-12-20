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
