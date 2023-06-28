import React from "react";
import { Button } from "@mui/material";
import { Stack } from "@mui/material";

const Buttons = () => {
  // Stack is a container component for arranging elements vertically or horizontally.
  return (
    <Stack
      className="buttonGroup"
      spacing={5}
      direction="row"
      justifyContent="center"
    >
      <Button className="buttonLeft" variant="contained">
        Button 1
      </Button>
      <Button className="buttonRight" variant="contained">
        Button 2
      </Button>
    </Stack>
  );
};

export default Buttons;
