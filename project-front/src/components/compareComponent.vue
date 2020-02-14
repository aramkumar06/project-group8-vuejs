<template>
  <v-menu
    open-on-hover
    top
    offset-y
    :close-on-content-click="false"
    :nudge-width="200"
    :nudge-top="20"
    :close-delay="300"
  >
    <template v-slot:activator="{ on, attrs }">
      <v-btn v-bind="attrs" v-on="on" fab fixed bottom right color="yellow">
        <v-icon color="green">input</v-icon>
      </v-btn>
    </template>

    <v-card :elevation="20" class="px-10" shaped height="350px" width="400px" >
      <v-row>
        <v-col class="ma-0 mt-5">
          <v-list-item-title class="headline font-weight-black mb-1">유튜버 비교하기</v-list-item-title>
          <v-divider></v-divider>
        </v-col>
      </v-row>
      <v-card :elevation="0" class=" " shaped height="180px">
        <v-row v-for="(item,index) in youtubers" :key="index">
          <v-col cols="1">
            <v-icon>keyboard_arrow_right</v-icon>
          </v-col>
          <v-col cols="8">
            <p class="font-weight-light">{{item.channelName}}</p>
          </v-col>
          <v-spacer></v-spacer>
          <v-col>
            <v-btn text icon color="red" @click="deleteYoutber(item.yno)">
              <v-icon>delete</v-icon>
            </v-btn>
          </v-col>
        </v-row>
      </v-card>
      <v-row>
        <v-col align="right">
          <v-btn @click="gotoComparePage" color="primary" rounded>
            비교하기
            <v-icon right>near_me</v-icon>
          </v-btn>
        </v-col>
      </v-row>
    </v-card>
  </v-menu>
</template>

<script>
import EventBus from "./eventBus";

export default {
  computed: {},
  watch: {},
  methods: {
    updateyoutubers: function() {
      console.log("updateyoutubers");
      var output = localStorage.getItem("compareYoutuber");
      var arr = JSON.parse(output);
      this.youtubers = arr;
      return this.youtubers;
    },
    deleteYoutber: function(yno) {
      console.log(yno);
      var output = localStorage.getItem("compareYoutuber");
      var arr = JSON.parse(output);
      const idx = arr.findIndex(function(item) {
        return item.yno === yno;
      });
      if (idx > -1) arr.splice(idx, 1);
      localStorage.setItem("compareYoutuber", JSON.stringify(arr));
      this.updateyoutubers();
    },
    gotoComparePage: function() {
      var output = localStorage.getItem("compareYoutuber");
      var arr = JSON.parse(output);
      if(arr.length != 2){
        alert("2명의 유튜버를 담아주세요");
        return;
      }
      console.log("gotoComparePage");
      this.$router.push("/comparePage");
    },
    insertYoutuber: function(yno, channelName) {
      var output = localStorage.getItem("compareYoutuber");
      var arr = JSON.parse(output);

      if (typeof arr == "undefined" || arr == null) {
        arr = [];
      }

      if (arr.length >= 2) {
        alert("더이상 비교하기에 유튜버를 담을 수 없습니다.");
        return;
      }

      if (arr.length ==1 && arr[0].yno == yno) {
        alert("같은 유튜버는 담을 수 없습니다.");
        return;
      }

      this.youtubers = arr;
      arr.push({ yno: yno, channelName: channelName });
      localStorage.setItem("compareYoutuber", JSON.stringify(arr));
    }
  },
  created() {
    EventBus.$on("insertYoutuber", (yno, channelName) => {
      this.insertYoutuber(yno, channelName);
    });
    var output = localStorage.getItem("compareYoutuber");
    var arr = JSON.parse(output);
    this.youtubers = arr;
  },
  data: () => ({
    youtubers: []
  })
};
</script>

