import threading
import time

# time.sleep() # 시간을 지연시킬 수 있는 코드


########## thread process first example
#######################################
# class firstThread:
#     def __init__(self):
#         pass
    
#     def firstThread(self):
#         print('firstThread')
#         threading.Timer(2, self.firstThread).start()
        
        
#     def secondThread(self):
#         print('secondThread')
#         threading.Timer(4, self.secondThread).start()

        
# if __name__ == '__main__':
#     obj = firstThread()
#     obj.firstThread()
#     obj.secondThread()
#######################################


########## thread process second example
########################################
class firstThread:
    def __init__(self):
        pass
    
    def firstThread(self):
        print('firstThread')
        threading.Timer(2, self.firstThread).start()
        
        
    def secondThread(self):
        print('secondThread')
        threading.Timer(4, self.secondThread).start()

        
if __name__ == '__main__':
    obj = firstThread()
    obj.firstThread()
    obj.secondThread()
########################################


