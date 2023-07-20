import React, {createContext, useReducer, useEffect} from "react";
import {CircularProgress} from "@mui/material";
import axios from "axios";
import mockTreeData from "./mockTreeData";

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
        case "UPDATE_TREE":
            return {
                ...state,
                treeData: action.payload
            };
        case "TOGGLE_CHECKBOX":
            return {
                ...state,
                treeData: toggleNodeAndChildren(state.treeData, action.payload)
            };

        case "ADD_NODE":
            return {
                ...state,
                treeData: addNodeToTree(state.treeData, action.payload),
            };
        case "DELETE_NODE":
            return {
                ...state,
                treeData: deleteNodeFromTree(state.treeData, action.payload),
            };
        default:
            return state;
    }
};

const initialState = {
    treeData: [],
    isLoading: true,
    error: null,
};

const deleteNodeFromTree = (treeData, nodeId) => {
    return treeData.filter(node => {
        if (node.id === nodeId) {
            return false;
        }

        if (node.children) {
            node.children = deleteNodeFromTree(node.children, nodeId);
        }

        return true;
    });
};


const addNodeToTree = (treeData, newNode) => {
    return treeData.map((node) => {
        if (node.id === newNode.parent_id) {
            return {...node, children: [...(node.children || []), newNode]};
        } else if (node.children && node.children.length > 0) {
            return {
                ...node,
                children: addNodeToTree(node.children, newNode),
            };
        } else {
            return node;
        }
    });
};


const updateNodeSelection = (treeData, nodeToUpdate) => {
    return treeData.map((node) => {
        if (node.id === nodeToUpdate.id) {
            return {...node, selected: !node.selected};
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

const toggleNodeAndChildren = (treeData, id, selected) => {
    return treeData.map((node) => {
        if (node.id === id) {
            const newNode = {...node, selected};
            if (node.children) {
                newNode.children = toggleNodeAndChildren(node.children, id, selected);
            }
            return newNode;
        } else if (node.children) {
            return {...node, children: toggleNodeAndChildren(node.children, id, selected)};
        } else {
            return node;
        }
    });
};


const getSelectedNodeIds = (treeData) => {
    let selectedIds = [];

    const traverseTree = (node) => {
        if (node.selected) {
            selectedIds.push(node.id);
        }

        if (node.children) {
            node.children.forEach(childNode => traverseTree(childNode));
        }
    }

    treeData.forEach(rootNode => traverseTree(rootNode));

    return selectedIds;
}


export const TreeContext = createContext();

const TreeContextProvider = ({children}) => {
    const [state, dispatch] = useReducer(reducer, initialState);

    useEffect(() => {
        axios
            .get("http://localhost:8000/api/v1/pap/purposes")
            .then((response) => {
                dispatch({type: "FETCH_SUCCESS", payload: response.data});
            })
            .catch(() => {
                dispatch({type: "FETCH_ERROR"});
            });
    }, []);

    const handleCheckboxChange = (nodeId) => {
        const findNode = (treeData, id) => {
            for (const node of treeData) {
                if (node.id === id) return node;
                if (node.children) {
                    const result = findNode(node.children, id);
                    if (result) return result;
                }
            }
            return null;
        }

        const nodeToChange = findNode(state.treeData, nodeId);

        if (!nodeToChange) {
            console.error(`Node with id ${nodeId} not found`);
            return;
        }

        const newTreeData = toggleNodeAndChildren(state.treeData, nodeId, !nodeToChange.selected);
        dispatch({type: "UPDATE_TREE", payload: newTreeData});
    };


    const handleAddNodeContext = (newNode) => {
        dispatch({type: "ADD_NODE", payload: newNode});
    };

    const handleDeleteNodeContext = (nodeId) => {
        dispatch({type: "DELETE_NODE", payload: nodeId});
    };


    return (
        <TreeContext.Provider
            value={{
                treeData: state.treeData,
                isLoading: state.isLoading,
                handleCheckboxChange,
                getSelectedNodeIds,
                handleAddNodeContext,
                handleDeleteNodeContext
            }}
        >
            {state.isLoading ? <CircularProgress/> : children}
        </TreeContext.Provider>
    );
};

export default TreeContextProvider;
