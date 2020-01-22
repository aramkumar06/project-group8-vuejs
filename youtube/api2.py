import urllib.request
import json
from decouple import config

idn = "UCwx6n_4OcLgzAGdty0RWCoA"  # 워크맨
key = config("YOUTUBE_APIKEY")
base_url = "https://www.googleapis.com/youtube/v3/channels"
part = "id,snippet,brandingSettings,contentDetails,invideoPromotion,statistics,topicDetails"
# id, snippet, brandingSettings, contentDetails, invideoPromotion, statistics, topicDetails
response = urllib.request.urlopen(base_url + "?part=%s&id=%s&key=%s" % (part, idn, key))
string = response.read().decode('utf-8')

json_obj = json.loads(string)
# jsoon_obj는 dictionary처럼 사용할 수 있다.
print(json_obj["items"][0]["statistics"]["subscriberCount"])
print(json_obj)