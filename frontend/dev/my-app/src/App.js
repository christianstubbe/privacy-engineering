import "./App.css";
import { MainComponent } from "./components/Main";
import Navbar from "./components/Navbar.js";
import Buttons from "./components/Button.js";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

// Add React.Frangment?
// div className="App"></div>;
function App() {
  return (
    <>
      <Navbar />
    </>
  );
}

export default App;

{
  /* <Router>
  <Navbar />
  <Routes>
    <Route path="/" exact components={Home} />
    <Route path="/products" components={Products} />
    <Route path="/reports" components={Reports} />
  </Routes>
</Router>; */
}
