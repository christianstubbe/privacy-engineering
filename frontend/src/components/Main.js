import * as React from "react";

import { Grid, Container } from "@mui/material";

import Leftbox from "./Leftbox";
import Rightbox from "./Rightbox";

const MainComponent = () => {
  return (
  <Container maxWidth="lg">
    <Grid container spacing={6}>
      <Grid item xs={6}>
        <Leftbox/>
      </Grid>
      <Grid item xs={6}>
        <Rightbox />
      </Grid>
    </Grid>
  </Container>
  );
};

export { MainComponent };