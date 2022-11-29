import * as React from "react";

import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import TableCell from "@mui/material/TableCell";
import TableContainer from "@mui/material/TableContainer";
import TableHead from "@mui/material/TableHead";
import TableRow from "@mui/material/TableRow";
import Paper from "@mui/material/Paper";

function createData(
  algorithmName: string,
  dataset1: number,
  dataset2: number,
  dataset3: number
) {
  return { algorithmName, dataset1, dataset2, dataset3 };
}

const rows = [
  createData("Quantum KNN", 78, 56, 90),
  createData("CNN with quantum layers", 34, 76, 78),
  createData("Quantum DNN", 12, 45, 32),
  createData("Quantum genetic algorithm", 43, 70, 67),
];

const BenchmarkScreen: React.FC = () => {
  return (
    <TableContainer component={Paper}>
      <Table sx={{ minWidth: 650 }} aria-label="simple table">
        <TableHead>
          <TableRow>
            <TableCell>Algorithms</TableCell>
            <TableCell align="right">Irises</TableCell>
            <TableCell align="right">Digits</TableCell>
            <TableCell align="right">Dogs vs Cats</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {rows.map((row) => (
            <TableRow
              key={row.algorithmName}
              sx={{ "&:last-child td, &:last-child th": { border: 0 } }}
            >
              <TableCell component="th" scope="row">
                {row.algorithmName}
              </TableCell>
              <TableCell align="right">{row.dataset1}%</TableCell>
              <TableCell align="right">{row.dataset3}%</TableCell>
              <TableCell align="right">{row.dataset2}%</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
};

export default BenchmarkScreen;
