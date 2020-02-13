import requests
import json
from bs4 import BeautifulSoup as bs


def get_trend(channel_id):
    trends = []
    str_date = '2020-01-15'
    url = 'https://en.noxinfluencer.com/api/youtube/detail/dimension/?channelId=' + channel_id + '&&startDate=' + str_date
    r = requests.get(url)
    html = json.loads(r.text)['retData']['dom']
    if json.loads(r.text)['errorNum'] != 0:
        print('errer')
        return trends
    soup = bs(html, "html.parser", from_encoding='utf-8')
    ul_list = soup.findAll('ul')
    for idx in range(1, len(ul_list) - 1):
        data = {}
        li_list = ul_list[idx].findAll('li')
        for (i, li) in enumerate(li_list):
            if i == 0:
                data['recordDate'] = li.text
            elif i == 1:
                span_list = li.findAll('span')
                if len(span_list) == 1:
                    data['pointSubscriber'] = get_real_value(span_list[0].text)
                    data['difSubscriber'] = 0
                else:
                    data['pointSubscriber'] = get_real_value(span_list[0].text)
                    data['difSubscriber'] = get_real_value(span_list[1].text)
            elif i == 2:
                span_list = li.findAll('span')
                if len(span_list) == 1:
                    data['pointView'] = get_real_value(span_list[0].text)
                    data['difView'] = 0
                else:
                    data['pointView'] = get_real_value(span_list[0].text)
                    data['difView'] = get_real_value(span_list[1].text)
                break
        trends.append(data)
    return trends


def get_real_value(txt):
    txt = txt.strip()
    value = 0
    if txt.isdigit():
        value = int(txt)
    if txt[len(txt) - 1] == 'M':
        value = float(txt.strip()[:-1]) * 1000000
    elif txt[len(txt) - 1] == 'K':
        value = float(txt.strip()[:-1]) * 1000
    return round(value)
