from django.shortcuts import render, HttpResponse
from django.db.models import Count
from .models import *
from .stat  import get_influence, get_activity, get_trend, get_basicstat, get_charm, get_grade
from .function import *
import urllib.request
import requests
from decouple import config
from urllib.request import urlopen, unquote
import datetime


key_list = [config('GOOGLEAPIKEY1'), config('GOOGLEAPIKEY2'),
            config('GOOGLEAPIKEY3'), config('GOOGLEAPIKEY4')]
key_index = 0


def index(request):
    return HttpResponse(Youtuber.objects.all()[0].youtubername)


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
    start = timeit.default_timer()
    res = {}
    url = url.replace('~', '/')

    # 1. 올바른 유튜브 채널 URL 판단
    if not is_youtube_channel_url(url):
        res['code'] = -1
        return HttpResponse(json.dumps(res))
    end1 = timeit.default_timer() - start
    print('1. Determine the correct YouTube channel URL : %.2f/%.2f s' % (end1, timeit.default_timer() - start))

    # 2. URL로부터 channel ID 얻기
    try:
        channel_id = get_channel_id_from_url(url)
    except:
        res['code'] = -2
        return HttpResponse(json.dumps(res))
    end2 = timeit.default_timer() - end1
    print('2. Get channel ID from URL : %.2f/%.2f s' % (end2, timeit.default_timer() - start))

    # 3. url 채널 정보가 DB에 없는지 판단
    yno = get_yno_from_channel_id(channel_id)
    if yno != -1:
        res['code'] = 1
        res['yno'] = yno
        return HttpResponse(json.dumps(res))
    end3 = timeit.default_timer() - end2
    print('3. Determines if channel information is not in the DB : %.2f/%.2f s' % (end3,timeit.default_timer() - start))

    # 4. 유튜버 channel info 수집 후 DB 추가
    now = time.gmtime(time.time())
    other_links = ['', '', '', '', '']
    for (i, site) in enumerate(get_channel_other_sites(url)):
        other_links[i] = site
    channel_info = get_channel_info(channel_id)
    print('구독자수 : ', int(channel_info['subscriberCount']))
    print('최소 수  :' , int(config('MIN_SUBSCRIBER')))
    if int(channel_info['subscriberCount']) < int(config('MIN_SUBSCRIBER')):
        res['code'] = -3
        return HttpResponse(json.dumps(res))
    youtuber = Youtuber.objects.create(
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
        grade='Unknown',
        influence='0',
        activity='0',
        subscribercounttrend='0',
        viewcounttrend='0',
        charm='0',
        clickcount='0',
        updateddate='%d-%d-%d %d:%d:%d' % (now.tm_year, now.tm_mon,
                                           now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec),
        regdate='%d-%d-%d' % (now.tm_year, now.tm_mon, now.tm_mday),
        otherlink1=other_links[0],
        otherlink2=other_links[1],
        otherlink3=other_links[2],
        otherlink4=other_links[3],
        otherlink5=other_links[4],
        uploadsid=channel_info['uploadsID']
    )
    try:
        youtuber.save()
    except:
        res['code'] = -4
        return HttpResponse(json.dumps(res))
    end4 = timeit.default_timer() - end3
    print('4. Add DB after collecting YouTube channel info : %.2f/%.2f s' % (end4, timeit.default_timer() - start))

    # 5. 생성된 유튜버의 yno를 DB에서 찾아 가져오기
    try:
        yno = get_yno_from_channel_id(channel_id)
    except:
        res['code'] = -5
        return HttpResponse(json.dumps(res))
    end5 = timeit.default_timer() - end4
    print('5. Locate and import the yno of the created user from the DB : %.2f/%.2f s' % (end5, timeit.default_timer() - start))

    # 6. Video 테이블 수집
    video_id_list = []
    video_detail_list = []
    try:
        video_id_list = get_video_list(channel_info['uploadsID'])
        end66 = timeit.default_timer() - end5
        print('6. get video list : %.2fs' % end66)
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
            print('   - get_video_detail : %.2f/%.2f s (%d/%d)' % (end666,timeit.default_timer() - start, idx + 1, len(video_id_list)))
    except:
        res['code'] = -6
        return HttpResponse(json.dumps(res))
    end6 = timeit.default_timer() - end666
    print('6. get & insert Video : %.2f/%.2f s' % (end6, timeit.default_timer() - start))

    # 7. trend 테이블 수집
    try:
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
    except:
        res['code'] = -7
        return HttpResponse(json.dumps(res))
    end7 = timeit.default_timer() - end6
    print('7. get & insert Trend : %.2f/%.2f s' % (end7, timeit.default_timer() - start))

    # 8. 카테고리-유튜버 관계 설정
    # 8-1 calculate valid ycano list
    valid_ycano_list = []
    tmp_ycano_list = Video.objects.filter(yno=yno).values('ycano').annotate(
        total=Count('ycano')).order_by('total').reverse()
    for ycategory in tmp_ycano_list:
        if ycategory['total'] >= len(video_id_list) * 0.14:
            valid_ycano_list.append(ycategory['ycano'])
    end8_1 = timeit.default_timer() - end7
    print('8-1. calculate valid ycano list : %.2f/%.2f s' % (end8_1, timeit.default_timer() - start))

    # 8-2 get our category
    our_cano_list = get_our_cano(valid_ycano_list, video_detail_list)
    end8_2 = timeit.default_timer() - end8_1
    print('8-2. get our category : %.2f/%.2f s' % (end8_2, timeit.default_timer() - start))

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
    print('8-3. add CategoryYoutubeRelation : %.2f/%.2f s' % (end8_3, timeit.default_timer() - start))
    
    # 9. news 테이블 수집
    news_list = get_news_list(youtuber, our_cano_list, datetime.datetime(2010, 1, 1))
    print('news 개수 : ', len(news_list))
    for news in news_list:
        new_news = News.objects.create(
            yno = youtuber,
            newslink = news['newsLink'],
            newstitle = news['newsTitle'],
            newsdescription = news['newsDescription'],
            newsdate = news['newsDate'],
            pressname = '',
            clickcount = 0,
        )
        new_news.save()
    end9 = timeit.default_timer() - end8_3
    print('9. add News Table : %.2f/%.2f s' % (end9, timeit.default_timer() - start))

    # 10.  community 테이블 수집 후 DB 추가
    try:
        get_daumCafe_search_result(youtuber, our_cano_list,  datetime.datetime(2010, 1, 1))
    except:
        res['code'] = -10
        return HttpResponse(json.dumps(res))
    end10 = timeit.default_timer() - end9
    print('10. calculate stat : %.2f/%.2f s' % (end10, timeit.default_timer() - start))


    # 11. 위에서 생성된 정보들 기반으로 스텟, 등급 계산
    #   - 파급력 ( 커뮤니티 언급수(그래프), 뉴스언급수, 조회수 ,구독자 대비 조회수)
    stat_influence = get_influence()
    print('    - stat_influence : ', stat_influence)
    #   - 활동 지수 ( 최근 10개 영상 업로드 주기 )
    stat_activity = get_activity(video_detail_list)
    print('    - stat_activity : ', stat_activity)
    #   - 성장세 ( 구독자 증가 추이 대비 증감량을 꺾은선 그래프로 나타냄, 기준은 주별 )
    stat_trend = get_trend()
    print('    - stat_trend : ', stat_trend)
    #   - 기본 데이터 ( 총 조회수, 구독자수 , 댓글수)
    stat_basicstat = get_basicstat()
    print('    - stat_basicstat : ', stat_basicstat)
    #   - 호감도 ( 좋아요 수, 총 영상의 좋아요, 싫어요 비율, 댓글 수 )
    stat_charm = get_charm(video_detail_list)
    print('    - stat_charm : ', stat_charm)
    #   - 등급 
    grade = get_grade()
    print('    - grade : ', grade)
    end11 = timeit.default_timer() - end10
    print('11. calculate stat : %.2f/%.2f s' % (end11, timeit.default_timer() - start))
    
    # Todo 12. 유튜버의 스텟, 등급, updatedDate 갱신
    now = datetime.datetime.now()
    print('현재 시간 : ',now)
    youtuber.updateddat = now + datetime.timedelta(hours=18)
    end = timeit.default_timer() - start
    print('*** total : %.2fs ***' % end)
    res['code'] = 0
    res['yno'] = yno
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
        print('   - get_video_detail : %.2f/%.2f s (%d/%d)' % (end666,timeit.default_timer() - start, idx + 1, len(video_id_list)))
    end6 = timeit.default_timer() - end666
    print('6. get & insert Video : %.2f/%.2f s' % (end6, timeit.default_timer() - start))

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
    print('7. get & insert Trend : %.2f/%.2f s' % (end7, timeit.default_timer() - start))

    # 8. 카테고리-유튜버 관계 설정
    # 8-1 calculate valid ycano list
    valid_ycano_list = []
    tmp_ycano_list = Video.objects.filter(yno=yno).values('ycano').annotate(
        total=Count('ycano')).order_by('total').reverse()
    for ycategory in tmp_ycano_list:
        if ycategory['total'] >= len(video_id_list) * 0.14:
            valid_ycano_list.append(ycategory['ycano'])
    end8_1 = timeit.default_timer() - end7
    print('8-1. calculate valid ycano list : %.2f/%.2f s' % (end8_1, timeit.default_timer() - start))

    # 8-2 get our category
    our_cano_list = get_our_cano(valid_ycano_list, video_detail_list)
    end8_2 = timeit.default_timer() - end8_1
    print('8-2. get our category : %.2f/%.2f s' % (end8_2, timeit.default_timer() - start))

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
    print('8-3. add CategoryYoutubeRelation : %.2f/%.2f s' % (end8_3, timeit.default_timer() - start))
    
    # 9. news 테이블 수집
    print(datetime.datetime.today())
    news_list = get_news_list(youtuber, our_cano_list, datetime.datetime.today())
    for news in news_list:
        new_news = News.objects.create(
            yno = youtuber,
            newslink = news['newsLink'],
            newstitle = news['newsTitle'],
            newsdescription = news['newsDescription'],
            newsdate = news['newsDate'],
            pressname = '',
            clickcount = 0,
        )
        new_news.save()
    end9 = timeit.default_timer() - end8_3
    print('9. add News Table : %.2f/%.2f s' % (end9, timeit.default_timer() - start))

    # 10.  community 테이블 수집 후 DB 추가
    get_daumCafe_search_result(youtuber, our_cano_list, datetime.datetime.today())
    end10 = timeit.default_timer() - end9
    print('10. calculate stat : %.2f/%.2f s' % (end10, timeit.default_timer() - start))


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
    print('11. calculate stat : %.2f/%.2f s' % (end11, timeit.default_timer() - start))
    
    # Todo 12. 유튜버의 스텟, 등급, updatedDate 갱신
    now = datetime.datetime.now()
    print('현재 시간 : ',now)
    youtuber.updateddate=now
    youtuber.save()

    end = timeit.default_timer() - start
    print('*** total : %.2fs ***' % end)
    return HttpResponse(0)
