export const PortfolioReducer = (state, action) => {
  switch(action.type) {
    case 'PORTFOLIO_ACTION':
      return { ...state, ...action.payload };
    default:
      return state;
  }
};
