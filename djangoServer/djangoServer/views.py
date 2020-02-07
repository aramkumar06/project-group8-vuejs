from django.shortcuts import render, HttpResponse
import threading
from datetime import datetime 


class updateThread:
    def __init__(self):
        pass

    def threadOpen(self):
        # 업데이트 로직 넣으면 됨
        threading.Timer(86000, self.threadOpen).start()


############## 서버 켜짐과 동시에 자동 업데이트를 실행하는 로직 ##############
# updateStart = updateThread()
# updateStart.threadOpen()

