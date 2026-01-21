import React, { createContext, useReducer } from 'react';
import { ThemeReducer } from './reducer';

const initialState = {};

export const ThemeContext = createContext(initialState);

export const ThemeProvider = ({ children }) => {
  const [state, dispatch] = useReducer(ThemeReducer, initialState);
  return (
    <ThemeContext.Provider value={{ state, dispatch }}>
      {children}
    </ThemeContext.Provider>
  );
};
