import React, { useState, useEffect }from "react";

import Box from '@mui/material/Box';
import FormControl from '@mui/material/FormControl';
import Autocomplete from '@mui/material/Autocomplete';
import TextField from '@mui/material/TextField';
import Fab from '@mui/material/Fab';
import SearchIcon from '@mui/icons-material/Search';
import Typography from '@mui/material/Typography';
import ImageList from '@mui/material/ImageList';
import ImageListItem from '@mui/material/ImageListItem';
import Divider from '@mui/material/Divider';
import {Dialog, DialogActions, DialogContent, DialogContentText, DialogTitle} from "@mui/material";
import Button from "@mui/material/Button";
import Alert from "@mui/material/Alert";

function RetrieveData() {

  const [isOpen, setIsOpen] = useState(false);
  const [openDialog, setOpenDialog] = useState(false);
  const [purposes, setPurposes] = useState([]);
  const [selectedPurpose, setSelectedPurpose] = useState(null);
  const [itemData, setItemData] = useState([]);
  const [justification, setJustification] = useState("");  // New state for justification text
  const [error, setError] = useState(false);  // New state for error handling


  const handleCloseDialog = () => {
    setOpenDialog(false);
  };

  const handleButtonClick = () => {
    setOpenDialog(true);
  };

  useEffect(() => {
    fetch('/api/v1/pap/purposes', {
          mode: 'cors',
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then((data) => setPurposes(data))
      .catch((error) => {
        console.error('Error:', error);
      });
  }, []);

  const handleLoadImages = () => {
    setIsOpen(true);
    fetch(`/api/v1/cloud/blob?purpose=${selectedPurpose.name}`, {
          mode: 'cors',
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then((data) => setItemData(data))
      .catch((error) => {
        console.error('Error:', error);
      });
  };

  const handleConfirmDialog = () => {
    if (justification.trim().length === 0) { // Check if the justification text field is empty
      setError(true);
      return;
    }
    setOpenDialog(false);
    handleLoadImages();  // Call the function to load images here
  };

  const handleJustificationChange = (event) => {
    setJustification(event.target.value);
    if (event.target.value.trim().length > 0) { // If the text field is not empty, clear the error
      setError(false);
    }
  };

  return (
    <Box sx={{ p: 5 }} >

      <Typography variant="h4" gutterBottom>
        Retrieve Data
      </Typography>

      <FormControl fullWidth margin="normal">
          <Autocomplete
            disablePortal
            id="purpose"
            options={purposes}
            getOptionLabel={(option) => option.name} // change 'name' to appropriate property in your objects
            onChange={(event, newValue) => setSelectedPurpose(newValue)} // Save selected value
            renderInput={(params) => <TextField {...params} label="Purpose" />}
          />
      </FormControl>

        <FormControl margin="normal">
        <Fab
          onClick={handleButtonClick}
          color="primary" variant="extended" aria-label="add">
          Load Images
          <SearchIcon />
        </Fab>
      </FormControl>

      <Dialog
        open={openDialog}
        onClose={handleCloseDialog}
        aria-labelledby="alert-dialog-title"
        aria-describedby="alert-dialog-description"
      >
        <DialogTitle id="alert-dialog-title">
          {"Purpose Confirmation"}
        </DialogTitle>
        <DialogContent>
          <DialogContentText id="alert-dialog-description">
            Do you confirm that you will use the retrieved data only for the "{selectedPurpose ? selectedPurpose.label : ''}" purpose?
          </DialogContentText>
          <TextField
            autoFocus
            margin="dense"
            id="justification"
            label="Justification"
            type="text"
            fullWidth
            value={justification}
            onChange={handleJustificationChange}
            error={error}
            helperText={error ? "You must provide a justification." : null}
          />
          {error && <Alert severity="error">Justification is required to proceed!</Alert>}
        </DialogContent>
        <DialogActions>
          <Button onClick={handleCloseDialog} color="primary">
            No, cancel this.
          </Button>
          <Button onClick={handleConfirmDialog} color="primary" style={{backgroundColor: 'forestgreen', color: 'white'}} autoFocus disabled={justification.trim().length === 0}>
            Yes, I confirm.
          </Button>
        </DialogActions>
      </Dialog>

        <Divider sx={{ margin: '30px 0' }} />

        <Typography variant="h5" gutterBottom>
          Results
        </Typography>


        {isOpen && <ImageList sx={{ width: 500, height: 450 }} cols={3} rowHeight={164}>
          {itemData.map((item) => (
            <ImageListItem key={item.img}>
              <img
                src={`${item.img}?w=164&h=164&fit=crop&auto=format`}
                srcSet={`${item.img}?w=164&h=164&fit=crop&auto=format&dpr=2 2x`}
                alt={item.title}
                loading="lazy"
              />
            </ImageListItem>
          ))}
        </ImageList>}

    </Box> 
  );  
}

export default RetrieveData;

