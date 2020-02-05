import requests




videoExample='xx8P0ubZtcI'
channelExample='UCwx6n_4OcLgzAGdty0RWCoA'

v='BWROdI-AgAU'
list='UUwx6n_4OcLgzAGdty0RWCoA'

v='BWROdI-AgAU'
list='PLHqqPM2t7weIMhLb_1_xa7qyPOKW8OCiq'

play_list_url = 'https://www.youtube.com/watch?v=jEA3p1ekzSw&list=PLHqqPM2t7weIMhLb_1_xa7qyPOKW8OCiq&index=13'
#### contentDetails : 재생목록
{
 "kind": "youtube#channelSectionListResponse",
 "etag": "\"Fznwjl6JEQdo1MGvHOGaz_YanRU/GalZNtnGQ1a60cyof-HqeAmScFw\"",
 "items": [
  {
   "kind": "youtube#channelSection",
   "etag": "\"Fznwjl6JEQdo1MGvHOGaz_YanRU/GTBbbUrDFVG9-NLH7gXjqRuHS5k\"",
   "id": "UCwx6n_4OcLgzAGdty0RWCoA.Zx4DA4xg9IM"
  },
  {
   "kind": "youtube#channelSection",
   "etag": "\"Fznwjl6JEQdo1MGvHOGaz_YanRU/5qU7BFxWxeobKfVJVw7z6m04YpI\"",
   "id": "UCwx6n_4OcLgzAGdty0RWCoA.__WLXNpu6u8",
   "contentDetails": {
    "playlists": [
     "PLHqqPM2t7weIMhLb_1_xa7qyPOKW8OCiq"
    ]
   }
  },
  {
   "kind": "youtube#channelSection",
   "etag": "\"Fznwjl6JEQdo1MGvHOGaz_YanRU/p4NlyBZQclJkZ6XLwjeXAt8fOfk\"",
   "id": "UCwx6n_4OcLgzAGdty0RWCoA.nGzAI5pLbMY",
   "contentDetails": {
    "playlists": [
     "PLHqqPM2t7weI1KzN1_i5iHFtEhd6d-2k9"
    ]
   }
  }
 ]
}



#### snippets : 유튜버 첫 페이지 재생 목록
{
 "kind": "youtube#channelSectionListResponse",
 "etag": "\"Fznwjl6JEQdo1MGvHOGaz_YanRU/ZQQD6yhk_cyemSyJj9HnRrUzucY\"",
 "items": [
  {
   "kind": "youtube#channelSection",
   "etag": "\"Fznwjl6JEQdo1MGvHOGaz_YanRU/2R15d_NlbD_6t-yeNNWaeTx5D54\"",
   "id": "UCwx6n_4OcLgzAGdty0RWCoA.Zx4DA4xg9IM",
   "snippet": {
    "type": "recentUploads",
    "style": "horizontalRow",
    "channelId": "UCwx6n_4OcLgzAGdty0RWCoA",
    "position": 0
   }
  },
  {
   "kind": "youtube#channelSection",
   "etag": "\"Fznwjl6JEQdo1MGvHOGaz_YanRU/s4zmbHAiYSCXdjQgT7qmPxBkwMo\"",
   "id": "UCwx6n_4OcLgzAGdty0RWCoA.__WLXNpu6u8",
   "snippet": {
    "type": "singlePlaylist",
    "style": "horizontalRow",
    "channelId": "UCwx6n_4OcLgzAGdty0RWCoA",
    "position": 1
   }
  },
  {
   "kind": "youtube#channelSection",
   "etag": "\"Fznwjl6JEQdo1MGvHOGaz_YanRU/lc7h_4beq4habZbSCNhP5cZKHuY\"",
   "id": "UCwx6n_4OcLgzAGdty0RWCoA.nGzAI5pLbMY",
   "snippet": {
    "type": "singlePlaylist",
    "style": "horizontalRow",
    "channelId": "UCwx6n_4OcLgzAGdty0RWCoA",
    "position": 2
   }
  }
 ]
}


{
 "kind": "youtube#channelSectionListResponse",
 "etag": "\"Fznwjl6JEQdo1MGvHOGaz_YanRU/vTBIVGRkLRmkw9H4EJgVIXBhwpE\"",
 "items": [
  {
   "kind": "youtube#channelSection",
   "etag": "\"Fznwjl6JEQdo1MGvHOGaz_YanRU/AjGvkoCqkZgJRYdkHPqy0a7V3_U\"",
   "id": "UCwx6n_4OcLgzAGdty0RWCoA.Zx4DA4xg9IM"
  },
  {
   "kind": "youtube#channelSection",
   "etag": "\"Fznwjl6JEQdo1MGvHOGaz_YanRU/uL4QFFAi2lNdfmwNkkPBA9Mvk_A\"",
   "id": "UCwx6n_4OcLgzAGdty0RWCoA.__WLXNpu6u8"
  },
  {
   "kind": "youtube#channelSection",
   "etag": "\"Fznwjl6JEQdo1MGvHOGaz_YanRU/NbC8NvJ_PxcJTYL1x1HmA2vWnB4\"",
   "id": "UCwx6n_4OcLgzAGdty0RWCoA.nGzAI5pLbMY"
  }
 ]
}



#### playlistitem contentDetails. 특정 플레이리스트에 해당하는 비디오들을 가졍로 수 있다.
{
 "kind": "youtube#playlistItemListResponse",
 "etag": "\"Fznwjl6JEQdo1MGvHOGaz_YanRU/Sb_l9Kd1WwX_saB1fVTMGGqhSP4\"",
 "nextPageToken": "CAUQAA",
 "pageInfo": {
  "totalResults": 36,
  "resultsPerPage": 5
 },
 "items": [
  {
   "kind": "youtube#playlistItem",
   "etag": "\"Fznwjl6JEQdo1MGvHOGaz_YanRU/MoLTILu47NlR5LbPeJVIf3DKP78\"",
   "id": "UExIcXFQTTJ0N3dlSU1oTGJfMV94YTdxeVBPS1c4T0NpcS4zQzFBN0RGNzNFREFCMjBE",
   "contentDetails": {
    "videoId": "BWROdI-AgAU",
    "videoPublishedAt": "2020-01-17T09:00:08.000Z"
   }
  },
  {
   "kind": "youtube#playlistItem",
   "etag": "\"Fznwjl6JEQdo1MGvHOGaz_YanRU/DuItnkd935eTkTecw56oFdBGktQ\"",
   "id": "UExIcXFQTTJ0N3dlSU1oTGJfMV94YTdxeVBPS1c4T0NpcS5GNDg1Njc1QzZERjlFRjE5",
   "contentDetails": {
    "videoId": "8tAkcFB6U_k",
    "videoPublishedAt": "2020-01-10T09:00:07.000Z"
   }
  },
  {
   "kind": "youtube#playlistItem",
   "etag": "\"Fznwjl6JEQdo1MGvHOGaz_YanRU/tDxww-r1cx6eMOga0ZivcNuPniI\"",
   "id": "UExIcXFQTTJ0N3dlSU1oTGJfMV94YTdxeVBPS1c4T0NpcS4xOTEzQzhBQzU3MDNDNjcz",
   "contentDetails": {
    "videoId": "DiUIl2hKdFE",
    "videoPublishedAt": "2020-01-03T09:00:02.000Z"
   }
  },
  {
   "kind": "youtube#playlistItem",
   "etag": "\"Fznwjl6JEQdo1MGvHOGaz_YanRU/dxUFtT9mvrGS_yGWICxI8Uihv44\"",
   "id": "UExIcXFQTTJ0N3dlSU1oTGJfMV94YTdxeVBPS1c4T0NpcS5BRjJDODk5REM0NjkzMUIy",
   "contentDetails": {
    "videoId": "7anO9e8ozP8",
    "videoPublishedAt": "2019-12-27T09:00:05.000Z"
   }
  },
  {
   "kind": "youtube#playlistItem",
   "etag": "\"Fznwjl6JEQdo1MGvHOGaz_YanRU/RTySVyAzslEf7o8CDqEtMJTGIQw\"",
   "id": "UExIcXFQTTJ0N3dlSU1oTGJfMV94YTdxeVBPS1c4T0NpcS40QTA3NTU2RkM1QzlCMzYx",
   "contentDetails": {
    "videoId": "1T9RmTK3dQc",
    "videoPublishedAt": "2019-12-20T09:00:06.000Z"
   }
  }
 ]
}


### 가져온 최신영상

{
 "kind": "youtube#searchListResponse",
 "etag": "\"Fznwjl6JEQdo1MGvHOGaz_YanRU/2ckDK6u6I21b-7BTMu5QTHzg5WA\"",
 "nextPageToken": "CAoQAA",
 "regionCode": "KR",
 "pageInfo": {
  "totalResults": 665,
  "resultsPerPage": 10
 },
 "items": [
  {
   "kind": "youtube#searchResult",
   "etag": "\"Fznwjl6JEQdo1MGvHOGaz_YanRU/SCmZ0pHr_4hnvtjrlX-dxJI2-Yw\"",
   "id": {
    "kind": "youtube#video",
    "videoId": "YPMARa8Ex58"
   },
   "snippet": {
    "publishedAt": "2020-01-20T09:45:40.000Z",
    "channelId": "UCUpJs89fSBXNolQGOYKn0YQ",
    "title": "2020 자바스크립트 트렌드는 어떻게 될까?",
    "description": "약 2만명의 자바스크립트 개발자를 인터뷰하여 정리한 자료 모음! 자바스크립트 연말정산 State of JavaScript! https://2019.stateofjs.com 을 함께 보고
 분석해...",
    "thumbnails": {
     "default": {
      "url": "https://i.ytimg.com/vi/YPMARa8Ex58/default.jpg",
      "width": 120,
      "height": 90
     },
     "medium": {
      "url": "https://i.ytimg.com/vi/YPMARa8Ex58/mqdefault.jpg",
      "width": 320,
      "height": 180
     },
     "high": {
      "url": "https://i.ytimg.com/vi/YPMARa8Ex58/hqdefault.jpg",
      "width": 480,
      "height": 360
     }
    },
    "channelTitle": "노마드 코더 Nomad Coders",
    "liveBroadcastContent": "none"
   }
  },
  {
   "kind": "youtube#searchResult",
   "etag": "\"Fznwjl6JEQdo1MGvHOGaz_YanRU/xymYRM_P9xb-p1SS4AEb1wmrD-U\"",
   "id": {
    "kind": "youtube#video",
    "videoId": "ufLmReluPww"
   },
   "snippet": {
    "publishedAt": "2020-01-13T09:22:48.000Z",
    "channelId": "UCUpJs89fSBXNolQGOYKn0YQ",
    "title": "서버리스는 서버가 없는걸까? 8분 개념 설명!",
    "description": "서버리스(Serverless)는 서버가 없는것이 아니냐는 코알못의 질문에 개념 설명을 해드림. #코알못 #프로그래밍 #코딩 . Youtube 구독은 사랑입니다...",
    "thumbnails": {
     "default": {
      "url": "https://i.ytimg.com/vi/ufLmReluPww/default.jpg",
      "width": 120,
      "height": 90
     },
     "medium": {
      "url": "https://i.ytimg.com/vi/ufLmReluPww/mqdefault.jpg",
      "width": 320,
      "height": 180
     },
     "high": {
      "url": "https://i.ytimg.com/vi/ufLmReluPww/hqdefault.jpg",
      "width": 480,
      "height": 360
     }
    },
    "channelTitle": "노마드 코더 Nomad Coders",
    "liveBroadcastContent": "none"
   }
  },
  {
   "kind": "youtube#searchResult",
   "etag": "\"Fznwjl6JEQdo1MGvHOGaz_YanRU/EfLN3MND8JhgqsWPT-CQ74INQrw\"",
   "id": {
    "kind": "youtube#video",
    "videoId": "FF6CF8TZIhE"
   },
   "snippet": {
    "publishedAt": "2020-01-06T09:15:01.000Z",
    "channelId": "UCUpJs89fSBXNolQGOYKn0YQ",
    "title": "프로그래밍 독학할때 자주 하는 실수 5가지",
    "description": "2020년 첫 영상은 아무래도 혼자서 공부하느라 힘들고. 외롭고. 조언이 필요한 분들을 위해서 만들었어요! #코알못 #프로그래밍 #코딩 . . 10만 구독자...",
    "thumbnails": {
     "default": {
      "url": "https://i.ytimg.com/vi/FF6CF8TZIhE/default.jpg",
      "width": 120,
      "height": 90
     },
     "medium": {
      "url": "https://i.ytimg.com/vi/FF6CF8TZIhE/mqdefault.jpg",
      "width": 320,
      "height": 180
     },
     "high": {
      "url": "https://i.ytimg.com/vi/FF6CF8TZIhE/hqdefault.jpg",
      "width": 480,
      "height": 360
     }
    },
    "channelTitle": "노마드 코더 Nomad Coders",
    "liveBroadcastContent": "none"
   }
  },
  {
   "kind": "youtube#searchResult",
   "etag": "\"Fznwjl6JEQdo1MGvHOGaz_YanRU/QbXsdITVWEWmGCkSMOwPnRxQa9M\"",
   "id": {
    "kind": "youtube#video",
    "videoId": "xx8P0ubZtcI"
   },
   "snippet": {
    "publishedAt": "2019-12-30T12:30:21.000Z",
    "channelId": "UCUpJs89fSBXNolQGOYKn0YQ",
    "title": "2020년에 주목해야 할 Tech Top 5",
    "description": "Happy New Year! 올해도 어김없이 2020년 신년 주목해야할 tech top 5 를 소개합니다! 저희에게 2019년은 정말이지 덕분해 너무 감사하고 멋진 한해였습니
다....",
    "thumbnails": {
     "default": {
      "url": "https://i.ytimg.com/vi/xx8P0ubZtcI/default.jpg",
      "width": 120,
      "height": 90
     },
     "medium": {
      "url": "https://i.ytimg.com/vi/xx8P0ubZtcI/mqdefault.jpg",
      "width": 320,
      "height": 180
     },
     "high": {
      "url": "https://i.ytimg.com/vi/xx8P0ubZtcI/hqdefault.jpg",
      "width": 480,
      "height": 360
     }
    },
    "channelTitle": "노마드 코더 Nomad Coders",
    "liveBroadcastContent": "none"
   }
  },
  {
   "kind": "youtube#searchResult",
   "etag": "\"Fznwjl6JEQdo1MGvHOGaz_YanRU/sBfYWXy8ViWM1wNpw97-AKH4sMQ\"",
   "id": {
    "kind": "youtube#video",
    "videoId": "S-01KjUJ3_Q"
   },
   "snippet": {
    "publishedAt": "2019-12-23T08:31:54.000Z",
    "channelId": "UCUpJs89fSBXNolQGOYKn0YQ",
    "title": "과연 이 언어가 C.C++를 대체할 수 있을까? feat.아마존",
    "description": "무려 4년 연속 가장 사랑을 많이 받은 언어라고 하던데? 2019년이 다가기전에 이 언어는 알아두고 가세요! 그나저나 Go 무료 강의는? #코알못 #프로그래...",
    "thumbnails": {
     "default": {
      "url": "https://i.ytimg.com/vi/S-01KjUJ3_Q/default.jpg",
      "width": 120,
      "height": 90
     },
     "medium": {
      "url": "https://i.ytimg.com/vi/S-01KjUJ3_Q/mqdefault.jpg",
      "width": 320,
      "height": 180
     },
     "high": {
      "url": "https://i.ytimg.com/vi/S-01KjUJ3_Q/hqdefault.jpg",
      "width": 480,
      "height": 360
     }
    },
    "channelTitle": "노마드 코더 Nomad Coders",
    "liveBroadcastContent": "none"
   }
  },
  {
   "kind": "youtube#searchResult",
   "etag": "\"Fznwjl6JEQdo1MGvHOGaz_YanRU/9x14rTSPPC5hcQ-CShhdbc90Kdg\"",
   "id": {
    "kind": "youtube#video",
    "videoId": "ThGbP9wgkz8"
   },
   "snippet": {
    "publishedAt": "2019-12-16T08:51:32.000Z",
    "channelId": "UCUpJs89fSBXNolQGOYKn0YQ",
    "title": "누구나 코딩을 할 수 있다? 5가지 팩폭 드림.",
    "description": "사실 무려 2년전 올렸던 영상이기도합니다만. 워낙 자주 나오는 질문이기도 해서. (매일 같은 질문....따흑... ) 다시 한번 정리해봤습니다. #코알못...",
    "thumbnails": {
     "default": {
      "url": "https://i.ytimg.com/vi/ThGbP9wgkz8/default.jpg",
      "width": 120,
      "height": 90
     },
     "medium": {
      "url": "https://i.ytimg.com/vi/ThGbP9wgkz8/mqdefault.jpg",
      "width": 320,
      "height": 180
     },
     "high": {
      "url": "https://i.ytimg.com/vi/ThGbP9wgkz8/hqdefault.jpg",
      "width": 480,
      "height": 360
     }
    },
    "channelTitle": "노마드 코더 Nomad Coders",
    "liveBroadcastContent": "none"
   }
  },
  {
   "kind": "youtube#searchResult",
   "etag": "\"Fznwjl6JEQdo1MGvHOGaz_YanRU/bgaFKdXPNUNL3LcMMEDPMMQg6GU\"",
   "id": {
    "kind": "youtube#video",
    "videoId": "z9chRlD1tec"
   },
   "snippet": {
    "publishedAt": "2019-12-09T09:42:07.000Z",
    "channelId": "UCUpJs89fSBXNolQGOYKn0YQ",
    "title": "아직도 SQL을 모른다고해서 5분 설명해드림",
    "description": "아니, SQL 무시하남여?! 아, 그리고 ORM 까지 이해하기. 문과도 쌉가능. 데이터베이스 초보는 들어오세요. 여기가 맛집임. (응?) . . . #코알못 #프로그래
...",
    "thumbnails": {
     "default": {
      "url": "https://i.ytimg.com/vi/z9chRlD1tec/default.jpg",
      "width": 120,
      "height": 90
     },
     "medium": {
      "url": "https://i.ytimg.com/vi/z9chRlD1tec/mqdefault.jpg",
      "width": 320,
      "height": 180
     },
     "high": {
      "url": "https://i.ytimg.com/vi/z9chRlD1tec/hqdefault.jpg",
      "width": 480,
      "height": 360
     }
    },
    "channelTitle": "노마드 코더 Nomad Coders",
    "liveBroadcastContent": "none"
   }
  },
  {
   "kind": "youtube#searchResult",
   "etag": "\"Fznwjl6JEQdo1MGvHOGaz_YanRU/Ocah23ykHCRz28PTxbPRxR30dY8\"",
   "id": {
    "kind": "youtube#video",
    "videoId": "VDaMhtWNSQU"
   },
   "snippet": {
    "publishedAt": "2019-11-25T13:31:29.000Z",
    "channelId": "UCUpJs89fSBXNolQGOYKn0YQ",
    "title": "왜 구글의 프로그래밍 언어 Go가 겁나 핫한건지 5분 설명",
    "description": "문과도 쌉 가능(!!) 왜 구글의 프로그래밍 언어 Go lang 이 요즘 유명한걸까요? 그 이유는 마스코트(Gopher)가 귀여워서.....(!?!) 왜 다들 go lang을 외
치는지...",
    "thumbnails": {
     "default": {
      "url": "https://i.ytimg.com/vi/VDaMhtWNSQU/default.jpg",
      "width": 120,
      "height": 90
     },
     "medium": {
      "url": "https://i.ytimg.com/vi/VDaMhtWNSQU/mqdefault.jpg",
      "width": 320,
      "height": 180
     },
     "high": {
      "url": "https://i.ytimg.com/vi/VDaMhtWNSQU/hqdefault.jpg",
      "width": 480,
      "height": 360
     }
    },
    "channelTitle": "노마드 코더 Nomad Coders",
    "liveBroadcastContent": "none"
   }
  },
  {
   "kind": "youtube#searchResult",
   "etag": "\"Fznwjl6JEQdo1MGvHOGaz_YanRU/XVn8v6wSXAbFDrxwMoJJv4lt_hs\"",
   "id": {
    "kind": "youtube#video",
    "videoId": "67UwxR3ts2E"
   },
   "snippet": {
    "publishedAt": "2019-11-18T13:30:00.000Z",
    "channelId": "UCUpJs89fSBXNolQGOYKn0YQ",
    "title": "비밀번호 털렸다고?  암호화. 해시함수. 5분 설명.",
    "description": "프로그래밍은 몰라도. 요건 배워두면 인생에 도움이 될 수 있음. 누구나 이해할 수 있도록 쉽게 패스워드 암호화에 대해서 설명해봤어요~! 그나저나...",
    "thumbnails": {
     "default": {
      "url": "https://i.ytimg.com/vi/67UwxR3ts2E/default.jpg",
      "width": 120,
      "height": 90
     },
     "medium": {
      "url": "https://i.ytimg.com/vi/67UwxR3ts2E/mqdefault.jpg",
      "width": 320,
      "height": 180
     },
     "high": {
      "url": "https://i.ytimg.com/vi/67UwxR3ts2E/hqdefault.jpg",
      "width": 480,
      "height": 360
     }
    },
    "channelTitle": "노마드 코더 Nomad Coders",
    "liveBroadcastContent": "none"
   }
  },
  {
   "kind": "youtube#searchResult",
   "etag": "\"Fznwjl6JEQdo1MGvHOGaz_YanRU/AZa1m6eITX15Q_qYYQl-Q8v8sLo\"",
   "id": {
    "kind": "youtube#video",
    "videoId": "Wn7j5dfbJF4"
   },
   "snippet": {
    "publishedAt": "2019-11-11T10:23:07.000Z",
    "channelId": "UCUpJs89fSBXNolQGOYKn0YQ",
    "title": "코딩 인생 꿀템 VSC 단축키 5분 정리해드림",
    "description": "보고나면 고마울껄요? 껄껄. 그나저나 5분 시리즈를 워낙들 좋아하셔서 벗어날수가 없돠~~~ 또 궁금한것 있으시면 언제든 댓글로 남겨주세요~ #코린...",
    "thumbnails": {
     "default": {
      "url": "https://i.ytimg.com/vi/Wn7j5dfbJF4/default.jpg",
      "width": 120,
      "height": 90
     },
     "medium": {
      "url": "https://i.ytimg.com/vi/Wn7j5dfbJF4/mqdefault.jpg",
      "width": 320,
      "height": 180
     },
     "high": {
      "url": "https://i.ytimg.com/vi/Wn7j5dfbJF4/hqdefault.jpg",
      "width": 480,
      "height": 360
     }
    },
    "channelTitle": "노마드 코더 Nomad Coders",
    "liveBroadcastContent": "none"
   }
  }
 ]
}


### 영상별 상세 정보: videos API
{
	"etag": "\"Fznwjl6JEQdo1MGvHOGaz_YanRU/a1fYLUKXsAwsVga8ihCpHLL21Vs\"",
	"kind": "youtube#videoListResponse",
	"pageInfo": {
		"totalResults": 1,
		"resultsPerPage": 1
	},
	"items": [
		{
			"etag": "\"Fznwjl6JEQdo1MGvHOGaz_YanRU/YgbAFtE-uNsYlQ1pa03C-OIzoLE\"",
			"id": "YPMARa8Ex58",
			"kind": "youtube#video",
			"snippet": {
				"channelId": "UCUpJs89fSBXNolQGOYKn0YQ",
				"tags": [
					"코딩",
					"프로그래밍"
				],
				"categoryId": "27",
				"description": "약 2만명의 자바스크립트 개발자를 인터뷰하여 정리한 자료 모음!\n자바스크립트 연말정산 State of JavaScript!\nhttps://2019.stateofjs.com 을 함께 보고 분석해봤습니다. ;)\n1. JS Flavors\n2. Front-end Frameworks \n3. Data Layer \n4. Back-end Frameworks\n5. Mobile & Desktop\n6. Opinions\n참고로. 작년 영상은 요기 있어요 👇🏼\nhttps://youtu.be/lvgEdrDZUgY\n-\n무료JS 강의는 요기 있어요 👇🏼\nhttps://academy.nomadcoders.co/p/javascript-basics-for-absolute-beginners-kr\n.\nYoutube 구독은 사랑입니다 ❤️\n니콜라스와 코딩 공부하기 👉🏻https://academy.nomadcoders.co 👈🏻",
				"channelTitle": "노마드 코더 Nomad Coders",
				"publishedAt": "2020-01-20T09:45:40.000Z",
				"defaultAudioLanguage": "en",
				"defaultLanguage": "ko",
				"title": "2020 자바스크립트 트렌드는 어떻게 될까?",
				"thumbnails": {
					"medium": {
						"url": "https://i.ytimg.com/vi/YPMARa8Ex58/mqdefault.jpg",
						"width": 320,
						"height": 180
					},
					"default": {
						"url": "https://i.ytimg.com/vi/YPMARa8Ex58/default.jpg",
						"width": 120,
						"height": 90
					},
					"high": {
						"url": "https://i.ytimg.com/vi/YPMARa8Ex58/hqdefault.jpg",
						"width": 480,
						"height": 360
					}
				},
				"localized": {
					"description": "약 2만명의 자바스크립트 개발자를 인터뷰하여 정리한 자료 모음!\n자바스크립트 연말정산 State of JavaScript!\nhttps://2019.stateofjs.com 을 함께 보고 분석해봤습니다. ;)\n1. JS Flavors\n2. Front-end Frameworks \n3. Data Layer \n4. Back-end Frameworks\n5. Mobile & Desktop\n6. Opinions\n참고로. 작년 영상은 요기 있어요 👇🏼\nhttps://youtu.be/lvgEdrDZUgY\n-\n무료JS 강의는 요기 있어요 👇🏼\nhttps://academy.nomadcoders.co/p/javascript-basics-for-absolute-beginners-kr\n.\nYoutube 구독은 사랑입니다 ❤️\n니콜라스와 코딩 공부하기 👉🏻https://academy.nomadcoders.co 👈🏻",
					"title": "2020 자바스크립트 트렌드는 어떻게 될까?"
				},
				"liveBroadcastContent": "none"
			}
		}
	]
}


# video statistics

{
	"items": [
		{
			"statistics": {
				"favoriteCount": "0",
				"dislikeCount": "812",
				"viewCount": "2425948",
				"likeCount": "74599",
				"commentCount": "5713"
			},
			"etag": "\"Fznwjl6JEQdo1MGvHOGaz_YanRU/XJMNjXCEOMRzDleTqIWhClwHbwM\"",
			"id": "rOCVOr130X8",
			"kind": "youtube#video"
		}
	],
	"etag": "\"Fznwjl6JEQdo1MGvHOGaz_YanRU/BtcUIPbAJbutlvKEVDW4g_yhuJM\"",
	"kind": "youtube#videoListResponse",
	"pageInfo": {
		"totalResults": 1,
		"resultsPerPage": 1
	}
}

# video topic detail
{
	"kind": "youtube#videoListResponse",
	"pageInfo": {
		"resultsPerPage": 1,
		"totalResults": 1
	},
	"etag": "\"Fznwjl6JEQdo1MGvHOGaz_YanRU/mM5wtt8AtXJLKW_4wZzWHZK4N-0\"",
	"items": [
		{
			"topicDetails": {
				"topicIds": [
					"/m/019_rr"
				],
				"topicCategories": [
					"https://en.wikipedia.org/wiki/Technology",
					"https://en.wikipedia.org/wiki/Lifestyle_(sociology)"
				],
				"relevantTopicIds": [
					"/m/07c1v",
					"/m/019_rr",
					"/m/07c1v"
				]
			},
			"kind": "youtube#video",
			"etag": "\"Fznwjl6JEQdo1MGvHOGaz_YanRU/7uTth0pQbMmgi0OdN1tiXFbwNTk\"",
			"id": "wpUiN5hBnyc"
		}
	]
}

# video snippet
{
	"items": [
		{
			"id": "IZXgjR9INsA",
			"etag": "\"Fznwjl6JEQdo1MGvHOGaz_YanRU/jdqZVL1UGLok9YksigKBg66xCC0\"",
			"snippet": {
				"liveBroadcastContent": "none",
				"publishedAt": "2020-01-15T18:00:52.000Z",
				"defaultLanguage": "en-US",
				"channelTitle": "PewDiePie",
				"thumbnails": {
					"default": {
						"height": 90,
						"url": "https://i.ytimg.com/vi/IZXgjR9INsA/default.jpg",
						"width": 120
					},
					"medium": {
						"height": 180,
						"url": "https://i.ytimg.com/vi/IZXgjR9INsA/mqdefault.jpg",
						"width": 320
					},
					"standard": {
						"height": 480,
						"url": "https://i.ytimg.com/vi/IZXgjR9INsA/sddefault.jpg",
						"width": 640
					},
					"maxres": {
						"height": 720,
						"url": "https://i.ytimg.com/vi/IZXgjR9INsA/maxresdefault.jpg",
						"width": 1280
					},
					"high": {
						"height": 360,
						"url": "https://i.ytimg.com/vi/IZXgjR9INsA/hqdefault.jpg",
						"width": 480
					}
				},
				"categoryId": "24",
				"channelId": "UC-lHJZR3Gqxm24_Vd_AJ5Yw",
				"localized": {
					"description": "Goodbye, See you soon.\n\nNerd City: https://www.youtube.com/watch?v=gtyyvMKTCuA\n\n100 CLUB MERCH OUT NOW! https://represent.com/store/pewdiepie (Thank you)\n\nPewdiepie's Pixelings DOWNLOAD:\niOS: https://buff.ly/2pNG0aT\nAndroid: https://buff.ly/34C68nZ\n#pewdiepie #pixelings\n\nMinecraft Playlist:\nhttps://www.youtube.com/watch?v=mhgS6...\n\nMy Stores:\nTSUKI:\nhttps://tsuki.market/\nMerch:\nhttps://represent.com/store/pewdiepie\n\nI drink GFUEL (affiliate link):\nhttps://gfuel.ly/31Kargr\n\nMy Setup (affiliate links):\nChair: https://clutchchairz.com/pewdiepie/\nOfficial Razer hardware:\nRazer Nari Ultimate headset: http://rzr.to/pdp-razer-nari \nRazer Customs phone cases: http://rzr.to/pdp-razer-case\n\nNordVPN DOWNLOAD (affiliate link):\nGo to https://NordVPN.com/pewdiepie or use code PEWDIEPIE for a special holiday deal. Get a 3-year plan with 81% off plus two amazing gifts: 4 extra months + NordPass password manager app (worth $194.61)\n\nI stream on DLive (ad):\nhttps://go.dlive.tv/pewdiepie",
					"title": "It's been real, but I'm out!"
				},
				"tags": [
					"SATIRE",
					"pewdiepie break",
					"pewdiepie break from youtube",
					"taking a break",
					"pewdiepie lwiay",
					"lwiay",
					"pewds",
					"pewdie",
					"pdp",
					"It's been real",
					"but I'm out!",
					"im out"
				],
				"title": "It's been real, but I'm out!",
				"description": "Goodbye, See you soon.\n\nNerd City: https://www.youtube.com/watch?v=gtyyvMKTCuA\n\n100 CLUB MERCH OUT NOW! https://represent.com/store/pewdiepie (Thank you)\n\nPewdiepie's Pixelings DOWNLOAD:\niOS: https://buff.ly/2pNG0aT\nAndroid: https://buff.ly/34C68nZ\n#pewdiepie #pixelings\n\nMinecraft Playlist:\nhttps://www.youtube.com/watch?v=mhgS6...\n\nMy Stores:\nTSUKI:\nhttps://tsuki.market/\nMerch:\nhttps://represent.com/store/pewdiepie\n\nI drink GFUEL (affiliate link):\nhttps://gfuel.ly/31Kargr\n\nMy Setup (affiliate links):\nChair: https://clutchchairz.com/pewdiepie/\nOfficial Razer hardware:\nRazer Nari Ultimate headset: http://rzr.to/pdp-razer-nari \nRazer Customs phone cases: http://rzr.to/pdp-razer-case\n\nNordVPN DOWNLOAD (affiliate link):\nGo to https://NordVPN.com/pewdiepie or use code PEWDIEPIE for a special holiday deal. Get a 3-year plan with 81% off plus two amazing gifts: 4 extra months + NordPass password manager app (worth $194.61)\n\nI stream on DLive (ad):\nhttps://go.dlive.tv/pewdiepie",
				"defaultAudioLanguage": "en-GB"
			},
			"kind": "youtube#video"
		}
	],
	"etag": "\"Fznwjl6JEQdo1MGvHOGaz_YanRU/HJWYl4qei4s3n-qdR6CWU4hlQY8\"",
	"kind": "youtube#videoListResponse",
	"pageInfo": {
		"totalResults": 1,
		"resultsPerPage": 1
	}
}