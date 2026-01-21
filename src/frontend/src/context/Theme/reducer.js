export const ThemeReducer = (state, action) => {
  switch(action.type) {
    case 'THEME_ACTION':
      return { ...state, ...action.payload };
    default:
      return state;
  }
};
