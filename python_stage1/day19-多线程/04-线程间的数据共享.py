"""
模拟多个人对同一个账号进行操作
同步锁(RLock)和互斥锁（Lock）
"""
import time
from threading import Thread,Lock,RLock
class Account:
    """账号类"""
    def __init__(self,balance):
        #余额
        self.balance = balance
        #创建锁对象
        self.lock = Lock()



    #存钱的过程：读出原来的余额，确定钱的一系列操作，
    # 将原来的余额加上存的数额，产生最新的余额再保存
    def save_money(self,amount):

        print("开始存钱")
        #加锁
        self.lock.acquire()
        #获取原来的余额
        old_amount = self.balance
        #模拟时间消耗
        time.sleep(5)
        #修改余额
        self.balance = old_amount + amount
        print("存钱成功,余额：",self.balance)

        #解锁
        self.lock.release()

        #取钱
    def get_money(self,amount):
        print("开始取钱")
        self.lock.acquire()
        old_amount = self.balance
        if old_amount < amount:
            print("余额不足！")
            return
        time.sleep(5)
        self.balance = old_amount - amount
        print("取钱成功，余额：",self.balance)
        self.lock.release()
    def show_balance(self):
        print("当前余额为：",self.balance)

#创建账号
account = Account(1000)
account.show_balance()
# account.save_money(200)
# account.get_money(100)
"""
当多个线程同时对一个数据进行操作的时候，可能会出现数据混乱的问题
"""

t1 = Thread(target=account.save_money,args=(200,))
t2 = Thread(target=account.save_money,args=(1300,))
t3 = Thread(target=account.get_money,args=(800,))
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
account.show_balance()


