import { configureStore } from "@reduxjs/toolkit";
import tokenReducer from "./security_token_slice";

export default configureStore({
  reducer: { token: tokenReducer },
});
