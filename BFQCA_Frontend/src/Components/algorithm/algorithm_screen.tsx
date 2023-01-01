import React, { useEffect, useState } from "react";
import axios from "axios";
import "../styles.css";
import AlgorithmModel from "./algorthm_model";
import AddAlgorithmScreen from "./add_algorithm_screen";

import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import TableCell from "@mui/material/TableCell";
import TableContainer from "@mui/material/TableContainer";
import TableHead from "@mui/material/TableHead";
import TableRow from "@mui/material/TableRow";
import Paper from "@mui/material/Paper";
import Button from "@mui/material/Button";

import { algorithmExecuteEndpoint, algorithmsGetEndpoint } from "../../constants";
import { tokenSlice } from "../../redux_functions/security_token_slice";
import { Menu, MenuItem } from "@mui/material";



const MainScreen: React.FC = () => {
  const [algorithmNames, setAlgorithmNames] = useState([]);
  const [showAlgorithms, setShowAlgorithms] = useState(true);
  const [page, setPage] = useState(0);
  const [limit, setLimit] = useState(5);
  const [anchorEl, setAnchorEl] = React.useState<null | HTMLElement>(null);
  const limitOpen = Boolean(anchorEl);
  const ColumnArray = Array.from(AlgorithmModel.values());
  const AlgorithmNameDefinitons = Array.from(AlgorithmModel.keys());

  useEffect(() => {
    getAlgorithms(page, limit);
  }, []);


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
    getAlgorithms(newPage, newLimit);
  }

  const getAlgorithms = async (pageToget: number, limitToSet: number) => {
    let benchmarksPromise = axios.post(
      algorithmsGetEndpoint + "?page=" + pageToget + "&limit=" + limitToSet,
      {
        headers: {
          "Content-Type": "application/json",
          header1: 'Bearer ' + tokenSlice
        },
      }
    );
    await benchmarksPromise.then((response) => {
      setAlgorithmNames(response.data);
    });
    console.info(algorithmNames);
  };



  const changePage = (increase: boolean) => {
    if (increase) {
      setPage(page + 1)
      getAlgorithms(page + 1, limit);
    }
    else {
      if (page > 0) {
        setPage(page - 1)
        getAlgorithms(page - 1, limit);
      }
      else {
        setPage(page)
        getAlgorithms(page, limit);
      }
    }

  }

  const executeAlgorithm = (algName: string, probName: string) => {
    axios
      .post(
        algorithmExecuteEndpoint,
        {
          algorithmName: algName,
          problemName: probName,
        },
        {
          headers: {
            "Content-Type": "application/json",
            Authorization: "---",
          },
        }
      )
      .then((response: any) => {
        console.log(response);
      })
      .catch((err: any) => {
        alert(err);
      });
  };


  return (
    <div className="pageDivStyle">
      {showAlgorithms ?
        <div>
          <TableContainer sx={{ width: '75%' }} component={Paper}>
            <Table aria-label="simple table">
              <TableHead>
                <TableRow>
                  {ColumnArray.map((column) => (
                    <TableCell>{column}</TableCell>
                  ))}
                </TableRow>
              </TableHead>
              <TableBody>
                {algorithmNames.map((row: any) => (
                  <TableRow>
                    {AlgorithmNameDefinitons.map((ColumnName) => {
                      if (row[ColumnName] != null) {
                        //has this parameter
                        return <TableCell>{row[ColumnName]}</TableCell>;
                      }
                      else {
                        //artificial empty parameter for button
                        return <TableCell>
                          <Button
                            color="success"
                            variant="contained"
                            onClick={() => {
                              executeAlgorithm(row['algorithmName'], row['problemName']);
                            }}
                            sx={{ width: 200, margin: 2 }}>Execute
                          </Button>
                        </TableCell>
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
              setShowAlgorithms(false);
            }}
            sx={{ width: 300, height: 60, margin: 2 }}
          >
            Add new Algorithm
          </Button>



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
        :
        <AddAlgorithmScreen showAlgorithm={setShowAlgorithms} />
      }
    </div>

  );
};

export default MainScreen;
