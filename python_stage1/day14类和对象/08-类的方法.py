"""
类中的方法：
1.对象方法（实例方法）
声明的形式：直接声明在类中
特点：自带一个不需要主动传参的默认参数self,谁来调用指向谁
调用：通过对象来调用
2.类方法
声明的形式:声明方法前需要使用@classmethod说明
特点：自带一个默认参数cls这个参数调用的时候不需要传值，系统自动传，谁调用指向谁,始终指向当前类

调用：通过类来调用 ---> 类.类方法()
3.静态方法
声明的形式：声明方法前需要使用@staticmethod说明
特点：没有默认参数
调用：通过类来调用 --->类.静态方法()



"""

class Class1:
    number = 1000
    #对象方法
    def object_func(self):
        print("对象方法")
    #声明类方法
    @classmethod
    def class_func(cls):
        print("cls:",cls.number)
        tc = cls()
        tc.object_func()
        print("类方法")
    #静态方法
    @staticmethod
    def static_func():
        print("静态方法")

c1 = Class1()
c1.object_func()
print(Class1.number)

Class1.class_func()
#调用静态方法
Class1.static_func()

"""
4.遇到问题怎么来选择使用哪种方法：
a.只要实现方法的功能需要用到对象的属性，我们就使用对象方法，否则就使用静态方法或类方法
b.不使用对象方法的前提下，如果实现功能需要用到类的字段就使用类方法
c.实现功能既不需要对象的属性，又不需要类的字段就用静态方法
注意：静态方法和类方法划分不用那么严格，静态方法能做的可以做，反之亦然
"""

class Person:
    number2 = 250
    @classmethod #类方法
    def show_number2(cls):
        print("人类的数量是:%d亿" % cls.number2)

    @staticmethod #静态方法
    def show_number3():
        print("人类的数量:%d亿" % Person.number2)
Person.show_number2()
Person.show_number3()