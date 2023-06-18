import React from "react";
import * as FaIcons from "react-icons/fa";
import * as AiIcons from "react-icons/ai";
import * as IoIcons from "react-icons/io";
import "./Navbar.css";

export const SidebarData = [
  // icon Nr.1
  {
    title: "Home",
    path: "/",
    icon: <AiIcons.AiFillHome />,
    cName: "navText",
  },
  // icon Nr.2
  {
    title: "Report",
    path: "/reports",
    icon: <IoIcons.IoIosPaper />,
    cName: "navText",
  },
  // icon Nr.2
  {
    title: "Products",
    path: "/products",
    icon: <FaIcons.FaCartPlus />,
    cName: "navText",
  },
];
