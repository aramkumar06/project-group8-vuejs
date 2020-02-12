# -*- encoding: utf-8 -*-

from django.shortcuts import render, HttpResponse
import threading
import datetime
from dataServer.models import Youtuber, Trend, Video, Community, CategoryYoutubeRelation, Category, News, Naverdatalab, Stat
from dataServer.function import get_channel_other_sites
from dataServer.views import update_stat_without_request
import time
from decouple import config
import urllib.request
import json
import pprint
from pytz import timezone, tzinfo
from django.utils import timezone
from IPython import embed
import requests
from dataServer.function import date_is_valid
from dataServer.stat import get_influence, get_activity3, get_views, get_trend, get_charm, get_grade


GOOGLE_KEY_LIST = [config('GOOGLEAPIKEY5'), config('GOOGLEAPIKEY7'), config('GOOGLEAPIKEY6'), config('GOOGLEAPIKEY8'), config('GOOGLEAPIKEY1'), config('GOOGLEAPIKEY2'), config('GOOGLEAPIKEY3'), config('GOOGLEAPIKEY4'), config('GOOGLEAPIKEY9')]
GOOGLE_KEY_INDEX = 0

DAUM_API_KEYS = [config('DAUM_API_KEY1'), config('DAUM_API_KEY2')]
DAUM_API_INDEX = 0

NAVER_ID_LIST = [config('X_NAVER_CLIENT_ID1'), config('X_NAVER_CLIENT_ID2')]
NAVER_SECRET_LIST = [config('X_NAVER_CLIENT_SECRET1'), config('X_NAVER_CLIENT_SECRET2')]
NAVER_ID_INDEX = 0

NAVER_DATA_ID = [config('NAVER_DATALAB_CLIENT_ID1'), config('NAVER_DATALAB_CLIENT_ID2')]
NAVER_DATA_SECRET = [config('NAVER_DATALAB_CLIENT_SECRET1'), config('NAVER_DATALAB_CLIENT_SECRET2')]
NAVER_DATA_ID_INDEX = 0

NECESSARY_WORD = [
    ['유튜브', '유튜버', '유투버', '채널'],
    ['게임', 'game'],
    ['엔터테인먼트', '예능', 'entertainment'],
    ['뷰티', '화장', '패션'],
    ['운동', 'Sports', '스포츠', '헬스'],
    ['먹방', '음식', '푸드', 'Food'],
    ['키즈', '어린이', 'Kids'],
    ['동물', '애니멀', 'Animal'],
    ['일상', '브이로그', 'V-log', 'Vlog'],
    ['IT', 'SW', '소프트웨어', '기술', '신제품', '노트북', '컴퓨터', '시스템', '스마트폰', '무선']
]

MONTH = ['', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

UPDATE_CIRCLE = 3600

LAST_ALL_UPDATE = Youtuber.objects.all()[0].updateddate

class updateThread:
    def __init__(self):
        pass

    def threadOpen(self):
        global GOOGLE_KEY_INDEX, GOOGLE_KEY_LIST
        global DAUM_API_KEYS, DAUM_API_INDEX
        global NAVER_ID_LIST, NAVER_SECRET_LIST, NAVER_ID_INDEX, NAVER_SECRET_INDEX
        global NAVER_DATA_ID, NAVER_DATA_SECRET, NAVER_DATA_ID_INDEX, NAVER_DATA_SECRET_INDEX
        global NECESSARY_WORD, MONTH
        global LAST_ALL_UPDATE, UPDATE_CIRCLE
        
        TIME_CHECK = datetime.datetime.now()
        
        if (TIME_CHECK - LAST_ALL_UPDATE).days >= 1:
            # 하루가 지나면 업데이트 시행
            print("-------------------------- UPDATE IS STARTED!")
            START = datetime.datetime.now() # 시작 시간
            youtubers = Youtuber.objects.all()
            left_google_api_keys = len(GOOGLE_KEY_LIST)
            for  youtuber in youtubers:
                print("-------------------------- Youtuber {}'s update is started!".format(youtuber.yno))
                ONE_START = datetime.datetime.now() # 시작 시간
                ################## 유튜버 테이블 업데이트
                while left_google_api_keys:
                    try:
                        KEY = GOOGLE_KEY_LIST[GOOGLE_KEY_INDEX]
                        base_url = "https://www.googleapis.com/youtube/v3/channels"
                        part = "snippet,brandingSettings,contentDetails,statistics"
                        response = urllib.request.urlopen(base_url + "?part=%s&id=%s&key=%s" % (part, youtuber.channelid, KEY))
                        break
                    except:
                        print('*--- next google key setting ---*')
                        GOOGLE_KEY_INDEX += 1
                        GOOGLE_KEY_INDEX %= len(GOOGLE_KEY_LIST)
                        left_google_api_keys -= 1
                if not left_google_api_keys:
                    print('key is expired during updating Youtuber Page. {} is not updated.'.format(youtuber.yno))
                    return HttpResponse('key is expired during updating Youtuber Page. {} is not updated.'.format(youtuber.yno))  # api_key 모두 소진
    
                info_obj = json.loads(response.read().decode('utf-8')).get('items')[0]
                
                snippet = info_obj.get('snippet')
                statistics = info_obj.get('statistics')
                branding_settings = info_obj.get('brandingSettings')
                content_details = info_obj.get('contentDetails')

                other_links = ['', '', '', '', '']
                for (i, site) in enumerate(get_channel_other_sites(youtuber.channellink)):
                    other_links[i] = site
                
                now = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=9) # 한국시간 기준
                
                youtuber.channelname = snippet.get('title')
                youtuber.youtubername = snippet.get('customURL')
                youtuber.channeldescription = snippet.get('description')
                youtuber.bannerimagelink = branding_settings.get('image').get('bannerImageUrl')
                if '/default_banner' in youtuber.bannerimagelink:
                    youtuber.bannerimagelink = ''
                youtuber.thumbnails = snippet.get('thumbnails').get('default').get('url')
                youtuber.subscriber = statistics.get('subscriberCount')  # 이건 트렌드에도 추가해야 됨
                youtuber.totalviewcount = statistics.get('viewCount')    # 이건 트렌드에도 추가해야 됨
                youtuber.totalvideocount = statistics.get('videoCount')
                youtuber.updateddate = '{0:04d}-{1:02d}-{2:02d} {3:02d}:{4:02d}:{5:02d}'.format(now.year, now.month, now.day, now.hour, now.minute, now.second)
                youtuber.otherlink1 = other_links[0]
                youtuber.otherlink2 = other_links[1]
                youtuber.otherlink3 = other_links[2]
                youtuber.otherlink4 = other_links[3]
                youtuber.otherlink5 = other_links[4]
                youtuber.uploadsid = content_details.get('relatedPlaylists').get('uploads')
                
                youtuber.save()
                
                print("------------- Yno {}'s youtuber table is updated.".format(youtuber.yno))
                
                ################# 트렌드 새로운 열 추가
                target_youtuber = Youtuber.objects.get(yno=youtuber.yno)
                
                last_trend = Trend.objects.all().filter(yno=youtuber).order_by('-recorddate')[0]
                last_date = last_trend.recorddate
                
                
                if last_date.day != now.day and last_date.month != now.month and last_date.year != now.year: 
                    last_subscriber = last_trend.pointsubscriber
                    last_pointview = last_trend.pointview
                    
                    new_trend = Trend.objects.create(
                        yno = target_youtuber,
                        recorddate = '{0:04d}-{1:02d}-{2:02d}'.format(now.year, now.month, now.day),
                        pointsubscriber = target_youtuber.subscriber,
                        difsubscriber = target_youtuber.subscriber - last_subscriber, # 이전 꺼 가져오기
                        pointview = target_youtuber.totalviewcount,
                        difview = target_youtuber.totalviewcount - last_pointview,
                    )
                    
                    new_trend.save()
                    
                    print("------------- Yno {}'s trend table is updated.".format(youtuber.yno))
                else:
                    print("------------- Yno {}'s trend table is not updated since last update is duplicate.".format(youtuber.yno))
                
                
                ################## 새로운 영상들 가져오기
                base_url = "https://www.googleapis.com/youtube/v3/playlistItems"
                upload_id = youtuber.uploadsid
                while left_google_api_keys:
                    try:
                        max_result = 50
                        response = urllib.request.urlopen(base_url + "?playlistId={}&key={}&part=snippet&maxResults={}".format(upload_id, GOOGLE_KEY_LIST[GOOGLE_KEY_INDEX], max_result))
                        break
                    except:
                        print('*--- next google key setting ---*')
                        GOOGLE_KEY_INDEX += 1
                        GOOGLE_KEY_INDEX %= len(GOOGLE_KEY_LIST)
                        left_google_api_keys -= 1
                if not left_google_api_keys:
                    print('key is expired during updating latest videos. {} is not updated.'.format(youtuber.yno))
                    return HttpResponse('key is expired during updating latest videos. {} is not updated.'.format(youtuber.yno))
                new_videos = []
                latest_videos = json.loads(response.read().decode('utf-8')).get('items') # test.json
                youtuber_videos = [video.videoid for video in Video.objects.filter(yno=youtuber).order_by('-regdate')] # videoID를 저장
                needed_updated_videos = youtuber_videos[:5] # 5개만 업데이트
                
                for video in latest_videos:
                    videoID = video.get('snippet').get('resourceId').get('videoId')
                    if videoID not in youtuber_videos:
                        new_videos.append(videoID)
                
                print('new_videos_id : {}'.format(new_videos) if new_videos else 'there is no new videos.')
                
                
                ########### 처리한 영상들을 업데이트하기
                ###### 새 비디오 추가
                for new_video_id in new_videos:
                    part = 'snippet,statistics'
                    base_url = 'https://www.googleapis.com/youtube/v3/videos'
                    while left_google_api_keys:
                        try:
                            response = urllib.request.urlopen(base_url + "?part={}&id={}&key={}&regionCode=KR".format(part, new_video_id, GOOGLE_KEY_LIST[GOOGLE_KEY_INDEX]))
                            info_obj = json.loads(response.read().decode('utf-8'))
                            break
                        except:
                            print('*--- next google key setting ---*')
                            GOOGLE_KEY_INDEX += 1
                            GOOGLE_KEY_INDEX %= len(GOOGLE_KEY_LIST)  
                            left_google_api_keys -= 1
                    if not left_google_api_keys:
                        print('key is expired during adding new videoes.')
                        return HttpResponse('key is expired during updating video details.')    
                    
                    snippet = info_obj.get('items')[0].get('snippet')
                    statistics = info_obj.get('items')[0].get('statistics')
                    try:
                        tags = ','.join(snippet.get('tags'))
                    except:
                        tags = ''
                    good = statistics.get('likeCount') if statistics.get('likeCount') else -1
                    bad = statistics.get('dislikeCount') if statistics.get('dislikeCount') else -1
                    videocommentcount = statistics.get('commentCount') if statistics.get('commentCount') else -1
                    
                    new_DB_video = Video.objects.create(
                        yno = youtuber,
                        videoid = new_video_id,
                        videoname = snippet.get('title'),
                        videodescription = snippet.get('description'),
                        videoviewcount = statistics.get('viewCount'),
                        videocommentcount = videocommentcount,
                        good = good,
                        bad = bad,
                        regdate = snippet.get('publishedAt')[:10],
                        ycano = snippet.get('categoryId'),
                        tags = tags,
                        thumbnail = snippet.get('thumbnails').get('default').get('url'),
                    )
                    
                    new_DB_video.save()
                    print('new video ID {} is added to DB.'.format(new_video_id))
                    
                ###### 이전 비디오 업데이트
                print('updating 5 videos')
                for video in needed_updated_videos: # video: id
                    part = 'statistics'
                    base_url = 'https://www.googleapis.com/youtube/v3/videos'
                    while left_google_api_keys:
                        try:
                            response = urllib.request.urlopen(base_url + "?part={}&id={}&key={}&regionCode=KR".format(part, video, GOOGLE_KEY_LIST[GOOGLE_KEY_INDEX]))
                            info_obj = json.loads(response.read().decode('utf-8'))
                            break
                        except:
                            print('*--- next google key setting ---*')
                            GOOGLE_KEY_INDEX += 1
                            GOOGLE_KEY_INDEX %= len(GOOGLE_KEY_LIST)  
                            left_google_api_keys -= 1
                    if not left_google_api_keys:
                        print('key is expired during updating video details.')
                        return HttpResponse('key is expired during updating video details.')
                    
                    try:
                        statistics = info_obj.get('items')[0].get('statistics')
                        good = statistics.get('likeCount') if statistics.get('likeCount') else -1
                        bad = statistics.get('dislikeCount') if statistics.get('dislikeCount') else -1
                        videocommentcount = statistics.get('commentCount') if statistics.get('commentCount') else -1                
                        
                        video_obj = Video.objects.get(videoid=video)
                        video_obj.good = good
                        video_obj.bad = bad
                        video_obj.videocommentcount = videocommentcount
                        
                        video_obj.save()
                        print('video ID {} is updated.'.format(video))
                    except:
                        continue
                
                
                            
                ############## 커뮤니티 가져오기
                print("------------- youtuber {}'s community articles update is started!".format(youtuber.yno))
                left_DAUM_KEY = len(DAUM_API_KEYS)
                daum_key = DAUM_API_KEYS[DAUM_API_INDEX]
                
                community_articles = Community.objects.filter(yno=youtuber).order_by('-articledate')
                
                searchKeyword = youtuber.searchkeyword if youtuber.searchkeyword else youtuber.channelname
                lastUpdate = community_articles[0].articledate if community_articles else datetime.date(2019, 1, 1) # datetime.date 타입
                lastUpdate = datetime.datetime(lastUpdate.year, lastUpdate.month, lastUpdate.day, 0, 0) # datetime.datetime으로 형변환
                keywords = NECESSARY_WORD[0]
                youtuber_category = [cate.cano.cano for cate in CategoryYoutubeRelation.objects.filter(yno=youtuber)]
                
                for add_category in youtuber_category:
                    keywords += NECESSARY_WORD[add_category]
                
                page = 1
                MORE_PAGES = True
                MORE_DATES = True
                DEFAULT_MAX = 2 # 2 * 50개인 100개 검색
                MAX_page = DEFAULT_MAX
                
                while MORE_PAGES and MORE_DATES:
                    if page >= MAX_page:
                        MORE_PAGES = False
                        break
                    params = {
                        'query': searchKeyword,
                        'sort': 'recency',
                        'page': page,
                        'size': 50
                    }
                    URL = 'https://dapi.kakao.com/v2/search/cafe'

                    while left_DAUM_KEY:
                        headers = {
                            'Authorization': 'KakaoAK ' + DAUM_API_KEYS[DAUM_API_INDEX]
                        }
                        response = requests.get(URL, headers=headers, params=params)
                        response_dict = json.loads(response.text)
                        if response.status_code == 200:
                            total_count = response_dict.get('meta').get('total_count')
                            break
                        else:
                            print('*--- next daum key setting ---*')
                            DAUM_API_INDEX += 1
                            DAUM_API_INDEX %= len(DAUM_API_KEYS)
                            left_DAUM_KEY -= 1
                    if not left_DAUM_KEY:
                        print('daum key is expired during updating community articles. {} is not updated.'.format(youtuber.yno))
                        return HttpResponse('daum key is expired during updating community articles. {} is not updated.'.format(youtuber.yno))
                    
                    MAX_page = min(DEFAULT_MAX, total_count // 50)
                    
                    documents = response_dict.get('documents')

                    for document in documents:
                        contents = document.get('contents')
                        if date_is_valid(document.get('datetime')[:10], lastUpdate):
                            for keyword in keywords:
                                if keyword in contents:
                                    community = Community.objects.create(
                                        yno = youtuber,
                                        articletitle = document.get('title'),
                                        articlelink = document.get('url'),
                                        articledescription = document.get('contents'),
                                        articledate = document.get('datetime')[:10],
                                    )
                                    community.save()
                                    print('article', community.pk, 'is saved.')
                                    break
                        else:
                            MORE_DATES = False
                            break
                    page += 1
                print("------------- youtuber {}'s community aricles update is done!".format(youtuber.yno))
                
                    
                ############## 뉴스 가져오기
                print("------------- youtuber {}'s news articles update is started!".format(youtuber.yno))
                latest_news = News.objects.filter(yno=youtuber).order_by('-newsdate')[0].newsdate if News.objects.filter(yno=youtuber).order_by('-newsdate') else datetime.date(2019, 1, 1)
                lastUpdate = datetime.datetime(latest_news.year, latest_news.month, latest_news.day, 0, 0)
                
                left_NAVER_API_KEYS = len(NAVER_ID_LIST)
                
                #### 키 돌려가며 사용하기 기술
                while left_NAVER_API_KEYS:
                    URL = 'https://openapi.naver.com/v1/search/news.json?'
                    
                    searchkeyword = youtuber.searchkeyword if youtuber.searchkeyword else youtuber.channelname
                    
                    params = {
                        'query': searchkeyword,
                        'display': 100,
                        'start': 1,
                        'sort': 'date'
                    }            
                    
                    headers = {
                        'X-Naver-Client-Id': NAVER_ID_LIST[NAVER_ID_INDEX],
                        'X-Naver-Client-Secret': NAVER_SECRET_LIST[NAVER_ID_INDEX],
                    }                  
                    
                    response = requests.get(URL, params=params, headers=headers)
                    if response.status_code == 200:
                        total = json.loads(response.text)["total"]
                        newses = json.loads(response.text)['items']
                        break
                    else:
                        print('*--- next naver key setting ---*')
                        NAVER_ID_INDEX += 1
                        NAVER_ID_INDEX %= len(NAVER_ID_LIST)
                        left_NAVER_API_KEYS -= 1                                    
                if not left_NAVER_API_KEYS:
                    print('naver key is expired during updating news articles. {} is not updated.'.format(youtuber.yno))
                    return HttpResponse('naver key is expired during updating news articles. {} is not updated.'.format(youtuber.yno))

                for news in newses:
                    is_correct = False
                    date = datetime.datetime(int(news["pubDate"][12:16]), MONTH.index(news["pubDate"][8:11]), int(news["pubDate"][5:7]))
                    if (date - lastUpdate).days < 0:
                        break
                    
                    for keyword in keywords:
                        if keyword in news.get('description'):
                            is_correct = True
                            break
                    if not is_correct:
                        continue
                
                    new_news = News.objects.create(
                        yno = youtuber,
                        newslink = news.get('link'),
                        newstitle = news.get('title'),
                        newsdescription = news.get('description'),
                        newsdate = str(date)[:10],
                        pressname = '',
                        clickcount = 0,
                    )
                    new_news.save()
                    print("------------- youtuber {}'s news is added!".format(youtuber.yno))                                
                print("------------- youtuber {}'s news aricles update is done!".format(youtuber.yno))
                
                ############## 데이터랩 가져오기
                print("------------- youtuber {}'s naver datalab update is started!".format(youtuber.yno))
                left_NAVER_DATA_ID = len(NAVER_DATA_ID)
                now = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=9) # 한국시간 기준
                year_ago = now - datetime.timedelta(days=364)
                while left_NAVER_DATA_ID:
                    url = "https://openapi.naver.com/v1/datalab/search"
                    startDate = '{0:04d}-{1:02d}-{2:02d}'.format(year_ago.year, year_ago.month, year_ago.day) # 현재부터 1년 전
                    endDate = '{0:04d}-{1:02d}-{2:02d}'.format(now.year, now.month, now.day) # 현재 날짜
                    timeUnit = 'week'
                    keyword = youtuber.searchkeyword if youtuber.searchkeyword else youtuber.channelname
                    
                    body = {
                        "startDate": startDate,
                        "endDate": endDate,
                        "timeUnit": timeUnit,
                        "keywordGroups": [
                                {
                                    "groupName": keyword, 
                                    "keywords": [
                                            keyword
                                        ]
                                }
                            ]
                    }
                    body = str(body).replace("'", '\"')            
                    
                    request = urllib.request.Request(url)
                    request.add_header("X-Naver-Client-Id", NAVER_DATA_ID[NAVER_DATA_ID_INDEX])
                    request.add_header("X-Naver-Client-Secret", NAVER_DATA_SECRET[NAVER_DATA_ID_INDEX])
                    request.add_header("Content-Type","application/json")
                    try:
                        response = urllib.request.urlopen(request, data=body.encode("utf-8"))
                        response_body = response.read().decode('utf-8')
                        data = json.loads(response_body).get('results')[0].get('data')
                        data = {'data': data}
                        result = json.dumps(data)
                        datalab = Naverdatalab.objects.filter(yno=youtuber)
                        
                        if datalab:
                            datalab = datalab[0]
                            datalab.searchkeyword = keyword
                            datalab.startdate = startDate
                            datalab.enddate = endDate
                            datalab.data = data
                            datalab.save()
                            print("------------- youtuber {}'s naver datalab is updated!".format(youtuber.yno))
                        else:
                            new_datalab = Naverdatalab.objects.create(
                                yno = youtuber,
                                searchkeyword = keyword,
                                startdate = startDate,
                                enddate = endDate,
                                data = data,
                            )
                            new_datalab.save()
                            print("------------- youtuber {}'s new naver datalab is added!".format(youtuber.yno))
                        break
                    except:
                        print('*--- next naver datalab key setting ---*')
                        NAVER_DATA_ID_INDEX += 1
                        NAVER_DATA_ID_INDEX %= len(NAVER_ID_LIST)
                        left_NAVER_DATA_ID -= 1            
                print("------------- youtuber {}'s naver datalab update is done!".format(youtuber.yno))
                print('---- youtuber {} takes {}.'.format(youtuber.yno, datetime.datetime.now() - ONE_START))
            
            ########### 스탯 업데이트 한 꺼번에 전부
            print("------------- stat update is started!".format(youtuber.yno))
            update_stat_without_request()
            print("------------- stat update is done!".format(youtuber.yno))
            print('total update takes {}.'.format(datetime.datetime.now() - START))
            ########## 모두 끝나고, 업데이트 주기 다시 실행!
            threading.Timer(UPDATE_CIRCLE, self.threadOpen).start()
        else:
            threading.Timer(UPDATE_CIRCLE, self.threadOpen).start()


def update_youtuber(request):
    updateStart = updateThread()
    threading.Timer(1, updateStart.threadOpen).start()
    return HttpResponse()