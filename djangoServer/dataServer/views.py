from django.shortcuts import render, HttpResponse
from django.db.models import Count
from .models import *
from .stat import *
from .function import *
import urllib.request
import requests
from decouple import config
from urllib.request import urlopen, unquote
import datetime
import time
from pytz import timezone


def update_stat_all(request):
    youtube_list = Youtuber.objects.all()
    print('|     yno | Influence |  Activity |     Trend |     Views |     Charm |')
    print('*--------------------------------------------------------------------*')
    for youtuber in youtube_list:
        Stat.objects.filter(yno=youtuber).filter().delete()
        video_list = Video.objects.filter(yno=youtuber)
        video_detail_list = []  # good, bad, reddate
        for video in video_list:
            temp = {}
            temp['regDate'] = video.regdate
            temp['good'] = video.good
            temp['bad'] = video.bad
            video_detail_list.append(temp)
        now = datetime.datetime.now(
            datetime.timezone.utc) + datetime.timedelta(hours=9)
        trends = Trend.objects.filter(yno=youtuber).order_by('-recorddate')
        last_month_trend = None
        for trend in trends:
            last_month_trend = trend
            if (now - trend.recorddate).days >= 30:
                break
        today_trend = trends[0]

        youtuber.influence = get_influence(youtuber)
        youtuber.activity = get_activity3(youtuber, video_detail_list)
        youtuber.viewcounttrend = get_views(
            youtuber, last_month_trend, today_trend)
        youtuber.subscribercounttrend = get_trend(
            youtuber, last_month_trend, today_trend)
        youtuber.charm = get_charm(video_detail_list)
        youtuber.grade = get_grade(youtuber, youtuber.influence, youtuber.activity,
                                   youtuber.subscribercounttrend, youtuber.viewcounttrend, youtuber.charm)
        youtuber.save()
        print('| %9d | %9d | %9d | %9d | %9d | %9d |' % (youtuber.yno, youtuber.influence, youtuber.activity, youtuber.subscribercounttrend, youtuber.viewcounttrend, youtuber.charm))
    return HttpResponse(0)


'''
## return 값 ## 
{code :   0, yno :  ???}, 성공적으로 성공하여 yno 가르쳐줌
{code :   1, yno :  ???}, DB에 존재하는 유튜버 url을 입력받아서 해당 유튜버의 yno를 반환
{code :  -1, yno : null}, 올바르지 않은 유튜브 채널 URL인 경우
{code :  -2, yno : null}, url 채널 정보가 DB에 없는지 판단 중 에러
{code :  -3, yno : null}, 너무 인기 없는 유튜버라서 지원안함
{code :  -4, yno : null}, 유튜버 channel info 수집 후 DB 추가 중 에러
{code :  -5, yno : null}, 생성된 유튜버의 yno를 DB에서 찾아 가져오기 중 에러
{code :  -6, yno : null}, Video 테이블 수집 중 에러
{code :  -7, yno : null}, trend 테이블 수집 중 에러
{code :  -8, yno : null}, Category_youtuber_relation 수집 중 설정
{code :  -9, yno : null}, news 테이블 수집 중 에러
{code : -10, yno : null}, community 테이블 수집 중 에러
{code : -11, yno : null}, 위에서 생성된 정보들 기반으로 스텟, 등급 계산 중 에러
{code : -12, yno : null}, 유튜버의 스텟, 등급, updatedDate 갱신 중 에러 
{code : -99, yno : null}, 알 수 없는 오류
'''


def make_new_youtuber(request, url):
    timer = []
    timer.append(timeit.default_timer())
    res = {}
    url = url.replace('~', '/')
    today = datetime.date.today()

    # 1. 올바른 유튜브 채널 URL 판단
    if not is_youtube_channel_url(url):
        res['code'] = -1
        return HttpResponse(json.dumps(res))
    timer.append(timeit.default_timer())
    print('%2d. [%5.2f / %5.2f s] Determine the correct YouTube channel URL'
          % (len(timer) - 1, timer[len(timer) - 1] - timer[len(timer) - 2], timer[len(timer) - 1] - timer[0]))

    # 2. URL로부터 channel ID 얻기
    try:
        channel_id = get_channel_id_from_url(url)
    except Exception as e:
        print(e)
        res['code'] = -2
        return HttpResponse(json.dumps(res))
    timer.append(timeit.default_timer())
    print('%2d. [%5.2f / %5.2f s] Get channel ID from URL'
          % (len(timer) - 1, timer[len(timer) - 1] - timer[len(timer) - 2], timer[len(timer) - 1] - timer[0]))

    # 3. url 채널 정보가 DB에 없는지 판단
    yno = get_yno_from_channel_id(channel_id)
    if yno != -1:
        res['code'] = 1
        res['yno'] = yno
        return HttpResponse(json.dumps(res))
    timer.append(timeit.default_timer())
    print('%2d. [%5.2f / %5.2f s] Determines if channel information is not in the DB'
          % (len(timer) - 1, timer[len(timer) - 1] - timer[len(timer) - 2], timer[len(timer) - 1] - timer[0]))

    # 4. 유튜버 channel info 수집 후 DB 추가
    youtuber = None
    other_links = ['', '', '', '', '']
    for (i, site) in enumerate(get_channel_other_sites(url)):
        other_links[i] = site
    channel_info = get_channel_info(channel_id)
    if int(channel_info['subscriberCount']) < int(config('MIN_SUBSCRIBER')):
        print('유튜버 channel info 수집 후 DB 추가 중 에러')
        res['code'] = -3
        return HttpResponse(json.dumps(res))
    try:
        youtuber = Youtuber(
            channelid=channel_id,
            channelname=channel_info['title'],
            youtubername=channel_info['customUrl'],
            channeldescription=channel_info['description'],
            bannerimagelink=channel_info['banner_url'],
            channellink=url,
            thumbnails=channel_info['thumbnail'],
            publisheddate=channel_info['publishedAt'],
            subscriber=channel_info['subscriberCount'],
            totalviewcount=channel_info['viewCount'],
            totalvideocount=channel_info['videoCount'],
            grade=0,
            influence='0',
            activity='0',
            subscribercounttrend='0',
            viewcounttrend='0',
            charm='0',
            clickcount='0',
            updateddate=datetime.datetime(2010, 1, 1),
            regdate=datetime.date.today(),
            otherlink1=other_links[0],
            otherlink2=other_links[1],
            otherlink3=other_links[2],
            otherlink4=other_links[3],
            otherlink5=other_links[4],
            uploadsid=channel_info['uploadsID'],
            status=11
        )
        youtuber.save()
    except Exception as e:
        print(e)
        res['code'] = -4
        return HttpResponse(json.dumps(res))
    timer.append(timeit.default_timer())
    print('%2d. [%5.2f / %5.2f s] Add DB after collecting YouTube channel info'
          % (len(timer) - 1, timer[len(timer) - 1] - timer[len(timer) - 2], timer[len(timer) - 1] - timer[0]))

    # 5. 생성된 유튜버의 yno를 DB에서 찾아 가져오기
    try:
        yno = get_yno_from_channel_id(channel_id)
    except Exception as e:
        print(e)
        res['code'] = -5
        return HttpResponse(json.dumps(res))
    timer.append(timeit.default_timer())
    print('%2d. [%5.2f / %5.2f s] Locate and import the yno of the created user from the DB'
          % (len(timer) - 1, timer[len(timer) - 1] - timer[len(timer) - 2], timer[len(timer) - 1] - timer[0]))
    youtuber.status = 12
    youtuber.save()

    # 6. Video 테이블 수집
    video_detail_list = []
    try:
        video_id_list = get_video_list(channel_info['uploadsID'])
        start_timer = timeit.default_timer()
        for (idx, video_id) in enumerate(video_id_list):
            video_detail = get_video_detail(video_id)
            video_detail_list.append(video_detail)
            Video.objects.create(
                yno=youtuber,
                videoid=video_detail['video_id'],
                videoname=video_detail['videoName'],
                videodescription=video_detail['videoDescription'],
                videoviewcount=video_detail['videoViewCount'],
                videocommentcount=video_detail['videoCommentCount'],
                good=video_detail['good'],
                bad=video_detail['bad'],
                regdate=video_detail['regDate'],
                ycano=video_detail['ycano'],
                tags=video_detail['tags'],
                thumbnail=video_detail['thumbnail'],
            )
            end_timer = timeit.default_timer()
            print(' -  [%5.2f / %5.2f s] get Video detail (%2d/%d)'
                  % (end_timer - start_timer, end_timer - timer[0], idx + 1, len(video_id_list)))
            start_timer = end_timer
    except Exception as e:
        print(e)
        res['code'] = -6
        return HttpResponse(json.dumps(res))
    timer.append(timeit.default_timer())
    print('%2d. [%5.2f / %5.2f s] Video 테이블 수집'
          % (len(timer) - 1, timer[len(timer) - 1] - timer[len(timer) - 2], timer[len(timer) - 1] - timer[0]))
    youtuber.status = 57
    youtuber.save()

    # 7. trend 테이블 수집
    today_trend = None
    try:
        trend_list = get_trend_list(channel_id)
        last_pointSubscriber = 0
        last_pointView = 0
        for (i, trend_item) in enumerate(trend_list):
            if i == len(trend_list):
                break
            last_pointSubscriber = trend_item['pointSubscriber']
            last_pointView = trend_item['pointView']
            Trend.objects.create(
                yno=youtuber,
                recorddate=datetime.datetime.strptime(
                    trend_item['recordDate'], "%Y-%m-%d"),
                pointsubscriber=trend_item['pointSubscriber'],
                difsubscriber=trend_item['difSubscriber'],
                pointview=trend_item['pointView'],
                difview=trend_item['difView']
            )
        today_trend = Trend(
            yno=youtuber,
            recorddate=datetime.datetime(
                today.year, today.month, today.day, 0, 0, 0),
            pointsubscriber=youtuber.subscriber,
            difsubscriber=int(youtuber.subscriber) - last_pointSubscriber,
            pointview=youtuber.totalviewcount,
            difview=int(youtuber.totalviewcount) - last_pointView,
        )
        today_trend.save()
    except Exception as e:
        print(e)
        res['code'] = -7
        return HttpResponse(json.dumps(res))
    timer.append(timeit.default_timer())
    print('%2d. [%5.2f / %5.2f s] trend 테이블 수집'
          % (len(timer) - 1, timer[len(timer) - 1] - timer[len(timer) - 2], timer[len(timer) - 1] - timer[0]))
    youtuber.status = 73
    youtuber.save()

    # 8 calculate valid ycano list
    valid_ycano_list = []
    tmp_ycano_list = Video.objects.filter(yno=yno).values(
        'ycano').annotate(total=Count('ycano')).order_by('total').reverse()
    for ycategory in tmp_ycano_list:
        if ycategory['total'] >= len(video_detail_list) * 0.11:
            valid_ycano_list.append(ycategory['ycano'])
    timer.append(timeit.default_timer())
    print('%2d. [%5.2f / %5.2f s] calculate valid ycano list'
          % (len(timer) - 1, timer[len(timer) - 1] - timer[len(timer) - 2], timer[len(timer) - 1] - timer[0]))
    youtuber.status = 77
    youtuber.save()

    # 9 get our category
    our_cano_list = get_our_cano(valid_ycano_list, video_detail_list)
    timer.append(timeit.default_timer())
    print('%2d. [%5.2f / %5.2f s] get our category'
          % (len(timer) - 1, timer[len(timer) - 1] - timer[len(timer) - 2], timer[len(timer) - 1] - timer[0]))
    youtuber.status = 80
    youtuber.save()

    # 10 add CategoryYoutubeRelation
    for our_cano in our_cano_list:
        category = Category.objects.get(cano=our_cano)
        CategoryYoutubeRelation.objects.create(
            yno=youtuber,
            cano=category
        )
    timer.append(timeit.default_timer())
    print('%2d. [%5.2f / %5.2f s] add CategoryYoutubeRelation'
          % (len(timer) - 1, timer[len(timer) - 1] - timer[len(timer) - 2], timer[len(timer) - 1] - timer[0]))
    youtuber.status = 83
    youtuber.save()

    # 11 news 테이블 수집
    news_list = get_news_list(youtuber, our_cano_list,
                              datetime.datetime(2010, 1, 1))
    for news in news_list:
        News.objects.create(
            yno=youtuber,
            newslink=news['newsLink'],
            newstitle=news['newsTitle'],
            newsdescription=news['newsDescription'],
            newsdate=news['newsDate'],
            pressname='',
            clickcount=0,
        )
    timer.append(timeit.default_timer())
    print('%2d. [%5.2f / %5.2f s] news 테이블 수집'
          % (len(timer) - 1, timer[len(timer) - 1] - timer[len(timer) - 2], timer[len(timer) - 1] - timer[0]))
    youtuber.status = 88
    youtuber.save()

    # 12.  community 테이블 수집 후 DB 추가
    try:
        get_daumCafe_search_result(
            youtuber, our_cano_list,  datetime.datetime(2010, 1, 1))
    except Exception as e:
        print('*ERROR (10) : ', e)
        res['code'] = -10
        return HttpResponse(json.dumps(res))
    timer.append(timeit.default_timer())
    print('%2d. [%5.2f / %5.2f s] community 테이블 수집 후 DB 추가'
          % (len(timer) - 1, timer[len(timer) - 1] - timer[len(timer) - 2], timer[len(timer) - 1] - timer[0]))
    youtuber.status = 90
    youtuber.save()

    # 13. naverDataLab 추가
    insert_naver_data_lab(youtuber)
    timer.append(timeit.default_timer())
    print('%2d. [%5.2f / %5.2f s] naverDataLab 추가'
          % (len(timer) - 1, timer[len(timer) - 1] - timer[len(timer) - 2], timer[len(timer) - 1] - timer[0]))
    youtuber.status = 92
    youtuber.save()

    # 14. 위에서 생성된 정보들 기반으로 스텟, 등급 계산
    now = datetime.datetime.now(
        datetime.timezone.utc) + datetime.timedelta(hours=9)
    trends = Trend.objects.filter(yno=youtuber).order_by('-recorddate')
    last_month_trend = None
    for trend in trends:
        last_month_trend = trend
        if (now - trend.recorddate).days >= 30:
            break
    youtuber.status = 97
    youtuber.save()

    timer.append(timeit.default_timer())
    print('%2d. [%5.2f / %5.2f s] 위에서 생성된 정보들 기반으로 스텟, 등급 계산'
          % (len(timer) - 1, timer[len(timer) - 1] - timer[len(timer) - 2], timer[len(timer) - 1] - timer[0]))

    stat_influence = get_influence(youtuber)
    stat_activity = get_activity(youtuber, video_detail_list)
    stat_trend = get_trend(youtuber, last_month_trend, today_trend)
    stat_views = get_views(youtuber, last_month_trend, today_trend)
    stat_charm = get_charm(video_detail_list)
    grade = get_grade(youtuber, stat_influence, stat_activity,
                      stat_trend, stat_views, stat_charm)
    print('*-----------------------------------------------------------*')
    print('| Influence |  Activity |     Trend |     Views |     Charm |')
    print('*-----------------------------------------------------------*')
    print('| %9d | %9d | %9d | %9d | %9d |' %
          (stat_influence, stat_activity, stat_trend, stat_views, stat_charm))
    print('*--------------------- Grade : %3d -------------------------*\n' % grade)

    youtuber.status = 99
    youtuber.save()
    # 15. 유튜버의 스텟, 등급, updatedDate 갱신
    now = datetime.datetime.now()
    youtuber.influence = stat_influence
    youtuber.activity = stat_activity
    youtuber.viewcounttrend = stat_views
    youtuber.subscribercounttrend = stat_trend
    youtuber.charm = stat_charm
    youtuber.grade = grade
    youtuber.updateddat = now
    
    print('*------------------ Total : %.2f s----------------------*' %
          (timeit.default_timer() - timer[0]))
    res['code'] = 0
    res['yno'] = yno
    time.sleep(1)
    youtuber.status = 0
    youtuber.save()
    return HttpResponse(json.dumps(res))

#-------------------------------------------------------------------------------------------------------------------------#
#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*#
#-------------------------------------------------------------------------------------------------------------------------#


def update_youtuber(request, yno):
    start = timeit.default_timer()
    # 6. Video 테이블 수집
    video_id_list = get_video_list(channel_info['uploadsID'])
    end66 = timeit.default_timer() - start
    print('6. get video list : %.2fs' % end66)
    video_detail_list = []
    for idx, video_id in enumerate(video_id_list):
        video_detail = get_video_detail(video_id)
        video_detail_list.append(video_detail)
        video = Video.objects.create(
            yno=youtuber,
            videoid=video_detail['video_id'],
            videoname=video_detail['videoName'],
            videodescription=video_detail['videoDescription'],
            videoviewcount=video_detail['videoViewCount'],
            videocommentcount=video_detail['videoCommentCount'],
            good=video_detail['good'],
            bad=video_detail['bad'],
            regdate=video_detail['regDate'],
            ycano=video_detail['ycano'],
            tags=video_detail['tags'],
            thumbnail=video_detail['thumbnail'],
            topic=video_detail['topic'],
        )
        video.save()
        end666 = timeit.default_timer() - end66
        print('   - get_video_detail : %.2f/%.2f s (%d/%d)' %
              (end666, timeit.default_timer() - start, idx + 1, len(video_id_list)))
    end6 = timeit.default_timer() - end666
    print('6. get & insert Video : %.2f/%.2f s' %
          (end6, timeit.default_timer() - start))

    # 7. trend 테이블 수집
    trend_list = get_trend_list(channel_id)
    for trend_item in trend_list:
        trend = Trend.objects.create(
            yno=youtuber,
            recorddate=trend_item['fields']['recordDate'],
            pointsubscriber=trend_item['fields']['pointSubscriber'],
            difsubscriber=trend_item['fields']['difSubscriber'],
            pointview=trend_item['fields']['pointView'],
            difview=trend_item['fields']['difView']
        )
        trend.save()
    end7 = timeit.default_timer() - end6
    print('7. get & insert Trend : %.2f/%.2f s' %
          (end7, timeit.default_timer() - start))

    # 8. 카테고리-유튜버 관계 설정
    # 8-1 calculate valid ycano list
    valid_ycano_list = []
    tmp_ycano_list = Video.objects.filter(yno=yno).values('ycano').annotate(
        total=Count('ycano')).order_by('total').reverse()
    for ycategory in tmp_ycano_list:
        if ycategory['total'] >= len(video_id_list) * 0.11:
            valid_ycano_list.append(ycategory['ycano'])
    end8_1 = timeit.default_timer() - end7
    print('8-1. calculate valid ycano list : %.2f/%.2f s' %
          (end8_1, timeit.default_timer() - start))

    # 8-2 get our category
    our_cano_list = get_our_cano(valid_ycano_list, video_detail_list)
    end8_2 = timeit.default_timer() - end8_1
    print('8-2. get our category : %.2f/%.2f s' %
          (end8_2, timeit.default_timer() - start))

    # 8-3 add CategoryYoutubeRelation
    for our_cano in our_cano_list:
        category = Category.objects.get(cano=our_cano)
        print(category.name)
        cy_relation = CategoryYoutubeRelation.objects.create(
            yno=youtuber,
            cano=category
        )
        cy_relation.save()
    end8_3 = timeit.default_timer() - end8_2
    print('8-3. add CategoryYoutubeRelation : %.2f/%.2f s' %
          (end8_3, timeit.default_timer() - start))

    # 9. news 테이블 수집
    print(datetime.datetime.today())
    news_list = get_news_list(youtuber, our_cano_list,
                              datetime.datetime.today())
    for news in news_list:
        new_news = News.objects.create(
            yno=youtuber,
            newslink=news['newsLink'],
            newstitle=news['newsTitle'],
            newsdescription=news['newsDescription'],
            newsdate=news['newsDate'],
            pressname='',
            clickcount=0,
        )
        new_news.save()
    end9 = timeit.default_timer() - end8_3
    print('9. add News Table : %.2f/%.2f s' %
          (end9, timeit.default_timer() - start))

    # 10.  community 테이블 수집 후 DB 추가
    get_daumCafe_search_result(
        youtuber, our_cano_list, datetime.datetime.today())
    end10 = timeit.default_timer() - end9
    print('10. calculate stat : %.2f/%.2f s' %
          (end10, timeit.default_timer() - start))

    # 11. 위에서 생성된 정보들 기반으로 스텟, 등급 계산
    #   - 파급력 ( 커뮤니티 언급수(그래프), 뉴스언급수, 조회수 ,구독자 대비 조회수)
    stat_influence = get_influence()
    print('    - stat_influence : ', stat_influence)
    #   - 활동 지수 ( 최근 10개 영상 업로드 주기 )
    stat_activity = get_activity()
    print('    - stat_activity : ', stat_activity)
    #   - 성장세 ( 구독자 증가 추이 대비 증감량을 꺾은선 그래프로 나타냄, 기준은 주별 )
    stat_trend = get_trend()
    print('    - stat_trend : ', stat_trend)
    #   - 기본 데이터 ( 총 조회수, 구독자수 , 댓글수)
    stat_basicstat = get_basicstat()
    print('    - stat_basicstat : ', stat_basicstat)
    #   - 호감도 ( 좋아요 수, 총 영상의 좋아요, 싫어요 비율, 댓글 수 )
    stat_charm = get_charm()
    print('    - stat_charm : ', stat_charm)
    #   - 등급
    grade = get_grade()
    print('    - grade : ', grade)
    end11 = timeit.default_timer() - end10
    print('11. calculate stat : %.2f/%.2f s' %
          (end11, timeit.default_timer() - start))

    # Todo 12. 유튜버의 스텟, 등급, updatedDate 갱신
    now = datetime.datetime.now()
    print('현재 시간 : ', now)
    youtuber.updateddate = now
    youtuber.save()

    end = timeit.default_timer() - start
    print('*** total : %.2fs ***' % end)
    return HttpResponse(0)


def is_youtube_channel_url(url):
    if 'youtube' not in url:
        return False
    if '/c/' not in url and '/user/' not in url and '/channel/' not in url:
        return False
    return True


def get_channel_id_from_url(url):
    html = urlopen(url).read()
    soup = bs(html, "html.parser", from_encoding='utf-8')
    ff = soup.find("button", attrs={'class': "yt-uix-button yt-uix-button-size-default "
                                    "yt-uix-button-subscribe-branded yt-uix-button-has-icon "
                                    "no-icon-markup yt-uix-subscription-button yt-can-buffer"})
    return ff.get('data-channel-external-id')


def get_yno_from_channel_id(channel_id):
    global text
    for youtuber in Youtuber.objects.all():
        if channel_id == youtuber.channelid:
            return youtuber.yno
    return -1


def get_channel_other_sites(input_url):
    other_link_list = []
    html = urlopen(input_url).read()
    soup = bs(html, "html.parser", from_encoding='utf-8')
    li_tags = soup.find_all("li", attrs={'class': "channel-links-item"})
    for li_tag in li_tags:
        before_link = li_tag.find('a').get('href')
        link = unquote(before_link[before_link.find('http'):])
        if '&' in link:
            link = link[:link.find('&')]
        other_link_list.append(link)
    return other_link_list


def get_channel_info(channelID):
    global key_index
    global key_list
    key = key_list[key_index]
    channel_info_dict = {}
    base_url = "https://www.googleapis.com/youtube/v3/channels"
    part = "id,snippet,brandingSettings,contentDetails,invideoPromotion,statistics,topicDetails"
    try:
        response = urllib.request.urlopen(
            base_url + "?part=%s&id=%s&key=%s" % (part, channelID, key))
    except urllib.request.HTTPError:
        print('*--- next key setting & restart ---*')
        key_index += 1
        key_index %= len(key_list)
        return get_channel_info(channelID)
    string = response.read().decode('utf-8')
    json_obj = json.loads(string)
    info_obj = json_obj["items"][0]

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


def get_growth_list(channel_id):
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko")
    driver = webdriver.Chrome('./chromedriver', options=options)

    url = 'https://socialblade.com/youtube/channel/' + channel_id + '/monthly'
    driver.get(url)
    el = '//*[@id="socialblade-user-content"]'
    orm = []
    try:
        content = driver.find_element_by_xpath(el).text.split('\n')
        cnt = 0
        flag = False
        pk = 0
        data = dict()
        for line in content:
            if line == 'ESTIMATED EARNINGS':
                flag = True
                continue
            elif line == 'Daily Averages':
                break
            if flag:
                if cnt == 1:
                    cnt += 1
                    continue
                if cnt == 6:
                    fin = dict()
                    fin['pk'] = pk
                    pk += 1
                    fin['model'] = "dataServer.growth"
                    fin['fields'] = data
                    temp = copy.deepcopy(fin)
                    orm.append(temp)
                    cnt = 0
                    continue
                elif cnt == 0:
                    data['recordDate'] = line
                    cnt += 1
                else:
                    x = line.replace('+', "").replace(",",
                                                      "").replace('--', '0').replace('LIVE', '')
                    total_stars = 0
                    if 'K' in x:
                        if len(x) > 1:
                            # convert k to a thousand
                            total_stars = float(x.replace('K', '')) * 1000
                    elif 'M' in x:
                        if len(x) > 1:
                            # convert M to a million
                            total_stars = float(x.replace('M', '')) * 1000000
                    else:
                        total_stars = int(x)  # Less than 1000
                    if cnt == 2:
                        data['difSubscriber'] = int(total_stars)
                    elif cnt == 3:
                        data['pointSubscriber'] = int(total_stars)
                    elif cnt == 4:
                        data['difView'] = int(total_stars)
                    elif cnt == 5:
                        data['pointView'] = int(total_stars)
                    cnt += 1
    except NoSuchElementException:
        pass
    driver.close()
    return orm


def get_video_list(uploads_id):
    global key_list
    global key_index
    key = key_list[key_index]
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
            key_index += 1
            key_index %= len(key_list)
            return get_video_list(uploads_id)
        string = response.read().decode('utf-8')
        json_objs = json.loads(string)
        for obj in json_objs['items']:
            video_id_lists.append(obj['snippet']['resourceId']['videoId'])
        #     pageToken
        if json_objs.get('nextPageToken') is None or json_objs.get('nextPageToken') == '':
            break
        page_token = json_objs.get('nextPageToken')
        cnt += 1
        if cnt == 2:
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
    global key_list
    global key_index
    key = key_list[key_index]
    # snippet으로 가져오는 정보: 유튜버, 제목, 설명, 게시일, 카테고리, 태그, 섬네일
    # statistics로 가져오는 정보: 조회수, 댓글 수, 좋아요 수, 싫어요 수
    # topicdetails로 가져오는 정보: 토픽
    part = 'snippet,statistics,topicDetails'
    url = 'https://www.googleapis.com/youtube/v3/videos?part={}&id={}&key={}'.format(
        part, video_id, key)
    try:
        response = urlopen(url).read().decode('utf-8')
    except:
        print('*--- next key setting & restart ---*')
        key_index += 1
        key_index %= len(key_list)
        return get_video_detail(video_id)
    res_dict = json.loads(response).get('items')[0]

    topic = []
    topic_details = res_dict.get('topicDetails')
    statistics = res_dict.get('statistics')
    snippet = res_dict.get('snippet')
    if topic_details:
        topic_id = topic_details.get('topicIds')
        if topic_id:
            topic += topic_id
        relevant_topic_id = topic_details.get('relevantTopicIds')
        if relevant_topic_id:
            topic += relevant_topic_id

    topic = list(set(topic))

    topic_result = []
    for result in topic:
        topic_result.append(TOPICS.get(result))

    try:
        tags = ','.join(snippet.get('tags'))
    except:
        tags = ''

    try:
        topic = ','.join(topic_result)
    except:
        topic = ''
    if statistics.get('likeCount') is None:
        statistics['likeCount'] = -1
    if statistics.get('dislikeCount') is None:
        statistics['dislikeCount'] = -1
    if statistics.get('commentCount') is None:
        statistics['commentCount'] = -1
    video = {
        'video_id': video_id,
        'videoName': res_dict.get('snippet').get('title'),
        'videoDescription': snippet.get('description'),
        'videoViewCount': statistics.get('viewCount'),
        'videoCommentCount': statistics.get('commentCount'),
        'good': statistics.get('likeCount'),
        'bad': statistics.get('dislikeCount'),
        'regDate': snippet.get('publishedAt')[:10],
        'ycano': snippet.get('categoryId'),
        'thumbnail': snippet.get('thumbnails').get('high').get('url'),
        'tags': tags,
        'topic': topic,
    }

    # 파일 출력
    # PATH = 'videoTableTest.json'
    # with open("{}".format(PATH), 'w', encoding='utf-8-sig') as file:
    #     json.dump(video, file, indent="\t", ensure_ascii=False)

    return video


def get_news_list(youtuber, category, last_updated_date):
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

    MONTH = ['', 'Jan', 'Feb', 'Mar', 'Apr', 'May',
             'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    YOUTUBER = youtuber  # DB 에서 yno 에 해당하는 channelName or youtubeName 을 입력
    CATEGORY = [2]  # 해당 유튜버의 카테고리가 게임과 엔터테인먼트

    URL = 'https://openapi.naver.com/v1/search/news.json?'
    params = {
        'query': YOUTUBER,
        'display': 100,
        'start': 1,
        'sort': 'date'
    }

    headers = {
        'X-Naver-Client-Id': config('X_NAVER_CLIENT_ID'),
        'X-Naver-Client-Secret': config('X_NAVER_CLIENT_SECRET'),
    }

    category_keyword = NECESSARY_WORD[0]
    for num in CATEGORY:
        category_keyword += NECESSARY_WORD[num]

    # 만약 last updatedDate 가 2019-03-15 면 3월 15일 이후의 기사만 가져와야함
    updated_date = datetime.datetime(2019, 3, 15)
    news_list = []
    while True:
        response = requests.get(
            URL, params=params, headers=headers).text  # str type
        total = json.loads(response)["total"]
        newses = json.loads(response)["items"]

        for news in newses:
            is_correct = False
            date = datetime.datetime(int(news["pubDate"][12:16]), MONTH.index(
                news["pubDate"][8:11]), int(news["pubDate"][5:7]))

            # 업데이트되어있는 기사는 추가하지 않음
            if (date - updated_date).days < 0:
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
    print('* ycano_list : ', ycano_list, len(video_detail_list))
    our_list = []
    for ycano in ycano_list:
        print('**', ycano)
        if str(ycano) in list(CANO_MAPPING.keys()):
            if CANO_MAPPING[str(ycano)] not in our_list:
                our_list.append(CANO_MAPPING[str(ycano)])
                print('***', CANO_MAPPING[str(ycano)], '추가')
        elif ycano == 1 or ycano == 24:
            count = 0
            for video_detail in video_detail_list:
                if 'kids' in video_detail['videoName'] or '키즈' in video_detail['videoName'] or '어린이' in video_detail['videoName']:
                    count += 1
            print('**ycano: 1 or 24:', count)
            if count >= len(video_detail_list) * 0.2:
                if 6 not in our_list:
                    our_list.append(6)
            else:
                if 2 not in our_list:
                    our_list.append(2)
        elif ycano == 22:
            count = 0
            for video_detail in video_detail_list:
                if 'mukbang' in video_detail['videoName'] or '먹방' in video_detail['videoName'] \
                        or '음식' in video_detail['videoName'] or 'food' in video_detail['videoName'] or '맛있' in video_detail['videoName']:
                    count += 1
            print('**ycano : 22 :', count)
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


def update_youtuber(request, yno):
    return HttpResponse(yno)


def add_video(request, videoId):
    pass
    # Todo 12. 유튜버의 스텟, 등급, updatedDate 갱신
    now = datetime.datetime.now()
    youtuber.activity = stat_activity
    youtuber.charm = stat_charm
    youtuber.updateddat = now + datetime.timedelta(hours=9)
    youtuber.save()

#-------------------------------------------------------------------------------------------------------------------------#
#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*#
#-------------------------------------------------------------------------------------------------------------------------#


def yno_from_url(request, url):
    res = {}
    url = url.replace('~', '/')
    try:
        channel_id = get_channel_id_from_url(url)
        yno = get_yno_from_channel_id(channel_id)
    except:
        res['yno'] = -1
        return HttpResponse(json.dumps(res))
    res['yno'] = yno
    return HttpResponse(json.dumps(res))


def status_from_yno(request, yno):
    res = {}
    res['status'] = Youtuber.objects.get(yno=yno).status
    return HttpResponse(json.dumps(res))

def update_stat_without_request():
    youtube_list = Youtuber.objects.all()
    print('|     yno | Influence |  Activity |     Trend |     Views |     Charm |')
    print('*--------------------------------------------------------------------*')
    for youtuber in youtube_list:
        Stat.objects.filter(yno=youtuber).filter().delete()
        video_list = Video.objects.filter(yno=youtuber)
        video_detail_list = []  # good, bad, reddate
        for video in video_list:
            temp = {}
            temp['regDate'] = video.regdate
            temp['good'] = video.good
            temp['bad'] = video.bad
            video_detail_list.append(temp)
        now = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=9)
        trends = Trend.objects.filter(yno=youtuber).order_by('-recorddate')
        last_month_trend = None
        for trend in trends:
            last_month_trend = trend
            if (now - trend.recorddate).days >= 30:
                break
        today_trend = trends[0]

        youtuber.influence = get_influence(youtuber)
        youtuber.activity = get_activity3(youtuber, video_detail_list)
        youtuber.viewcounttrend = get_views(youtuber, last_month_trend, today_trend)
        youtuber.subscribercounttrend = get_trend(youtuber, last_month_trend, today_trend)
        youtuber.charm = get_charm(video_detail_list)
        youtuber.grade = get_grade(youtuber, youtuber.influence, youtuber.activity, youtuber.subscribercounttrend, youtuber.viewcounttrend, youtuber.charm)
        youtuber.save()
        print('| %9d | %9d | %9d | %9d | %9d | %9d |' % (youtuber.yno, youtuber.influence, youtuber.activity, youtuber.subscribercounttrend, youtuber.viewcounttrend, youtuber.charm))