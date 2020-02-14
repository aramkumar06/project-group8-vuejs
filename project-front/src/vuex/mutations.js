import Constant from "./Constant";
import store from "./store";

export default {
  [Constant.GET_TEST]: (state, payload) => {
    store.state.testID = payload.testID;
  },
  [Constant.GET_YOUTUBERS_PER_CATEGORY]: (state, payload) => {
    store.state.youtubersPerCategory = payload.youtuberslist;
  },
  [Constant.CHANGE_CATEGORY_LOADING]: (state, payload) => {
    store.state.isCategoryLoading = payload.bool;
  },
  [Constant.CHANGE_CURRENT_CATEGORY]: (state, payload) => {
    store.state.currentcategory = payload.category;
  },
  [Constant.GET_YOUTUBER]: (state, payload) => {
    console.log(payload.youtuber);
    store.state.youtuber = payload.youtuber;
  },
  [Constant.SEARCH_YOUTUBER]: (state, payload) => {
    store.state.searchyoutuber = payload.youtubers;
  },
  [Constant.GET_MANYTOP5]: (state, payload) => {
    store.state.manytop5list = payload.list;
  },
  [Constant.GET_YNO_FROM_URL]: (state, payload) => {
    store.state.yno = payload.yno;
  },
  [Constant.GET_STATUS_FROM_YNO]: (state, payload) => {
    if(payload.value != store.state.tempValue){
        store.state.value = payload.value;
    }
    store.state.tempValue = payload.value;
  }
};
