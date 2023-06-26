import React from "react";
import "./Navbar.css";
import * as BiIcons from "react-icons/bi";
import logo_TU from "../images/logo_TU.png";

import AppBar from "@mui/material/AppBar";
import Box from "@mui/material/Box";
import Toolbar from "@mui/material/Toolbar";
import Typography from "@mui/material/Typography";
import Button from "@mui/material/Button";
import IconButton from "@mui/material/IconButton";
import MenuIcon from "@mui/material/Menu";

// const theme = createTheme({
//   components: {
//     Paper: {
//       styleOverrides: {
//         root: { backgroundColor: "#202020" },
//       },
//     },
//   },
// });

function Navbar() {
  return (
    <>
      <Box sx={{ flexGrow: 1, marginBottom: 0 }}>
        <AppBar
          sx={{ backgroundColor: "lightgray" }}
          className="appBar"
          position="static"
        >
          <Toolbar>
            <IconButton
              size="large"
              edge="start"
              color="inherit"
              aria-label="menu"
              sx={{ mr: 2 }}
            >
              <MenuIcon />
              <img className="logo" src={logo_TU} />
            </IconButton>
            <Typography
              variant="h6"
              component="div"
              align="center"
              sx={{ flexGrow: 1, color: "black" }}
            >
              [Name of the Toolbox]
            </Typography>
            <div>
              <BiIcons.BiUserCircle className="icon" />
            </div>
            <Button sx={{ color: "green" }} color="inherit">
              You're logged in!
            </Button>
          </Toolbar>
        </AppBar>
      </Box>
    </>
  );
}
export default Navbar;

// import "./Header.css";

// const Navbar = () => (
//   <nav className="navbar">
//     <div className="infoToolbox">
//       <img className="logo" src={logo_TU} alt="Logo TU" />
//       <h4 className="font-sans hover:font-serif">Internal Image Upload</h4>
//     </div>
//     <div className="userInfo">
//       <BiIcons.BiUserCircle className="icon" />
//     </div>
//   </nav>
// );
