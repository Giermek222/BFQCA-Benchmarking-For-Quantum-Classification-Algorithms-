import React, { ChangeEvent, useState } from "react";

import TextField from "@mui/material/TextField";
import Button from "@mui/material/Button";
import "../styles.css";
import { algorithmExecuteEndpoint } from "../../constants";
import axios from "axios";
import { Menu, MenuItem } from "@mui/material";

const styles = {
  display: 'flex',
  alignItems: 'center',
  justifyContent: 'center',
  
};

type Props = {
  showAlgorithm: (value: boolean) => void;
  userName: string
};

const AddAlgorithmScreen: React.FC<Props> = ({ showAlgorithm, userName }) => {
  const [algName, setAlgName] = useState("");
  const [problemName, setProblemName] = useState("");
  const [problemDescription, setProblemDescription] = useState("")
  const [description, setDescription] = useState("");
  const [code, setCode] = useState("");
  const [anchorEl, setAnchorEl] = React.useState<null | HTMLElement>(null);
  const limitOpen = Boolean(anchorEl);

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
          userName: userName
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

  const setProblemToPenguins = () => {
    setProblemName("Palmer Penguin")
    setProblemDescription("Palmer Penguin")
    handleLimitClose()
  }
  const setProblemToIris = () => {
    setProblemName("Iris")
    setProblemDescription("Iris")
    handleLimitClose()
  }
  const setProblemToDiabetes = () => {
    setProblemName("Pima Indians Diabetic")
    setProblemDescription("Pima Indians Diabetic")
    handleLimitClose()
  }

  const handleLimitClose = () => {
    setAnchorEl(null);
  };

  return (
    <div >
      <div >

        Selected Problem:
        <Button
          id="basic-button"
          aria-controls={limitOpen ? 'basic-menu' : undefined}
          aria-haspopup="true"
          aria-expanded={limitOpen ? 'true' : undefined}
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
            'aria-labelledby': 'basic-button',
          }}
        >
          <MenuItem onClick={setProblemToIris}>Iris</MenuItem>
          <MenuItem onClick={setProblemToPenguins}>Palmer Penguin</MenuItem>
          <MenuItem onClick={setProblemToDiabetes}>Pima Indians Diabetic</MenuItem>
        </Menu>
      </div>
      <div className="columnDivStyle">
        <TextField
          label="Algorithm name"
          id="outlined-size-small"
          defaultValue="Algorithm name"
          size="small"
          value={algName}
          onChange={onChangeAlgorithmName}
        />
      </div>

      <div className="columnDivStyle">
        <TextField
          label="Algorithm Description"
          id="outlined-size-small"
          defaultValue="Algorithm name"
          size="small"
          value={description}
          onChange={onChangeDescription}
        />

      </div>
      <div className="columnDivStyle">
        <TextField
          label="Code"
          id="outlined-size-small"
          defaultValue="Algorithm name"
          size="small"
          value={code}
          onChange={onChangeCode}
        />


      </div>
      <div className="columnDivStyle">
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