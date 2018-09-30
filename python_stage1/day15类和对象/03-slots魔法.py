class Person:
    #通过solts中存的元素的属性的值来约束当前这个类的对象的属性
    #对象的属性只能比元组中的元素少，不能多

    __slots__ = ("name","age","face")
    def __init__(self):
        self.name = "张三"
        self.age = 20
        self.face = 70
        #self.sex = "boy"   #__slots__中并没有sex

p1 = Person()
# p1.sex = "girl"
# print(p1.sex)
#
# p1.name = "小明"
print(p1.name)

#注意，一旦在类中给__slots__属性赋了值，那么这个类的对象的
# __dict__属性就不能用了