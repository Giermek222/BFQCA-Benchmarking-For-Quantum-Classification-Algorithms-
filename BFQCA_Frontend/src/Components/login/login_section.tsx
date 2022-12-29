import React, { useState } from "react";

import TextField from "@mui/material/TextField";
import Button from "@mui/material/Button";
import { setTokenValue } from "../../redux_functions/security_token_slice";
import { userLoginEndpoint } from "../../constants";
import axios from "axios";
import md5 from 'md5';

type Props = {
  logged: (value: boolean) => void;
};

const LoginSection: React.FC<Props> = ({ logged }) => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");


  return (
    <div className="inner-container">
      <div className="box">
        <div className="input-group">
          <TextField
            variant="standard"
            type="text"
            name="username"
            className="login-input"
            placeholder="Username"
            style={{ padding: 10 }}
            onChange={(e) => {
              setEmail(e.target.value);
            }}
          />
        </div>
        <div className="input-group">
          <TextField
            variant="standard"
            type="password"
            name="password"
            className="login-input"
            placeholder="Password"
            style={{ padding: 10 }}
            onChange={(e) => {
              setPassword(e.target.value);
            }}
          />
        </div>

        <Button
          type="button"
          className="login-btn"
          variant="contained"
          style={{ margin: 10 }}
          onClick={() => {
            axios
              .post(
                userLoginEndpoint,
                {
                  username: email,
                  password: md5(password),
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
                if (response.status === 200) {
                  logged(true);
                  setTokenValue(response.data)
                }
              })
              .catch((err: any) => {
                alert(err);
              });
          }}
        >
          Login
        </Button>
      </div>
    </div>
  );
};

export default LoginSection;
