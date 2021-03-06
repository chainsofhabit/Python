# 1.定义一个学生类。有属性：姓名、年龄、成绩（语文，数学，英语)[每课成绩的类型为整数]
# 方法： a. 获取学生的姓名：getname() b. 获取学生的年龄：getage()
# c. 返回3门科目中最高的分数。get_course()

import math

class Student:
    def __init__(self,name,age):
        self.course = []
        self.name = name
        self.age = age

    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_course(self):
        if not self.course:
            return False
        return max(self.course)
stu1 = Student("咻咻",21)
stu1.course = [80,90,85]
print("姓名:",stu1.get_name())
print("年龄:",stu1.get_age())
print("最高分:",stu1.get_course())


# 2.建立一个汽车类Auto，包括轮胎个数，汽车颜色，车身重量，速度等成员变量，
# 并通过不同的构造方法创建实例。至少要求 汽车能够加速 减速 停车。
# 再定义一个小汽车类CarAuto 继承Auto 并添加空调、CD等成员变量 覆盖加速 减速的方法
class Auto:
    def __init__(self,tire_num,color,weight,speed):
        self.tire_num = tire_num
        self.color = color
        self.weight = weight
        self.speed = speed
    def speed_up(self):
        print("加速")
    def slow_down(self):
        print("减速")
    def stop(self):
        print("停车")

    def __str__(self):
        return str(self.__dict__)[1:-1]
class CarAuto(Auto):
    def speed_up(self):
        print("覆盖加速")
    def slow_down(self):
        print("播放CD:我是隔壁的泰山")
car1 = Auto(4,"白色","2.0t","90Km")
print(car1)
car1.speed_up()
car1.slow_down()
car1.stop()

car2 = CarAuto(4,"黑色","1.5t","100km")
print(car2)
car2.speed_up()
car2.slow_down()
car2.stop()

# 3.创建一个名为User 的类，其中包含属性firstname 和lastname ，还有用户简介通常会存储的其他几个属性。
# 在类User 中定义一个名 为describeuser() 的方法，
# 它打印用户信息摘要;再定义一个名为greetuser() 的方法，它向用户发出个性化的问候。
class User:
    def __init__(self,first_name,last_name,sex,age,height):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.age = age
        self.height = height
    def describe_user(self):
        print("姓:%s,名:%s,性别:%s,年龄:%d,身高：%.f" % (self.last_name,self.first_name,self.sex,self.age,self.height))
    def greet_user(self):
        print("Hello,%s%s,天天开心" % (self.last_name,self.first_name))
user1 = User("子熙","王","男",7,140)
user1.describe_user()
user1.greet_user()

# 管理员是一种特殊的用户。编写一个名为Admin 的类，让它继承User类。添加一个名为privileges 的属性，
# 用于存储一个由字符串(如"can add post"、"can delete post"、"can ban user"等)组成的列表。
# 编写一个名为show_privileges()的方法，它显示管理员的权限。创建一个Admin 实例，并调用这个方法。
class Admin(User):
    def __init__(self,first_name,last_name,sex,age,height):
        super().__init__(first_name,last_name,sex,age,height)
        self.privileges = ["can add post","can delete post","can ban user"]
    def show_privileges(self):
        print(self.privileges)
user2 = Admin("子熙","王","男",7,140)
user2.show_privileges()

#4.创建一个Person类，添加一个类字段用来统计Perosn类的对象的个数
class Person:
    count = 0
    def __init__(self,name):
        Person.count += 1
        self.name = name

    @classmethod
    def number(cls):
        return cls.count
p1 = Person("Tom")
p2 = Person("Jerry")
p3 = Person("Haha")
print(Person.count)


# 5.写一个类，其功能是：1.解析指定的歌词文件的内容 2.按时间显示歌词
# 提示：歌词文件的内容一般是按下面的格式进行存储的。
# 歌词前面对应的是时间，在对应的时间点可以显示对应的歌词






