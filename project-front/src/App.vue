<template>
  <v-app id="app">
    <header-component></header-component>

    <v-content>
      <router-view :key="$route.fullPath" />
    </v-content>

    <footer-component></footer-component>

    <compare-component />
  </v-app>
</template>

<script>
import headerComponent from "./components/headerComponent";
import footerComponent from "./components/footerComponent";
import compareComponent from "./components/compareComponent";

export default {
  name: "app",
  components: {
    headerComponent,
    footerComponent,
    compareComponent
  },
  data() {
    return {
      //
    };
  },
  created() {
    // var arr = [{"aaaa" : "aaaaa"},{"nnnnn" :"nnnn"}];

    // localStorage.setItem("compareYoutuber", JSON.stringify(arr));
    // localStorage.setItem("currentCategory", 0);

  }
};
</script>
