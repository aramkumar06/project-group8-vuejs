#############################
# 이 파일은 URL만으로 유튜버의 정보를 가져오는 로직을 만들기 위해 준비하는 코드입니다.
#############################

from urllib.request import urlopen
from bs4 import BeautifulSoup
from decouple import config
import json
import sys
import io
import useAPI


sys.stdin = open('test.txt')

################## functions


##################


# 1. 유튜버의 URL을 입력 받는다.
URL = input()

# 2. URL을 기반으로 유튜버가 누군지 알아내고 관련 정보를 모두 가져온다.
channelID = useAPI.get_channelID_from_URL(URL)

# 2-1. API키가 만료되었을 때 바꿀 수 있도록 만든다.
# 3. JSON으로 저장한다. or DB에 저장한다.
# 4. 업데이트한다.
# 4-1. 기존에 있던 유튜버들을 검사해서 기존에 없던 동영상이 들어왔을 경우 새로 추가한다.
# 4-2. 유튜버의 URL만을 받고도 처리가 되도록 만든다.
# 4-3. 만약 유튜버의 구독자 수가 만 명 미만이라면 추가를 진행하지 않는다.