import Constant from "./Constant";
import http from "./http-common";
import axios from "axios"

export default {
    [Constant.GET_YOUTUBERS_PER_CATEGORY]: (store, payload) => {
        console.log("action_GET_YOUTUBERS_PER_CATEGORY " + payload.category);

        http
            .get("/category/" + payload.category)
            .then(response => {

                //error 코드
                var failCallback = payload.failCallback;
                if (response.data.state != 'ok') {
                    console.log("너 여기 들어가니?")
                    failCallback();
                    return;
                }

                store.commit(Constant.GET_YOUTUBERS_PER_CATEGORY, {
                    youtuberslist: response.data.data
                });
            })
            .catch(exp => {
                alert("GET_YOUTUBERS_PER_CATEGORY에 실패하였습니다!\n" + exp);
            });
    },
    [Constant.GET_ALLYOUTUBER]: (store, payload) => {
        console.log("action_GET_ALLYOUTUBER ");
        http
            .get("/youtuber/all")
            .then(response => {
                console.log(response.data.data[0]);

                //error 코드
                var failCallback = payload.failCallback;
                if (response.data.status != 'ok') {
                    failCallback();
                    return;
                }

                store.commit(Constant.GET_YOUTUBERS_PER_CATEGORY, {
                    youtuberslist: response.data.data
                });
            })
            .catch(exp => {
                alert("Constant.GET_ALLYOUTUBER에 실패하였습니다\n" + exp);
            });
    },
    [Constant.GET_YOUTUBER]: (store, payload) => {
        console.log("action_GET_YOUTUBER ");

        var yno = payload.yno
        var callback = payload.callback
        var failCallback = payload.failCallback

        //youtuber 기본정보
        const BasicImpormation = new Promise((resolve, reject) => {
            http
                .get("/youtuber/" + yno)
                .then(response => {
                    resolve(response);
                })
                .catch(err => {
                    reject(err);
                });
        });


        // activity : youtuber 활동력 최근 {{month}}간 몇개의 영상을 올렸는지
        var month = 1
        const videoDuringMonth = new Promise((resolve, reject) => {
            http
                .get("/youtuber/detail/activity/videoCount/" + yno + "_" + month)
                .then(response => {
                    resolve(response);
                })
                .catch(err => {
                    reject(err);
                });
        });

        // activity : youtuber {{week}}주동안 영상 업로드 수
        var week = 4
        const video4Weeks = new Promise((resolve, reject) => {
            http
                .get("/youtuber/detail/activity/termVideoCount/" + yno + "_" + week)
                .then(response => {
                    resolve(response);
                })
                .catch(err => {
                    reject(err);
                });
        });

        // charm : 최근 {{recent}}개의 전체 좋아요비율
        var recent = 10
        const entiregoodratio = new Promise((resolve, reject) => {
            http
                .get("/youtuber/detail/charm/goodRatio/" + yno + "_" + recent)
                .then(response => {

                    resolve(response);
                })
                .catch(err => {
                    reject(err);
                });
        });

        // charm : 최근 {{videoCount}}개의 각 동영상의 좋아요 비율
        var videoCount = 3
        const goodRatioperVideo = new Promise((resolve, reject) => {
            http
                .get("/youtuber/detail/charm/video/" + yno + "_" + videoCount)
                .then(response => {
                    resolve(response);
                })
                .catch(err => {
                    reject(err);
                });
        });

        //influence : {{term}} 달간 달마다 커뮤니티에서 언급된 횟수
        var term = 12
        const communityCount = new Promise((resolve, reject) => {
            http
                .get("/youtuber/detail/influence/community/" + yno + "_" + term)
                .then(response => {
                    resolve(response);
                })
                .catch(err => {
                    reject(err);
                });
        });

        //influence : {{term}}달간 달마다 뉴스에서 언급된 횟수
        term = 12
        const newsCount = new Promise((resolve, reject) => {
            http
                .get("/youtuber/detail/influence/news/" + yno + "_" + term)
                .then(response => {
                    resolve(response);
                })
                .catch(err => {
                    reject(err);
                });
        });

        //subscriberCount,viewCount : {{num}}개의 증감추이
        var num = 100
        const subscriberViewCount = new Promise((resolve, reject) => {
            http
                .get("/youtuber/detail/trend/subscriberCount/" + yno + "_" + num)
                .then(response => {
                    resolve(response);
                })
                .catch(err => {
                    reject(err);
                });
        });

        //news 
        const news = new Promise((resolve, reject) => {
            http
                .get("/youtuber/detail/news/" + yno)
                .then(response => {
                    resolve(response);
                })
                .catch(err => {
                    reject(err);
                });
        });

        //유튜버가 속한 카테고리
        const categoryOfYoutuber = new Promise((resolve, reject) => {
            http
                .get("/youtuber/category/" + yno)
                .then(response => {
                    resolve(response);
                })
                .catch(err => {
                    reject(err);
                });
        });


        Promise.all([BasicImpormation, videoDuringMonth, video4Weeks, entiregoodratio, goodRatioperVideo, communityCount, newsCount, subscriberViewCount, news, categoryOfYoutuber]).then(
            axios.spread((...responses) => {

                var responsesNew = []

                for (let index = 0; index < responses.length; index++) {
                    if (responses[index].data.state != 'ok') {
                        console.log("fail")
                        failCallback();
                        return;
                    }
                }
                for (let index = 0; index < responses.length; index++) {
                    responsesNew.push(responses[index].data.data)
                }

                for (var i = 0; i < responses.length; i++) {
                    console.log(responses[i].data.data)
                }
                callback(...responsesNew)

            })
        )

    },
    [Constant.SEARCH_YOUTUBER]: (store, payload) => {
        console.log("action-SEARCH_YOUTUBER " + payload.searchWord);
        //store.commit(Constant.CHANGE_CATEGORY_LOADING, { bool: true });
        http
            .get("/youtuber/search/" + payload.searchWord)
            .then(response => {
                console.log(response.data.data);

                //error 코드
                var failCallback = payload.failCallback;
                if (response.data.status != 'ok') {
                    failCallback();
                    return;
                }

                store.commit(Constant.SEARCH_YOUTUBER, {
                    youtubers: response.data.data
                });
                //store.commit(Constant.CHANGE_CATEGORY_LOADING, { bool: false });
            })
            .catch(exp => {
                alert("GET_YOUTUBER 실패하였습니다\n" + exp);
            });
    },
    [Constant.GET_COMPARE_YOUTUBER]: (store, payload) => {

        var yno1 = payload.yno1;
        var yno2 = payload.yno2;
        var callback = payload.callback;

        //youtuber1 기본정보
        const BasicImpormation1 = new Promise((resolve, reject) => {
            http
                .get("/youtuber/" + yno1)
                .then(response => {
                    // if (response.data.stata == "fail") {}
                    resolve(response);
                })
                .catch(err => {
                    reject(err);
                });
        });

        //youtuber2 기본정보
        const BasicImpormation2 = new Promise((resolve, reject) => {
            http
                .get("/youtuber/" + yno2)
                .then(response => {
                    // if (response.data.stata == "fail") {}
                    resolve(response);
                })
                .catch(err => {
                    reject(err);
                });
        });


        // activity1 : youtuber {{week}}주동안 영상 업로드 수
        var week = 25
        const video4Weeks1 = new Promise((resolve, reject) => {
            http
                .get("/youtuber/detail/activity/termVideoCount/" + yno1 + "_" + week)
                .then(response => {
                    resolve(response);
                })
                .catch(err => {
                    reject(err);
                });
        });

        // activity2 : youtuber {{week}}주동안 영상 업로드 수
        week = 25
        const video4Weeks2 = new Promise((resolve, reject) => {
            http
                .get("/youtuber/detail/activity/termVideoCount/" + yno2 + "_" + week)
                .then(response => {
                    resolve(response);
                })
                .catch(err => {
                    reject(err);
                });
        });

        //subscriberCount,viewCount1 : {{num}}개의 증감추이
        var num = 50
        const subscriberViewCount1 = new Promise((resolve, reject) => {
            http
                .get("/youtuber/detail/trend/subscriberCount/" + yno1 + "_" + num)
                .then(response => {
                    resolve(response);
                })
                .catch(err => {
                    reject(err);
                });
        });


        //subscriberCount,viewCount2 : {{num}}개의 증감추이
        num = 50
        const subscriberViewCount2 = new Promise((resolve, reject) => {
            http
                .get("/youtuber/detail/trend/subscriberCount/" + yno2 + "_" + num)
                .then(response => {
                    resolve(response);
                })
                .catch(err => {
                    reject(err);
                });
        });


        Promise.all([BasicImpormation1, BasicImpormation2, video4Weeks1, video4Weeks2, subscriberViewCount1, subscriberViewCount2]).then(
            axios.spread((...responses) => {

                var responsesNew = []

                var failCallback = payload.failCallback
                for (let index = 0; index < responses.length; index++) {
                    if (responses[index].data.state != 'ok') {
                        console.log(responses[index].data);
                        console.log("fail");
                        failCallback();
                        return;
                    }
                }
                for (let index = 0; index < responses.length; index++) {
                    responsesNew.push(responses[index].data.data)
                }

                for (var i = 0; i < responses.length; i++) {
                    console.log(responses[i].data.data)
                }
                callback(...responsesNew);

            }))

    },

    [Constant.INSERT_YOUTUBUER]: (store, payload) => {
        //통신하기

        function replaceAll(str, searchStr, replaceStr) {
            return str.split(searchStr).join(replaceStr);
        }
        var address = replaceAll(payload.address, "/", "~")
        var callback = payload.callback


        console.log("INSERT_YOUTUBUER" + address)


        axios
            .get("http://15.165.77.1:8000/data/newYoutuber/" + address)
            .then(response => {
                var code = response.data.code
                var yno = response.data.yno

                console.log("*****************" + code)

                console.log(response);

                callback(code, yno)
            })
            .catch(exp => {
                callback(-100, 0)
                console.log(exp);

            });



    },

    [Constant.GET_MANYTOP5]: (store) => {
        // var callback = payload.callback;

        const subscriber = new Promise((resolve, reject) => {
            http
                .get("/youtuber/rank/subscriber_5")
                .then(response => {
                    resolve(response);
                })
                .catch(err => {
                    reject(err);
                });
        });

        const totalViewCount = new Promise((resolve, reject) => {
            http
                .get("/youtuber/rank/totalViewCount_5")
                .then(response => {
                    resolve(response);
                })
                .catch(err => {
                    reject(err);
                });
        });

        const totalVideoCount = new Promise((resolve, reject) => {
            http
                .get("/youtuber/rank/totalVideoCount_5")
                .then(response => {
                    resolve(response);
                })
                .catch(err => {
                    reject(err);
                });
        });

        const grade = new Promise((resolve, reject) => {
            http
                .get("/youtuber/rank/grade_5")
                .then(response => {
                    resolve(response);
                })
                .catch(err => {
                    reject(err);
                });
        });

        const clickCount = new Promise((resolve, reject) => {
            http
                .get("/youtuber/rank/clickCount_5")
                .then(response => {
                    resolve(response);
                })
                .catch(err => {
                    reject(err);
                });
        });



        Promise.all([subscriber, totalViewCount, totalVideoCount, grade, clickCount]).then(
            axios.spread((...responses) => {

                // var failCallback = payload.failCallback
                // for (let index = 0; index < responses.length; index++) {
                //     if (responses[index].data.status != 'ok') {
                //         console.log("fail")
                //         failCallback();
                //         return;
                //     }
                // }

                var list = []
                var titles = ["구독자", "총영상조회수", "총영상수", "등급", "사이트조회수"]

                for (var i = 0; i < responses.length; i++) {
                    list.push({ title: titles[i], list: responses[i].data.data })
                }

                console.log(list)

                // callback(responses[0], responses[1]);

                store.commit(Constant.GET_MANYTOP5, {
                    list: list
                });

            })
        );
    },
    [Constant.GET_YNO_FROM_URL]: (store, payload) => {
        function replaceAll(str, searchStr, replaceStr) {
            return str.split(searchStr).join(replaceStr);
        }
        var address = replaceAll(payload.url, "/", "~")
        axios
            .get("http://15.165.77.1:8000/data/ynoFromUrl/" + address)
            .then(response => {
                // console.log('얻어온 yno:', response.data.yno)
                store.commit(Constant.GET_YNO_FROM_URL, {
                    yno: response.data.yno
                });
            })
            .catch(exp => {
                exp
                // alert("GET_YNO_FROM_URL에 실패하였습니다\n" + exp);
            });
    },
    [Constant.GET_STATUS_FROM_YNO]: (store, payload) => {
        axios
            .get("http://15.165.77.1:8000/data/statusFromYno/" + payload.yno)
            .then(response => {
                // console.log('얻어온 status:', response.data.status)
                store.commit(Constant.GET_STATUS_FROM_YNO, {
                    value: response.data.status
                });
            })
            .catch(exp => {
                exp
                // alert("GET_STATUS_FROM_YNO에 실패하였습니다\n" + exp);
            });
    },
};