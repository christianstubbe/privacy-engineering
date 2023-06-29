import React from "react";
import LogoTU from "../images/tu-berlin-logo-long-red.svg";

import AppBar from "@mui/material/AppBar";
import Box from "@mui/material/Box";
import Toolbar from "@mui/material/Toolbar";
import Typography from "@mui/material/Typography";
import Tooltip from "@mui/material/Tooltip";

import AccountCircleIcon from '@mui/icons-material/AccountCircle';

function Navbar() {
  return (
    <>
      <Box sx={{ flexGrow: 1, marginBottom: 0 }}>
        <AppBar
          className="appBar"
          position="static"
        >
          <Toolbar>
            <img className="logo" alt="Logo TU Berlin" src={LogoTU} />
            <Typography
              variant="h6"
              component="div"
              align="center"
              sx={{ flexGrow: 1, color: "black" }}
            >
            </Typography>
            <Tooltip title="Logged In">
              <AccountCircleIcon />
            </Tooltip>
          </Toolbar>
        </AppBar>
      </Box>
    </>
  );
}
export default Navbar;