import React, { createContext, useReducer } from 'react';
import { PortfolioReducer } from './reducer';

const initialState = {};

export const PortfolioContext = createContext(initialState);

export const PortfolioProvider = ({ children }) => {
  const [state, dispatch] = useReducer(PortfolioReducer, initialState);
  return (
    <PortfolioContext.Provider value={{ state, dispatch }}>
      {children}
    </PortfolioContext.Provider>
  );
};
