import React, { ChangeEvent, useState } from "react";

import TextField from "@mui/material/TextField";
import Button from "@mui/material/Button";
import "../styles.css";
import { datasetEndpoint } from "../../constants";
import axios from "axios";
import { Box } from "@mui/material";
import { useNavigate } from "react-router-dom";

const styles = {
  display: "flex",
  alignItems: "center",
  justifyContent: "center",
};

type Props = {
  userName: string;
};

const AddDatasetScreen: React.FC<Props> = ({ userName }) => {
  let navigate = useNavigate();
  const [problemName, setProblemName] = useState("");
  const [code, setCode] = useState("");

  const onChangeDatasetName = (e: ChangeEvent<HTMLInputElement>) => {
    const searchTitle: string = e.target.value;
    setProblemName(searchTitle);
  };

  const onChangeCode = (e: ChangeEvent<HTMLInputElement>) => {
    const searchTitle: string = e.target.value;
    setCode(searchTitle);
  };

  const sendNewAlgorithm = () => {
    axios
      .post(
        datasetEndpoint,
        {
          datasetName: problemName !== "" ? problemName : null,
          datasetCode: code !== "" ? code : null,
          userName: userName,
        },

        {
          headers: {
            "Content-Type": "application/json",
            Authorization: "---",
          },
        }
      )
      .then((response: any) => {})
      .catch((err: any) => {
        alert(err);
      });
  };
  const styles = {
    paddingTop: "50px",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
  };

  return (
    <div style={styles}>
      <Box
        sx={{
          display: "grid",
          gap: 1,
          gridTemplateRows: "repeat(5)",
          width: "75%",
        }}
      >
        <TextField
          label="Dataset name"
          id="datasetNameTF"
          defaultValue="Dataset name"
          size="small"
          value={problemName}
          onChange={onChangeDatasetName}
        />

        <TextField
          label="Code"
          id="codeTF"
          defaultValue="Code for generating datasets"
          size="small"
          value={code}
          multiline
          rows={10}
          onChange={onChangeCode}
        />

        <Box
          sx={{
            display: "grid",
            gap: 1,
            gridTemplateColumns: "repeat(2, 1fr)",
          }}
        >
          <Button
            variant="contained"
            color="success"
            onClick={() => {
              sendNewAlgorithm();
              navigate(-1);
            }}
            sx={{ width: 300, height: 60, margin: 2 }}
          >
            Sumbmit
          </Button>
          <Button
            variant="contained"
            color="error"
            onClick={() => {
              navigate(-1);
            }}
            sx={{ width: 300, height: 60, margin: 2 }}
          >
            Back
          </Button>
        </Box>
      </Box>
    </div>
  );
};
export default AddDatasetScreen;
