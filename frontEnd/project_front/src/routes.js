import mainPage from "./views/mainPage.vue";
import categoryPage from "./views/categoryPage.vue";
import tmpPage3 from "./views/tmpPage3.vue";

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
        path: "/tmpPage3",
        name: "tmpPage3",
        component: tmpPage3
    }
];