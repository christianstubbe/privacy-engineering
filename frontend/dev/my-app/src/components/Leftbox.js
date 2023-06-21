import React from "react";

function Leftbox() {
  return (
    // add some tailwindcss here ..
    <div className="upload img">
      <div className="grid grid-cols-2 gap-2 mt-20">
        <div className="bg-blue-50 ml-10 flex items-center justify-center h-60 w-60 border-2 border-blue-500 rounded-3xl hover:bg-blue-100 font-mono">
          Img preview
        </div>
        <button
          className="bg-red-600 h-10 w-20 border-2 border-black rounded-3xl text-base font-mono"
          type="button"
        >
          Remove
        </button>
      </div>
      <div class="mb-3 mt-10 px-10">
        <label
          for="formFileLg"
          class=" text-base mb-2 inline-block text-neutral-700 dark:text-neutral-200"
        >
          Upload the image here ...
        </label>
        <input
          class="relative m-0 block w-full min-w-0 flex-auto cursor-pointer border-2 rounded-md border-black bg-clip-padding px-3 py-[0.32rem] font-normal leading-[2.15] text-neutral-700 transition duration-300 ease-in-out file:-mx-3 file:-my-[0.32rem] file:cursor-pointer file:overflow-hidden file:rounded-md file:rounded-r-none file:border-0 file:border-solid file:border-inherit file:bg-neutral-100 file:px-3 file:py-[0.32rem] file:text-neutral-700 file:transition file:duration-150 file:ease-in-out file:[border-inline-end-width:1px] file:[margin-inline-end:0.75rem] hover:file:bg-neutral-200 focus:border-primary focus:text-neutral-700 focus:shadow-te-primary focus:outline-none dark:border-neutral-600 dark:text-neutral-200 dark:file:bg-neutral-700 dark:file:text-neutral-100 dark:focus:border-primary"
          id="formFileMultiple"
          type="file"
        />
      </div>
    </div>
  );
}

export default Leftbox;
