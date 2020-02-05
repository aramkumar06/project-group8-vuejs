import json
import requests
from decouple import config
import datetime

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

MONTH = ['', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
YOUTUBER = 'workman'    # DB 에서 yno 에 해당하는 channelName or youtubeName 을 입력
CATEGORY = [2]     # 해당 유튜버의 카테고리가 게임과 엔터테인먼트

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
updatedDate = datetime.datetime(2019, 3, 15)
news_list = []
while True:
    response = requests.get(URL, params=params, headers=headers).text  # str type
    total = json.loads(response)["total"]
    newses = json.loads(response)["items"]

    for (index, news) in enumerate(newses):
        isCorrect = False
        date = datetime.datetime(int(news["pubDate"][12:16]), MONTH.index(news["pubDate"][8:11]), int(news["pubDate"][5:7]))

        # 업데이트되어있는 기사는 추가하지 않음
        if (date - updatedDate).days < 0:
            break

        # Description 에 특정 키워드가 없는 기사는 추가하지 않음
        for keyword in category_keyword:
            if keyword in news["description"]:
                isCorrect = True
                break
        if not isCorrect:
            continue

        newNews = {
            'newsLink': news["link"],
            'newsTitle': news["title"],
            'newsDescription': news["description"],
            'newsDate': str(date)[:10]
        }
        news_list.append(newNews)
    if params['start'] >= min(1000, total):
        break
    params['start'] += params['display']
