// File to build the single React components

import * as React from "react";
import Leftbox from "./Leftbox";
import Rightbox from "./Rightbox";

const MainComponent = () => {
  return (
    <main className="flex justify-evenly h-screen bg-slate-200">
      <div className="basis-1/2 text-center text-lg font-mono mt-10">
        UPLOAD IMAGE
        <Leftbox />
      </div>
      <div className="basis-1/2 text-center text-lg font-mono mt-10">
        RETRIEVE IMAGES
        <Rightbox />
      </div>
    </main>
  );
};

export { MainComponent };
