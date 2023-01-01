import React, { ChangeEvent, useState } from "react";

import TextField from "@mui/material/TextField";
import Button from "@mui/material/Button";
import { setTokenValue } from "../../redux_functions/security_token_slice";
import { algorithmExecuteEndpoint, userLoginEndpoint } from "../../constants";
import axios from "axios";

const divStyle = {
  display: 'flex',
  alignItems: 'center'
};

type Props = {
  showAlgorithm: (value: boolean) => void;
};

const AddAlgorithmScreen: React.FC<Props> = ({ showAlgorithm }) => {
  const [algName, setAlgName] = useState("");
  const [problemName, setProblemName] = useState("");
  const [description, setDescription] = useState("");
  const [code, setCode] = useState("");

  const onChangeAlgorithmName = (e: ChangeEvent<HTMLInputElement>) => {
    const searchTitle: string = e.target.value;
    setAlgName(searchTitle);
  };

  const onChangeProblemName = (e: ChangeEvent<HTMLInputElement>) => {
    const searchTitle: string = e.target.value;
    setProblemName(searchTitle);
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
      <div style={divStyle}>
        <div>Algorithm Name </div> <TextField variant="outlined"
          value={algName}
          onChange={onChangeAlgorithmName} />
      </div>
      <div style={divStyle}>
        <div>Problem Name </div><TextField variant="outlined"
          value={problemName}
          onChange={onChangeProblemName} />
      </div>
      <div style={divStyle}>
        <div>Description </div>
        <TextField 
          variant="outlined"
          value={description}
          onChange={onChangeDescription} />
      </div>
      <div style={divStyle}>
        <div>Code </div> <TextField variant="outlined"
          value={code}
          onChange={onChangeCode} />
      </div>
      <div style={divStyle}>
      <Button
        variant="contained"
        onClick={() => {
          sendNewAlgorithm()
          showAlgorithm(true);
        }}
        sx={{ width: 300, height: 60, margin: 2 }}>
        Sumbmit
      </Button>
      <Button
        variant="contained"
        onClick={() => {
          showAlgorithm(true);
        }}
        sx={{ width: 300, height: 60, margin: 2 }}>
        Back
      </Button>
      </div>

    </div>
  );
};
export default AddAlgorithmScreen;