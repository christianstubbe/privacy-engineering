// File to build the single React components

// import MUI materials
import Container from "@mui/material/Container";
import * as React from "react";
import Box from "@mui/material/Box";
import Paper from "@mui/material/Paper";
import Grid from "@mui/material/Grid";
import "./Main.css";
import Leftbox from "./Leftbox";

const MainComponent = () => {
  return (
    <main className="main">
      <div className="leftBox">
        🛫 UPLOAD IMAGE
        <Leftbox />
      </div>
      <div className="rightBox"> 🛬 RETRIEVE IMAGES</div>
    </main>
  );
};

export { MainComponent };
