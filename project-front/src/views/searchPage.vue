<template>
  <!-- vuetify를 참고하여 작성하기
  https://vuetifyjs.com/ko/components/api-explorer
  -->

  <div>
    <v-card>
      <v-list-item-content
        class="justify-center py-6"
        style="background-color:#cdcdcd ; height : 300px"
      >
        <v-list-item-title class="font-weight-black display-3 font-italic" align="center"></v-list-item-title>
        <v-list-item-title
          class="font-weight-black display-3 font-italic"
          align="center"
        >SEARCH PAGE</v-list-item-title>
        <v-list-item-title class="font-weight-bold" style="font-size:30px" align="center">
          "{{this.$route.query.word}}" 을(를) 검색한 결과입니다.
          <v-icon color="blue" x-large>mdi-magnify</v-icon>
        </v-list-item-title>
      </v-list-item-content>
    </v-card>

    <v-container>
      <!--youtuber-->
      <v-container wrap style="background : white" border class="my-3">
        <v-row class="pt-0 pl-3">
          <v-col>
            <h1 class="font-weight-light mb-1">Youtuber</h1>
            <v-divider></v-divider>
          </v-col>
        </v-row>

        <v-container v-if="displayyoutuber.length == 0">
          <v-hover v-slot:default="{ hover }" open-delay="50">
            <v-card :elevation="hover ? 7 : 0" flat class="my-3 mx-3" shaped>
              <v-list-item-content
                class="justify-center py-6"
                style="background-color:#cdcdcd ; height : 250px"
              >
                <v-list-item-title class="font-weight-ligth" style="font-size:20px" align="center"></v-list-item-title>
                <v-list-item-title class="font-weight-black" align="center" style="font-size:25px">
                  <v-icon color="red" x-large>mdi-alert-circle</v-icon>검색어에 해당하는 유튜버가 없습니다.
                </v-list-item-title>
                <v-list-item-title
                  class="font-weight-ligth"
                  style="font-size:20px"
                  align="center"
                >유튜버를 추가하고 싶으신가요?</v-list-item-title>
                <v-list-item-title class="font-weight-ligth" style="font-size:20px" align="center">
                  <inputComponent></inputComponent>
                </v-list-item-title>
              </v-list-item-content>
            </v-card>
          </v-hover>
        </v-container>
        <v-container v-else>
          <v-hover
            v-slot:default="{ hover }"
            open-delay="50"
            v-for="(item,i) in displayyoutuber"
            :key="i"
          >
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
                <v-col cols="9" class="pa-1">
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
        <v-row>
          <v-col align="center">
            <v-btn text color="black" @click="youtuberPageDown">
              <v-icon>arrow_downward</v-icon>더보기
            </v-btn>
          </v-col>
        </v-row>
      </v-container>

      <!-- video -->
      <!-- 최신동영상 -->
      <v-container wrap style="background : white" border class="my-3">
        <v-row class="pt-0 pl-3">
          <v-col>
            <h1 class="font-weight-light mb-1">Video</h1>
            <v-divider></v-divider>
          </v-col>
        </v-row>
        <v-row class="mx-3">
          <v-hover
            v-slot:default="{ hover }"
            open-delay="50"
            v-for="(item,i) in displayvideo"
            :key="i"
          >
            <v-col cols="4" class="px-1">
              <v-card height="510px">
                <v-container class="pa-2">
                  <v-row>
                    <v-col>
                      <v-list-item-content class="py-0">
                        <iframe
                          :src="String('https://www.youtube.com/embed/')+item.videoID"
                          frameborder="0"
                          allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
                          allowfullscreen
                        ></iframe>
                      </v-list-item-content>
                    </v-col>
                  </v-row>
                  <v-row>
                    <v-col class="pt-0">
                      <p class="text-truncate title mb-0">{{item.videoName}}</p>
                      <p
                        style="font-size: 13px"
                      >게시일 : {{item.regDate}} / 조회수 : {{tc(item.videoViewCount)}} 회</p>
                      <p
                        v-html="item.videoDescription.substring(0,120).concat('...')"
                        class="font-weight-light"
                      ></p>
                    </v-col>
                  </v-row>
                  <v-row>
                    <v-col v-if ="item.tags.length != 1">
                      <v-btn
                        v-for="(tag,index) in item.tags"
                        :key="index"
                        rounded
                        color="#6EE3F7"
                        dark
                        class="ml-1 mb-1"
                      >{{tag}}</v-btn>
                    </v-col>
                  </v-row>
                </v-container>
              </v-card>
            </v-col>
          </v-hover>
        </v-row>

        <v-row>
          <v-col align="center">
            <v-btn text color="black" @click="videoPageDown">
              <v-icon>arrow_downward</v-icon>더보기
            </v-btn>
          </v-col>
        </v-row>
      </v-container>

      <!-- news -->
      <v-container wrap style="background : white" border class="my-3">
        <v-row class="pt-0 pl-3">
          <v-col>
            <h1 class="font-weight-light mb-1">News</h1>
            <v-divider></v-divider>
          </v-col>
        </v-row>
        <v-hover
          v-slot:default="{ hover }"
          open-delay="50"
          v-for="(item,i) in displaynews"
          :key="i"
        >
          <v-card :elevation="hover ? 7 : 0" outlined flat class="my-3 mx-3" shaped>
            <!-- 타이틀 -->
            <v-row>
              <v-col class="mx-5">
                <v-row>
                  <v-col cols="12" class="pb-0">
                    <a
                      target="_blank"
                      :href="item.newsLink"
                      v-html="item.newsTitle"
                      class="font-weight-black thin title ma-0 text-truncate"
                    ></a>
                  </v-col>
                </v-row>
                <!-- 게시 날짜 -->
                <v-row>
                  <v-col cols="12" class="py-0">
                    <p
                      class="font-weight-light thin ma-0"
                      style="font-size:13px"
                    >개설일 : {{item.newsDate}}</p>
                  </v-col>
                </v-row>
                <!-- 뉴스 설명 -->
                <v-row>
                  <v-col cols="12" class="py-1">
                    <span v-html="item.newsDescription"></span>
                  </v-col>
                </v-row>
              </v-col>
            </v-row>
          </v-card>
        </v-hover>
        <v-row>
          <v-col align="center">
            <v-btn text color="black" @click="newsPageDown">
              <v-icon>arrow_downward</v-icon>더보기
            </v-btn>
          </v-col>
        </v-row>
      </v-container>

    </v-container>
  </div>
</template>


<script>
import http from "../vuex/http-common";
import axios from "axios";
import tc from "thousands-counter";
import inputComponent from "../components/inputComponent";

export default {
  components: {
    inputComponent
  },
  name: "searchPage",

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
    youtuberPageDown() {
      this.pageyoutuber++;
      if (this.searchedyoutuber.length + this.range > this.pageyoutuber * 3) {
        this.displayyoutuber = this.searchedyoutuber.slice(
          0,
          this.pageyoutuber * this.range
        );
      } else {
        alert("유튜버 검색 결과의 끝 페이지입니다.");
      }
    },
    newsPageDown() {
      this.pagenews++;
      if (this.searchednews.length + this.range > this.pagenews * 3) {
        this.displaynews = this.searchednews.slice(
          0,
          this.pagenews * this.range
        );
      } else {
        alert("뉴스 검색 결과의 끝 페이지입니다.");
      }
    },
    videoPageDown() {
      this.pagevideo++;
      console.log(this.pagevideo + " " + this.searchednews.length);
      if (this.searchedvideo.length + this.range > this.pagevideo * 3) {
        this.displayvideo = this.searchedvideo.slice(
          0,
          this.pagevideo * this.range
        );
      } else {
        alert("비디오 검색 결과의 끝 페이지입니다.");
      }
    },
    failCallback() {
      var random = Math.floor(Math.random() * (10 - 1) + 1);
      this.$router.push({ path: 'youtuberPage', query: { word : this.$route.query.word , reloding : random}});
    },
  },
  mounted() {
    this.$vuetify.goTo(0);
    const youtuberSearch = new Promise((resolve, reject) => {
      http
        .get("/youtuber/search/" + this.$route.query.word)
        .then(response => {
          resolve(response);
        })
        .catch(err => {
          reject(err);
        });
    });

    const newsSearch = new Promise((resolve, reject) => {
      http
        .get("/news/search/" + this.$route.query.word)
        .then(response => {
          resolve(response);
        })
        .catch(err => {
          reject(err);
        });
    });

    const videoSearch = new Promise((resolve, reject) => {
      http
        .get("/video/search/" + this.$route.query.word)
        .then(response => {
          resolve(response);
        })
        .catch(err => {
          reject(err);
        });
    });

    Promise.all([youtuberSearch, newsSearch, videoSearch]).then(
      axios.spread((...responses) => {
        console.log("***************")
        console.log(responses)
        for (let index = 0; index < responses.length; index++) {
          if (responses[index].data.state != "ok") {
            console.log("fail");
            this.failCallback();
            return;
          }
        }

        this.searchedyoutuber = responses[0].data.data;
        this.displayyoutuber = this.searchedyoutuber.slice(0, 3);
        this.searchednews = responses[1].data.data;
        this.displaynews = this.searchednews.slice(0, 3);
        this.searchedvideo = responses[2].data.data;
        for (let index = 0; index < this.searchedvideo.length; index++) {
          var tags = this.searchedvideo[index].tags.split(",", 3);
          this.searchedvideo[index].tags = tags;
        }
        this.displayvideo = this.searchedvideo.slice(0, 3);

        console.log(this.searchedyoutuber);
        console.log(this.searchednews);
        console.log(this.searchedvideo);
      })
    );
  },
  computed: {},
  watch: {
    // $route(to, from) {
    //   this.$vuetify.goTo(0);
    //   if (to.path === "/searchPage") {
    //     if (to.query.word != from.query.word) {
          
    //     }
    //   }
    // }
  },
  data() {
    return {
      searchedyoutuber: [],
      searchednews: [],
      searchedvideo: [],
      displayyoutuber: [],
      displaynews: [],
      displayvideo: [],
      pageyoutuber: 1,
      pagenews: 1,
      pagevideo: 1,
      range: 6
    };
  }
};
</script>

<style scoped>
.circle {
  border-radius: 50%;
}
</style>
