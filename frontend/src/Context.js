import React, { createContext, useReducer, useEffect } from 'react';
import axios from 'axios';

const initialState = {
    treeData: [],
    isLoading: true,
    error: null,
};

const reducer = (state, action) => {
    switch (action.type) {
        case 'FETCH_SUCCESS':
            return {
                isLoading: false,
                treeData: action.payload,
                error: null,
            };
        case 'FETCH_ERROR':
            return {
                isLoading: false,
                treeData: [],
                error: 'Something went wrong!',
            };
        default:
            return state;
    }
};

export const TreeContext = createContext();

const TreeContextProvider = ({ children }) => {
    const [state, dispatch] = useReducer(reducer, initialState);

    useEffect(() => {
        axios
            .get('/api/v1/pap/purpose/')
            .then(response => {
                dispatch({ type: 'FETCH_SUCCESS', payload: response.data });
            })
            .catch(() => {
                dispatch({ type: 'FETCH_ERROR' });
            });
    }, []);

    return (
        <TreeContext.Provider value={{ treeData: state.treeData, isLoading: state.isLoading }}>
            {children}
        </TreeContext.Provider>
    );
};

export default TreeContextProvider;
