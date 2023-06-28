import React from "react";
import * as BiIcons from "react-icons/bi";
import logo_TU from "../images/tu-berlin-logo-long-red.svg";

import AppBar from "@mui/material/AppBar";
import Box from "@mui/material/Box";
import Toolbar from "@mui/material/Toolbar";
import Typography from "@mui/material/Typography";
import Button from "@mui/material/Button";

function Navbar() {
  return (
    <>
      <Box sx={{ flexGrow: 1, marginBottom: 0 }}>
        <AppBar
          className="appBar"
          position="static"
        >
          <Toolbar>
            <img className="logo" alt="Logo TU Berlin" src={logo_TU} />
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