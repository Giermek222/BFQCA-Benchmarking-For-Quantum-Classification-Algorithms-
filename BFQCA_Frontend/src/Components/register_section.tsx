import React from "react";

import TextField from "@mui/material/TextField";
import Button from "@mui/material/Button";
import { useNavigate } from "react-router-dom";

const RegisterSection: React.FC = () => {
  const navigate = useNavigate();

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
          />
        </div>

        <div className="input-group">
          <TextField
            variant="standard"
            type="text"
            name="email"
            className="login-input"
            placeholder="Email"
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
            style={{ padding: 10 }}
          />
        </div>
        <Button
          variant="contained"
          type="button"
          className="login-btn"
          style={{ margin: 10 }}
          onClick={() => {
            navigate("/main");
          }}
        >
          Register
        </Button>
      </div>
    </div>
  );
};

export default RegisterSection;
