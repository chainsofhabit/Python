from threading import Thread
import time
from datetime import datetime
from random import randint
#在两个子线程中下载两个电影，在主线程中统计两个电影下载的总的时间
#如果希望两个线程结束后才执行某个操作，就用那个线程调用join方法
class DownloadThread(Thread):
    def __init__(self,file):
        super().__init__()
        self.file = file
    def run(self):
        print(self.file+"开始下载:",datetime.now())
        time.sleep(randint(5,15))
        print(self.file+"下载结束:",datetime.now())
t1 = DownloadThread("钢铁侠")
t2 = DownloadThread("金刚狼")
start = time.time()

tim1 = t1.start()
tim2 = t2.start()

#系统t1和t2中的代码都结束后才执行下面的代码
t1.join()   #这句代码在t1的线程结束后才执行
t2.join()
end = time.time()
print(end-start)
