import { TableBody, TableCell, TableRow } from "@mui/material"
import Table from "@mui/material/Table"

const styles = {
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    
  };

const ProblemScreen = () => {


    return (
        <div style={styles}>
            <Table sx={{width: '75%' }}>
                <TableBody>
                    <TableRow>
                        <TableCell>
                            <h2>Iris</h2>
                            <h3>This dataset orgination from 1936 research paper became staple of modern data analysis. It contains 4 input values describing features of a flower, allowing it to be assigned to one of 3 species </h3>
                        </TableCell>
                        <TableCell>
                            <img
                                src="https://th.bing.com/th/id/R.7dcec1fe314185e04816c6b5b5c0d28a?rik=YHD6KmPRfkoZmQ&riu=http%3a%2f%2fcdn.shopify.com%2fs%2ffiles%2f1%2f1419%2f7120%2fproducts%2fGracieuse.DeG.jpg_-_Copy_bc97548b-f2ee-49cc-b71f-dcf94a1906b8.jpg%3fv%3d1574284932&ehk=HZohccy4voA7SbdT7Yx1LOJvaRa2uwarP7Ld93FkZRc%3d&risl=&pid=ImgRaw&r=0"
                                alt="Iris"
                                width={300}
                                height={225}
                            />
                        </TableCell>
                    </TableRow>
                    <TableRow>
                        <TableCell>
                            <img
                                src="https://rubikscode.net/wp-content/uploads/2021/07/undraw_doctor_kw5l.png"
                                alt="flat"
                                width={300}
                                height={225}
                            /></TableCell>
                        <TableCell>
                            <h2>Pima Indians Diabetic Dataset</h2>
                            <h3>
                                Dataset originating from  National Institute of Diabetes and Digestive and Kidney Diseases.
                                allowing to determine whether patient has diabetes. It contains 768 observations with 8 input features.
                            </h3>
                        </TableCell>
                    </TableRow>
                    <TableRow>
                        <TableCell>
                            <h2>Palmer Penguin Dataset</h2>
                            <h3>Dataset containing features of 688 penguins that can be categorized into 3 different species</h3>
                        </TableCell>
                        <TableCell>                            <img
                            src="https://rubikscode.net/wp-content/uploads/2020/07/lter_penguins.png"
                            alt="flat"
                            width={300}
                            height={225}
                        /></TableCell>
                    </TableRow>
                </TableBody>
            </Table>
        </div>
    )
}
export default ProblemScreen