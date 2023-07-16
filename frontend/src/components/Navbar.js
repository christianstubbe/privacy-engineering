import React from "react";
import LogoTU from "../images/tu-berlin-logo-long-red.svg";

import AppBar from "@mui/material/AppBar";
import Box from "@mui/material/Box";
import Toolbar from "@mui/material/Toolbar";
import Typography from "@mui/material/Typography";
import Tooltip from "@mui/material/Tooltip";

import AccountCircleIcon from '@mui/icons-material/AccountCircle';
import {Drawer, IconButton, List, ListItem, ListItemText} from "@mui/material";
import {Link} from "react-router-dom";
import MenuIcon from "@mui/icons-material/Menu";
import { makeStyles } from '@mui/styles';

const useStyles = makeStyles({
  list: {
    width: 250,
  },
  fullList: {
    width: 'auto',
  },
});

function Navbar() {
  const classes = useStyles();
  const [state, setState] = React.useState({ left: false });

  const toggleDrawer = (anchor, open) => (event) => {
    setState({ ...state, [anchor]: open });
  };

  const list = (anchor) => (
    <div
      className={classes.list}
      role="presentation"
      onClick={toggleDrawer(anchor, false)}
      onKeyDown={toggleDrawer(anchor, false)}
    >
      <List>
        <ListItem button key={'Home'} component={Link} to="/">
          <ListItemText primary={'Home'} />
        </ListItem>
        <ListItem button key={'RetrieveData'} component={Link} to="/retrieve">
          <ListItemText primary={'Retrieve Images'} />
        </ListItem>
        <ListItem button key={'UploadData'} component={Link} to="/upload">
          <ListItemText primary={'Upload Images'} />
        </ListItem>
        <ListItem button key={'QueryData'} component={Link} to="/query">
          <ListItemText primary={'Retrieve Tabular Data'} />
        </ListItem>
      </List>
    </div>
  );

  return (
    <>
      <Box sx={{ flexGrow: 1, marginBottom: 0 }}>
        <AppBar
          className="appBar"
          position="static"
        >
          <Toolbar>
            <IconButton edge="start" color="inherit" aria-label="menu" onClick={toggleDrawer('left', true)}>
              <MenuIcon />
            </IconButton>
            <Drawer anchor={'left'} open={state['left']} onClose={toggleDrawer('left', false)}>
            {list('left')}
          </Drawer>
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