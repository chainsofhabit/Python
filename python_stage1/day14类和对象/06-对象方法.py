"""
对象方法：
a.什么样的方法是对象方法：直接声明在类中的函数默认是对象方法，有一个默认参数self
b.对象方法要通过对象来调用：对象.对象方法()
c.对象方法中默认参数self，不需要传参。因为在调用这个方法的时候，系统会自动将当前对象传给self
那个对象调用的方法，self就指向谁

"""
import math

class Circle:
    def __init__(self,radius1):
        self.radius = radius1
    #声明了一个对象方法area
    #在这self就是调用area方法的对象，对象能做的事情，self都能做
    def area(self):
        # print(id(self))
        # print("求圆的面积")
        return math.pi *(self.radius ** 2)

#写一个矩形类，有长和宽，有两个功能，求面积和周长

class Rect:
    def __init__(self,length1,width1):
        self.length = length1
        self.width = width1
    def area(self):
        return self.length * self.width
    def meter(self):
        return 2*(self.length + self.width)

#写一个班级类，班级里有多个学生的成绩（一门），可以获取班级成绩里的最高分

class PythonClass:
    def __init__(self,name):
        self.grade = []
        self.name = name
    # def __init__(self,class_name1,*grade1):
    #     self.class_name = class_name1
    #     self.grade = grade1
    def max_grade(self):
        if not self.grade:
            return 0
        return max(self.grade)

c1 = Circle(3)
print(c1.radius)
print("c1的面积：",c1.area())

#创建一个半径是5的圆的对象

c2 = Circle(5)
print("c2的面积：",c2.area())

r1 = Rect(4,5)
print("r1的面积：",r1.area())
print("r1的周长:",r1.meter())


# c3 = PythonClass("Python1806",89,70,60,90,94,92)
c3 = PythonClass("Python1806")
c3.grade = [89,70,60,90,94,92]
print(c3.max_grade())

