import React from "react";

function Leftbox() {
  return (
    // add some tailwindcss here ..
    <div className="upload img h-screen">
      <div className="relative grid grid-cols-2 gap-1 mt-20 h-[50vh] p-3 bg-slate-400 ml-8 mr-8 shadow-lg hover:shadow-xl">
        <div className=" p-5 w-full items-center justify-center border border-black rounded hover:bg-blue-100 font-mono">
          Img preview
        </div>
        <div className="relative h-358 w-340">
          <button
            className="bg-red-600 h-8 w-20 border-1 ml-5 rounded text-xs font-mono absolute bottom-0 left-0  hover:bg-red-700"
            type="button"
          >
            Remove
          </button>
        </div>
      </div>
      <div className="mb-3 mt-10 bg-slate-400 ml-8 mr-8">
        <div className="shadow-lg hover:shadow-xl">
          <label for="formFileLg" className=""></label>
          <input
            class="relative block w-full min-w-0 flex-auto cursor-pointer bg-clip-padding px-3 py-[0.32rem] font-normal leading-[2.15] text-neutral-700 transition duration-300 ease-in-out file:-mx-3 file:-my-[0.32rem] file:cursor-pointer file:overflow-hidden file:px-3 file:py-[0.32rem] file:text-neutral-700 file:transition file:duration-150 file:ease-in-out file:[margin-inline-end:0.75rem] hover:file:bg-neutral-200 focus:text-neutral-700 focus:shadow-te-primary focus:outline-none"
            id="formFileMultiple"
            type="file"
          />
        </div>
      </div>
    </div>
  );
}

export default Leftbox;
