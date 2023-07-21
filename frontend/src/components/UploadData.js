import React, {useState, useContext} from "react";

import Typography from "@mui/material/Typography";
import Avatar from "@mui/material/Avatar";
import Button from "@mui/material/Button";
import Box from "@mui/material/Box";
import FormControl from "@mui/material/FormControl";
import Divider from "@mui/material/Divider";
import Fab from "@mui/material/Fab";
import Alert from "@mui/material/Alert";

import DeleteIcon from "@mui/icons-material/Delete";
import PurposeTree from "./PurposeTree";
import TreeContextProvider, {TreeContext} from "../TreeContext";
import axios from "axios";
import {Snackbar} from "@mui/material";

function UploadData() {
    const [selectedImages, setSelectedImages] = useState([]);
    const [selectedFiles, setSelectedFiles] = useState([]);

    const handleImageChange = (e) => {
        let files = [...e.target.files];
        setSelectedFiles(files);
        let images = files.map((file) => URL.createObjectURL(file));
        setSelectedImages(images);
    };

    const handleDeleteImage = (indexToDelete) => {
        setSelectedImages(
            selectedImages.filter((_, index) => index !== indexToDelete)
        );
        setSelectedFiles(
            selectedFiles.filter((_, index) => index !== indexToDelete)
        );
    };

    return (
        <Box sx={{p: 5}}>
            <Typography variant="h4" gutterBottom>
                Upload Data
            </Typography>

            <Typography variant="h5" gutterBottom>
                Current Photo(s)
            </Typography>
            <Box sx={{display: "flex", flexWrap: "wrap"}}>
                {selectedImages.map((image, index) => (
                    <Box key={index} sx={{margin: 1}}>
                        <Avatar
                            alt={`Selected image ${index + 1}`}
                            src={image}
                            sx={{width: 128, height: 128}}
                        />
                        <Fab
                            sx={{marginLeft: "70px", marginTop: "-34px"}}
                            color="error"
                            aria-label="delete"
                            onClick={() => handleDeleteImage(index)}
                        >
                            <DeleteIcon/>
                        </Fab>
                    </Box>
                ))}
            </Box>

            <Divider sx={{margin: "30px 0"}}/>

            <Typography variant="h5" gutterBottom>
                Upload new Photo
            </Typography>

            <FormControl>
                <Button
                    variant="outlined"
                    color="inherit"
                    component="label"
                    sx={{height: "56px"}}
                >
                    Choose Photo(s)
                    <input
                        type="file"
                        hidden
                        multiple
                        onChange={handleImageChange}
                    />
                </Button>
            </FormControl>

            <Divider sx={{margin: "30px 0"}}/>
            <Typography variant="h5" gutterBottom>
                Select Purpose(s)
            </Typography>

            <TreeContextProvider>
                <PurposeTree/>
                <UploadButton
                    selectedFiles={selectedFiles}
                />
            </TreeContextProvider>
        </Box>
    );
}

function UploadButton({selectedFiles}) {
    const {getSelectedNodeIds, treeData} = useContext(TreeContext);
    const [validationError, setValidationError] = useState(false);
    const [snackbarOpen, setSnackbarOpen] = useState(false);
    const [snackbarMessage, setSnackbarMessage] = useState('');
    const [severity, setSeverity] = useState('success');

    const handleSubmit = async () => {
            const selectedNodeIds = getSelectedNodeIds(treeData);
            if (selectedNodeIds.length === 0) {
                setValidationError(true);
                return;
            }

            const formData = new FormData();
            selectedFiles.forEach((file, index) => {
                formData.append(`files`, file);
            });
            formData.append('purpose_ids', JSON.stringify(selectedNodeIds));

            try {
                const response = await axios.post("http://localhost:8000/api/v1/cloud/blob", formData, {
                    headers: {
                        'Content-Type': 'multipart/form-data'
                    }
                });
                console.log(response.data);
                setSnackbarMessage('Upload Successful!');
                setSeverity('success');
                setSnackbarOpen(true);
            } catch
                (error) {
                console.error(error);
                setSnackbarMessage('Upload Failed!' + error.response?.data?.detail);
                setSeverity('error');
                setSnackbarOpen(true);
            }

        }
    ;

    return (
        <FormControl margin="normal">
            {validationError &&
                <Alert severity="error">At least one purpose must be selected before uploading.</Alert>}
            <Fab color="primary" variant="extended" aria-label="add" onClick={handleSubmit}>
                Upload
            </Fab>
            <Snackbar
                open={snackbarOpen}
                autoHideDuration={6000}
                onClose={() => setSnackbarOpen(false)}
            >
                <Alert onClose={() => setSnackbarOpen(false)} severity={severity} sx={{width: '100%'}}>
                    {snackbarMessage}
                </Alert>
            </Snackbar>
        </FormControl>
    );
}

export default UploadData;
