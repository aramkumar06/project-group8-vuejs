<template>
  <!-- vuetify를 참고하여 작성하기
  https://vuetifyjs.com/ko/components/api-explorer
  -->
  <div>
    <h1>categoryPage</h1>
    <h1>{{category}}</h1>
  </div>
</template>

<script>
export default {
  components: {},
  name: "categoryPage",

  created() {},
  methods: {},
  computed: {},
  data() {
    return { category : this.$route.params.cate};
  }
};
</script>

<style scoped></style>
