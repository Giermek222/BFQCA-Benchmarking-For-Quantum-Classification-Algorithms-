import React, { useState } from "react";

import TextField from "@mui/material/TextField";
import Button from "@mui/material/Button";
import { useNavigate } from "react-router-dom";
import { userRegisterEndpoint } from "../../constants";
import axios from "axios";
import md5 from 'md5';

const RegisterSection: React.FC = () => {
  const navigate = useNavigate();

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
            onChange={(e) => {
              setEmail(e.target.value);
            }}
            style={{ padding: 10 }}
          />
        </div>


        <div className="input-group">
          <TextField
            variant="standard"
            type="password"
            name="password"
            className="login-input"
            placeholder="Password"
            onChange={(e) => {
              setPassword(e.target.value);
            }}
            style={{ padding: 10 }}
          />
        </div>
        <Button
          variant="contained"
          type="button"
          className="login-btn"
          style={{ margin: 10 }}
          onClick={() => {
            axios
              .post(
                userRegisterEndpoint,
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
              .catch((err: any) => {
                alert(err);
              });
          }}
        >
          Register
        </Button>
      </div>
    </div>
  );
};

export default RegisterSection;
