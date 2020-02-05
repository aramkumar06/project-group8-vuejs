from urllib.request import urlopen
from decouple import config
import json
from pprint import pprint


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


def make_video_table(video_id):
    # snippet으로 가져오는 정보: 유튜버, 제목, 설명, 게시일, 카테고리, 태그, 섬네일
    # statistics로 가져오는 정보: 조회수, 댓글 수, 좋아요 수, 싫어요 수
    # topicdetails로 가져오는 정보: 토픽
    part = 'snippet,statistics,topicDetails'
    url = 'https://www.googleapis.com/youtube/v3/videos?part={}&id={}&key={}'.format(part, video_id, config('GOOGLEAPIKEY'))
    response = urlopen(url).read().decode('utf-8')
    res_dict = json.loads(response).get('items')[0]    
    
    topic = []
    if res_dict.get('topicDetails'):
        topic_id = res_dict.get('topicDetails').get('topicIds')
        if topic_id:
            topic += topic_id
        relevant_topic_id = res_dict.get('topicDetails').get('relevantTopicIds')
        if relevant_topic_id:
            topic += relevant_topic_id
    
    topic = list(set(topic))
    
    topic_result = []
    for result in topic:
        topic_result.append(TOPICS.get(result))
    
    try:
        tags = ','.join(res_dict.get('snippet').get('tags'))
    except:
        tags = ''
    
    try:
        topic = ','.join(topic_result)
    except:
        topic = ''

    video = {
        'vno': video_id,
        'yno': res_dict.get('snippet').get('channelId'),
        'videoName': res_dict.get('snippet').get('title'),
        'videoDescription': res_dict.get('snippet').get('description'),
        'videoViewCount': res_dict.get('statistics').get('viewCount'),
        'videoCommentCount': res_dict.get('statistics').get('commentCount'),
        'good': res_dict.get('statistics').get('likeCount'),
        'bad': res_dict.get('statistics').get('dislikeCount'),
        'regDate': res_dict.get('snippet').get('publishedAt')[0:10], 
        'ycano': res_dict.get('snippet').get('categoryId'),
        'thumbnail': res_dict.get('snippet').get('thumbnails').get('high').get('url'),
        'tags': tags,
        'topic': topic,
    }
    
    # 파일 출력
    # PATH = 'videoTableTest.json'
    # with open("{}".format(PATH), 'w', encoding='utf-8-sig') as file: 
    #     json.dump(video, file, indent="\t", ensure_ascii=False)

    return video


print(make_video_table('2oP4ni2ojBU'))
