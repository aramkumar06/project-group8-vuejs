<template>
  <!-- vuetify를 참고하여 작성하기
  https://vuetifyjs.com/ko/components/api-explorer
  -->
  <div>
  <div>tmpPage3</div>
  <v-btn large color="error" type="button" @click="tmpFunction()">
      back에 no 3으로 testID값 얻기 위해 GET요청 보내기
    </v-btn>
    <br />
    testID : "{{ testID }}"
    <br />
    <input
      type="button"
      value="router를 활용해서 tmpPage2로 이동하기"
      @click="tmpMove()"
    />
    <br />
  </div>
</template>

<script>
import Constant from "../vuex/Constant";
import mapGetters from 'vuex';


export default {
  components: {  },
  name: "mainPage",


  created() {},
  methods: {
    tmpFunction() {
      this.$store.dispatch(Constant.GET_TEST, {
        no: 3
      });
    },
    tmpMove() {
      this.$router.push("/categoryPage");
    }
  },
  computed: {
    ...mapGetters(['categories'])
  },
  data() {
    return {
      tmp : [[2, 2, 1, 2, 2, 3, 3, 3, 3, 3, 3]],
      layout: [2, 2, 1, 2, 2, 3, 3, 3, 3, 3, 3]
    };
  }
};
</script>

<style scoped></style>
