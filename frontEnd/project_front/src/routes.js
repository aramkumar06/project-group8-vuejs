import mainPage from "./views/mainPage.vue";
import categoryPage from "./views/categoryPage.vue";

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
];