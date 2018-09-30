#1.声明一个电脑类: 属性:品牌、颜色、内存    方法:打游戏、写代码、看视频
class Computer:
    def __init__(self,brand = "华硕",color = "黑色",memory = 256):
        self.brand = brand
        self.color = color
        self.memory = memory
    @classmethod
    def play_game(cls):
        print("打游戏")
    @classmethod
    def write_code(cls):
        print("写代码")
    @classmethod
    def see_video(cls):
        print("看视频")
com1 = Computer()
print("品牌:%s,颜色:%s,内存:%s" % (com1.brand,com1.color,com1.memory))
# 方法a 获取
print("品牌：%s" % com1.brand)
# 修改
com1.color = "银色"
print("颜色：%s" % com1.color)
#添加
com1.run_memory = "8G"
print("运行内存:%s" % com1.run_memory)
#删除
del com1.memory
#方法b获取
print(getattr(com1,"brand"))
#修改
setattr(com1,"brand","戴尔")
print("品牌:%s" % com1.brand)
#添加
setattr(com1,"screen_size",15.6)
print("屏幕大小:%s" % com1.screen_size)
#删除
delattr(com1,"run_memory")
com1.play_game()
com1.write_code()
com1.see_video()


#2.声明一个人的类和狗的类：
# 狗的属性：名字、颜色、年龄 狗的方法：叫唤
# 人的属性：名字、年龄、狗  人的方法：遛狗
# a.创建人的对象小明，让他拥有一条狗大黄，然后让小明去遛大黄

class Person:
    def __init__(self,name,age,dog):
        self.name = name
        self.age = age
        self.dog = dog
    @classmethod
    def walk_dog(cls):
        tc = cls()
        tc.walk_dog()
class Dog:
    def __init__(self,name,color,age):
        self.name = name
        self.color = color
        self.age = age
    @classmethod
    def dogs(cls):
        print("汪 汪汪")

p1 = Person("小明",20,"大黄")
dog1 = Dog("大黄","黄色",3)

print("{}在遛{}".format(p1.name,p1.dog))
dog1.dogs()

# 3.声明一个矩形类：
# 属性：长、宽  方法：计算周长和面积
# a.创建不同的矩形，并且打印其周长和面积
class Rect:
    def __init__(self,length1,width1):
        self.length = length1
        self.width = width1
    def area(self):
        return self.length * self.width
    def meter(self):
        return 2*(self.length + self.width)

r1 = Rect(4,5)
print("r1的面积：",r1.area())
print("r1的周长:",r1.meter())

r2 = Rect(7,8)
print("r2的面积：",r2.area())
print("r2的周长:",r2.meter())
#
#
# 4.创建一个学生类：
# 属性：姓名，年龄，学号 方法：答到，展示学生信息
# 创建一个班级类：
# 属性：学生，班级名 方法：添加学生，删除学生，点名

class Student:
    def __init__(self,name,age,id):
        self.name = name
        self.age = age
        self.id = id
    def answer(self):
        print("%s:到" % self.name)
    def show(self):
        print("姓名：%s,年龄:%d,学号:%s" % (self.name,self.age,self.id))
class PythonClass:
    def __init__(self,class_name):
        self.class_name = class_name
        self.students = []
    def add_student(self,student):
        self.students.append(student)






