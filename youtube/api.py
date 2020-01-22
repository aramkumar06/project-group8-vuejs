import json
import requests
################## requests로 API 요청
URL = 'https://www.googleapis.com/youtube/v3/guideCategories?'
params = {
    'key': '',
    'part': 'snippet',
    'id': 'UCygs-_iDpCJOnhuCZibK7JQ',
    # 'relatedToVideoId': '41MKKToLRrk',
    # 'channelID': 'UCygs-_iDpCJOnhuCZibK7JQ',
    # 'maxResults': 7
}
URL = requests.get(URL, params=params).text # str type
result = json.loads(URL)
# # 가져온 정보를 json 파일로 만들기
with open("item.json", 'w', encoding='utf-8') as file:
    json.dump(result, file, indent="\t")
# # json으로 저장한 파일을 콘솔창에 print하기
with open("item.json", 'r', encoding='utf-8') as file:
    json_data = json.load(file)
print(json.dumps(json_data, indent='\t'))
######################
