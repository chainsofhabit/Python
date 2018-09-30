#1电脑类
class Computer:
    def __init__(self,brand = "华硕",color = "黑色",memory = 256):
        self.brand = brand
        self.color = color
        self.memory = memory
    @staticmethod
    def play_game(game):
        print("玩 %s" % game)
    @staticmethod
    def code():
        print("写Pyhton代码")
    @staticmethod
    def watch_video(video):
        print("在看%s" % video)
com1 = Computer(memory=256)
#查
print(com1.color)
print(getattr(com1,"color","银色"))
#改
com1.brand = "华硕"
setattr(com1,"brand","戴尔")
#增
com1.size = 15.6
print(com1.size)
#删
del com1.size
delattr(com1,"memory")


#=========2.人和狗============

class Dog:
    """狗"""
    def __init__(self,name = "",color = "",age = ""):
        self.name = name
        self.color = color
        self.age = age

    def shout(self):
        print("%s在汪汪叫" % self.name)

class Person:
    """人"""
    def __init__(self,name = "",age = 0):
        self.name = name
        self.age = age
        self.dog = None

    def took_dog(self):
        #遛狗的前提判断有没有狗
        if not self.dog:
            print("没有狗，自己遛遛")
            return
        print("%s牵着%s在玩" % (self.name,self.dog.name))
p1 = Person("小明")
p1.dog = Dog("大黄","黄色",2)
p1.took_dog()

#============学生和班级===========
class Student:
    def __init__(self,name,age,id = ""):
        self.name = name
        self.age = age
        self.id = id
    def response(self):
        print("%s,到!" % self.name)
    def show_info(self):
        print("姓名：%s 年龄：%d 学号：%s" % (self.name,self.age,self.id))


class Class:
    def __init__(self,name):
        self.students = []
        self.name = name
        self.__count = 0

    def add_student(self):
        name = input("姓名：")
        age = input("年龄：")

        #学号
        self.__count += 1
        id = "py" + str(self.__count).rjust(3,"0")
        #创建学生对象
        stu = Student(name,int(age),id)

        #将学生保存到班级
        self.students.append(stu)

    def del_student(self):
        """删除学生"""
        del_name = input("输入想要删除的学生姓名：")
        is_del = False
        #遍历列表拿到学生对象
        for stu in self.students:
            if stu.name == del_name:
                self.students.remove(stu)
                print("删除成功!")
                is_del = True
        if not is_del:
            print("没有该学生!")
    def call_names(self):
        for stu in self.students:
            print(stu.name)
            stu.response()
class1 = Class("python1806")
for _ in range(5):
    class1.add_student()
class1.del_student()
class1.call_names()


#==============4.数学类=========
class Math:
    pi = 3.141159265358
    e = 2.7182818284
    @staticmethod
    def sum_double(self,num1,num2):
        return num1 + num2
    @classmethod
    def circle_area(cls,r):
        return cls.pi *r**2
