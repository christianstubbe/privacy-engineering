import * as React from "react";

import CssBaseline from '@mui/material/CssBaseline';
import { Grid, Container } from "@mui/material";

import UploadData from "./components/UploadData";
import RetrieveData from "./components/RetrieveData";
import Navbar from "./components/Navbar.js";

function App() {
  return (
    <>
      <CssBaseline />
      <Navbar />
      <Container maxWidth="lg">
        <Grid container spacing={6}>
          <Grid item xs={6}>
            <UploadData/>
          </Grid>
          <Grid item xs={6}>
            <RetrieveData />
          </Grid>
        </Grid>
      </Container>
    </>
  );
}

export default App;