import React, { ChangeEvent } from "react";

import "../styles.css";
import AddAlgorithmScreen from "./add_algorithm_logic";

import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import TableCell from "@mui/material/TableCell";
import TableContainer from "@mui/material/TableContainer";
import TableHead from "@mui/material/TableHead";
import TableRow from "@mui/material/TableRow";
import Paper from "@mui/material/Paper";
import Button from "@mui/material/Button";
import { Menu, MenuItem, TextField } from "@mui/material";


const commonStyles = {
    bgcolor: 'background.paper',
    borderColor: 'text.primary',
    m: 1,
    border: 1,
  };

type Props = {
    page: number,
    userName : string,
    limitOpen: boolean,
    algorithmNames: any,
    problemFilter: string,
    ColumnArray: string[],
    showAlgorithms: boolean,
    algorithmFilter: string,
    setNewLimitTo5: () => void,
    setNewLimitTo10: () => void,
    setNewLimitTo20: () => void,
    handleLimitClose: () => void,
    anchorEl: HTMLElement | null,
    AlgorithmNameDefinitons: string[],
    changePage: (increase: boolean) => void,
    filterByProblem: (e: ChangeEvent<HTMLInputElement>) => void,
    executeAlgorithm: (algName: string, probName: string) => void,
    filterByAlgorithm: (e: ChangeEvent<HTMLInputElement>) => void,
    setShowAlgorithms: React.Dispatch<React.SetStateAction<boolean>>,
    handleLimitClick: (event: React.MouseEvent<HTMLButtonElement>) => void,
};

const styles = {
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    
  };

const AlgorithmScreen: React.FC<Props> = ({
    showAlgorithms,
    algorithmFilter,
    userName,
    filterByAlgorithm,
    problemFilter,
    filterByProblem,
    ColumnArray,
    algorithmNames,
    AlgorithmNameDefinitons,
    executeAlgorithm,
    setShowAlgorithms,
    changePage,
    page,
    limitOpen,
    handleLimitClick,
    anchorEl,
    handleLimitClose,
    setNewLimitTo5,
    setNewLimitTo10,
    setNewLimitTo20
}) => {
    return (
        <div style={styles}>
            {showAlgorithms ?
                <div>

                    <div>
                        <TextField
                            
                            label="Algorithm name"
                            id="outlined-size-small"
                            defaultValue="Algorithm name"
                            size="small"
                            value={algorithmFilter}
                            onChange={filterByAlgorithm}
                        />
                        
                        <TextField
                            label="Problem name"
                            id="outlined-size-small"
                            defaultValue="Problem name"
                            size="small"
                            value={problemFilter}
                            onChange={filterByProblem}
                        />
                    </div>

                    <TableContainer sx={{ width: '75%' }} component={Paper}>
                        <Table aria-label="simple table">
                            <TableHead>
                                <TableRow>
                                    {ColumnArray.map((column: any) => (
                                        <TableCell>{column}</TableCell>
                                    ))}
                                </TableRow>
                            </TableHead>
                            <TableBody>
                                {algorithmNames.map((row: any) => (
                                    <TableRow>
                                        {AlgorithmNameDefinitons.map((ColumnName: any) => {
                                            if (row[ColumnName] != null) {
                                                return <TableCell>{row[ColumnName]}</TableCell>;
                                            }
                                            else {
                                                return <TableCell>
                                                    <Button
                                                        color="success"
                                                        variant="contained"
                                                        onClick={() => {
                                                            executeAlgorithm(row['algorithmName'], row['problemName']);
                                                        }}
                                                        sx={{ width: 200, margin: 2 }}>Execute
                                                    </Button>
                                                </TableCell>
                                            }
                                        })}
                                    </TableRow>
                                ))}
                            </TableBody>
                        </Table>
                    </TableContainer>
                    <Button
                        variant="contained"
                        onClick={() => {
                            setShowAlgorithms(false);
                        }}
                        sx={{ width: 300, height: 60, margin: 2 }}
                    >
                        Add new Algorithm
                    </Button>
                    <div className="columnDivStyle">
                        <Button
                            variant="contained"
                            onClick={() => {
                                changePage(false)
                            }}
                            sx={{ width: 75, height: 20, margin: 2 }}
                        >
                            previous
                        </Button>
                        page : {page}
                        <Button
                            variant="contained"
                            onClick={() => {
                                changePage(true)
                            }}
                            sx={{ width: 75, height: 20, margin: 2 }}
                        >
                            next
                        </Button>
                        <div>
                            <Button
                                id="basic-button"
                                aria-controls={limitOpen ? 'basic-menu' : undefined}
                                aria-haspopup="true"
                                aria-expanded={limitOpen ? 'true' : undefined}
                                onClick={handleLimitClick}
                            >
                                Set Limit
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
                                <MenuItem onClick={setNewLimitTo5}>5 algorithms per page:</MenuItem>
                                <MenuItem onClick={setNewLimitTo10}>10 algorithms per page:</MenuItem>
                                <MenuItem onClick={setNewLimitTo20}>20 algorithms per page:</MenuItem>
                            </Menu>
                        </div>
                    </div>
                </div>
                :
                <AddAlgorithmScreen showAlgorithm={setShowAlgorithms} userName = {userName} />
            }
        </div>

    );
};

export default AlgorithmScreen;