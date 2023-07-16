import React from 'react';
import { DataGrid } from '@mui/x-data-grid';
import Typography from "@mui/material/Typography";
import FormControl from "@mui/material/FormControl";
import Autocomplete from "@mui/material/Autocomplete";
import TextField from "@mui/material/TextField";

function QueryData() {
  const rows = [
    { id: 1, name: "John", position: "Manager", department: "HR", address: "123 Street", phone: "123-456-7890", dob: "01-01-1990", salary: "10000" },
    { id: 2, name: "Doe", position: "Clerk", department: "Finance", address: "456 Avenue", phone: "098-765-4321", dob: "02-02-1980", salary: "8000" },
    { id: 3, name: "Jane", position: "Supervisor", department: "Marketing", address: "789 Boulevard", phone: "111-222-3333", dob: "03-03-1985", salary: "9000" },
  ];

  const columns = [
    { field: 'id', headerName: 'ID', width: 90 },
    { field: 'name', headerName: 'Name', width: 150 },
    { field: 'position', headerName: 'Position', width: 130 },
    { field: 'department', headerName: 'Department', width: 130 },
    { field: 'address', headerName: 'Home Address', width: 200 },
    { field: 'phone', headerName: 'Phone Number', width: 150 },
    { field: 'dob', headerName: 'Date of Birth', width: 150 },
    { field: 'salary', headerName: 'Salary', width: 110 }
  ];

    const purposes = [
    { label: 'Sales' },
    { label: 'Microsoft 365' },
    { label: 'LinkedIn' },
    { label: 'Marketing' },
    { label: 'Marketing – Offline' },
    { label: 'Marketing – Online' },
  ]

  return (
    <div style={{ height: 400, width: '100%' }}>
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
      <DataGrid
        rows={rows}
        columns={columns}
        pageSize={5}
        rowsPerPageOptions={[5]}
        checkboxSelection
      />
    </div>
  );
}

export default QueryData;
