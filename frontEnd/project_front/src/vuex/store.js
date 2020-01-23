import Vue from "vue";
import Vuex from "vuex";
import actions from "./actions";
import mutations from "./mutations";

Vue.use(Vuex);

const state = {
    items: [{
            text: 'Home',
            to: '/',
            name: "mainPage"
        },
        {
            text: 'Top5',
            to: '/categoryPage',
            name: "categoryPage"
        }
    ],
    category: [{
            nameEng: "game",
            nameKor: "게임"
        },
        {
            nameEng: "entertainment",
            nameKor: "엔터"
        },
        {
            nameEng: "beauty",
            nameKor: "뷰티"
        },
        {
            nameEng: "sports",
            nameKor: "운동"
        },
        {
            nameEng: "mukbang",
            nameKor: "먹방"
        },
        {
            nameEng: "kids",
            nameKor: "키즈"
        },
        {
            nameEng: "animals",
            nameKor: "동물"
        },
        {
            nameEng: "life",
            nameKor: "일상"
        },
        {
            nameEng: "it",
            nameKor: "IT"
        },
    ]
};

const getters = {
    categories: state => {

        return state.category;
    },
    links: state => {
        return state.items
    }

}

export default new Vuex.Store({
    state,
    getters,
    mutations,
    actions
});


Vue.use(Vuex)