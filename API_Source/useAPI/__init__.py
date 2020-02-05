from bs4 import BeautifulSoup as BS
from decouple import config
from urllib.request import urlopen, unquote
import urllib.request
import json
import time
import sys
import io

############### print 할 때 utf-8 디코딩이 안 될 경우 주석 해제
# sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
# sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


TOPICS = {
    '/m/04rlf': 'Music',
    '/m/05fw6t': "Children's music",
    '/m/02mscn': 'Christian music',
    '/m/0ggq0m': 'Classical music',    
    '/m/01lyv': 'Country',
    '/m/02lkt': 'Electronic music',
    '/m/0glt670': 'Hip hop music',
    '/m/05rwpb': 'Independent music',
    '/m/03_d0': 'Jazz',
    '/m/028sqc': 'Music of Asia',
    '/m/0g293': 'Music of Latin America',
    '/m/064t9': 'Pop music',
    '/m/06cqb': 'Reggae',
    '/m/06j6l': 'Rhythm and blues',
    '/m/06by7': 'Rock music',
    '/m/0gywn': 'Soul music',
    '/m/0bzvm2': 'Gaming',
    '/m/025zzc': 'Action game',
    '/m/02ntfj': 'Action-adventure game',
    '/m/0b1vjn': 'Casual game',
    '/m/02hygl': 'Music video game',
    '/m/04q1x3q': 'Puzzle video game',
    '/m/01sjng': 'Racing video game',
    '/m/0403l3g': 'Role-playing video game',
    '/m/021bp2': 'Simulation video game',
    '/m/022dc6': 'Sports game',
    '/m/03hf_rm': 'Strategy video game',
    '/m/06ntj': 'Sports',
    '/m/0jm_': 'American football',
    '/m/018jz': 'Baseball',
    '/m/018w8': 'Basketball',
    '/m/01cgz': 'Boxing',
    '/m/09xp_': 'Cricket',
    '/m/02vx4': 'Football',
    '/m/037hz': 'Golf',
    '/m/03tmr': 'Ice hockey',
    '/m/01h7lh': 'Mixed martial arts',
    '/m/0410tth': 'Motorsport',
    '/m/066wd': 'Professional wrestling',
    '/m/07bs0': 'Tennis',
    '/m/07_53': 'Volleyball',
    '/m/02jjt': 'Entertainment',
    '/m/095bb': 'Animated cartoon',
    '/m/09kqc': 'Humor',
    '/m/02vxn': 'Movies',
    '/m/05qjc': 'Performing arts',
    '/m/019_rr': 'Lifestyle',
    '/m/032tl': 'Fashion',
    '/m/027x7n': 'Fitness',
    '/m/02wbm': 'Food',
    '/m/0kt51': 'Health',
    '/m/03glg': 'Hobby',
    '/m/068hy': 'Pets',
    '/m/041xxh': 'Physical attractiveness [Beauty]',
    '/m/07c1v': 'Technology',
    '/m/07bxq': 'Tourism',
    '/m/07yv9': 'Vehicles',
    '/m/01k8wb': 'Knowledge',
    '/m/098wr': 'Society',
}


def get_channelID_from_URL(input_URL):
    # 해당 유튜버 페이지의 버튼 태그에서 속성값을 가져온다.
    html = urlopen(input_URL).read()
    page_obj = BS(html, "html.parser", from_encoding='utf-8')
    class_attr = "yt-uix-button yt-uix-button-size-default yt-uix-button-subscribe-branded yt-uix-button-has-icon no-icon-markup yt-uix-subscription-button yt-can-buffer"
    channelID = page_obj.find(
        "button", 
        attrs = {
                'class': class_attr 
            }).get('data-channel-external-id')

    return channelID


def get_latest_videos_using_channelID(channelID):
    KEY = config('GOOGLEAPIKEY')
    URL = 'https://www.googleapis.com/youtube/v3/search?key={}&channelId={}&part=snippet,id&order=date&maxResults={}'.format(KEY, channelID, maxResult)
    response = urlopen(URL).read().decode('utf8')
    
    # response에 str 타입으로 자료가 넘어옴
    # response = requests.get(URL).text
    
    print(type(response))
    print(response)


def get_video_details(videoId):
    # snippet으로 가져오는 정보: 유튜버, 제목, 설명, 게시일, 카테고리, 태그, 섬네일
    # statistics로 가져오는 정보: 조회수, 댓글 수, 좋아요 수, 싫어요 수
    # topicdetails로 가져오는 정보: 토픽
    part = 'snippet,statistics,topicDetails'
    URL = 'https://www.googleapis.com/youtube/v3/videos?part={}&id={}&key={}'.format(part, videoId, config('GOOGLEAPIKEY'))
    response = urlopen(URL).read().decode('utf-8')
    res_dict = json.loads(response).get('items')[0]    
    
    
    topic = []
    if res_dict.get('topicDetails'):
        topicId = res_dict.get('topicDetails').get('topicIds')
        if topicId:
            topic += topicId
        relevantTopicId = res_dict.get('topicDetails').get('relevantTopicIds')
        if relevantTopicId:
            topic += relevantTopicId 
    
    topic = list(set(topic))
    
    topic_result = []
    for result in topic:
        topic_result.append(TOPICS.get(result))
        print(topic_result)
    
    try:
        tags = ','.join(res_dict.get('snippet').get('tags'))
    except:
        tags = ''
    
    try:
        topic = ','.join(topic_result)
    except:
        topic = ''

    video = {
        'vno': videoId,
        'yno': res_dict.get('snippet').get('channelId'),
        'videoName': res_dict.get('snippet').get('title'),
        'videoDescription': res_dict.get('snippet').get('description'),
        'videoViewCount': res_dict.get('statistics').get('viewCount'),
        'videoCommentCount': res_dict.get('statistics').get('commentCount'),
        'good': res_dict.get('statistics').get('likeCount'),
        'bad': res_dict.get('statistics').get('dislikeCount'),
        'regDate': res_dict.get('snippet').get('publishedAt')[0:10], 
        'youtubeCategory': res_dict.get('snippet').get('categoryId'),
        'thumbnail': res_dict.get('snippet').get('thumbnails').get('high').get('url'),
        'tags': tags,
        'topic': topic,
    }
    
    ###### 파일 출력
    # PATH = 'videoTableTest.json'
    # with open("{}".format(PATH), 'w', encoding='utf-8-sig') as file: 
    #     json.dump(video, file, indent="\t", ensure_ascii=False)

    return video


def get_channel_other_sites(input_url):
    other_link_list = []
    html = urlopen(input_url).read()
    soup = BS(html, "html.parser", from_encoding='utf-8')
    li_tags = soup.find_all("li", attrs={'class': "channel-links-item"})
    for li_tag in li_tags:
        before_link = li_tag.find('a').get('href')
        link = unquote(before_link[before_link.find('http'):])
        if '&' in link:
            link = link[:link.find('&')]
        other_link_list.append(link)
    return other_link_list


def get_channel_info(channelID):
    channel_info_dict = {}
    base_url = "https://www.googleapis.com/youtube/v3/channels"
    part = "id,snippet,brandingSettings,contentDetails,invideoPromotion,statistics,topicDetails"
    response = urllib.request.urlopen(base_url + "?part=%s&id=%s&key=%s" % (part, channelID, key))
    string = response.read().decode('utf-8')
    json_obj = json.loads(string)

    snippet = json_obj["items"][0]["snippet"]
    channel_info_dict["title"] = snippet["title"]
    channel_info_dict['customUrl'] = snippet.get('customUrl')
    channel_info_dict["description"] = snippet["description"]
    channel_info_dict["thumbnail"] = snippet["thumbnails"]["default"]["url"]
    channel_info_dict['publishedAt'] = snippet["publishedAt"][:10]

    statistics = json_obj["items"][0]["statistics"]
    channel_info_dict["viewCount"] = statistics["viewCount"]
    channel_info_dict["subscriberCount"] = statistics["subscriberCount"]
    channel_info_dict["videoCount"] = statistics["videoCount"]

    brandingSettings = json_obj["items"][0]["brandingSettings"]
    channel_info_dict['banner_url'] = brandingSettings["image"]["bannerImageUrl"]

    return channel_info_dict


if __name__ == "__main__":
    key = config('GOOGLEAPIKEY')
    now = time.gmtime(time.time())
    url = "https://www.youtube.com/channel/UCdUcjkyZtf-1WJyPPiETF1g"
    channel_id = get_channelID_from_URL(url)
    # get_latest_videos_using_channelID(channel_id)
    other_links = get_channel_other_sites(url)
    channel_info = get_channel_info(channel_id)

    print('* url : ' + url)
    print('* channel_id : ' + channel_id)
    print('* other_links : ' + str(len(other_links)))
    for index, link in enumerate(other_links):
        print('\t%d - %s' % (index + 1, link))
    print('* channel_info')
    for item in channel_info:
        print('\t%s - %s' % (item, channel_info[item]))

    youtuber = {
        'channelID': channel_id,
        'channelName': channel_info['title'],
        'youtubeName': channel_info['customUrl'],
        'channelDescription': channel_info['description'],
        'bannerImageLink': channel_info['banner_url'],
        'channelLink': url,
        'thumbnail': channel_info['thumbnail'],
        'publishedDate': channel_info['publishedAt'],
        'subscriber': channel_info['subscriberCount'],
        'totalViewCount': channel_info['viewCount'],
        'totalVideoCount': channel_info['videoCount'],
        'updateDate': '%d-%d-%d %d:%d:%d' % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec),
        'regDate': '%d-%d-%d' % (now.tm_year, now.tm_mon, now.tm_mday),
    }
    for (index, item) in enumerate(other_links):
        youtuber['otherLink{}'.format(index + 1)] = item
