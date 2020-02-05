import json
import copy
from selenium import webdriver


def get_growth(channel_id, yno):
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko")
    driver = webdriver.Chrome('./chromedriver', options=options)

    url = 'https://socialblade.com/youtube/channel/' + channel_id + '/monthly'
    driver.get(url)
    el = '//*[@id="socialblade-user-content"]'
    content = driver.find_element_by_xpath(el).text.split('\n')
    cnt = 0
    flag = False
    pk = 0
    orm = []
    data = dict()
    data['yno'] = yno
    for line in content:
        if line == 'ESTIMATED EARNINGS':
            flag = True
            continue
        elif line == 'Daily Averages':
            break
        if flag:
            if cnt == 1:
                cnt += 1
                continue
            if cnt == 6:
                fin = dict()
                fin['pk'] = pk
                pk += 1
                fin['model'] = "dataServer.growth"
                fin['fields'] = data
                print(fin)
                temp = copy.deepcopy(fin)
                orm.append(temp)
                cnt = 0
                continue
            elif cnt == 0:
                data['recordDate'] = line
                cnt += 1
            else:
                x = line.replace('+', "").replace(",", "").replace('--', '0').replace('LIVE', '')
                total_stars = 0
                if 'K' in x:
                    if len(x) > 1:
                        total_stars = float(x.replace('K', '')) * 1000  # convert k to a thousand
                elif 'M' in x:
                    if len(x) > 1:
                        total_stars = float(x.replace('M', '')) * 1000000  # convert M to a million
                else:
                    total_stars = int(x)  # Less than 1000
                if cnt == 2:
                    data['difSubscriber'] = int(total_stars)
                elif cnt == 3:
                    data['pointSubscriber'] = int(total_stars)
                elif cnt == 4:
                    data['difView'] = int(total_stars)
                elif cnt == 5:
                    data['pointView'] = int(total_stars)
                cnt += 1
    print(orm)
    print(json.dumps(orm, ensure_ascii=False, indent="\t"))
    driver.close()


if __name__ == '__main__':
    get_growth('UChQ-VMvdGrYZxviQVMTJOHg')
