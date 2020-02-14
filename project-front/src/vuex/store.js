import Vue from "vue";
import Vuex from "vuex";
import actions from "./actions";
import mutations from "./mutations";

Vue.use(Vuex);

const state = {
  items: [
    {
      text: "Home",
      to: "/",
      name: "mainPage"
    },
    {
      text: "Top5",
      to: "/categoryPage",
      name: "categoryPage"
    }
  ],
  category: [
    {
      nameEng: "game",
      nameKor: "게임",
      cano: 1
    },
    {
      nameEng: "entertainment",
      nameKor: "엔터",
      cano: 2
    },
    {
      nameEng: "know-how/style",
      nameKor: "노하우/스타일",
      cano: 3
    },
    {
      nameEng: "sports",
      nameKor: "스포츠/운동",
      cano: 4
    },
    {
      nameEng: "mukbang/food",
      nameKor: "먹방/음식/푸드",
      cano: 5
    },
    {
      nameEng: "kids/edu",
      nameKor: "키즈/교육",
      cano: 6
    },
    {
      nameEng: "animals",
      nameKor: "동물",
      cano: 7
    },
    {
      nameEng: "life",
      nameKor: "일상",
      cano: 8
    },
    {
      nameEng: "science",
      nameKor: "과학",
      cano: 9
    }
  ],
  youtubersPerCategory: [],
  isCategoryLoading: false,
  currentCategory: "life",
  youtuber: {},
  searchyoutuber: [],
  compareyoutuber: ["aaaaaa", "Bbbbbbbba"],
  manytop5list: [],
  yno: 0,
  value: 0,
  tempValue: 0
};

const getters = {
  categories: state => {
    return state.category;
  },
  links: state => {
    return state.items;
  },
  youtubersPerCategory: state => {
    return state.youtubersPerCategory;
  },
  youtuber: state => {
    return state.youtuber;
  },
  searchyoutuber: state => {
    return state.searchyoutuber;
  },
  compareyoutuber: state => {
    return state.compareyoutuber;
  },
  manytop5list: state => {
    return state.manytop5list;
  }
};

export default new Vuex.Store({
  state,
  getters,
  mutations,
  actions
});

Vue.use(Vuex);
