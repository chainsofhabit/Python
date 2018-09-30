"""
如果希望类的对象支持相应的运算符操作（例如：+,-,*,/,>,<等）就必须实现相应的魔法方法
+:__add__(self, other):
>:__gt__
"""

"""
一般情况需要对>或者<进行重载，重载后可以通过sort方法直接对对象的列表进行排序
"""


# class Student:
#     def __init__(self,name = "",age = 0,score = 0):
#         self.name = name
#         self.age = age
#         self.score = score
#     #self:+前面的对象
#     #other：+后面的对象
#     def __add__(self, other):
#         return self.score + other.score
#
# class Schoolchild(Student):
#     pass
#
#     #重载 > 符号
#     #注意：重载>或<可以只重载一个，另外一个对应的功能自动取反
#     def __gt__(self, other):
#         return self.age > other.age
#     #重写魔法方法__str__用来定制对象的打印样式
#     def __str__(self):
#         return "Student:%s %d %d " % (self.name,self.age,self.score)
#
# stu1 = Schoolchild("小命",19,90)
# stu2 = Schoolchild("阿猪",26,60)
# stu3 = Schoolchild("阿强",29,70)
# all_students = [stu1,stu2,stu3]
# all_students.sort()
# for stu in all_students:
#     print(stu.name,stu.age,stu.score)
#
#
# print(stu1 + stu2)
# print(stu1 < stu2)
# print(stu1 > stu2)
#
# c1 = Schoolchild("小咻咻",9,90)
# c2 = Schoolchild("啾啾",8,80)
# print(c1 + c2)

class Student:
    def __init__(self, name='', age=0, score=0):
        self.name = name
        self.age = age
        self.score = score

    # self：+前面的对象
    # other: +后面的对象
    def __add__(self, other):
        return self.score + other.score

    # 重载 > 符号
    # 注意：重载>和<可以只重载一个，另外一个对应的功能自动取反
    def __gt__(self, other):
        return self.age > other.age

    # 重写魔法方法__str__，用来定制对象的打印样式
    def __str__(self):
        # return '<%s.%s object at 0x%x>' % (self.__module__, self.__class__.__name__, id(self))
        # return 'Student: %s %d %d' % (self.name, self.age, self.score)
        return str(self.__dict__)[1:-1]

class Schoolchild(Student):
    def __add__(self, other):
        return self.age + other.age


if __name__ == '__main__':

    stu1 = Student('小明', 18, 90)
    stu2 = Student('老王', 29, 84)
    stu3 = Student('小花', 20, 78)

    print(stu1)

    all_students = [stu1, stu2, stu3]
    all_students.sort(reverse=True)
    for stu in all_students:
        print(stu.name, stu.age, stu.score)

    print(stu1 > stu2)
    print(stu1 < stu2)
    print(stu1 + stu2)
    print(stu3 > stu1)

    # 父类重载了运算符，子类也能用
    c1 = Schoolchild('小明明', 8, 70)
    c2 = Schoolchild('小花花', 10, 67)
    print(c1+c2)