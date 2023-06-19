import React from "react";
import "./Navbar.css";
import * as BiIcons from "react-icons/bi";
import styles from "../index.css";
// import "./Header.css";
import logo_TU from "../images/logo_TU.png";
const Navbar = () => (
  <nav className="navbar">
    <div className="infoToolbox">
      <img className="h-41 w-110" src={logo_TU} alt="Logo TU" />
      <h4>Internal Image Upload</h4>
    </div>
    <div className="userInfo">
      <BiIcons.BiUserCircle className="icon" />
    </div>
  </nav>
);
export default Navbar;

// className="navbar
// className="logo"
