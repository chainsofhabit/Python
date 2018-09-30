"""
类中的内容：属性和方法
1.属性(保存值的)：
a.对象的属性:不同的对象，对应的值可能不一样，这样的属性是对象属性
类中的对象属性是声明在init方法中的，并且声明格式是：self.属性名 = 初值
对象属性的使用：对象.属性名

b.类的字段：属于类的，所有的对象对应的值是一样的
2.方法（保存功能的）：
a.对象方法
b.类方法
c.静态方法
"""

class Student:
    """学生类"""
    def __init__(self):
        #声明对象属性name,age,id
        self.name = "张山"
        self.age = "18"
        self.id = "001"

class Dog:
    """狗类"""
    def __init__(self,type1,color1):  #type1,color1形参
        self.type = type1
        self.color = color1

class Computer:
    def __init__(self,color = "白色",memory = 1000):
        self.color = color
        self.memory = memory
if __name__ == '__main__':
    stu1 = Student()
    print(stu1.name,stu1.age,stu1.id)

    #通过对象去修改对象的属性
    stu1.name = "江有才"
    print(stu1.name)

    dog1 = Dog("中华田园犬","黄色")
    print(dog1.type,dog1.color)


    comp1 = Computer()
    print(comp1.color,comp1.memory)
    comp2 = Computer("黑色",1024)
    print(comp2.color,comp2.memory)


#写一个矩形类，拥有属性长和宽
class Rect:
    def __init__(self,lenth,width):
        self.lenth = lenth
        self.width = width
