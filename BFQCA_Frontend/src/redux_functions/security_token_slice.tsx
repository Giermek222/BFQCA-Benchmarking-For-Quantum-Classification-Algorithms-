import { createSlice } from "@reduxjs/toolkit";

export const tokenSlice = createSlice({
  name: "token",
  initialState: {
    value: -1,
  },
  reducers: {
    setTokenValue: (state, action) => {
      state.value = action.payload;
    },
  },
});

export const { setTokenValue } = tokenSlice.actions;

// The function below is called a selector and allows us to select a value from
// the state. Selectors can also be defined inline where they're used instead of
// in the slice file. For example: `useSelector((state) => state.counter.value)`
export const selectToken = (state: { token: { value: Number } }) =>
  state.token.value;

export default tokenSlice.reducer;
