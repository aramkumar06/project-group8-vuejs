import json
import requests
from pprint import pprint
from decouple import config

YOUTUBER = '피지컬갤러리'

NEWS_URL = 'https://openapi.naver.com/v1/search/news.json?'
BLOG_URL = 'https://openapi.naver.com/v1/search/blog.json?'
CAFE_URL = 'https://openapi.naver.com/v1/search/cafearticle.json?'
WEB_URL = 'https://openapi.naver.com/v1/search/webkr.json?'

################## requests로 API 요청

##### NEWS URL
URL = NEWS_URL
params = {
    'query': YOUTUBER,
    'display': '10',
    'start': '1',
    'sort': 'date'
}
#####

headers = {
    'X-Naver-Client-Id': config('X_NAVER_CLIENT_ID'),
    'X-Naver-Client-Secret': config('X_NAVER_CLIENT_SECRET'),
}

response = requests.get(URL, params=params, headers=headers).text # str type
result = json.loads(response)



# ################### 가져온 정보를 json 파일로 만들기
# PATH = '{}.json'.format(YOUTUBER)
# with open("{}".format(PATH), 'w', encoding='utf-8-sig') as file: 
#     json.dump(result, file, indent="\t", ensure_ascii=False)
# # json으로 저장한 파일을 콘솔창에 print하기
# # with open(f"{ YOUTUBER }.json", 'r', encoding='utf-8-sig') as file:
# #     json_data = json.load(file)
# # pprint(json.dumps(json_data, indent='\t'))
# # ######################
