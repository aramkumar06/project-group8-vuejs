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
    print('%2d. [%5.2f / %5.2f s] Determine the correct YouTube channel URL' % (len(timer) - 1, timer[len(timer) - 1] - timer[len(timer) - 2], timer[len(timer) - 1] - timer[0]))

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
        youtuber.delete()
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
        youtuber.delete()
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
        youtuber.delete()
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
            recorddate=datetime.datetime(today.year, today.month, today.day, 0, 0, 0),
            pointsubscriber=youtuber.subscriber,
            difsubscriber=int(youtuber.subscriber) - last_pointSubscriber,
            pointview=youtuber.totalviewcount,
            difview=int(youtuber.totalviewcount) - last_pointView,
        )
        today_trend.save()
    except Exception as e:
        print(e)
        youtuber.delete()
        res['code'] = -7
        return HttpResponse(json.dumps(res))
    timer.append(timeit.default_timer())
    print('%2d. [%5.2f / %5.2f s] trend 테이블 수집'
          % (len(timer) - 1, timer[len(timer) - 1] - timer[len(timer) - 2], timer[len(timer) - 1] - timer[0]))
    youtuber.status = 73
    youtuber.save()

    # 8 calculate valid ycano list
    valid_ycano_list = []
    tmp_ycano_list = Video.objects.filter(yno=yno).values('ycano').annotate(total=Count('ycano')).order_by('total').reverse()
    for ycategory in tmp_ycano_list:
        if ycategory['total'] >= len(video_detail_list) * 0.11:
            valid_ycano_list.append(ycategory['ycano'])
    timer.append(timeit.default_timer())
    print('%2d. [%5.2f / %5.2f s] calculate valid ycano list'
          % (len(timer) - 1, timer[len(timer) - 1] - timer[len(timer) - 2], timer[len(timer) - 1] - timer[0]))
    youtuber.status = 77
    youtuber.save()

    # 9 get our category (에러날일이 없다)
    our_cano_list = get_our_cano(valid_ycano_list, video_detail_list)
    timer.append(timeit.default_timer())
    print('%2d. [%5.2f / %5.2f s] get our category'
          % (len(timer) - 1, timer[len(timer) - 1] - timer[len(timer) - 2], timer[len(timer) - 1] - timer[0]))
    youtuber.status = 80
    youtuber.save()

    # 10 add CategoryYoutubeRelation
    try:
        for our_cano in our_cano_list:
            category = Category.objects.get(cano=our_cano)
            CategoryYoutubeRelation.objects.create(
                yno=youtuber,
                cano=category
            )
    except Exception as e:
        print(e)
        youtuber.delete()
        res['code'] = -8
        return HttpResponse(json.dumps(res))
    timer.append(timeit.default_timer())
    print('%2d. [%5.2f / %5.2f s] add CategoryYoutubeRelation'
          % (len(timer) - 1, timer[len(timer) - 1] - timer[len(timer) - 2], timer[len(timer) - 1] - timer[0]))
    youtuber.status = 83
    youtuber.save()

    # 11 news 테이블 수집
    try:
        news_list = get_news_list(youtuber, our_cano_list, datetime.datetime(2010, 1, 1))
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
    except Exception as e:
        print(e)
        youtuber.delete()
        res['code'] = -9
        return HttpResponse(json.dumps(res))
    timer.append(timeit.default_timer())
    print('%2d. [%5.2f / %5.2f s] news 테이블 수집'
          % (len(timer) - 1, timer[len(timer) - 1] - timer[len(timer) - 2], timer[len(timer) - 1] - timer[0]))
    youtuber.status = 88
    youtuber.save()

    # 12.  community 테이블 수집 후 DB 추가
    try:
        get_daumCafe_search_result(youtuber, our_cano_list,  datetime.datetime(2010, 1, 1))
    except Exception as e:
        print('*ERROR (10) : ', e)
        youtuber.delete()
        res['code'] = -10
        return HttpResponse(json.dumps(res))
    timer.append(timeit.default_timer())
    print('%2d. [%5.2f / %5.2f s] community 테이블 수집 후 DB 추가'
          % (len(timer) - 1, timer[len(timer) - 1] - timer[len(timer) - 2], timer[len(timer) - 1] - timer[0]))
    youtuber.status = 90
    youtuber.save()

    # 13. naverDataLab 추가
    try:
        insert_naver_data_lab(youtuber)
    except Exception as e:
        print('*ERROR naverDataLab : ', e)
        youtuber.delete()
        res['code'] = -10
        return HttpResponse(json.dumps(res))
    timer.append(timeit.default_timer())
    print('%2d. [%5.2f / %5.2f s] naverDataLab 추가'
          % (len(timer) - 1, timer[len(timer) - 1] - timer[len(timer) - 2], timer[len(timer) - 1] - timer[0]))
    youtuber.status = 92
    youtuber.save()

    # 14. 위에서 생성된 정보들 기반으로 스텟, 등급 계산
    last_month_trend = None
    try:
        now = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=9)
        trends = Trend.objects.filter(yno=youtuber).order_by('-recorddate')
        for trend in trends:
            last_month_trend = trend
            if (now - trend.recorddate).days >= 30:
                break
    except Exception as e:
        print(e)
        youtuber.delete()
        res['code'] = -11
        return HttpResponse(json.dumps(res))

    youtuber.status = 97
    youtuber.save()

    timer.append(timeit.default_timer())
    print('%2d. [%5.2f / %5.2f s] 위에서 생성된 정보들 기반으로 스텟, 등급 계산'
          % (len(timer) - 1, timer[len(timer) - 1] - timer[len(timer) - 2], timer[len(timer) - 1] - timer[0]))

    try:
        stat_influence = get_influence(youtuber)
        stat_activity = get_activity(youtuber, video_detail_list)
        stat_trend = get_trend(youtuber, last_month_trend, today_trend)
        stat_views = get_views(youtuber, last_month_trend, today_trend)
        stat_charm = get_charm(video_detail_list)
        grade = get_grade(youtuber, stat_influence, stat_activity, stat_trend, stat_views, stat_charm)
    except Exception as e:
        print('* Exception :', e)
        youtuber.delete()
        res['code'] = -12
        return HttpResponse(json.dumps(res))
    print('*-----------------------------------------------------------*')
    print('| Influence |  Activity |     Trend |     Views |     Charm |')
    print('*-----------------------------------------------------------*')
    print('| %9d | %9d | %9d | %9d | %9d |' % (stat_influence, stat_activity, stat_trend, stat_views, stat_charm))
    print('*--------------------- Grade : %3d -------------------------*\n' % grade)
    youtuber.status = 100
    youtuber.save()

    # 15. 유튜버의 스텟, 등급, updatedDate 갱신
    try:
        now = datetime.datetime.now()
        youtuber.influence = stat_influence
        youtuber.activity = stat_activity
        youtuber.viewcounttrend = stat_views
        youtuber.subscribercounttrend = stat_trend
        youtuber.charm = stat_charm
        youtuber.grade = grade 
        youtuber.updateddat = now
        print('*---------------------- Total : %.2f s----------------------*' % (timeit.default_timer() - timer[0]))
        res['code'] = 0
        res['yno'] = yno
        time.sleep(1.5)
        youtuber.status = 0
        youtuber.save()
    except Exception as e:
        print('* Exception :', e)
        youtuber.delete()
        res['code'] = -12
        return HttpResponse(json.dumps(res))
    return HttpResponse(json.dumps(res))

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