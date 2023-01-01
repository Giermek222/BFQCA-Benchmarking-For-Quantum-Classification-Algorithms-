import "../styles.css";
import axios from "axios";
import AlgorithmModel from "./algorthm_model";
import AlgorithmScreen from "./algorithm_screen";
import React, { ChangeEvent, useEffect, useState } from "react";
import { tokenSlice } from "../../redux_functions/security_token_slice";
import { algorithmExecuteEndpoint, algorithmsGetEndpoint } from "../../constants";



const MainScreen: React.FC = () => {
  const [algorithmNames, setAlgorithmNames] = useState([]);
  const [showAlgorithms, setShowAlgorithms] = useState(true);
  const [page, setPage] = useState(0);
  const [limit, setLimit] = useState(5);
  const [algorithmFilter, setAlgorithmFilter] = useState("");
  const [problemFilter, setProblemFilter] = useState("")
  const [anchorEl, setAnchorEl] = React.useState<null | HTMLElement>(null);

  const limitOpen = Boolean(anchorEl);
  const ColumnArray = Array.from(AlgorithmModel.values());
  const AlgorithmNameDefinitons = Array.from(AlgorithmModel.keys());

  useEffect(() => {
    getAlgorithms(page, limit, algorithmFilter, problemFilter);
  }, []);


  const handleLimitClick = (event: React.MouseEvent<HTMLButtonElement>) => {
    setAnchorEl(event.currentTarget);
  };
  const handleLimitClose = () => {
    setAnchorEl(null);
  };
  const setNewLimitTo5 = () => {
    SetNewLimit(5);
    handleLimitClose();
  }
  const setNewLimitTo10 = () => {
    SetNewLimit(10)
    handleLimitClose();
  }
  const setNewLimitTo20 = () => {
    SetNewLimit(20);
    handleLimitClose();
  }

  const SetNewLimit = (newLimit: number) => {
    let currentlyShownAlgorithm = page * limit;
    let newPage = Math.floor(currentlyShownAlgorithm / newLimit);
    setPage(newPage);
    setLimit(newLimit);
    getAlgorithms(newPage, newLimit, algorithmFilter, problemFilter);
  }

  const getAlgorithms = async (pageToget: number, limitToSet: number, algFilter: String, probFilter : String) => {
    let benchmarksPromise = axios.post(
      algorithmsGetEndpoint + "?page=" + pageToget + "&limit=" + limitToSet,
      {
        algorithmName: algFilter,
        problem: probFilter,
      },
      {
        
        headers: {
          "Content-Type": "application/json",
          header1: 'Bearer ' + tokenSlice
        },
      }
    );
    await benchmarksPromise.then((response) => {
      setAlgorithmNames(response.data);
    });
    console.info(algorithmNames);
  };



  const changePage = (increase: boolean) => {
    if (increase) {
      setPage(page + 1)
      getAlgorithms(page + 1, limit, algorithmFilter, problemFilter);
    }
    else {
      if (page > 0) {
        setPage(page - 1)
        getAlgorithms(page - 1, limit, algorithmFilter, problemFilter);
      }
      else {
        setPage(page)
        getAlgorithms(page, limit, algorithmFilter, problemFilter);
      }
    }

  }

  const executeAlgorithm = (algName: string, probName: string) => {
    axios
      .post(
        algorithmExecuteEndpoint,
        {
          algorithmName: algName,
          problemName: probName,
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

  const filterByAlgorithm = (e: ChangeEvent<HTMLInputElement>) => {
    const searchedAlgorithm: string = e.target.value;
    setAlgorithmFilter(searchedAlgorithm);
    getAlgorithms(page, limit, searchedAlgorithm, problemFilter);
  }

  const filterByProblem = (e: ChangeEvent<HTMLInputElement>) => {
    const searchedProblem: string = e.target.value;
    setProblemFilter(searchedProblem)
    getAlgorithms(page, limit, algorithmFilter, searchedProblem);
  }

  return (
      <AlgorithmScreen
      page = {page}
      anchorEl = {anchorEl}
      limitOpen = {limitOpen}
      ColumnArray = {ColumnArray}
      showAlgorithms={showAlgorithms}
      problemFilter = {problemFilter}
      algorithmNames = {algorithmNames}
      algorithmFilter = {algorithmFilter}
      AlgorithmNameDefinitons = {AlgorithmNameDefinitons}
      changePage = {changePage}
      setNewLimitTo5 = {setNewLimitTo5}
      setNewLimitTo10 = {setNewLimitTo10}
      setNewLimitTo20 = {setNewLimitTo20}
      filterByProblem = {filterByProblem}
      executeAlgorithm = {executeAlgorithm}
      handleLimitClick = {handleLimitClick}
      handleLimitClose = {handleLimitClose}
      filterByAlgorithm = {filterByAlgorithm}
      setShowAlgorithms = {setShowAlgorithms}
      />
  );
};

export default MainScreen;
