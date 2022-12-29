import React, { useEffect, useState } from "react";
import axios from "axios";
import "./styles.css";
import {
  Grid,
  TextField,
  Button,
  Select,
  MenuItem,
  FormHelperText,
  InputLabel,
  FormControl,
  Card,
  CardContent,
  CardActions,
  Typography,
} from "@mui/material";

import g1 from "../images/graph1.png";
import g2 from "../images/graph2.png";
import { useNavigate } from "react-router-dom";
import { algorithmExecuteEndpoint, algorithmsGetEndpoint } from "../constants";
const MainScreen: React.FC = () => {
  const [algorithmNames, setAlgorithmNames] = useState([]);
  const [chosenAlgorithm, setChosenAlgorithm] = useState("QKNN_DEFAULT");
  let algorithmIndex = 0;
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

  const buttonHandler = (algName: string) => {
    axios
      .post(
        algorithmExecuteEndpoint,
        {
          algorithmName: algName,
          description: "default description",
          problemName: "Irises",
          code: "fallus",
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

  const navigate = useNavigate();
  return (
    <Grid container style={{ height: "100vh", justifyContent: "flex-start" }}>
      {/* <Grid item xs={4}></Grid> */}
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
  );
};

export default MainScreen;
