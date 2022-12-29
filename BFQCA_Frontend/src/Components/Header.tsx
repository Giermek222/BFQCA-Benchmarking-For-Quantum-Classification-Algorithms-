import React from 'react'
import {NavLink} from 'react-router-dom'

const Header = () => {
    const activeStyle = { color: "#F15B2A"}

    return (
        <nav>
            <NavLink to="/" style ={activeStyle}>
            Algorithms
            </NavLink>
            {" | "}
            <NavLink to="/benchmark" style ={activeStyle}>
            Benchmakrs
            </NavLink>
            {" | "}
            <NavLink to="/idk" style ={activeStyle}>
            Problems
            </NavLink>
        </nav>
    )
}
export default Header