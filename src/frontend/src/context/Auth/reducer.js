export const AuthReducer = (state, action) => {
  switch(action.type) {
    case 'AUTH_ACTION':
      return { ...state, ...action.payload };
    default:
      return state;
  }
};
