import React from "react";

import { useState } from "react";

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

function RetrieveData() {

  const [isOpen, setIsOpen] = useState(false);

  function toggle() {
    setIsOpen((isOpen) => !isOpen);
  }

  const purposes = [
    { label: 'Sales' },
    { label: 'Microsoft 365' },
    { label: 'LinkedIn' },
    { label: 'Marketing' },
    { label: 'Marketing – Offline' },
    { label: 'Marketing – Online' },
  ]

  const transformations = [
    {label: 'Blurred'},
    {label: 'Label Only'},
    {label: 'Downsized'},
    {label: 'Without Background'}
  ]

  const itemData = [
    {
      img: 'https://images.unsplash.com/photo-1506794778202-cad84cf45f1d',
      title: 'Person'
    },
    {
      img: 'https://images.unsplash.com/photo-1687360440361-1919309339e3',
      title: 'Person'
    },
    {
      img: 'https://images.unsplash.com/photo-1534528741775-53994a69daeb',
      title: 'Person'
    },
    {
      img: 'https://images.unsplash.com/photo-1580489944761-15a19d654956',
      title: 'Person'
    },
    {
      img: 'https://images.unsplash.com/photo-1544005313-94ddf0286df2',
      title: 'Person'
    },
    {
      img: 'https://images.unsplash.com/photo-1552374196-c4e7ffc6e126',
      title: 'Person'
    },
    {
      img: 'https://images.unsplash.com/photo-1567532939604-b6b5b0db2604',
      title: 'Person'
    },
    {
      img: 'https://images.unsplash.com/photo-1687360440741-f5df549b352d',
      title: 'Person'
    },
    {
      img: 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d',
      title: 'Person'
    },
    {
      img: 'https://images.unsplash.com/photo-1494790108377-be9c29b29330',
      title: 'Person'
    },
    {
      img: 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e',
      title: 'Person'
    },
    {
      img: 'https://images.unsplash.com/photo-1687360440102-78d15c3e5045',
      title: 'Person'
    }
  ];

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
            renderInput={(params) => <TextField {...params} label="Purpose" />}
          />
      </FormControl>

      <FormControl fullWidth margin="normal">
        <Autocomplete
          disablePortal
          id="transformation"
          freeSolo
          multiple
          options={transformations}
          renderInput={(params) => <TextField {...params} label="Data Transformation" />}
        />
      </FormControl>

        <FormControl margin="normal">
          <Fab
            onClick={toggle}
            color="primary" variant="extended" aria-label="add">
            Load Images
            <SearchIcon />
          </Fab>
        </FormControl>

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
