<template>
  <v-carousel height="500" hide-delimiter-background show-arrows-on-hover>
    <v-carousel-item v-for="(top5list, i) in manytop5list" :key="i" interval="10">
      <v-sheet color="transparent" height="100%">
        <!-- table -->
        <v-container>
          <v-row>
            <v-col class="pb-0" cols="11">
              <p class="headline font-weight-black mb-1" style="color:black">{{top5list.title}} TOP5</p>
            </v-col>
            <v-col cols="1" class="pb-0 fill-height" align="center" justify="center">
              <a href="/rankPage">>더보기</a>
            </v-col>
          </v-row>
          <v-divider color="gray"></v-divider>
          <v-row class="fill-height" align="center" justify="center">
            <v-simple-table style="width: 100%;" light>
              <template v-slot:default>
                <thead>
                  <th style="width:7%"></th>
                  <th style="width:5%"></th>
                  <th style="width:35%">채널명</th>
                  <th style="width:10%">구독자</th>
                  <th style="width:10%">총영상조회수</th>
                  <th style="width:10%">총비디오수</th>
                  <!-- <th>사이트조회수</th> -->
                  <th>등급</th>
                </thead>
                <tbody>
                  <tr
                    v-for="(item,index) in top5list.list"
                    :key="index"
                    @click="gotoYoutuberPage(item.yno)"
                  >
                    <td>
                      <b>{{index+1}}위</b>
                    </td>
                    <td>
                      <v-row>
                        <v-img
                          :name="item.thumbnails"
                          class="circle"
                          :src="item.thumbnails"
                          flat
                          :aspect-ratio="1/1"
                        />
                      </v-row>
                    </td>
                    <td>{{item.channelName}}</td>
                    <td>{{tc(item.subscriber)}}</td>
                    <td>{{tc(item.totalViewCount)}}</td>
                    <td>{{numberWithCommas(item.totalVideoCount)}}</td>
                    <td>{{setGrade(item.grade)}}</td>
                  </tr>
                </tbody>
              </template>
            </v-simple-table>
          </v-row>
        </v-container>
      </v-sheet>
    </v-carousel-item>
  </v-carousel>
</template>


<script>
import Constant from "../vuex/Constant.js";
import { mapGetters } from "vuex";
import tc from "thousands-counter";

export default {
  data() {
    return {
      colors: [
        "indigo",
        "warning",
        "pink darken-2",
        "red lighten-1",
        "deep-purple accent-4"
      ],
      slides: ["First", "Second", "Third", "Fourth", "Fifth"],
      youtuber_stat: []
    };
  },
  created() {
    this.$store.dispatch(Constant.GET_MANYTOP5, {
      callback: this
    });
    //render table
    this.youtuber_stat = [
      { name: "영향력", figure1: 1 },
      { name: "활동력", figure1: 2 },
      { name: "성장력", figure1: 3 },
      { name: "기본수치", figure1: 4 },
      { name: "매력", figure1: 5 }
    ];
  },
  methods: {
    gotoYoutuberPage: function(yno) {
      this.dialog = false;
      this.$vuetify.goTo(0);
      this.$router.push({ path: "/youtuberPage", query: { yno: yno } });
      this.$vuetify.goTo(0);
    },
    tc(num) {
      return tc(num);
    },
    numberWithCommas(x) {
      return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
    },
    setGrade(num) {
      if (num >= 95) {
        return "SS";
      } else if (num >= 90) {
        return "S";
      } else if (num >= 80) {
        return "A";
      } else if (num >= 50) {
        return "B";
      } else if (num >= 20) {
        return "C";
      } else {
        return "D";
      }
    },
  },
  computed: {
    ...mapGetters(["manytop5list"])
  }
};
</script>

<style scoped>
.circle {
  border-radius: 50%;
}
</style>