// File to build the single React components

import * as React from "react";
import Leftbox from "./Leftbox";
import Rightbox from "./Rightbox";

const MainComponent = () => {
  return (
    <main className="flex justify-evenly bg-gradient-to-r from-sky-100 to-sky-200">
      <div className="basis-1/2 text-center text-lg font-mono">
        <Leftbox />
      </div>
      <div className="basis-1/2 text-center text-lg font-mono">
        <Rightbox />
      </div>
    </main>
  );
};

export { MainComponent };
