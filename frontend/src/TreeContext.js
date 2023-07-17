import React, { createContext, useReducer, useEffect } from "react";
import axios from "axios";

const initialState = {
  treeData: [],
  isLoading: true,
  error: null,
};

const reducer = (state, action) => {
  switch (action.type) {
    case "FETCH_SUCCESS":
      return {
        isLoading: false,
        treeData: action.payload,
        error: null,
      };
    case "FETCH_ERROR":
      return {
        isLoading: false,
        treeData: [],
        error: "Something went wrong!",
      };
    default:
      return state;
  }
};

const mockTreeData = [
  {
    purpose_id: 1,
    name: "All purposes",
    transformations: [],
    parent_id: null,
    children: [
      {
        purpose_id: 2,
        name: "Marketing",
        transformations: ["BLUR", "REMOVEBG"],
        parent_id: 1,
        children: [
          {
            purpose_id: 3,
            name: "Offline",
            transformations: ["BLACKWHITE"],
            parent_id: 2,
            children: [
              {
                purpose_id: 4,
                name: "Print Advertising",
                transformations: ["REMOVEBG"],
                parent_id: 3,
              },
              {
                purpose_id: 5,
                name: "Outdoor Advertising",
                transformations: ["REMOVEBG"],
                parent_id: 3,
              },
              {
                purpose_id: 6,
                name: "Event Marketing",
                transformations: ["REMOVEBG"],
                parent_id: 3,
              },
              {
                purpose_id: 7,
                name: "TV and Radio Advertising",
                transformations: ["REMOVEBG"],
                parent_id: 3,
              },
            ],
          },
          {
            purpose_id: 8,
            name: "Online",
            transformations: ["BLACKWHITE"],
            parent_id: 2,
            children: [
              {
                purpose_id: 9,
                name: "Social Media",
                transformations: ["BLACKWHITE"],
                parent_id: 8,
                children: [
                  {
                    purpose_id: 3,
                    name: "LinkedIn",
                    transformations: ["BLACKWHITE"],
                    parent_id: 9,
                  },
                  {
                    purpose_id: 3,
                    name: "Instagram",
                    transformations: ["BLACKWHITE"],
                    parent_id: 9,
                  },
                  {
                    purpose_id: 3,
                    name: "Facebook",
                    transformations: ["BLACKWHITE"],
                    parent_id: 9,
                  },
                ],
              },
              {
                purpose_id: 10,
                name: "Website",
                transformations: ["BLACKWHITE"],
                parent_id: 8,
              },
            ],
          },
        ],
      },
      {
        purpose_id: 11,
        name: "HR",
        transformations: [],
        parent_id: null,
        children: [
          {
            purpose_id: 12,
            name: "Recruitment",
            transformations: ["BLACKWHITE"],
            parent_id: 6,
          },
          {
            purpose_id: 13,
            name: "Payroll Processing",
            transformations: ["BLACKWHITE"],
            parent_id: 6,
          },
          {
            purpose_id: 14,
            name: "Training and Development",
            transformations: ["BLACKWHITE"],
            parent_id: 6,
          },
          {
            purpose_id: 15,
            name: "Performance Evaluation",
            transformations: ["BLACKWHITE"],
            parent_id: 6,
          },
        ],
      },
      {
        purpose_id: 16,
        name: "Sales",
        transformations: ["BLACKWHITE"],
        parent_id: 2,
        children: [
          {
            purpose_id: 17,
            name: "Customer Relationship Management Access",
            transformations: ["BLACKWHITE"],
            parent_id: 11,
          },
          {
            purpose_id: 18,
            name: "Sales Order Processing",
            transformations: ["BLACKWHITE"],
            parent_id: 11,
          },
          {
            purpose_id: 19,
            name: "Sales Campaign Management",
            transformations: ["BLACKWHITE"],
            parent_id: 11,
          },
          {
            purpose_id: 20,
            name: "Sales Forecasting",
            transformations: ["BLACKWHITE"],
            parent_id: 11,
          },
        ],
      },
      {
        purpose_id: 21,
        name: "Microsoft 365",
        transformations: ["REMOVEBG"],
        parent_id: 1,
        children: [
          {
            purpose_id: 22,
            name: "User Management",
            transformations: ["REMOVEBG"],
            parent_id: 21,
          },
          {
            purpose_id: 23,
            name: "Exchange Online Administration",
            transformations: ["REMOVEBG"],
            parent_id: 21,
          },
          {
            purpose_id: 24,
            name: "SharePoint Online Administration",
            transformations: ["REMOVEBG"],
            parent_id: 21,
          },
          {
            purpose_id: 25,
            name: "Microsoft Teams Administration",
            transformations: ["REMOVEBG"],
            parent_id: 21,
          },
          {
            purpose_id: 26,
            name: "License Management",
            transformations: ["REMOVEBG"],
            parent_id: 21,
          },
        ],
      },
    ],
  },
];

export const TreeContext = createContext();

const TreeContextProvider = ({ children }) => {
  const [state, dispatch] = useReducer(reducer, initialState);

  useEffect(() => {
    axios
      .get("/api/v1/pap/purpose/")
      .then((response) => {
        dispatch({ type: "FETCH_SUCCESS", payload: response.data });
      })
      .catch(() => {
        dispatch({ type: "FETCH_ERROR" });
      });
  }, []);

  return (
    <TreeContext.Provider
      value={{ treeData: mockTreeData, isLoading: state.isLoading }}
    >
      {children}
    </TreeContext.Provider>
  );
};

export default TreeContextProvider;
