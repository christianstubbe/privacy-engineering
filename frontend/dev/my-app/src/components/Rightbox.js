import React from "react";
import { Dropdown, Ripple, initTE } from "tw-elements";

initTE({ Dropdown, Ripple });

function Rightbox() {
  return (
    // add some tailwindcss here ..
    <div className="retrieve img h-screen">
      <div className="relative grid grid-cols-2 gap-1 mt-20 h-[50vh] p-3 bg-slate-400 ml-8 mr-8 shadow-lg hover:shadow-xl">
        <div className=" p-5 w-full items-center justify-center border border-black rounded hover:bg-blue-100 font-mono">
          [Here comes the dropdown menu]
        </div>
        <div className="relative h-358 w-340">
          <button
            className="bg-green-600 h-8 w-20 border-1 ml-5 rounded text-xs font-mono absolute bottom-0 left-0  hover:bg-green-700"
            type="button"
          >
            Apply
          </button>
        </div>
      </div>
      <div className="mb-3 mt-10 bg-slate-400 ml-8 mr-8 w-656 h-52 font-mono">
        [Here comes the the image gallery]
        <div className="shadow-lg hover:shadow-xl">
          {/* Here comes the image gallery  */}
        </div>
      </div>
    </div>
  );
}

export default Rightbox;
