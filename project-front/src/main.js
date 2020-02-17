import Vue from "vue";
import App from "./App.vue";
import Router from "vue-router";
import routes from "./routes";
import store from "./vuex/store";
import vuetify from "./plugins/vuetify";
import imagePreloader from "vue-image-preloader";
import BootstrapVue from "bootstrap-vue";
import AxiosPlugin from "vue-axios-cors";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap-vue/dist/bootstrap-vue.css";
import VueApexCharts from "vue-apexcharts";
import VueSession from "vue-session";
import "@mdi/font/css/materialdesignicons.css"; // Ensure you are using css-loader
Vue.use(VueApexCharts);
Vue.use(AxiosPlugin);

Vue.config.productionTip = false;
Vue.config.devtools = true;

Vue.use(Router);
Vue.use(imagePreloader);
Vue.use(BootstrapVue);
Vue.component("apexchart", VueApexCharts);
Vue.use(vuetify, {
  iconfont: "mdi" // 'md' || 'mdi' || 'fa' || 'fa4'
});
var sessionOptions = {
  persist: true
};
Vue.use(VueSession, sessionOptions);

const router = new Router({
  mode: "history",
  routes
});

import IdleVue from "idle-vue";

const eventsHub = new Vue();

Vue.use(IdleVue, {
  eventEmitter: eventsHub,
  store,
  idleTime: 1000 * 60 * 60 * 3, // 3 hour,
  startAtIdle: false
});

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount("#app");

var filter = function(text, length, clamp){
  clamp = clamp || '...';
  var node = document.createElement('div');
  node.innerHTML = text;
  var content = node.textContent;
  return content.length > length ? content.slice(0, length) + clamp : content;
};

Vue.filter('truncate', filter);
