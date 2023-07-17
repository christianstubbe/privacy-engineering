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
    selected: false,
    transformations: [],
    parent_id: null,
    children: [
      {
        purpose_id: 2,
        name: "Marketing",
        selected: false,
        transformations: ["BLUR", "REMOVEBG"],
        parent_id: 1,
        children: [
          {
            purpose_id: 3,
            name: "Offline",
            selected: false,
            transformations: ["BLACKWHITE"],
            parent_id: 2,
            children: [
              {
                purpose_id: 4,
                name: "Print Advertising",
                selected: false,
                transformations: ["REMOVEBG"],
                parent_id: 3,
              },
              {
                purpose_id: 5,
                name: "Outdoor Advertising",
                selected: false,
                transformations: ["REMOVEBG"],
                parent_id: 3,
              },
              {
                purpose_id: 6,
                name: "Event Marketing",
                selected: false,
                transformations: ["REMOVEBG"],
                parent_id: 3,
              },
              {
                purpose_id: 7,
                name: "TV and Radio Advertising",
                selected: false,
                transformations: ["REMOVEBG"],
                parent_id: 3,
              },
            ],
          },
          {
            purpose_id: 8,
            name: "Online",
            selected: false,
            transformations: ["BLACKWHITE"],
            parent_id: 2,
            children: [
              {
                purpose_id: 9,
                name: "Social Media",
                selected: false,
                transformations: ["BLACKWHITE"],
                parent_id: 8,
                children: [
                  {
                    purpose_id: 3,
                    name: "LinkedIn",
                    selected: false,
                    transformations: ["BLACKWHITE"],
                    parent_id: 9,
                  },
                  {
                    purpose_id: 3,
                    name: "Instagram",
                    selected: false,
                    transformations: ["BLACKWHITE"],
                    parent_id: 9,
                  },
                  {
                    purpose_id: 3,
                    name: "Facebook",
                    selected: false,
                    transformations: ["BLACKWHITE"],
                    parent_id: 9,
                  },
                ],
              },
              {
                purpose_id: 10,
                name: "Website",
                selected: false,
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
        selected: false,
        transformations: [],
        parent_id: null,
        children: [
          {
            purpose_id: 12,
            name: "Recruitment",
            selected: false,
            transformations: ["BLACKWHITE"],
            parent_id: 6,
          },
          {
            purpose_id: 13,
            name: "Payroll Processing",
            selected: false,
            transformations: ["BLACKWHITE"],
            parent_id: 6,
          },
          {
            purpose_id: 14,
            name: "Training and Development",
            selected: false,
            transformations: ["BLACKWHITE"],
            parent_id: 6,
          },
          {
            purpose_id: 15,
            name: "Performance Evaluation",
            selected: false,
            transformations: ["BLACKWHITE"],
            parent_id: 6,
          },
        ],
      },
      {
        purpose_id: 16,
        name: "Sales",
        selected: false,
        transformations: ["BLACKWHITE"],
        parent_id: 2,
        children: [
          {
            purpose_id: 17,
            name: "Customer Relationship Management Access",
            selected: false,
            transformations: ["BLACKWHITE"],
            parent_id: 11,
          },
          {
            purpose_id: 18,
            name: "Sales Order Processing",
            selected: false,
            transformations: ["BLACKWHITE"],
            parent_id: 11,
          },
          {
            purpose_id: 19,
            name: "Sales Campaign Management",
            selected: false,
            transformations: ["BLACKWHITE"],
            parent_id: 11,
          },
          {
            purpose_id: 20,
            name: "Sales Forecasting",
            selected: false,
            transformations: ["BLACKWHITE"],
            parent_id: 11,
          },
        ],
      },
      {
        purpose_id: 21,
        name: "Microsoft 365",
        selected: false,
        transformations: ["REMOVEBG"],
        parent_id: 1,
        children: [
          {
            purpose_id: 22,
            name: "User Management",
            selected: false,
            transformations: ["REMOVEBG"],
            parent_id: 21,
          },
          {
            purpose_id: 23,
            name: "Exchange Online Administration",
            selected: false,
            transformations: ["REMOVEBG"],
            parent_id: 21,
          },
          {
            purpose_id: 24,
            name: "SharePoint Online Administration",
            selected: false,
            transformations: ["REMOVEBG"],
            parent_id: 21,
          },
          {
            purpose_id: 25,
            name: "Microsoft Teams Administration",
            selected: false,
            transformations: ["REMOVEBG"],
            parent_id: 21,
          },
          {
            purpose_id: 26,
            name: "License Management",
            selected: false,
            transformations: ["REMOVEBG"],
            parent_id: 21,
          },
        ],
      },
    ],
  },
];

const handleCheckboxChange = (node) => {
  const updatedTreeData = updateNodeSelection(mockTreeData, node);
  // dispatch({ type: "FETCH_SUCCESS", payload: updatedTreeData });
};

const updateNodeSelection = (treeData, nodeToUpdate) => {
  return treeData.map((node) => {
    if (node.purpose_id === nodeToUpdate.purpose_id) {
      return { ...node, selected: !node.selected };
    } else if (node.children && node.children.length > 0) {
      return {
        ...node,
        children: updateNodeSelection(node.children, nodeToUpdate),
      };
    } else {
      return node;
    }
  });
};

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
      value={{
        treeData: mockTreeData,
        isLoading: state.isLoading,
        handleCheckboxChange,
      }}
    >
      {children}
    </TreeContext.Provider>
  );
};

export default TreeContextProvider;
