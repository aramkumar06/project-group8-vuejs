<template>
  <v-app id="app">
    
    <v-app-bar app fixed flat>
      <header-component></header-component>
    </v-app-bar>

    <v-content>
      <router-view />
    </v-content>

    <footer-component></footer-component>
  </v-app>
</template>

<script>
import headerComponent from "./components/headerComponent";
import footerComponent from "./components/footerComponent";

export default {
  name: "app",
  components: {
    headerComponent, footerComponent,
  },
    data () {
      return {
      //
      }
    }
};
</script>
