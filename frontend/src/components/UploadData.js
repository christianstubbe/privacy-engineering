import React from "react";

import Typography from '@mui/material/Typography';
import Avatar from "@mui/material/Avatar";
import Button from "@mui/material/Button";
import Box from "@mui/material/Box";
import FormControl from '@mui/material/FormControl';
import Divider from '@mui/material/Divider';
import Fab from '@mui/material/Fab';

import DeleteIcon from '@mui/icons-material/Delete';
import PurposeTree from "./PurposeTree";
import TreeContextProvider from "../TreeContext";

function UploadData() {


    return (
        <Box sx={{p: 5}}>

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
                sx={{width: 128, height: 128}}
            />
            <Fab sx={{marginLeft: '70px', marginTop: '-34px'}} color="error" variant="extended" aria-label="delete">
                <DeleteIcon/>
            </Fab>

            <Divider sx={{margin: '30px 0'}}/>

            <Typography variant="h5" gutterBottom>
                Upload new Photo
            </Typography>

            <FormControl fullWidth>
                <Button variant="outlined" color="inherit" component="label" sx={{height: '56px'}}>
                    Choose Photo(s)
                    <input type="file" hidden/>
                </Button>
            </FormControl>

            <Divider sx={{margin: '30px 0'}}/>
            <Typography variant="h5" gutterBottom>
                Configure Purpose-base Access Control for Uploaded Data
            </Typography>

            <TreeContextProvider>
                <PurposeTree/>
            </TreeContextProvider>

            <FormControl margin="normal">
                <Fab color="primary" variant="extended" aria-label="add">
                    Upload
                </Fab>
            </FormControl>

        </Box>
    );
}

export default UploadData;