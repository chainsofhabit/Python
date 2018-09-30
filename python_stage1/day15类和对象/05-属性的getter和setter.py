"""
保护类型的属性：
a.就是在声明对象属性的时候在属性名前加一个下划线来代表这个属性是受保护的属性
那么以后访问这个属性的时候就不要直接访问，要通过getter来获取这个属性的值
setter来给这个属性赋值
b.如果一个属性已经声明成保护类型的属性，
那么我们就需要给这个属性添加getter,也可以添加setter

2.添加getter
添加getter其实就是声明一个没有返回值的函数
a.声明的格式:
@property
def 去掉下划线的属性名(self)
    函数体
    将属性相关的值返回
b.使用场景
1.如果想要获取对象的某个属性的值前，想要再做点别的事情，就可以给这个属性添加getter
2.想要拿到某个属性被使用的时刻
3.添加setter
添加setter就是声明一个有一个参数但是没有返回值的函数，作用是给属性赋值
格式

"""
class Car:
    def __init__(self):
        self.color = "黄色"
        self.type = "自行车"
        #_price是保护类型
        self._price = 1000
    #给_price属性添加getter
    @property
    def price(self):
        print("保护属性")
        return self._price/1000

    #想要给一个属性添加setter必须先给这个属性添加getter
    @price.setter
    def price(self,price):
        if isinstance(price,int) or isinstance(price,float):
            self._price = price
        else:
            self.price = 0

#练习，声明一个员工类，其中有一个属性是是否已婚(bool)，
# 获取值之前根据存的值返回“已婚/未婚”
class Staff:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self._is_married = False

    @property
    def is_married(self):
        if self._is_married:
            return "已婚"
        else:
            return "未婚"
    @is_married.setter
    def is_married(self,married):
        self._is_married = married
staff1 = Staff("咻咻",23)
print(staff1.is_married)

staff1.is_married = True
print(staff1.is_married)





car1 = Car()
print(car1.color,car1._price)
#添加完getter后就通过getter去获取属性的值
#price就是_price的getter
print(car1.price,"k")  #实质是在调用getter对应的方法
#通过setter给_price属性赋值，实质是在调用setter对应的方法
car1.price = 3000
print(car1.price)

car1.price = "asc"
print(car1.price)