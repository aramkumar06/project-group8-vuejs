import urllib.request
import json
from decouple import config

idn = "UCbD8EppRX3ZwJSou-TVo90A"
key = config('GOOGLEAPIKEY')
base_url = "https://www.googleapis.com/youtube/v3/channels"
part = "id,snippet,brandingSettings,contentDetails,invideoPromotion,statistics,topicDetails"
response = urllib.request.urlopen(base_url + "?part=%s&id=%s&key=%s" % (part, idn, key))
string = response.read().decode('utf-8')
json_obj = json.loads(string)
# print(json_obj["items"][0]["statistics"]["subscriberCount"] // 구독자수 표시
print(string)