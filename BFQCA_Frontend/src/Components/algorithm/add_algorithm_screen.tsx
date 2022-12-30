import React, { useState } from "react";

import TextField from "@mui/material/TextField";
import Button from "@mui/material/Button";
import { setTokenValue } from "../../redux_functions/security_token_slice";
import { userLoginEndpoint } from "../../constants";
import axios from "axios";
import md5 from 'md5';

const divStyle = {
  display: 'flex',
  alignItems: 'center'
};

type Props = {
  showAlgorithm: (value: boolean) => void;
};

const addAlgorithmScreen:  React.FC<Props> = ({ showAlgorithm }) => {

  return (
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
          
          <Button            
            variant="contained"
            onClick={() => {
              showAlgorithm(true);
            }}
            sx={{ width: 300, height: 60, margin: 2 }}>
            Sumbmit
          </Button>
    </div>
  );
};
export default addAlgorithmScreen;