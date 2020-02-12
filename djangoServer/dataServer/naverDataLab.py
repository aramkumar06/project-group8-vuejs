import os
import sys
import urllib.request
from decouple import config
import json
from pprint import pprint
import datetime

def get_naver_data_lab(keyword):
    client_id = config("NAVER_DATALAB_CLIENT_ID")
    client_secret = config("NAVER_DATALAB_CLIENT_SECRET")
    url = "https://openapi.naver.com/v1/datalab/search";
    startDate = (datetime.datetime.utcnow() + datetime.timedelta(days=-365)).strftime("%Y-%m-%d")
    endDate = datetime.datetime.utcnow().strftime("%Y-%m-%d") 
    timeUnit = 'week'

    body = {
        "startDate": startDate,
        "endDate": endDate,
        "timeUnit": timeUnit,
        "keywordGroups": [
                {
                    "groupName": keyword, 
                    "keywords": [
                            keyword
                        ]
                }
            ]
    }

    body = str(body).replace("'", '\"')


    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    request.add_header("Content-Type","application/json")

    response = urllib.request.urlopen(request, data=body.encode("utf-8"))
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read().decode('utf-8')
        data = json.loads(response_body).get('results')[0].get('data') 
        result = json.dumps(data) # result를 DB data에 담는다.
        pprint(result)
    else:
        print("Error Code:" + rescode)
    return result