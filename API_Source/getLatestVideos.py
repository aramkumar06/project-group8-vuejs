from urllib.request import urlopen
from decouple import config


# channeID로 최신 동영상 가져오기


channelID = 'UCUpJs89fSBXNolQGOYKn0YQ'
KEY = config('GOOGLEAPIKEY')
maxResult = 2 # 가져올 동영상의 수
URL = 'https://www.googleapis.com/youtube/v3/search?key={}&channelId={}&part=snippet,id&order=date&maxResults={}'.format(KEY, channelID, maxResult)
response = urlopen(URL).read().decode('utf8')
# headers = {'Content-Type': 'charset=utf-8'}
# response = requests.get(URL).text
print(response)
