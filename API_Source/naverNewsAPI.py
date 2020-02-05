import json
import requests
from pprint import pprint
from decouple import config

# ++ 날짜 형식은 YYYY-MM-DD 형식으로 바꾸기

YOUTUBER = '피지컬갤러리'

PATH = '{}.json'.format(YOUTUBER)
try:
    with open("{}".format(PATH), 'r', encoding='utf-8-sig') as file:
        DATA = json.load(file)
except FileNotFoundError:
    DATA = dict()


NEWS_URL = 'https://openapi.naver.com/v1/search/news.json?'
DISPLAY = 100    # 검색결과 출력 건수(10 ~ 100)
START = 112      # 검색 시작 위치(1 ~ 1000)

URL = NEWS_URL

params = {  # 매개변수
    'query': YOUTUBER,
    'display': DISPLAY,
    'start': START,
    'sort': 'date'
}

headers = {  # 헤더 정보
    'X-Naver-Client-Id': config('X_NAVER_CLIENT_ID'),
    'X-Naver-Client-Secret': config('X_NAVER_CLIENT_SECRET'),
}

# 요청 결과
response = requests.get(URL, params=params, headers=headers).text # type str
result = json.loads(response)   # type dict



### 여기에 필터를 추가할 것

# DATA와 result를 합친다.
for key, value in result.items():
    # 기사 목록은 이전 정보들과 합친다.
    if key == 'items':
        try:
            DATA[key] += value
        except KeyError:
            DATA[key] = value
    # 과거 정보는 새로운 정보로 업데이트
    else:
        DATA[key] = value


# 가져온 정보를 json 파일로 만들기
with open("{}".format(PATH), 'w', encoding='utf-8-sig') as file: 
    json.dump(DATA, file, indent="\t", ensure_ascii=False)
















# # json으로 저장한 파일을 콘솔창에 print하기
# with open("{}".format(PATH), 'r', encoding='utf-8-sig') as file:
#     json_data = json.load(file)
# pprint(json_data)

