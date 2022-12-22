import React, { useState } from "react";

import TextField from "@mui/material/TextField";
import Button from "@mui/material/Button";
import { useNavigate } from "react-router-dom";
import { setTokenValue } from "../redux_functions/security_token_slice";
import { userLoginEndpoint } from "../constants";
import axios from "axios";

const LoginSection: React.FC = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();
  const submitLogin = () => {
    // navigate("/main");
    setTokenValue(1);
  };
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
                  password: password,
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
                  navigate("/main");
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
