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
import TextField from "@mui/material/TextField";

const divStyle = {
  display: 'flex',
  alignItems: 'center'
};

const ColumnArray = Array.from(AlgorithmModel.values());
const AlgorithmNameDefinitons = Array.from(AlgorithmModel.keys());

const MainScreen: React.FC = () => {
  const [algorithmNames, setAlgorithmNames] = useState([]);
  const [showAlgorithms, setShowAlgorithms] = useState(true)

  const getAlgorithms = async () => {
    let benchmarksPromise = axios.post(
      algorithmsGetEndpoint + "?page=0&limit=5000",
      {
        headers: {
          "Content-Type": "application/json",
          Authorization: "---",
        },
      }
    );
    await benchmarksPromise.then((response) => {
      setAlgorithmNames(response.data);
    });
    console.info(algorithmNames);
  };

  useEffect(() => {
    getAlgorithms();
  }, []);

  const buttonHandler = (algName: string, probName: string) => {
    axios
      .post(
        algorithmExecuteEndpoint,
        {
          algorithmName: algName,
          description: "default description",
          problemName: probName,
          code: "",
          params: [],
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
    <div>
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
                              buttonHandler(row['algorithmName'], row['problemName']);
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
        </div>
        :
        <div>
          <AddAlgorithmScreen/>
          <div>
            <div style={divStyle}>
              <div>Algorithm Name </div> <TextField variant="outlined" />
            </div>
            <div style={divStyle}>
              <div>Problem Name </div><TextField  variant="outlined" />
            </div>
            <div style={divStyle}>
              <div>Description </div> <TextField   variant="outlined" />
            </div>
            <div style={divStyle}>
              <div>Code </div> <TextField   variant="outlined" />
            </div>
          </div>
          <Button            
            variant="contained"
            onClick={() => {
              setShowAlgorithms(true);
            }}
            sx={{ width: 300, height: 60, margin: 2 }}>
            Sumbmit
          </Button>
        </div>
      }
    </div>





    /*
    <Grid container style={{ height: "100vh", justifyContent: "flex-start" }}>
      { <Grid item xs={4}></Grid> }
      {algorithmNames.map((algorithm) => (
        <Grid container xs={12}>
          <Card
            sx={{
              minWidth: "100%",
              maxHeight: 90,
            }}
          >
            <CardContent>
              <CardActions sx={{ justifyContent: "space-between" }}>
                <Typography variant="h4" sx={{ width: 400 }}>
                  {algorithm["algorithmName"]}
                </Typography>

                <Typography variant="h5" align="center" sx={{ width: 400 }}>
                  {algorithm["problemName"]}
                </Typography>

                <Button
                  color="success"
                  variant="contained"
                  onClick={() => {
                    buttonHandler(algorithm["algorithmName"]);
                  }}
                  sx={{ width: 200, margin: 2 }}
                >
                  RUN
                </Button>
              </CardActions>
            </CardContent>
          </Card>
        </Grid>
      ))}
      <Button
        variant="contained"
        onClick={() => {
          navigate("/benchmark");
        }}
        sx={{ width: 300, height: 60, margin: 2 }}
      >
        BENCHMARK
      </Button>
    </Grid>
    */
  );
};

export default MainScreen;
