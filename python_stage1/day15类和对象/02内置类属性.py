"""
内置类属性就是魔法属性
魔法属性:属性名的前面和后面都有两个下划线
魔法方法：方法的前面和后面都有两个下划线
"""
import datetime
class Person:
    """人类"""
    number = 61  #类的字段
    def __init__(self,name1,age1,height1):
        self.name = name1
        self.age = age1
        self.height = height1
    def run(self):
        print("%s在跑步" % self.name)
    #类方法
    @classmethod
    def show_number(cls):
        print("人类的数量为:%亿" % cls.number)

    #静态方法
    @staticmethod
    def destroy():
        print("人类在破坏环境")
p1 = Person("张三",25,175)
#1.__name__属性
name = Person.__name__
print(name,type(name))

#2.___classs__属性
#对象的属性，
#my_class是一个类，之前类能做的事他都能做
my_class = p1.__class__
p2 = my_class("小明",20,175)

#__dict__属性---将对象属性及其对应的值装换成键值对存到一个字典中

print((Person.__dict__))
#4.__doc__属性--->获取类的说明文档
#类的属性
doc= Person.__doc__
print(doc)

#5.__module__属性---获取类所在的模块对应的名字
print(Person.__module__)
print(datetime.datetime.__module__)

#6.__base__属性  --获取当前类的父类
print(Person.__bases__)

