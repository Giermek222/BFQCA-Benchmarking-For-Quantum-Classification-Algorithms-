import React from "react";

import TextField from "@mui/material/TextField";
import Button from "@mui/material/Button";

class RegisterSection extends React.Component {
  submitRegister() {}

  render() {
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
            onClick={this.submitRegister.bind(this)}
          >
            Register
          </Button>
        </div>
      </div>
    );
  }
}

export default RegisterSection;
