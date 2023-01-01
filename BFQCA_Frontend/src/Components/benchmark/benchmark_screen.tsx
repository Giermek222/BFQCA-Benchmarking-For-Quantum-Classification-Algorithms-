import * as React from "react";
import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import TableCell from "@mui/material/TableCell";
import TableContainer from "@mui/material/TableContainer";
import TableHead from "@mui/material/TableHead";
import TableRow from "@mui/material/TableRow";
import Paper from "@mui/material/Paper";
import Button from "@mui/material/Button";
import { useEffect, useState } from "react";
import axios from "axios";
import { benchmarkGetEndpoint } from "../../constants";
import { tokenSlice } from "../../redux_functions/security_token_slice";
import BenchmarkModel from "./benchmark_model";
import { Menu, MenuItem } from "@mui/material";



const BenchmarkScreen: React.FC = () => {
  const [benchmarks, setbenchmarks] = useState([]);
  const [page, setPage] = useState(0);
  const [limit, setLimit] = useState(5);
  const [anchorEl, setAnchorEl] = React.useState<null | HTMLElement>(null);
  const limitOpen = Boolean(anchorEl);
  const ColumnArray = Array.from(BenchmarkModel.values());
  const BenchmarkNameDefinitons = Array.from(BenchmarkModel.keys());

  const handleLimitClick = (event: React.MouseEvent<HTMLButtonElement>) => {
    setAnchorEl(event.currentTarget);
  };
  const handleLimitClose = () => {
    setAnchorEl(null);
  };
  const setNewLimitTo5 = () => {
    SetNewLimit(5);
    handleLimitClose();
  }
  const setNewLimitTo10 = () => {
    SetNewLimit(10)
    handleLimitClose();
  }
  const setNewLimitTo20 = () => {
    SetNewLimit(20);
    handleLimitClose();
  }

  const SetNewLimit = (newLimit: number) => {
    let currentlyShownAlgorithm = page * limit;
    let newPage = Math.floor(currentlyShownAlgorithm / newLimit);
    setPage(newPage);
    setLimit(newLimit);
    getBenchmarkdata(newPage, newLimit);
  }
  const changePage = (increase: boolean) => {
    if (increase) {
      setPage(page + 1)
      getBenchmarkdata(page + 1, limit);
    }
    else {
      if (page > 0) {
        setPage(page - 1)
        getBenchmarkdata(page - 1, limit);
      }
      else {
        setPage(page)
        getBenchmarkdata(page, limit);
      }
    }

  }


  const getBenchmarkdata = async (page: number, limit: number) => {
    let benchmarksPromise = axios.post(
      benchmarkGetEndpoint + "?page=" + page + "&limit=" + limit,
      {
        headers: {
          "Content-Type": "application/json",
          "Security-Token": tokenSlice.name,
          Authorization: "---",
        },
      }
    );

    await benchmarksPromise.then((response) => {
      setbenchmarks(response.data);
    });
  };

  useEffect(() => {
    getBenchmarkdata(page, limit);
  }, []);

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

      <div className="columnDivStyle">
        <Button
          variant="contained"
          onClick={() => {
            changePage(false)
          }}
          sx={{ width: 75, height: 20, margin: 2 }}

        >
          previous
        </Button>
        page : {page}
        <Button
          variant="contained"
          onClick={() => {
            changePage(true)
          }}
          sx={{ width: 75, height: 20, margin: 2 }}
        >
          next
        </Button>
        <div>
          <Button
            id="basic-button"
            aria-controls={limitOpen ? 'basic-menu' : undefined}
            aria-haspopup="true"
            aria-expanded={limitOpen ? 'true' : undefined}
            onClick={handleLimitClick}
          >
            Set Limit
          </Button>
          <Menu
            id="basic-menu"
            anchorEl={anchorEl}
            open={limitOpen}
            onClose={handleLimitClose}
            MenuListProps={{
              'aria-labelledby': 'basic-button',
            }}
          >
            <MenuItem onClick={setNewLimitTo5}>5 algorithms per page:</MenuItem>
            <MenuItem onClick={setNewLimitTo10}>10 algorithms per page:</MenuItem>
            <MenuItem onClick={setNewLimitTo20}>20 algorithms per page:</MenuItem>
          </Menu>
        </div>
      </div>
    </div>
  );
};

export default BenchmarkScreen;
