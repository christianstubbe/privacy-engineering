import React, { useState } from "react";
import { Dropdown, Ripple, initTE } from "tw-elements";
import { AiFillCaretUp, AiFillCaretDown } from "react-icons/ai";
import { RxCross1 } from "react-icons/rx";
import list from "./list.json";

initTE({ Dropdown, Ripple });

function Leftbox() {
  const [isOpen, setIsOpen] = useState(false);
  return (
    // add some tailwindcss here ..
    <div className="upload img h-screen">
      <div className="relative grid grid-cols-2 gap-1 mt-5 h-[50vh] p-3 bg-sky-800 ml-8 mr-8">
        <div className=" text-purple-100 p-5 w-full items-center justify-center border border-black rounded hover:bg-blue-100 font-mono transition duration-300 hover:text-black">
          [here comes the img preview]
        </div>
        <div className="relative h-358 w-340">
          <button
            className="bg-red-600 h-8 w-8 flex justify-center items-center border-1 ml-2 rounded-full font-extrabold text-lg absolute bottom-0 left-0  hover:bg-red-700 shadow-lg"
            type="button"
          >
            <RxCross1 className="" />
          </button>
        </div>
      </div>
      <div className="bg-sky-800 ml-8 mr-8">
        <div className="shadow-lg hover:shadow-xl">
          <label for="formFileLg" className=""></label>
          <input
            class="relative block w-full min-w-0 flex-auto cursor-pointer bg-clip-padding px-3 py-[0.32rem] font-sans tracking-wider leading-[2.15] text-purple-100 text-sm transition duration-300 ease-in-out file:-mx-3 file:-my-[0.32rem] file:cursor-pointer file:overflow-hidden file:px-3 file:py-[0.32rem] file:text-purple-100 file:font-sans file:tracking-wider file:text-base file:bg-sky-800 file:transition file:duration-150 file:ease-in-out file:[margin-inline-end:0.75rem] hover:file:bg-sky-500 "
            id="formFileMultiple"
            type="file"
          />
        </div>
      </div>
      <div className="relative grid grid-cols-2 gab-1 ml-8 mr-8 mt-2">
        <div className="">
          <button
            className=" text-purple-100 justify-center  bg-green-700 h-8 w-28 border-1 rounded text font-sans tracking-wider hover:bg-green-700"
            type="button"
          >
            Apply
          </button>
        </div>
        <div className="relative flex flex-col items-center">
          {/* add "active:" for when clicking  */}
          <button
            onClick={() => setIsOpen((prevState) => !prevState)}
            className="text-lg font-sans text-purple-100 tracking-wider bg-sky-800 w-full flex justify-between p-2 h-8 items-center border-2 border-transparent active:border-purple-100 duration-75 active:text-white rounded-lg"
          >
            Select purpose
            {!isOpen ? (
              <AiFillCaretDown className="h-8" />
            ) : (
              <AiFillCaretUp className="h-8" />
            )}
          </button>
          {isOpen && (
            <div className="bg-sky-600 absolute mt-10 flex flex-col items-start rounded-lg p-2 w-full">
              {/* map the json file list */}
              {list.map((item, i) => (
                <div
                  className="flex w-full justify-between hover:bg-sky-500 cursor-pointer rounded-r-lg border-l-transparent hover:border-l-purple-100 border-l-4"
                  key={i}
                >
                  <h3 className="text-purple-100 font-sans tracking-wider text-base ml-2">
                    {item.purpose}
                  </h3>
                </div>
              ))}
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

export default Leftbox;
