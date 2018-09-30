from threading import Thread
import datetime
import time
from random import randint
"""
面向对象实现多线程技术
1.声明一个类，继承自Thread类
2.重写run方法，将需要在子线程中执行的任务放到run方法中
3.在需要子线程的位置去创建这个类的对象，然后用对象调用start方法
"""


class DownloadThread(Thread):
    def __init__(self,file):
        super().__init__()
        self.file = file

    def run(self):
        print(self.file+"开始下载:",datetime.datetime.now())
        time.sleep(randint(5,10))
        print(self.file+"下载结束:",datetime.datetime.now())
print("======")
t1 = DownloadThread("水形物语")
t1.start()
print("++++++")


