import * as React from "react";
import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import TableCell from "@mui/material/TableCell";
import TableHead from "@mui/material/TableHead";
import TableRow from "@mui/material/TableRow";
import Button from "@mui/material/Button";
import { ChangeEvent, useEffect, useState } from "react";
import axios from "axios";
import { benchmarkGetEndpoint } from "../../constants";
import BenchmarkModel from "./benchmark_model";
import { Box, Menu, MenuItem, TextField } from "@mui/material";

const styles = {
  display: 'flex',
  alignItems: 'center',
  justifyContent: 'center',
};

const stylesLeft = {
  display: 'flex',
  alignItems: 'center',
  justifyContent: 'left',
};

const BenchmarkScreen: React.FC = () => {
  const [benchmarks, setbenchmarks] = useState([]);
  const [page, setPage] = useState(0);
  const [limit, setLimit] = useState(5);
  const [algorithmFilter, setAlgorithmFilter] = useState("");
  const [problemFilter, setProblemFilter] = useState("")
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
    getBenchmarkdata(newPage, newLimit, algorithmFilter, problemFilter);
  }
  const changePage = (increase: boolean) => {
    if (increase) {
      setPage(page + 1)
      getBenchmarkdata(page + 1, limit, algorithmFilter, problemFilter);
    }
    else {
      if (page > 0) {
        setPage(page - 1)
        getBenchmarkdata(page - 1, limit, algorithmFilter, problemFilter);
      }
      else {
        setPage(page)
        getBenchmarkdata(page, limit, algorithmFilter, problemFilter);
      }
    }

  }

  const filterByAlgorithm = (e: ChangeEvent<HTMLInputElement>) => {
    const searchedAlgorithm: string = e.target.value;
    setAlgorithmFilter(searchedAlgorithm);
    getBenchmarkdata(page, limit, searchedAlgorithm, problemFilter);
  }

  const filterByProblem = (e: ChangeEvent<HTMLInputElement>) => {
    const searchedProblem: string = e.target.value;
    setProblemFilter(searchedProblem)
    getBenchmarkdata(page, limit, algorithmFilter, searchedProblem);
  }


  const getBenchmarkdata = async (page: number, limit: number, algFilter: String, probFilter: String) => {
    let benchmarksPromise = axios.post(
      benchmarkGetEndpoint + "?page=" + page + "&limit=" + limit,
      {
        algorithmName: algFilter,
        problem: probFilter,
      },
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
    getBenchmarkdata(page, limit, algorithmFilter, problemFilter);
  }, []);

  return (
    <div style={styles}>
      <Box
        sx={{
          display: 'grid',
          gap: 3,
          gridTemplateRows: 'repeat(5)',
          width: '75%',
        }}
      >
        <div></div>
        <Box
          sx={{
            display: 'grid',
            gap: 1,
            gridTemplateColumns: 'repeat(2, 1fr)',
          }}>
          <TextField
            label="Filter by algorithm name"
            id="outlined-size-small"
            defaultValue="Filter by algorithm name"
            size="small"
            value={algorithmFilter}
            onChange={filterByAlgorithm}
          />

          <TextField
            label="Filter by problem name"
            id="outlined-size-small"
            defaultValue="Filter by problem name"
            size="small"
            value={problemFilter}
            onChange={filterByProblem}
          />
        </Box>

        <Table aria-label="simple table" sx={{width:'100%'}}>
          <TableHead>
            <TableRow>
              {ColumnArray.map((column) => (
                <TableCell><h3>{column}</h3></TableCell>
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


        
           <div style={stylesLeft}>    

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
      </Box >




    </div >
  );
};

export default BenchmarkScreen;
