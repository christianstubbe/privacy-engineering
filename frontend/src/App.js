import * as React from "react";

import CssBaseline from '@mui/material/CssBaseline';
import UploadData from "./components/UploadData";
import RetrieveData from "./components/RetrieveData";
import Navbar from "./components/Navbar.js";
import {BrowserRouter, Routes, Route} from 'react-router-dom';
import Home from "./components/Home";
import QueryData from "./components/QueryData";


function App() {

    return (
        <>
            <CssBaseline/>
            <BrowserRouter>
                <Navbar/>
                <Routes>
                    <Route path='/' element={<Home/>}/>
                    <Route path='/retrieve' element={<RetrieveData/>}/>
                    <Route path='/upload' element={<UploadData/>}/>
                    <Route path='/query' component={<QueryData/>}/>
                </Routes>
            </BrowserRouter>
        </>
    );
}

export default App;