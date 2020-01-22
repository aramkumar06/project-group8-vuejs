import Constant from "./Constant";
import store from "./store";

export default {
  [Constant.GET_TEST]: (state, payload) => {
    store.state.testID = payload.testID;
  }
};
