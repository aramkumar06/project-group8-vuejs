import Constant from "./Constant";
import http from "./http-common";

export default {
  [Constant.GET_TEST]: store => {
    http
      .get("/test/")
      .then(response => {
        console.log(response.data.data[0]);
        alert(response.data.data[0]);
        store.commit(Constant.GET_TEST, {
          testID: response.data.data[0].id
        });
      })
      .catch(exp => {
        alert("TEST에 실패하였습니다\n" + exp);
      });
  }
};
