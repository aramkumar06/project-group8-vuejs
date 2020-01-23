<template>
  <!-- vuetify를 참고하여 작성하기
  https://vuetifyjs.com/ko/components/api-explorer
  -->
  <div>
    <banner />
  <v-container >
    <v-layout wrap>
      <v-flex 
        v-for="(category,i) in categories"
        :key = i
        xs12
        md4
        class="pa-3"
        
        >
        <v-responsive :aspect-ratio="1/1">
        <v-btn 
        block 
        :aspect-ratio="1/1"
        :to= "{ name: 'categoryPage', params: { cate: category.nameEng }}"
        height="100%"
        >
        <v-img
          :src="require('@/assets/logo.png')"
        >
        <h1> {{category.nameEng}} </h1>

        </v-img>
      </v-btn>
      </v-responsive>
      
      </v-flex>

    </v-layout>
    
    <h1 v-for=" a in  tmp" :key="a">
      아 진짜 하기 싫다
    </h1>

  </v-container>
  </div>
</template>

<script>
import banner from "../components/banner";
import {
    mapGetters
}from 'vuex'


export default {
  components: { banner },
  name: "mainPage",
  methods: { },
  computed: {
    ...mapGetters(['categories'])
  },
  data() {
    return {
      tmp : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
      layout: [2, 2, 1, 2, 2, 3, 3, 3, 3, 3, 3]
    };
  }
};
</script>

<style scoped>


</style>
