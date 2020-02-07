import datetime
from .models import *


#   - 파급력 ( 커뮤니티 언급수(그래프), 뉴스언급수, 조회수 ,구독자 대비 조회수)
def get_influence():
    value = 0

    return value

#   - 활동 지수 ( 최근 10개 영상 업로드 주기 )
def get_activity(video_detail_list):
    max_num = min(len(video_detail_list), 10)
    datetime_list = []
    for i in range(max_num):
        datetime_list.append(datetime.datetime.strptime(video_detail_list[i]['regDate'], '%Y-%m-%d'))
    dif_sum = 0
    for i in range(max_num - 1):
        dif_sum += (datetime_list[i] - datetime_list[i+1]).days
    print('%d 개 평균 업로드 주기 지수 : %f' % (max_num, dif_sum/max_num))
    stat = Stat.objects.create(
        
    )
    return 

#   - 성장세 ( 구독자 증가 추이 대비 증감량을 꺾은선 그래프로 나타냄, 기준은 주별 )
def get_trend():
    value = 0
    
    return value

#   - 기본 데이터 ( 총 조회수, 구독자수 , 댓글수)
def get_basicstat():
    value = 0
    
    return value

#   - 호감도 ( 좋아요 수, 총 영상의 좋아요, 싫어요 비율, 댓글 수 )
def get_charm(video_list):
    good = 0
    bad = 0
    value = 0
    for video in video_list:
        if not video['good'] or video['good'] == None:
            continue
        good += int(video['good'])
        bad += int(video['bad'])
    if good + bad == 0:
        value = 0
    else:
        value = int(good * 100 / (good + bad))
    return value

#   - 등급 
def get_grade():
    grade = ''
    
    return grade