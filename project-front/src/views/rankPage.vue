<template>
  <!-- vuetify를 참고하여 작성하기
  https://vuetifyjs.com/ko/components/api-explorer
  -->

  <div>
    <v-card>
      <v-card-title class="justify-center py-6" style="background-color:#cdcdcd ; height : 300px">
        <i class="font-weight-black display-3">RANK PAGE</i>
      </v-card-title>
    </v-card>

    <v-container v-scroll="onScroll">
      <v-row>
        <v-col cols="2" class="">
          <v-card
            class=""
            top="50px"
            flat
            outlined
            id="sortCard"
            v-bind:style="{ position : 'absolute', top: sortCardPosition +'px' }"
          >
            <v-container>
              <v-row class="">
                <v-col class="pb-0">
                  <h1 class="font-weight-light mb-1" style="font-size :30px">정렬</h1>
                  <v-divider class=""></v-divider>
                </v-col>
              </v-row>
              <v-row fluid>
                <v-col class="py-0">
                  <v-radio-group v-model="orderGroup">
                    <v-radio label="구독자순" value="subscriber" checked></v-radio>
                    <v-radio label="등급순" value="grade"></v-radio>
                    <v-radio label="누적조회수" value="totalViewCount"></v-radio>
                    <v-radio label="총영상수" value="totalVideoCount"></v-radio>
                    <v-radio label="영향력" value="influence"></v-radio>
                    <v-radio label="활동력" value="activity"></v-radio>
                    <v-radio label="호감도" value="charm"></v-radio>
                  </v-radio-group>
                </v-col>
              </v-row>
            </v-container>
          </v-card>
        </v-col>

        <!-- 유튜버 리스트 -->
        <v-col cols="10">
          <v-container wrap style="background : white" border class="my-3">
            <v-row class="pt-0 pl-3">
              <v-col>
                <h1 class="font-weight-light mb-1">RANK PAGE</h1>
                <v-divider></v-divider>
              </v-col>
            </v-row>

            <v-container>
              <v-hover v-slot:default="{ hover }" open-delay="50" v-for="(item,i) in list" :key="i">
                <v-card
                  :elevation="hover ? 7 : 0"
                  outlined
                  flat
                  @click="gotoYoutuberPage(item.yno)"
                  class="my-3 mx-3"
                  shaped
                >
                  <v-row align="center">
                    <!-- thumbnail -->
                    <v-col class="ml-3 pr-0" cols="1" align="center">
                      <p class="title mb-0">{{i+1}}위</p>
                    </v-col>
                    <v-col class="ml-3 pr-0" cols="1" align="center">
                      <v-img
                        class="circle"
                        :src="item.thumbnails"
                        flat
                        :aspect-ratio="1/1"
                        width="200px"
                      />
                    </v-col>
                    <v-divider vertical class="mx-3"></v-divider>
                    <!-- 유튜버 설명 -->
                    <v-col cols="7" class="pa-1">
                      <v-row align="center">
                        <v-col cols="12" class="py-1">
                          <p
                            class="font-weight-black thin display-1 ma-0 text-truncate"
                          >{{item.channelName}}</p>
                        </v-col>
                      </v-row>
                      <v-row>
                        <v-col cols="12" class="py-0">
                          <p
                            class="font-weight-light thin ma-0"
                            style="font-size:13px"
                          >개설일 : {{item.publishedDate}}</p>
                        </v-col>
                      </v-row>
                      <v-row>
                        <v-col cols="12" class="py-0">
                          <p class="font-weight-light thin ma-0">
                            구독자 수 :
                            <b>{{tc(item.subscriber)}}</b> / 누적조회수 :
                            <b>{{tc(item.totalViewCount)}}</b> / 총영상수 :
                            <b>{{item.totalVideoCount}}</b>
                          </p>
                        </v-col>
                      </v-row>
                      <v-row>
                        <v-col cols="12" class="py-0">
                          <p
                            class="font-weight-light thin ma-0"
                          >영향력 : {{item.influence}} / 활동력 : {{item.activity}} / 조회수력 : {{item.viewCountTrend}} / 구독자력 : {{item.subscriberCountTrend}} / 호감도 : {{item.charm}}</p>
                        </v-col>
                      </v-row>
                    </v-col>
                    <v-divider vertical class="pl"></v-divider>
                    <!-- 등급 -->
                    <v-col>
                      <v-row align="center">
                        <v-col class="py-1">
                          <p class="font-weight-bold ma-0">&nbsp;&nbsp;GRADE</p>
                        </v-col>
                      </v-row>
                      <v-divider class="mr-10 mt-0 mb-0"></v-divider>
                      <v-row>
                        <v-col class="py-2">
                          <v-btn
                            class="mx-0"
                            fab
                            dark
                            large
                            :color="setGradeColor(item.grade)"
                            height="80px"
                            width="80px"
                          >
                            <v-icon dark>{{setGrade(item.grade)}}</v-icon>
                          </v-btn>
                        </v-col>
                      </v-row>
                    </v-col>
                  </v-row>
                </v-card>
              </v-hover>
            </v-container>
            <infinite-loading @infinite="infiniteHandler"></infinite-loading>
          </v-container>
        </v-col>
      </v-row>

      <!--youtuber-->
    </v-container>
  </div>
</template>

<script>
import http from "../vuex/http-common";
import tc from "thousands-counter";
import { orderBy } from "natural-orderby";
import InfiniteLoading from "vue-infinite-loading";

export default {
  components: {
    InfiniteLoading
  },
  name: "rankPage",

  methods: {
    setGradeColor(num) {
      if (typeof num == "undefined") {
        return "gray";
      }
      if (num >= 95) {
        return "red";
      } else if (num >= 90) {
        return "orange";
      } else if (num >= 80) {
        return "yellow";
      } else if (num >= 50) {
        return "green";
      } else if (num >= 20) {
        return "blue";
      } else {
        return "gray";
      }
    },
    gotoYoutuberPage: function(yno) {
      this.dialog = false;
      this.$vuetify.goTo(0);
      this.$router.push({ path: "/youtuberPage", query: { yno: yno } });
      this.$vuetify.goTo(0);
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
    tc(num) {
      return tc(num);
    },
    callback(list) {
      this.youtubers = list;
      this.youtubers = orderBy(
        this.youtubers,
        [v => v["subscriber"]],
        ["desc"]
      );
      this.list = this.youtubers.slice(0, this.range);
    },
    infiniteHandler($state) {
      setTimeout(() => {
        var tmplist = this.youtubers.slice(
          this.page * this.range,
          this.page * this.range + this.range
        );
        if (tmplist.length > 0) {
          this.page += 1;
          this.list.push(...tmplist);
          $state.loaded();
        } else {
          $state.complete();
        }
      }, 500);
    },
    onScroll() {
      var scroll = window.pageYOffset;
      var fix = 180;
      if (scroll > fix) {
        this.sortCardPosition = 25 + scroll - fix;
      } else {
        this.sortCardPosition = 25;
      }
    },
    failCallback() {
      var random = Math.floor(Math.random() * (10 - 1) + 1);
      this.$router.push({ path: 'youtuberPage', query: {reloding : random}});
    }
  },
  mounted() {},
  created() {
    http
      .get("/youtuber/all")
      .then(response => {
        console.log(response.data)
        if(response.data.state != 'ok'){
          this.failCallback
        }else{
          this.callback(response.data.data);
        }
      })
      .catch(exp => {
        alert("유튜버 로딩에 실패하였습니다\n" + exp);
      });
    this.orderGroup = "subscriber";
    this.page = 1;
  },
  computed: {},
  watch: {
    orderGroup: function() {
      this.youtubers = orderBy(
        this.youtubers,
        [v => v[this.orderGroup]],
        ["desc"]
      );
      this.list = this.youtubers.slice(0, this.range * this.page);
    }
  },
  data() {
    return {
      youtubers: [],
      list: [],
      orderGroup: {},
      page: 1,
      range: 7,
      sortCardPosition: 20

    };
  }
};
</script>

<style scoped>
.circle {
  border-radius: 50%;
}
/* #sortCard{position:absolute;top:100px;} */
</style>
