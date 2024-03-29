import React, { ChangeEvent, useEffect, useState } from "react";

import TextField from "@mui/material/TextField";
import Button from "@mui/material/Button";
import "../styles.css";
import { algorithmExecuteEndpoint, datasetEndpoint } from "../../constants";
import axios from "axios";
import { Box, Menu, MenuItem } from "@mui/material";
import { useNavigate } from "react-router-dom";

const styles = {
  display: "flex",
  alignItems: "center",
  justifyContent: "center",
};

type Props = {
  userName: string;
};

const AddAlgorithmScreen: React.FC<Props> = ({ userName }) => {
  const navigate = useNavigate();
  const [algName, setAlgName] = useState("");
  const [problemName, setProblemName] = useState("");
  const [problemDescription, setProblemDescription] = useState("");
  const [description, setDescription] = useState("");
  const [code, setCode] = useState("");
  const [anchorEl, setAnchorEl] = React.useState<null | HTMLElement>(null);
  const limitOpen = Boolean(anchorEl);

  const [datasets, setDatasets] = useState<string[]>([]);

  useEffect(() => {
    axios
      .get(datasetEndpoint, {
        headers: {
          "Content-Type": "application/json",
          Authorization: "---",
        },
      })
      .then((response) => {
        setDatasets(response.data);
      });
  }, []);

  const onChangeAlgorithmName = (e: ChangeEvent<HTMLInputElement>) => {
    const searchTitle: string = e.target.value;
    setAlgName(searchTitle);
  };

  const onChangeDescription = (e: ChangeEvent<HTMLInputElement>) => {
    const searchTitle: string = e.target.value;
    setDescription(searchTitle);
  };

  const onChangeCode = (e: ChangeEvent<HTMLInputElement>) => {
    const searchTitle: string = e.target.value;
    setCode(searchTitle);
  };

  const sendNewAlgorithm = () => {
    axios
      .post(
        algorithmExecuteEndpoint,
        {
          algorithmName: algName !== "" ? algName : null,
          description: description !== "" ? description : null,
          problemName: problemName !== "" ? problemName : null,
          code: code !== "" ? code : null,
          userName: userName,
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

  const handleLimitClick = (event: React.MouseEvent<HTMLButtonElement>) => {
    setAnchorEl(event.currentTarget);
  };

  const handleLimitClose = () => {
    setAnchorEl(null);
  };

  // @ts-ignore
  // @ts-ignore
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
        <div>
          Selected Problem:
          <Button
            id="basic-button"
            aria-controls={limitOpen ? "basic-menu" : undefined}
            aria-haspopup="true"
            aria-expanded={limitOpen ? "true" : undefined}
            onClick={handleLimitClick}
          >
            {problemDescription === "" ? "Click to select" : problemDescription}
          </Button>
          <Menu
            id="basic-menu"
            anchorEl={anchorEl}
            open={limitOpen}
            onClose={handleLimitClose}
            MenuListProps={{
              "aria-labelledby": "basic-button",
            }}
          >
            {datasets.map((dataset: string) => (
              <MenuItem
                onClick={() => {
                  setProblemName(dataset);
                  setProblemDescription(dataset + "Dataset");
                  handleLimitClose();
                }}
              >
                {dataset}
              </MenuItem>
            ))}
          </Menu>
        </div>

        <TextField
          label="Algorithm name"
          id="outlined-size-small"
          defaultValue="Algorithm name"
          size="small"
          value={algName}
          onChange={onChangeAlgorithmName}
        />

        <TextField
          label="Algorithm Description"
          id="outlined-size-small"
          defaultValue="Algorithm name"
          size="small"
          multiline
          rows={4}
          value={description}
          onChange={onChangeDescription}
        />

        <TextField
          label="Code"
          id="outlined-size-small"
          defaultValue="Algorithm name"
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
export default AddAlgorithmScreen;
