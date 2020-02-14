<template>
  <div>
    <div v-if="loading == 'loading'">
      <v-container>
        <v-row>
          <v-col cols="12">데이터 요청중입니다 ...</v-col>
        </v-row>
        <v-row>
          <v-spacer></v-spacer>
          <v-col>
            <v-progress-circular :size="200" :width="50" color="blue" indeterminate></v-progress-circular>
          </v-col>
          <v-spacer></v-spacer>
        </v-row>
      </v-container>
    </div>
    <div v-if="loading == 'fail'">서버와 오류가 발생헀습니다 새로고침(F5)를 눌러주세요.</div>
    <div v-if="loading == 'success'">
      <!-- header -->
      <v-card flat class="pa-0">
        <v-img :src="youtuber.bannerImageLink" class="py-6 lighten-5"></v-img>
      </v-card>

      <!-- content -->
      <v-container class="pa-0">
        <transition appear name="slide-fade">
          <!--기본정보-->
          <v-card class="my-3" outlined flat>
            <v-container fluid>
              <v-row>
                <!-- thumbnail -->
                <v-col cols="2" class="pa-3">
                  <v-img class="circle" :src="youtuber.thumbnails" flat :aspect-ratio="1/1" />
                </v-col>

                <!-- 기본정보 -->
                <v-col cols="10">
                  <v-row>
                    <v-col class="pb-0">
                      <span
                        class="font-weight-black thin display-3 ma-0"
                      >{{youtuber.channelName}}&nbsp;&nbsp;</span>
                      <v-btn
                        v-for="(category,index) in categoryOfYoutuber"
                        :key="index"
                        rounded
                        color="blue"
                        @click="onCategoryButtonClicked(category.cano)"
                        justify="center"
                      >
                        <b>{{category.name}}</b>
                      </v-btn>
                      <v-btn v-if="loginStatus" text icon color="red" @click="manageFav">
                        <v-icon v-if="flag" @click="deleteFav" x-large>mdi-heart</v-icon>
                        <v-icon v-if="!flag" @click="insertFav" x-large>mdi-heart-outline</v-icon>
                      </v-btn>
                    </v-col>
                  </v-row>
                  <v-row>
                    <v-col class="pt-0">
                      <span class="font-weight-light mr-4">개설일 : {{youtuber.publishedDate}}</span>
                      
                    </v-col>
                  </v-row>
                  <v-row>
                    <v-col class="ma-0 pa-0">
                      <v-divider class="pa-0 ma-0"></v-divider>
                    </v-col>
                  </v-row>

                  <v-row>
                    <v-col>
                      <span class="font-weight-bold">구독자 수</span>
                      <br />
                      {{tc(youtuber.subscriber)}}
                    </v-col>
                    <v-divider vertical class="mx-3"></v-divider>
                    <v-col>
                      <span class="font-weight-bold">총 영상 수</span>
                      <br />
                      {{youtuber.totalVideoCount}}
                    </v-col>
                    <v-divider vertical class="mx-3"></v-divider>
                    <v-col>
                      <span class="font-weight-bold">총 영상조회 수</span>
                      <br />
                      {{tc(youtuber.totalViewCount)}}
                    </v-col>
                    <v-divider vertical class="mx-3"></v-divider>
                    <!-- 외부링크 -->
                    <v-col cols="4">
                      <v-row align="center" style="float: left;">
                        <!--youtuber -->
                        <v-img
                          width="32px"
                          class="ml-2 mr-2 my-3"
                          src="../assets/youtubeIcon.png"
                          @click="openNewWindow(youtuber.channelLink)"
                          style="cursor:pointer"
                        />
                        <!-- instagram -->
                        <v-img
                          width="32px"
                          class="ml-2 mr-2 my-3"
                          v-if="otherLinkIcon[0] != '' "
                          src="../assets/instagramIcon.png"
                          @click="openNewWindow(otherLinkIcon[0])"
                          style="cursor:pointer"
                        />
                        <!-- twitter -->
                        <v-img
                          width="32px"
                          class="ml-2 mr-2 my-3"
                          v-if="otherLinkIcon[1] != '' "
                          src="../assets/twitterIcon.png"
                          @click="openNewWindow(otherLinkIcon[1])"
                          style="cursor:pointer"
                        />
                        <!-- facebook -->
                        <v-img
                          width="32px"
                          class="ml-2 mr-2 my-3"
                          v-if="otherLinkIcon[2] != '' "
                          src="../assets/facebookIcon.png"
                          @click="openNewWindow(otherLinkIcon[2])"
                          style="cursor:pointer"
                        />
                        <!-- tiktok -->
                        <v-img
                          width="32px"
                          class="ml-2 mr-2 my-3"
                          v-if="otherLinkIcon[3] != '' "
                          src="../assets/tiktokIcon.png"
                          @click="openNewWindow(otherLinkIcon[3])"
                          style="cursor:pointer"
                        />
                      </v-row>
                    </v-col>
                    <v-spacer></v-spacer>
                  </v-row>
                </v-col>
              </v-row>
            </v-container>
          </v-card>
        </transition>

        <v-row>
          <v-col cols="9">
            <v-col class="pa-0 pb-3">
              <v-card outlined flat>
                <v-row>
                  <v-col class="ma-5">
                    <v-list-item-title class="headline font-weight-black mb-1">능력치</v-list-item-title>
                    <v-divider></v-divider>
                  </v-col>
                </v-row>
                <apexchart
                  type="radar"
                  height="700"
                  :options="chartOptions"
                  :series="mainData"
                  id="myapexchart"
                  ref="myDiv"
                ></apexchart>
              </v-card>
            </v-col>
            <!-- 각능력치-->
            <v-col class="pa-0 py-3">
              <v-card outlined flat>
                <v-row>
                  <v-col class="ma-5 pb-0 mb-0">
                    <v-list-item-title class="headline font-weight-black mb-1">각능력치</v-list-item-title>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col>
                    <v-container>
                      <v-tabs v-model="tab" background-color="gray" dark grow fixed>
                        <v-tab>영향력</v-tab>
                        <v-tab>활동력</v-tab>
                        <v-tab>영상조회수증감추이</v-tab>
                        <v-tab>구독자증감추이</v-tab>
                        <v-tab>호감도</v-tab>
                      </v-tabs>

                      <v-tabs-items v-model="tab">
                        <!-- 영향력 -->
                        <v-tab-item>
                          <v-container class="ma-5">
                            <v-card outlined flat class="mr-10 my-3 pa-5">
                              <v-row class="pt-0 pl-3">
                                <v-col>
                                  <v-list-item-title
                                    class="headline font-weight-black mb-1"
                                  >지난 12개월간 커뮤니티 언급수</v-list-item-title>
                                  <v-divider></v-divider>
                                </v-col>
                              </v-row>
                              <v-row>
                                <v-col>
                                  <apexchart
                                    :options="influenceCommunityOption"
                                    :series="influenceCommunityData"
                                    style="width:100%"
                                  ></apexchart>
                                </v-col>
                              </v-row>
                            </v-card>
                            <v-card outlined flat class="mr-10 my-3 pa-5">
                              <v-row class="pt-0 pl-3">
                                <v-col>
                                  <v-list-item-title
                                    class="headline font-weight-black mb-1"
                                  >지난 12개월간 뉴스 언급수</v-list-item-title>
                                  <v-divider></v-divider>
                                </v-col>
                              </v-row>
                              <v-row>
                                <v-col>
                                  <apexchart
                                    :options="influenceNewsOption"
                                    :series="influenceNewsData"
                                    style="width:100%"
                                  ></apexchart>
                                </v-col>
                              </v-row>
                            </v-card>
                          </v-container>
                        </v-tab-item>

                        <!-- 활동력 -->
                        <v-tab-item>
                          <v-container class="ma-5">
                            <v-card outlined flat class="mr-10 my-3 pa-5">
                              <v-row class="pt-0 pl-3">
                                <v-col>
                                  <v-list-item-title class="headline font-weight-black mb-1">
                                    한달간 영상의 수는
                                    <b style="color: red">{{activityDuringMonth}}개</b> 입니다.
                                  </v-list-item-title>
                                  <v-divider></v-divider>
                                </v-col>
                              </v-row>
                              <v-row class="mr-10">
                                <v-col>
                                  <apexchart
                                    :options="activityOptions"
                                    :series="activity4weeksData"
                                    ref="activityChart"
                                    style="width:100%"
                                  ></apexchart>
                                </v-col>
                              </v-row>
                            </v-card>
                          </v-container>
                        </v-tab-item>

                        <!-- 영상조회수증감추이 -->
                        <v-tab-item>
                          <v-container class="ma-5">
                            <v-card outlined flat class="mr-10 my-3 pa-5">
                              <v-row class="pt-0 pl-3">
                                <v-col>
                                  <v-list-item-title
                                    class="headline font-weight-black mb-1"
                                  >지난 영상조회수증감추이</v-list-item-title>
                                  <v-divider></v-divider>
                                </v-col>
                              </v-row>
                              <v-row>
                                <v-col>
                                  <apexchart
                                    :options="subscriberViewOption"
                                    :series="viewData"
                                    style="width:100%"
                                  ></apexchart>
                                </v-col>
                              </v-row>
                            </v-card>
                          </v-container>
                        </v-tab-item>

                        <!-- 구독자증감추이 -->
                        <v-tab-item>
                          <v-container class="ma-5">
                            <v-card outlined flat class="mr-10 my-3 pa-5">
                              <v-row class="pt-0 pl-3">
                                <v-col>
                                  <v-list-item-title
                                    class="headline font-weight-black mb-1"
                                  >지난 구독자증감추이</v-list-item-title>
                                  <v-divider></v-divider>
                                </v-col>
                              </v-row>
                              <v-row>
                                <v-col>
                                  <apexchart
                                    :options="subscriberViewOption"
                                    :series="subscriberData"
                                    style="width:100%"
                                  ></apexchart>
                                </v-col>
                              </v-row>
                            </v-card>
                          </v-container>
                        </v-tab-item>

                        <!-- 호감도 -->
                        <v-tab-item>
                          <v-container class="ma-5">
                            <v-card outlined flat class="mr-10 my-3 pa-5">
                              <v-row class="pt-0 pl-3">
                                <v-col>
                                  <v-list-item-title
                                    class="headline font-weight-black mb-1"
                                  >최근 10개 동영상 좋아요/싫어요 비율</v-list-item-title>
                                  <v-divider></v-divider>
                                </v-col>
                              </v-row>
                              <v-row class="ma-5">
                                <v-col cols="2" align="right">
                                  <v-icon x-large color="blue">thumb_up</v-icon>
                                </v-col>
                                <v-col cols="8">
                                  <v-progress-linear
                                    background-color="red"
                                    color="blue"
                                    :value="entiregoodratio*100"
                                    height="40"
                                  >
                                    <template v-slot="{ value }">
                                      <strong>{{ value}}%</strong>
                                    </template>
                                  </v-progress-linear>
                                </v-col>
                                <v-col cols="2">
                                  <v-icon x-large color="red">thumb_down</v-icon>
                                </v-col>
                              </v-row>
                            </v-card>

                            <v-card outlined flat class="mr-10 my-3 pa-5">
                              <v-row class="pt-0 pl-3 pb-0">
                                <v-col>
                                  <v-list-item-title
                                    class="headline font-weight-black mb-1"
                                  >최근 3개의 동영상 좋아요비율</v-list-item-title>
                                  <v-divider></v-divider>
                                </v-col>
                              </v-row>
                              <v-row v-for="(video,i) in recentVideoList" :key="i" class="pa-1">
                                <v-col cols="6">
                                  <iframe
                                    :src="String('https://www.youtube.com/embed/')+video.videoID"
                                    frameborder="0"
                                    allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
                                    allowfullscreen
                                  ></iframe>
                                </v-col>
                                <v-col cols="6">
                                  <v-card outlined>
                                    <v-container>
                                      <v-list-item-content>
                                        <v-list-item-title
                                          class="mb-1 text-truncate"
                                        >{{video.videoName}}</v-list-item-title>
                                        <v-list-item-subtitle align="right">{{video.regDate}}</v-list-item-subtitle>
                                      </v-list-item-content>
                                      <v-divider></v-divider>

                                      <v-row>
                                        <v-col
                                          class="pa-1"
                                          cols="2"
                                          style="text-align : center"
                                        >{{video.good}}</v-col>
                                        <v-col class="pa-1">
                                          <v-progress-linear
                                            background-color="red"
                                            color="blue"
                                            :value="video.goodRatio==0 ? 50 : video.goodRatio*100"
                                            height="30"
                                          ></v-progress-linear>
                                        </v-col>
                                        <v-col
                                          class="pa-1"
                                          cols="2"
                                          style="text-align : center"
                                        >{{video.bad}}</v-col>
                                      </v-row>
                                    </v-container>
                                  </v-card>
                                </v-col>
                              </v-row>
                            </v-card>
                          </v-container>
                        </v-tab-item>
                      </v-tabs-items>
                    </v-container>
                  </v-col>
                </v-row>
              </v-card>
            </v-col>

            <!-- 최신동영상 -->
            <v-col class="pa-0 pb-3">
              <v-card outlined flat class="mr-0 my-3 pa-3">
                <v-row class="pt-0 pl-3 pb-0">
                  <v-col>
                    <v-list-item-title class="headline font-weight-black mb-1">최신동영상</v-list-item-title>
                    <v-divider></v-divider>
                  </v-col>
                </v-row>
                <!-- scroll 녛기 -->
                <v-row class="pt-0 pl-0 pb-0 ml-0 mr-1">
                  <v-col
                    v-for="(item, $index) in videolist"
                    :key="$index"
                    :data-num="$index + 1"
                    class="pa-5"
                    cols="6"
                  >
                    <v-card>
                      <v-container>
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
                              style="color:gray"
                            ></p>
                          </v-col>
                        </v-row>
                      </v-container>
                    </v-card>
                  </v-col>
                </v-row>
                <infinite-loading @infinite="infiniteHandler"></infinite-loading>
              </v-card>
            </v-col>
          </v-col>

          <v-col cols="3">
            <!-- 등급 -->
            <v-card outlined flat class="pa-4 pt-0 mb-3">
              <v-row>
                <v-col class="ma-5 mx-0">
                  <v-list-item-title class="headline font-weight-black mb-1">
                    등급
                    <v-tooltip bottom>
                      <template v-slot:activator="{ on }">
                        <v-icon v-on="on">info</v-icon>
                      </template>
                      <span>
                        등급산정기준은 현재 사이트 기준으로 상위 5%는
                        <br />SS등급, 10%는 S등급, 20%는 A등급, 50%는 B등급, 80%는 C등급으로 챙적하고 있습니다.
                      </span>
                    </v-tooltip>
                  </v-list-item-title>
                  <v-divider></v-divider>
                </v-col>
              </v-row>
              <transition appear name="fade">
                <!-- <v-btn
                  fab
                  :color="setGradeColor(youtuber.grade)"
                  style="width: 100%;height: 0;padding-bottom: 50%; padding-top: 50%;"
                >
                  <p
                    style="font-weight-black text-align: center;position: absolute;top: 50%;left: 50%;transform: translate(-50%, -50%);color: white;font-size: 150px;"
                  >{{setGrade(youtuber.grade)}}</p>
                </v-btn>-->
                <v-btn
                  fab
                  :color="setGradeColor(youtuber.grade)"
                  style="width: 100%;height: 0;padding-bottom: 50%; padding-top: 40%;"
                >
                  <p
                    style="font-weight-black text-align: center;position: absolute;top: 50%;left: 50%;transform: translate(-50%, -50%);color: white;font-size: 150px;"
                  >{{setGrade(youtuber.grade)}}</p>
                </v-btn>
              </transition>
            </v-card>

            <!-- 최신뉴스 -->
            <v-card outlined flat class="pa-4 pt-0">
              <v-row>
                <v-col class="ma-5 mx-0 mb-0 pb-0">
                  <v-list-item-title class="headline font-weight-black mb-1">최신뉴스</v-list-item-title>
                  <v-divider></v-divider>
                </v-col>
              </v-row>
              <v-hover
                v-slot:default="{ hover }"
                open-delay="100"
                v-for="i in ((news.length >= 5)?[0,1,2,3,4]:news.slice(0,news.length))"
                :key="i"
              >
                <v-card class="my-3 px-2" :elevation="hover ? 7 : 0">
                  <v-list-item-content>
                    <v-list-item-title class="mb-1 text-truncate">
                      <a target="_blank" :href="news[i].newsLink" v-html="news[i].newsTitle"></a>
                    </v-list-item-title>
                    <v-list-item-subtitle class="mb-3" align="right">{{news[i].newsDate}}</v-list-item-subtitle>
                    <span v-html="news[i].newsDescription.substring(0,300).concat('...')"></span>
                  </v-list-item-content>
                </v-card>
              </v-hover>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </div>
  </div>
</template>

<script>
import http from "../vuex/http-common";
import Constant from "../vuex/Constant";
import InfiniteLoading from "vue-infinite-loading";
import tc from "thousands-counter";

export default {
  name: "youtuberPage",
  components: {
    InfiniteLoading
  },
  beforecreated() {},
  created() {
    this.$vuetify.goTo(0);
    this.loading = "loading";
  },
  mounted() {
    this.$store.dispatch(Constant.GET_YOUTUBER, {
      yno: this.$route.query.yno,
      callback: this.render,
      failCallback: this.failCallback
    });
    if (this.$session.exists()) {
      this.loginStatus = true;
      let initialUrl = this.$route.query.yno + "&" + this.$session.get("token");
      console.log(initialUrl);
      http
        .get("/favorite/select/" + initialUrl)
        .then(data => (this.flag = data.data.data == 0 ? false : true));
    }
  },
  methods: {
    manageFav() {
      this.flag ? (this.flag = false) : (this.flag = true);
    },
    insertFav() {
      console.log("insert");
      console.log(this.$session.get("token"));
      console.log(this.youtuber.yno);
      let par = this.youtuber.yno + "&" + this.$session.get("token");
      http
        .get("/favorite/insert/" + par)
        .then(function(response) {
          console.log(response);
        })
        .catch(function(error) {
          console.log(error);
        });
    },
    deleteFav() {
      console.log("delete");
      console.log(this.$session.get("token"));
      console.log(this.youtuber.yno);
      let par = this.youtuber.yno + "&" + this.$session.get("token");
      let deleteUrl = "/favorite/delete/" + par;
      http
        .delete(deleteUrl)
        .then(function(response) {
          console.log(response);
        })
        .catch(function(error) {
          console.log(error);
        });
    },
    render(...responses) {
      var youtuber = responses[0];
      var activityDuringMonth = responses[1];
      var activity4weeks = responses[2];
      var charmentiregoodratio = responses[3];
      var charmRecentVideo = responses[4];
      var influencecommunity = responses[5];
      var influencenews = responses[6];
      var subscriberView = responses[7];
      var news = responses[8];
      var categoryOfYoutuber = responses[9];

      //데이터 집어넣기
      this.youtuber = youtuber;
      this.activityDuringMonth = activityDuringMonth;
      this.entiregoodratio = charmentiregoodratio;
      this.recentVideoList = charmRecentVideo;
      this.news = news;
      this.categoryOfYoutuber = categoryOfYoutuber;

      //활동력 : 차트에 데이터 집어넣기
      this.activity4weeksData = [
        {
          name: " ",
          data: [
            activity4weeks[0],
            activity4weeks[1],
            activity4weeks[2],
            activity4weeks[3]
          ],
          animation: true
        }
      ];

      //mainData 집어넣기
      var influence = this.youtuber.influence;
      var activity = this.youtuber.activity;
      var viewCountTrend = this.youtuber.viewCountTrend;
      var subscriberCountTrend = this.youtuber.subscriberCountTrend;
      var charm = this.youtuber.charm;
      this.mainData = [
        {
          name: " ",
          data: [
            influence,
            activity,
            viewCountTrend,
            subscriberCountTrend,
            charm
          ]
        }
      ];

      //influece Comminuty Data 집어넣기
      for (let index = 0; index < influencecommunity.length; index++) {
        this.influenceCommunityData[0]["data"].push(influencecommunity[index]);
        this.influenceCommunityOption["xaxis"]["categories"].push(
          influencecommunity.length - index + "주 전"
        );
      }

      //influece new Data 집어넣기
      for (let index = 0; index < influencenews.length; index++) {
        this.influenceNewsData[0]["data"].push(influencenews[index]);
        this.influenceNewsOption["xaxis"]["categories"].push(
          influencenews.length - index + "주 전"
        );
      }

      //subscriberView Data 집어넣기
      console.log(subscriberView.length)
      for (let index = 0; index < subscriberView.length; index++) {
        this.subscriberData[0]["data"].push(
          subscriberView[index]["pointSubscriber"]
        );
        this.viewData[0]["data"].push(subscriberView[index]["pointView"]);
        this.subscriberViewOption["xaxis"]["categories"].push(
          subscriberView[index]["recordDate"]
        );
      }

      this.makeOtherLinkIcon();
      this.loading = "success";

      console.log(this.loading);
      // this.renderMainChart();
      // this.renderActivityChart(activity4weeks);
    },

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
    failCallback() {
      var random = Math.floor(Math.random() * (10 - 1) + 1);
      this.$router.push({
        path: "youtuberPage",
        query: { yno: this.$route.query.yno, reloding: random }
      });
    },
    onCategoryButtonClicked(i) {
      localStorage.setItem("currentCategory", i);
      this.$router.push("/categoryPage");
    },
    makeOtherLinkIcon() {
      var site = ["instagram", "twitter", "facebook", "tiktok"];
      var y = this.youtuber;
      var link = [
        y.otherLink1,
        y.otherLink2,
        y.otherLink3,
        y.otherLink4,
        y.otherLink5
      ];

      this.otherLinkIcon = ["", "", "", ""];

      for (let i = 0; i < link.length; i++) {
        for (let j = 0; j < site.length; j++) {
          if (link[i].indexOf(site[j]) != -1) {
            this.otherLinkIcon[j] = link[i];
            break;
          }
        }
      }
    },
    openNewWindow(str) {
      window.open(str);
    },
    infiniteHandler($state) {
      var range = 10;
      var rawList = [];
      http
        .get("/youtuber/detail/video/" + this.$route.query.yno)
        .then(({ data }) => {
          rawList = data.data;
          var tmplist = rawList.slice(
            this.page * range,
            this.page * range + range
          );
          console.log(rawList);
          if (tmplist.length > 0) {
            this.page += 1;
            this.videolist.push(...tmplist);
            $state.loaded();
          } else {
            $state.complete();
          }
        });
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
    }
  },
  computed: {},
  data() {
    return {
      youtuber: {},
      mainData: [],
      chartOptions: {
        chart: {
          type: "radar",
          dropShadow: {
            enabled: true,
            blur: 1,
            left: 1,
            top: 1
          },
          toolbar: {
            show: false
          }
        },
        title: {},
        stroke: {
          width: 0
        },
        fill: {
          opacity: 0.4
        },
        markers: {
          size: 0
        },
        xaxis: {
          categories: [
            "영향력",
            "활동력",
            "영상조회수증감추이",
            "구독자증감추이",
            "호감도"
          ],
          labels: {
            style: {
              fontSize: "20px",
              colors: ["black", "black", "black", "black", "black"],
              fontFamily: "bold"
            }
          }
        },
        yaxis: {
          show: false,
          max: 100,
          min: 0
        },
        dataLabels: {
          enabled: true,
          background: {
            enabled: true,
            borderRadius: 2
          }
        },
        animations: {
          enabled: false
        }
      },
      activityOptions: {
        series: [],
        chart: {
          type: "line",
          zoom: {
            enabled: false
          }
        },
        dataLabels: {
          enabled: true
        },
        stroke: {
          width: 7,
          curve: "smooth"
        },
        title: {
          text: "동영상",
          align: "center"
        },
        grid: {
          row: {
            colors: ["#f3f3f3", "transparent"],
            opacity: 0.5
          }
        },
        xaxis: {
          categories: ["4주전", "3주전", "2주전", "1주전"]
        }
      },
      influenceCommunityOption: {
        series: [],
        chart: {
          type: "line",
          zoom: {
            enabled: false
          }
        },
        dataLabels: {
          enabled: true
        },
        stroke: {
          width: 7,
          curve: "smooth"
        },
        title: {
          align: "center"
        },
        grid: {
          row: {
            colors: ["#f3f3f3", "transparent"],
            opacity: 0.5
          }
        },
        xaxis: {
          categories: []
        }
      },
      influenceNewsOption: {
        series: [],
        chart: {
          type: "line",
          zoom: {
            enabled: false
          }
        },
        dataLabels: {
          enabled: true
        },
        stroke: {
          width: 7,
          curve: "smooth"
        },
        title: {
          align: "center"
        },
        grid: {
          row: {
            colors: ["#f3f3f3", "transparent"],
            opacity: 0.5
          }
        },
        xaxis: {
          categories: []
        }
      },
      subscriberViewOption: {
        series: [],
        chart: {
          type: "line",
          zoom: {
            enabled: false
          }
        },
        dataLabels: {
          enabled: false
        },
        stroke: {
          width: 7,
          curve: "smooth"
        },
        title: {
          align: "center"
        },
        grid: {
          row: {
            colors: ["#f3f3f3", "transparent"],
            opacity: 0.5
          }
        },
        xaxis: {
          categories: []
        }
      },
      activityDuringMonth: 0,
      entiregoodratio: 0,
      recentVideoList: [],
      tab: null,
      activity4weeksData: [],
      loading: "loading",
      influenceCommunityData: [{ data: [] }],
      influenceNewsData: [{ data: [] }],
      subscriberData: [{ data: [] }],
      viewData: [{ data: [] }],
      news: [],
      categoryOfYoutuber: [],
      otherLinkIcon: [],
      flag: false,
      page: 0,
      videolist: [],
      loginStatus: false
    };
  }
};
</script>

<style scoped>
.slide-fade-enter-active {
  transition: all 2s ease;
}
.slide-fade-leave-active {
  transition: all 0.8s cubic-bezier(1, 0.5, 0.8, 1);
}
.slide-fade-enter, .slide-fade-leave-to
/* .slide-fade-leave-active below version 2.1.8 */ {
  transform: translateX(100px);
  opacity: 0;
}
.circle {
  border-radius: 50%;
}
.jb {
  text-align: center;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  color: white;
}
.fade-enter-active,
.fade-leave-active {
  transition: opacity 3s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0;
}
.ellipsis {
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 3; /* number of lines to show */
}
</style>
