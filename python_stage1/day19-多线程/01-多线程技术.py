import threading
import datetime
import time
"""
1.主线程
每个进程默认都会有一个线程，这个线程我们一般叫它主线程
默认情况下，所有的代码都是在主线程中执行
2.子线程
一个进程中可以有多个线程，除了主线程以外，其他的线程需要手动的添加

3.threading是python中的内置模块，用来支持多线程
Thread类的对象就是线程对象，需要线程的时候，就创建这个类或者这个类的子类对象
"""
def download(file):
    print("开始下载",datetime.datetime.now())
    time.sleep(5)
    print(file+"下载结束:",datetime.datetime.now())


# print("主线程中的代码")
# #1.在线程中下载两个电影
# download("速度与激情")
# download("沉默的羔羊")
print(threading.currentThread())

#2.在两个子线程中去下载电影
"""
Thread(target,args)
target:需要在子线程中调用的函数的函数名
args:函数的实参
返回值:创建好的线程对象

"""
t1 = threading.Thread(target=download,args=("速度与激情",))

#开始执行t1对应的线程中的任务
t1.start()

t2 = threading.Thread(target=download,args=("哆啦A梦",))
#想要在子线程中执行任务，必须通过线程对象调用start方法才行
t2.start()
print("==========")