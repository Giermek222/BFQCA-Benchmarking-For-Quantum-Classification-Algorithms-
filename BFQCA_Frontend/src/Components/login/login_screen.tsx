import React, { useState } from "react";
import { Grid } from "@mui/material";
import { Container } from "@mui/system";
import Button from "@mui/material/Button";
import TextField from "@mui/material/TextField";
import bg from "../../images/blue.png";
import LoginSection from "./login_section";
import RegisterSection from "./register_section";
import RadioGroup from "@mui/material/RadioGroup";
import Divider from "@mui/material/Divider";

const lightBlue = "#1976D2";
var fontStyle = "serif";
type Props = {
  logged: (value: boolean) => void;
  setUserName: (value: string) => void
};

const LoginScreen: React.FC<Props> = ({ logged, setUserName }) => {
  // Set slices for login data
  const handleLogin = async (event: any) => {};
  const [isLoginOpen, setIsLoginOpen] = useState(true);

  return (
    <div>
      <Grid container style={{ minHeight: "100vh" }}>
        <Grid item xs={12} sm={6}>
          <div className="head-text">
            <div className="head-image">
              <img
                data-testid="background-img"
                src={bg}
                style={{ width: "100%", height: "100vh", objectFit: "cover" }}
                alt="brand"
              />
            </div>
            <div
              style={{
                position: "absolute",
                right: "90%",
                left: "10%",
                bottom: "50%",
              }}
            >
              <label
                style={{
                  fontSize: 100,
                  fontWeight: "bold",
                  color: "white",
                  fontFamily: fontStyle,
                }}
              >
                Q
              </label>
              <label
                style={{
                  fontSize: 25,
                  fontWeight: "bold",
                  color: "white",
                  fontFamily: fontStyle,
                }}
              >
                UANTUM
                <br />
              </label>
              <label
                style={{
                  fontSize: 25,
                  fontWeight: "bold",
                  color: "white",
                  fontFamily: fontStyle,
                }}
              >
                BENCHMARKING
              </label>
            </div>
          </div>
        </Grid>
        <Grid
          container
          xs={12}
          sm={6}
          alignItems="center"
          direction="column"
          style={{ padding: 10, paddingTop: 80 }}
        >
          <div />
          <div
            style={{
              display: "flex",
              flexDirection: "column",
              maxWidth: 400,
              minWidth: 300,
            }}
          >
            <Grid container>
              {/* <img data-testid="logo-img" src={logo} width={300} alt="logo" /> */}
            </Grid>

            <Grid container>
              <Grid item xs={6}>
                <div
                  className={
                    "controller " + (isLoginOpen ? "selected-controller" : "")
                  }
                  onClick={() => setIsLoginOpen(true)}
                >
                  <div
                    style={{
                      display: "flex",
                      justifyContent: "space-evenly",
                      flexDirection: "column",
                    }}
                  >
                    <label
                      style={{
                        textAlign: "center",
                        color: isLoginOpen ? lightBlue : "grey",
                        fontSize: 20,
                        fontWeight: "bold",
                      }}
                    >
                      LOGIN
                    </label>
                    {isLoginOpen ? (
                      <Divider
                        style={{
                          backgroundColor: lightBlue,
                          height: 2,
                        }}
                      />
                    ) : null}
                  </div>
                </div>
              </Grid>
              <Grid item xs={6}>
                <div
                  className={
                    "controller " + (!isLoginOpen ? "selected-controller" : "")
                  }
                  onClick={() => setIsLoginOpen(false)}
                >
                  <div
                    style={{
                      display: "flex",
                      justifyContent: "space-evenly",
                      flexDirection: "column",
                    }}
                  >
                    <label
                      style={{
                        textAlign: "center",
                        color: isLoginOpen ? "grey" : lightBlue,
                        fontSize: 20,
                        fontWeight: "bold",
                      }}
                    >
                      Register
                    </label>
                    {isLoginOpen ? null : (
                      <Divider
                        style={{
                          backgroundColor: lightBlue,
                          height: 2,
                        }}
                      />
                    )}
                  </div>
                </div>
              </Grid>
            </Grid>
            <Grid item xs={12}>
              <div
                style={{
                  paddingTop: 80,
                  minWidth: 240,
                }}
              >
                <label
                  style={{
                    textAlign: "center",
                    display: "inline-block",
                    fontSize: 20,
                    justifySelf: "center",
                    width: "100%",
                  }}
                >
                  Hello, fellow scientist.
                  <br />
                  Please sign in
                </label>
              </div>
            </Grid>
            <div
              className="box-container"
              style={{
                display: "flex",
                justifyContent: "center",
                alignItems: "center",
                height: "50vh",
              }}
            >
              {isLoginOpen ? <LoginSection logged={logged} setUserName={setUserName} /> : <RegisterSection/>}
            </div>
          </div>
          <div />
        </Grid>
      </Grid>
    </div>
  );
};
export default LoginScreen;
