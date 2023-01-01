import { TableBody, TableCell, TableRow } from "@mui/material"
import Table from "@mui/material/Table"


const ProblemScreen = () => {


    return (
        <div>
            <Table>
                <TableBody>
                    <TableRow>
                        <TableCell>
                            <h2>Dataset name</h2>
                            <h3>Short description of data set </h3>
                        </TableCell>
                        <TableCell>
                            <img
                                src="https://th.bing.com/th/id/R.7dcec1fe314185e04816c6b5b5c0d28a?rik=YHD6KmPRfkoZmQ&riu=http%3a%2f%2fcdn.shopify.com%2fs%2ffiles%2f1%2f1419%2f7120%2fproducts%2fGracieuse.DeG.jpg_-_Copy_bc97548b-f2ee-49cc-b71f-dcf94a1906b8.jpg%3fv%3d1574284932&ehk=HZohccy4voA7SbdT7Yx1LOJvaRa2uwarP7Ld93FkZRc%3d&risl=&pid=ImgRaw&r=0"
                                alt="flat"
                                width={300}
                                height={225}
                            />
                        </TableCell>
                    </TableRow>
                    <TableRow>
                        <TableCell>                            <img
                            src="https://rubikscode.net/wp-content/uploads/2021/07/undraw_doctor_kw5l.png"
                            alt="flat"
                            width={300}
                            height={225}
                        /></TableCell>
                        <TableCell>
                            <h2>Dataset name</h2>
                            <h3>Short description of data set</h3>
                        </TableCell>
                    </TableRow>
                    <TableRow>
                        <TableCell>
                            <h2>Dataset name</h2>
                            <h3>Short description of data set</h3>
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