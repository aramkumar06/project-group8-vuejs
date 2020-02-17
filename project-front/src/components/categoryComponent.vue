<template>
<div>
    <v-container wrap style="background : gray">
      <h1> hello {{currentCategory}}</h1>
      <v-card v-for="(item,i) in yovutubersPerCategory" :key=i class="ma-5" >
        <v-container>
          <v-row> 
          <v-col justify="space-between">
            <v-col width>
              <v-card
                height="1000"
                width="1000"
                :src="item.thumbnails"
                :to= "{ name: 'youtuberPage', params: { yno : item.yno }}"
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
    </v-container>
</template>


<script>
  import Constant from"../vuex/Constant";
  import EventBus from "./eventBus"
  import {
    mapGetters,
    mapState
}from 'vuex'

  export default {
    data () {
      return {
        
      }
    },
    created(){
        console.log("categoryComponent_created : "+this.currentCategory);
        
        this.$store.dispatch(Constant.GET_YOUTUBERS_PER_CATEGORY, {
          category : this.findCano()
        })
  },
    watch :{
      currentCategory : function() {
        console.log("categoryComponent_watch : "+ this.currentCategory);
        
        this.$store.dispatch(Constant.GET_YOUTUBERS_PER_CATEGORY, {
          category : this.findCano()
        })
      }
    },
    computed : {
      ...mapGetters(['categories']),
      ...mapGetters(['youtubersPerCategory']),
      ...mapState({
        currentCategory : 'currentCategory'
      })

    },
    methods : {
      
    }
  }
</script>

<style scoped>

</style>