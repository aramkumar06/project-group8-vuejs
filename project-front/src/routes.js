import mainPage from "./views/mainPage.vue";
import categoryPage from "./views/categoryPage.vue";
import youtuberPage from "./views/youtuberPage.vue";
import searchPage from "./views/searchPage.vue";
import comparePage from "./views/comparePage.vue";
import testPage from "./views/test.vue";
import memberPage from "./views/memberPage.vue";
import rankPage from "./views/rankPage.vue"



export default [{
        path: "/",
        name: "mainPage",
        component: mainPage
    },
    {
        path: "/categoryPage",
        name: "categoryPage",
        component: categoryPage
    },
    {
        path: "/youtuberPage",
        name: "youtuberPage",
        component: youtuberPage
    },
    {
        path: "/searchPage",
        name: "searchPage",
        component: searchPage
    },
    {
        path: "/comparePage",
        name: "comparePage",
        component: comparePage
    },
    {
        path: "/test",
        name: "testPage",
        component: testPage
    },
    {
        path: "/memberPage",
        name: "memberPage",
        component: memberPage
    },
    {
        path: "/rankPage",
        name: "rankPage",
        component: rankPage
    },



];