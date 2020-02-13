# -*- coding:utf-8 -*-

from django.shortcuts import render, HttpResponse
from django.db.models import Count
from .models import *
from .stat import get_influence, get_activity, get_trend, get_views, get_charm, get_grade
from decouple import config
import requests
import urllib.request
from urllib.request import urlopen, unquote
from bs4 import BeautifulSoup as bs
import json
import copy
import timeit
import datetime


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


# 기본, 게임, 엔터테인먼트, 뷰티, 스포츠, 먹망, 키즈, 동물, 일상, IT
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


def is_youtube_channel_url(url):
    if 'youtube' not in url:
        return False
    if '/c/' not in url and '/user/' not in url and '/channel/' not in url:
        return False
    return True


def get_channel_id_from_url(url):
    html = urlopen(url).read()
    soup = bs(html, "lxml", from_encoding='utf-8')
    ff = soup.find("button", attrs={'class': "yt-uix-button yt-uix-button-size-default "
                                    "yt-uix-button-subscribe-branded yt-uix-button-has-icon "
                                    "no-icon-markup yt-uix-subscription-button yt-can-buffer"})
    return ff.get('data-channel-external-id')


def get_yno_from_channel_id(channel_id):
    ylist = Youtuber.objects.filter(channelid=channel_id)
    for youtuber in ylist:
        if channel_id == youtuber.channelid:
            return youtuber.yno
    return -1


def get_channel_other_sites(input_url):
    other_link_list = []
    html = urlopen(input_url).read()
    soup = bs(html, "lxml", from_encoding='utf-8')
    li_tags = soup.find_all("li", attrs={'class': "channel-links-item"})
    for li_tag in li_tags:
        before_link = li_tag.find('a').get('href')
        link = unquote(before_link[before_link.find('http'):])
        if '&' in link:
            link = link[:link.find('&')]
        other_link_list.append(link)
    return other_link_list


def get_trend_list(channel_id):
    trends = []
    str_date = (datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=9) + datetime.timedelta(days=-30)).strftime('%Y-%m-%d')
    url = 'https://en.noxinfluencer.com/api/youtube/detail/dimension/?channelId=' + channel_id + '&&startDate=' + str_date
    r = requests.get(url)
    html = json.loads(r.text)['retData']['dom']
    if json.loads(r.text)['errorNum'] != 0:
        print('errer')
        return trends
    soup = bs(html, "html.parser", from_encoding='utf-8')
    ul_list = soup.findAll('ul')
    for idx in range(1, len(ul_list) - 2):
        data = {}
        li_list = ul_list[idx].findAll('li')
        for (i, li) in enumerate(li_list):
            if i == 0:
                data['recordDate'] = li.text
            elif i == 1:
                span_list = li.findAll('span')
                if len(span_list) == 1:
                    data['pointSubscriber'] = get_real_value(span_list[0].text)
                    data['difSubscriber'] = 0
                else:
                    data['pointSubscriber'] = get_real_value(span_list[0].text)
                    data['difSubscriber'] = get_real_value(span_list[1].text)
            elif i == 2:
                span_list = li.findAll('span')
                if len(span_list) == 1:
                    data['pointView'] = get_real_value(span_list[0].text)
                    data['difView'] = 0
                else:
                    data['pointView'] = get_real_value(span_list[0].text)
                    data['difView'] = get_real_value(span_list[1].text)
                break
        trends.append(data)
    return trends


def get_channel_info(channelID):
    global GOOGLE_KEY_INDEX
    global GOOGLE_KEY_LIST
    key = GOOGLE_KEY_LIST[GOOGLE_KEY_INDEX]
    channel_info_dict = {}
    base_url = "https://www.googleapis.com/youtube/v3/channels"
    part = "id,snippet,brandingSettings,contentDetails,invideoPromotion,statistics,topicDetails"
    try:
        response = urllib.request.urlopen(
            base_url + "?part=%s&id=%s&key=%s" % (part, channelID, key))
    except urllib.request.HTTPError:
        print('*--- %d -> %d : next key setting & restart ---*' %
              (GOOGLE_KEY_INDEX, (GOOGLE_KEY_INDEX+1) % len(GOOGLE_KEY_LIST)))
        GOOGLE_KEY_INDEX += 1
        GOOGLE_KEY_INDEX %= len(GOOGLE_KEY_LIST)
        return get_channel_info(channelID)
    info_obj = json.loads(response.read().decode('utf-8'))["items"][0]

    snippet = info_obj["snippet"]
    channel_info_dict["title"] = snippet["title"]
    channel_info_dict['customUrl'] = snippet.get('customUrl')
    channel_info_dict["description"] = snippet["description"]
    channel_info_dict["thumbnail"] = snippet["thumbnails"]["default"]["url"]
    channel_info_dict['publishedAt'] = snippet["publishedAt"][:10]

    statistics = info_obj["statistics"]
    channel_info_dict["viewCount"] = statistics["viewCount"]
    channel_info_dict["subscriberCount"] = statistics["subscriberCount"]
    channel_info_dict["videoCount"] = statistics["videoCount"]
    branding_settings = info_obj["brandingSettings"]
    channel_info_dict['banner_url'] = branding_settings["image"]["bannerImageUrl"]
    if '/default_banner' in channel_info_dict['banner_url']:
        channel_info_dict['banner_url'] = ''

    content_details = info_obj['contentDetails']
    channel_info_dict['uploadsID'] = content_details['relatedPlaylists']['uploads']
    return channel_info_dict


def get_real_value(txt):
    txt = txt.strip()
    value = 0
    if txt.isdigit():
        value = int(txt)
    if txt[len(txt) - 1] == 'M':
        value = float(txt.strip()[:-1]) * 1000000
    elif txt[len(txt) - 1] == 'K':
        value = float(txt.strip()[:-1]) * 1000
    elif txt[len(txt) - 1] == 'B':
        value = float(txt.strip()[:-1]) * 1000000000
    return round(value)




def get_video_list(uploads_id):
    global GOOGLE_KEY_LIST
    global GOOGLE_KEY_INDEX
    key = GOOGLE_KEY_LIST[GOOGLE_KEY_INDEX]
    video_id_lists = []
    page_token = ''
    base_url = "https://www.googleapis.com/youtube/v3/playlistItems"
    cnt = 0
    while True:
        url = base_url + \
            "?playlistId=%s&key=%s&part=snippet&maxResults=50" % (
                uploads_id, key)
        if page_token != '':
            url += "&pageToken=" + page_token
        try:
            response = urllib.request.urlopen(url)
        except urllib.request.HTTPError:
            print('*--- next key setting & restart ---*')
            GOOGLE_KEY_INDEX += 1
            GOOGLE_KEY_INDEX %= len(GOOGLE_KEY_LIST)
            return get_video_list(uploads_id)
        json_objs = json.loads(response.read().decode('utf-8'))
        for obj in json_objs['items']:
            video_id_lists.append(obj['snippet']['resourceId']['videoId'])
        #     pageToken
        if json_objs.get('nextPageToken') is None or json_objs.get('nextPageToken') == '':
            break
        page_token = json_objs.get('nextPageToken')
        cnt += 1
        if cnt == 1:
            break
    return video_id_lists


TOPICS = {
    '/m/04rlf': 'Music',
    '/m/05fw6t': "Children's music",
    '/m/02mscn': 'Christian music',
    '/m/0ggq0m': 'Classical music',
    '/m/01lyv': 'Country',
    '/m/02lkt': 'Electronic music',
    '/m/0glt670': 'Hip hop music',
    '/m/05rwpb': 'Independent music',
    '/m/03_d0': 'Jazz',
    '/m/028sqc': 'Music of Asia',
    '/m/0g293': 'Music of Latin America',
    '/m/064t9': 'Pop music',
    '/m/06cqb': 'Reggae',
    '/m/06j6l': 'Rhythm and blues',
    '/m/06by7': 'Rock music',
    '/m/0gywn': 'Soul music',
    '/m/0bzvm2': 'Gaming',
    '/m/025zzc': 'Action game',
    '/m/02ntfj': 'Action-adventure game',
    '/m/0b1vjn': 'Casual game',
    '/m/02hygl': 'Music video game',
    '/m/04q1x3q': 'Puzzle video game',
    '/m/01sjng': 'Racing video game',
    '/m/0403l3g': 'Role-playing video game',
    '/m/021bp2': 'Simulation video game',
    '/m/022dc6': 'Sports game',
    '/m/03hf_rm': 'Strategy video game',
    '/m/06ntj': 'Sports',
    '/m/0jm_': 'American football',
    '/m/018jz': 'Baseball',
    '/m/018w8': 'Basketball',
    '/m/01cgz': 'Boxing',
    '/m/09xp_': 'Cricket',
    '/m/02vx4': 'Football',
    '/m/037hz': 'Golf',
    '/m/03tmr': 'Ice hockey',
    '/m/01h7lh': 'Mixed martial arts',
    '/m/0410tth': 'Motorsport',
    '/m/066wd': 'Professional wrestling',
    '/m/07bs0': 'Tennis',
    '/m/07_53': 'Volleyball',
    '/m/02jjt': 'Entertainment',
    '/m/095bb': 'Animated cartoon',
    '/m/09kqc': 'Humor',
    '/m/02vxn': 'Movies',
    '/m/05qjc': 'Performing arts',
    '/m/019_rr': 'Lifestyle',
    '/m/032tl': 'Fashion',
    '/m/027x7n': 'Fitness',
    '/m/02wbm': 'Food',
    '/m/0kt51': 'Health',
    '/m/03glg': 'Hobby',
    '/m/068hy': 'Pets',
    '/m/041xxh': 'Physical attractiveness [Beauty]',
    '/m/07c1v': 'Technology',
    '/m/07bxq': 'Tourism',
    '/m/07yv9': 'Vehicles',
    '/m/01k8wb': 'Knowledge',
    '/m/098wr': 'Society',
}


def get_video_detail(video_id):
    global GOOGLE_KEY_LIST
    global GOOGLE_KEY_INDEX
    key = GOOGLE_KEY_LIST[GOOGLE_KEY_INDEX]
    # snippet으로 가져오는 정보: 유튜버, 제목, 설명, 게시일, 카테고리, 태그, 섬네일
    # statistics로 가져오는 정보: 조회수, 댓글 수, 좋아요 수, 싫어요 수
    # topicdetails로 가져오는 정보: 토픽
    part = 'snippet,statistics'
    url = 'https://www.googleapis.com/youtube/v3/videos?part={}&id={}&key={}'.format(
        part, video_id, key)
    try:
        response = urlopen(url).read().decode('utf-8')
    except:
        print('*--- next key setting & restart ---*')
        GOOGLE_KEY_INDEX += 1
        GOOGLE_KEY_INDEX %= len(GOOGLE_KEY_LIST)
        return get_video_detail(video_id)
    res_dict = json.loads(response).get('items')[0]

    statistics = res_dict.get('statistics')
    snippet = res_dict.get('snippet')
    
    try:
        tags = ','.join(snippet.get('tags'))
    except:
        tags = ''

    if statistics.get('likeCount') is None:
        statistics['likeCount'] = -1
    if statistics.get('dislikeCount') is None:
        statistics['dislikeCount'] = -1
    if statistics.get('commentCount') is None:
        statistics['commentCount'] = -1
    video = {
        'video_id': video_id,
        'videoName': snippet.get('title'),
        'videoDescription': snippet.get('description'),
        'videoViewCount': statistics.get('viewCount'),
        'videoCommentCount': statistics.get('commentCount'),
        'good': statistics.get('likeCount'),
        'bad': statistics.get('dislikeCount'),
        'regDate': snippet.get('publishedAt')[:10],
        'ycano': snippet.get('categoryId'),
        'thumbnail': snippet.get('thumbnails').get('high').get('url'),
        'tags': tags,
    }
    return video


def get_news_list(youtuber, category, last_updated_date):

    MONTH = ['', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    YOUTUBER = youtuber.channelname  # DB 에서 yno 에 해당하는 channelName or youtubeName 을 입력
    CATEGORY = category

    URL = 'https://openapi.naver.com/v1/search/news.json?'
    params = {
        'query': YOUTUBER,
        'display': 100,
        'start': 1,
        'sort': 'date'
    }

    headers = {
        'X-Naver-Client-Id': config('X_NAVER_CLIENT_ID2'),
        'X-Naver-Client-Secret': config('X_NAVER_CLIENT_SECRET2'),
    }

    category_keyword = NECESSARY_WORD[0]
    for num in CATEGORY:
        category_keyword += NECESSARY_WORD[num]

    # 만약 last updatedDate 가 2019-03-15 면 3월 15일 이후의 기사만 가져와야함
    news_list = []
    while True:
        response = requests.get(URL, params=params, headers=headers)
        response.encoding = 'utf-8'
        response = response.text
        try:
            total = json.loads(response)["total"]
            newses = json.loads(response)["items"]
        except:
            print(json.loads(response))
        for news in newses:
            is_correct = False
            date = datetime.datetime(int(news["pubDate"][12:16]), MONTH.index(news["pubDate"][8:11]), int(news["pubDate"][5:7]))

            # 업데이트되어있는 기사는 추가하지 않음
            if (date - last_updated_date).days < 0:
                break

            # Description 에 특정 키워드가 없는 기사는 추가하지 않음
            for keyword in category_keyword:
                if keyword in news["description"]:
                    is_correct = True
                    break
            if not is_correct:
                continue

            new_news = {
                'newsLink': news["link"],
                'newsTitle': news["title"],
                'newsDescription': news["description"],
                'newsDate': str(date)[:10]
            }
            news_list.append(new_news)
        if params['start'] >= min(1000, total):
            break
        params['start'] += params['display']
    return news_list


CANO_MAPPING = {
    '2': 9,
    '10': 2,
    '15': 7,
    '17': 4,
    '19': 8,
    '20': 1,
    '23': 2,
    '25': 8,
    '26': 3,
    '27': 6,
    '28': 9,
    '29': 8
}


def get_our_cano(ycano_list, video_detail_list):
    our_list = []
    for ycano in ycano_list:
        if str(ycano) in list(CANO_MAPPING.keys()):
            if CANO_MAPPING[str(ycano)] not in our_list:
                our_list.append(CANO_MAPPING[str(ycano)])
        elif ycano == 1 or ycano == 24:
            count = 0
            for keyword in ['kids', '키즈', '어린이', '장난감', '토이']:
                for video_detail in video_detail_list:
                    if keyword in video_detail['videoName']:
                        count += 1
            if count >= len(video_detail_list) * 0.2:
                if 6 not in our_list:
                    our_list.append(6)
            else:
                if 2 not in our_list:
                    our_list.append(2)
        elif ycano == 22:
            count = 0
            for keyword in ['mukbang', '먹방', '음식', 'food', '맛있']:
                for video_detail in video_detail_list:
                    if keyword in video_detail['videoName']:
                        count += 1
            if count >= len(video_detail_list) * 0.2:
                if 5 not in our_list:
                    our_list.append(5)
            else:
                if 8 not in our_list:
                    our_list.append(8)
        else:
            if 0 not in our_list:
                our_list.append(0)
    return our_list


def date_is_valid(dateStr, lastupdate):  # ex) '2019-03-16'
    article_date = datetime.datetime.strptime(dateStr, '%Y-%m-%d')
    if (article_date - lastupdate).days > 0:
        return True
    else:
        return False


def get_daumCafe_search_result(YOUTUBER, category, lastupdate):
    # API_KEY를 더 넣도록 합시다.
    API_KEYS = [config('DAUM_API_KEY2')]

    # YOUTUBER를 활용해, searchKeyword, lastUpdate, category 등등을 가져온다.
    searchKeyword = YOUTUBER.channelname
    lastUpdate = lastupdate
    keywords = NECESSARY_WORD[0]
    youtuber_category = category

    for add_category in youtuber_category:
        keywords += NECESSARY_WORD[add_category]

    page = 1
    MORE_PAGES = True
    MORE_DATES = True

    DEFAULT_MAX = 6  # 6이면, 6 * 50 인 300개 검색
    MAX_page = DEFAULT_MAX

    while MORE_PAGES and MORE_DATES:
        if page >= MAX_page:
            MORE_PAGES = False

        params = {
            'query': searchKeyword,
            'sort': 'recency',
            'page': page,
            'size': 50
        }

        URL = 'https://dapi.kakao.com/v2/search/cafe'

        for API_KEY in API_KEYS:
            headers = {
                'Authorization': 'KakaoAK ' + API_KEY
            }
            response = requests.get(URL, headers=headers, params=params)
            response_dict = json.loads(response.text)
            if response.status_code == 200:
                total_count = response_dict.get(
                    'meta').get('total_count')  # 검색 결과 수
                break
        else:
            # 모든 API_KEY를 다 썼을 경우
            return "---------- Can't get daum cafe articles since api keys are ran out. ----------"

        MAX_page = min(DEFAULT_MAX, total_count // 50)

        documents = response_dict.get('documents')  # 가져온 글들의 모든 목록

        if (response.status_code == 200):
            for document in documents:
                contents = document.get('contents')
                if date_is_valid(document.get('datetime')[:10], lastUpdate):
                    for keyword in keywords:
                        if keyword in contents:
                            community = Community.objects.create(
                                yno=YOUTUBER,
                                articletitle=document.get('title'),
                                articlelink=document.get('url'),
                                articledescription=document.get('contents'),
                                articledate=document.get('datetime')[:10],
                            )
                            community.save()
                            break
                else:
                    MORE_DATES = False
                    break
        page += 1


def insert_naver_data_lab(youtuber):
    result = ''
    client_id = config("NAVER_DATALAB_CLIENT_ID2")
    client_secret = config("NAVER_DATALAB_CLIENT_SECRET2")
    url = "https://openapi.naver.com/v1/datalab/search"
    startDate = (datetime.datetime.now() + datetime.timedelta(days=-365)).strftime("%Y-%m-%d")
    endDate = datetime.datetime.utcnow().strftime("%Y-%m-%d")
    timeUnit = 'week'
    keyword = youtuber.channelname

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
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    request.add_header("Content-Type", "application/json")
    try:
        response = urllib.request.urlopen(request, data=body.encode("utf-8"))
        rescode = response.getcode()
        if(rescode == 200):
            response_body = response.read().decode('utf-8')
            data = json.loads(response_body).get('results')[0].get('data')
            result = json.dumps(data)  # result를 DB data에 담는다.
            Naverdatalab.objects.create(
                yno=youtuber,
                searchkeyword=keyword,
                startdate=startDate,
                enddate=endDate,
                data=data
            )
        else:
            print("Error Code:" + rescode)
    except:
        Naverdatalab.objects.create(
            yno=youtuber,
            searchkeyword=keyword,
            startdate=startDate,
            enddate=endDate,
            data='[]'
        )
    return result
