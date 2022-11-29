import React from "react";

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
} from "@mui/material";

import g1 from "../images/graph1.png";
import g2 from "../images/graph2.png";
import { useNavigate } from "react-router-dom";

const MainScreen: React.FC = () => {
  let handleSelect = () => {};
  const navigate = useNavigate();
  return (
    <Grid container style={{ height: "100vh" }}>
      <Grid xs={6}>
        <Grid xs={6} padding={1}>
          <FormControl sx={{ m: 1, minWidth: 240 }}>
            <InputLabel id="label1">Choose Algorithm</InputLabel>
            <Select
              label="Choose Algorithm"
              labelId="label1"
              id="id1"
              onChange={handleSelect}
            >
              <MenuItem value={1}>Quantum KNN</MenuItem>
              <MenuItem value={2}>Quantum CNN</MenuItem>
            </Select>
          </FormControl>
        </Grid>
        <Grid xs={6} padding={1}>
          <FormControl sx={{ m: 1, minWidth: 240 }}>
            <InputLabel id="label2">Choose Dataset</InputLabel>
            <Select
              label="Choose Dataset"
              labelId="label2"
              id="id2"
              onChange={handleSelect}
            >
              <MenuItem value={1}>Irises</MenuItem>
              <MenuItem value={2}>Digits</MenuItem>
            </Select>
          </FormControl>
        </Grid>
        <Grid xs={6} padding={1}>
          <Card sx={{ minWidth: 270 }}>
            <CardContent>
              <FormControl sx={{ m: 1, minWidth: 240 }}>
                <InputLabel id="label3">Choose Parameter 1</InputLabel>
                <Select labelId="label3" id="id3" onChange={handleSelect}>
                  <MenuItem value={1}>4 Neighbours</MenuItem>
                  <MenuItem value={2}>8 Neighbours</MenuItem>
                </Select>
              </FormControl>
            </CardContent>
            <CardContent>
              <FormControl sx={{ m: 1, minWidth: 240 }}>
                <InputLabel id="label4">Choose Parameter 2</InputLabel>
                <Select labelId="label4" id="id4" onChange={handleSelect}>
                  <MenuItem value={3}>1 dataset parameter1</MenuItem>
                  <MenuItem value={1}>3 dataset parameters</MenuItem>
                  <MenuItem value={2}>4 dataset parameters</MenuItem>
                </Select>
              </FormControl>
            </CardContent>
            <CardContent>
              <FormControl sx={{ m: 1, minWidth: 240 }}>
                <InputLabel id="label5">Choose Parameter 3</InputLabel>
                <Select labelId="label5" id="id5" onChange={handleSelect}>
                  <MenuItem value={1}>Float8</MenuItem>
                  <MenuItem value={2}>Float32</MenuItem>
                </Select>
              </FormControl>
            </CardContent>
          </Card>
        </Grid>

        <Grid xs={6} padding={1}>
          <Card sx={{ minWidth: 270 }}>
            <CardContent>
              <label>Available virtual machines: 3</label>
            </CardContent>
            <CardContent>
              <label>Running virtual machines: 0</label>
            </CardContent>
          </Card>
        </Grid>
        <Grid xs={6} padding={1} container minWidth={270}>
          <div
            style={{
              display: "flex",
              alignItems: "justify",
              justifyContent: "center",
              width: "270px",
            }}
          >
            <Button color="success" variant="contained" fullWidth={true}>
              RUN
            </Button>
            <Button color="error" variant="contained" fullWidth={true}>
              STOP
            </Button>
          </div>
        </Grid>
      </Grid>

      <Grid xs={6}>
        <img
          data-testid="background-img1"
          src={g1}
          style={{ width: "430px" }}
          alt="brand"
        />
        <img
          data-testid="background-img1"
          src={g2}
          style={{ width: "430px" }}
          alt="brand"
        />
        <Button
          variant="contained"
          onClick={() => {
            navigate("/benchmark");
          }}
          sx={{ width: 300, margin: 2 }}
        >
          BENCHMARK
        </Button>
      </Grid>
    </Grid>
  );
};

export default MainScreen;
