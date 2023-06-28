import CssBaseline from '@mui/material/CssBaseline';

import { MainComponent } from "./components/Main";
import Navbar from "./components/Navbar.js";

function App() {
  return (
    <>
      <CssBaseline />
      <Navbar />
      <MainComponent />
    </>
  );
}

export default App;