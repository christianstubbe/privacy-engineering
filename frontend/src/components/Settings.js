import React from 'react';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import TreeContextProvider from "../TreeContext";
import PurposeTree from "./PurposeTree";

function Settings() {
  return (
    <Box sx={{ p: 4 }}>
      <Typography variant="h4" gutterBottom>Settings</Typography>
      <TreeContextProvider>
          <PurposeTree settingsView={true} />
      </TreeContextProvider>
    </Box>
  );
}

export default Settings;
