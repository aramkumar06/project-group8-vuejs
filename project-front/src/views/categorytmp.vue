<template>
<div>
  <v-card>
    <v-card-title class="text-center justify-center py-6" style="background-color:#cdcdcd ; height : 500px">
      <h1 class="font-weight-bold display-2 ">CATEGORY</h1>
    </v-card-title>
  </v-card>
<v-container>
     <v-tabs
      v-model="tab"
      background-color="transparent"
      color="basil"
      grow
    >
      <v-tab
        v-for="(item,index) in categories"
        :key="index"
        @click="onCategoryButtonClicked(index)"
      >
        {{ item. nameEng}}
      </v-tab>
    </v-tabs>

    <v-tabs-items v-model="tab">
      <v-tab-item
        v-for="(item,index) in categories"
        :key="index"
      >
        <v-card
          color="basil"
          flat
        >
          <v-card-content>

            <v-card v-for="(item,i) in youtubersPerCategory" :key=i class="ma-5" >
        <v-container>
          <v-row> 
          <v-col justify="space-between">
            <v-col width>
              <v-card
                height="200"
                width="200"
                :img="item.thumbnails"
                :to= "{ path: 'youtuberPage', query: { yno : item.yno}}"
                flat
              />
            </v-col>
          </v-col>

          <v-col>
            <h1> {{item.channelName}} </h1>
            {{item.channelDescription}} <br>
            {{item.regDate}}
          </v-col>
          </v-row>
        </v-container>
      </v-card>
          </v-card-content>
        </v-card>
      </v-tab-item>
    </v-tabs-items>

    
</v-container>
</div>
</template>


<script>
import {
    mapGetters
}from 'vuex'
import Constant from"../vuex/Constant";


export default {
  components: {},
  name: "categoryPage",

  
  methods: {
    onCategoryButtonClicked(index){
      this.$store.state.currentCategory = index;
      this.$store.dispatch(Constant.GET_YOUTUBERS_PER_CATEGORY, {
           category : this.findCano()
         })
    },
    findCano : function() {
      
        console.log(this.$store.state.currentCategory)
        console.log(typeof(this.$store.state.currentCategory))
        if(typeof(this.$store.state.currentCategory) == "undefined"){
          return 0;
        }
        return this.categories[this.$store.state.currentCategory].cano;
      }
  },
  mounted(){
this.$vuetify.goTo(0)
  },
  created(){
         this.$store.dispatch(Constant.GET_YOUTUBERS_PER_CATEGORY, {
           category : this.findCano()
         })
  },
  computed: {
    ...mapGetters(['categories']),
    ...mapGetters(['youtubersPerCategory']),
    currentCategory () {
      return "tab-"+this.$store.state.currentCategory
    }
  },
  watch: {
    // currentCategory : function(){
    // console.log("dsfsdfsdfsd")

    //   this.$store.dispatch(Constant.GET_YOUTUBERS_PER_CATEGORY, {
    //       category : this.findCano()
    //     })
    // }
    
  },
  data () {
      return {
        tab: null,
        items: [
          'Appetizers', 'Entrees', 'Deserts', 'Cocktails',
        ],
        text: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
        

      }
    },
};
</script>

<style scoped>
.box {
    position:absolute;
    top:50%; left:50%;
    transform: translate(-50%, -50%);
    }
</style>
