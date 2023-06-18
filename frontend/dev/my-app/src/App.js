import "./App.css";
import { MainComponent } from "./components/Main";
import Header from "./components/Header.js";
import Buttons from "./components/Button.js";
import Navbar from "./components/Navbar";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { FaHome } from "react-icons/fa";
import Home from "./pages/Home";
import Reports from "./pages/Reports";
import Products from "./pages/Products";

// Add React.Frangment?
// div className="App"></div>;
function App() {
  return (
    <>
      <Router>
        <Navbar />
        <Routes>
          <Route path="/" exact components={Home} />
          <Route path="/products" components={Products} />
          <Route path="/reports" components={Reports} />
        </Routes>
      </Router>
    </>
  );
}

export default App;
