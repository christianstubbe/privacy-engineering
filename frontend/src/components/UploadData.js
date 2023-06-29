import React from "react";

import Typography from '@mui/material/Typography';
import Avatar from "@mui/material/Avatar";
import Button from "@mui/material/Button";
import Box from "@mui/material/Box";
import FormControl from '@mui/material/FormControl';
import Autocomplete from '@mui/material/Autocomplete';
import Divider from '@mui/material/Divider';
import TextField from '@mui/material/TextField';
import Fab from '@mui/material/Fab';

import DeleteIcon from '@mui/icons-material/Delete';

function Leftbox() {

  const purposes = [
    { label: 'Marketing' },
    { label: 'Sales' },
    { label: 'Admin' },
    { label: 'Shipping' },
    { label: 'Purchase' }
  ]

  const limitations = [
    {label: 'Blurred'},
    {label: 'Label Only'},
    {label: 'Downsized'}
  ]

  return (
    <Box sx={{ p: 5 }} >

      <Typography variant="h4" gutterBottom>
        Upload Data
      </Typography>

      <Typography variant="h5" gutterBottom>
        Current Photo
      </Typography>
      <Avatar 
            alt="Headshot" 
            // src="https://placehold.co/128x128" 
            src="https://images.unsplash.com/photo-1633332755192-727a05c4013d?w=128&h=128&fit=crop&auto=format"
            sx={{ width: 128, height: 128 }}  
      />
        <Fab  sx={{ marginLeft: '70px', marginTop: '-34px' }} color="error" variant="extended" aria-label="delete">
          <DeleteIcon />
        </Fab>

      <Divider sx={{ margin: '30px 0' }} />

      <Typography variant="h5" gutterBottom>
        Upload new Photo
      </Typography>

      <FormControl fullWidth>
        <Button variant="outlined" color="inherit" component="label" sx={{ height: '56px' }}>
          Choose Photo
          <input type="file" hidden />
        </Button>
      </FormControl>

      <FormControl fullWidth margin="normal">
        <Autocomplete
          disablePortal
          id="purpose"
          freeSolo
          multiple
          options={purposes}
          renderInput={(params) => <TextField {...params} label="Purpose" />}
        />
      </FormControl>

      <FormControl fullWidth margin="normal">
        <Autocomplete
          disablePortal
          id="purpose"
          freeSolo
          multiple
          options={limitations}
          renderInput={(params) => <TextField {...params} label="Limitation" />}
        />
      </FormControl>

      <FormControl margin="normal">
        <Fab color="primary" variant="extended" aria-label="add">
          Upload new Photo
        </Fab>
      </FormControl>


    </Box>
  );
}

export default Leftbox;