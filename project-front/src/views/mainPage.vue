<template>
    <!-- vuetify를 참고하여 작성하기
                      https://vuetifyjs.com/ko/components/api-explorer
                      -->
    <div>
    
    <image-preloader
    :src="require('@/assets/coolcat.png')">
    </image-preloader>
        <v-card>
            <v-img :src="require('@/assets/coolcat.png')" class="py-6 lighten-5">
                <i class="font-weight-black display-4 jb mb-5 pm-5">Youtube Analysis</i>
                <!-- <v-text-field class="mt-5 jb" background-color="#be228a94" append-icon="mdi-magnify" flat hide-details solo-inverted style="max-width: 300px; " @keyup.enter="search" v-model="searchWord" :key="$route.fullPath"/> -->
            </v-img>
        </v-card>
    
        <banner />
    
        <v-container transition="slide-y-transition">
            <v-layout wrap class="pa-12 ma-10">
                <v-flex v-for="(category,i) in categories" :key=i xs6 md4 class="pa-8" background-color="none">
                    <v-responsive :aspect-ratio="1/1">
                        <v-btn block :aspect-ratio="1/1" @click="onCategoryButtonClicked(i)" height="100%" width="50px" class="rounded-card">
                            <v-img :src="require('@/assets/' + i + '.png')" class="rounded-card pa-5">
                                
                            </v-img>
                        </v-btn>
                    </v-responsive>
                    <h1 class="categoryName"> {{category.nameEng}} </h1>
                </v-flex>
            </v-layout>
        </v-container>
    </div>
</template>

<script>
import banner from "../components/banner";
// import inputComponent from "../components/inputComponent";
import {
    mapGetters
} from 'vuex'


export default {
    components: { 
        // inputComponent,
        banner 
    },
    name: "mainPage",
    methods: {
        onCategoryButtonClicked(i) {
            localStorage.setItem('currentCategory',i+1)
            this.$router.push("/categoryPage");
        },
    },
    computed: {
        ...mapGetters(['categories']),
        ...mapGetters(['youtubersPerCategory']),
    },
    data() {
        return {
            tmp: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
            layout: [2, 2, 1, 2, 2, 3, 3, 3, 3, 3, 3]
        };
    },
};
</script>

<style scoped>
.jb {
    text-align: center;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate( -50%, -50%);
    color: black;
    background-color: #95b3e8a9;
    margin-bottom: 50px;
}
.rounded-card{   
    border-radius:20%;
    box-shadow: none;
}
.categoryName {
    font-family: PT sans;
    color: blacks;
    text-align: center;
}
</style>
