#练习，写一个Person类，拥有属性name,age,sex,要求创建Person对象的时候必须给name和age赋值，sex可赋可不赋
  #再写一个Staff类继承自Person类，要求保留Person中所有的属性，并且添加新的属性salary
  #要求创建Staff类对象的时候，只能给name赋值（必须赋）

class Person:
    def __init__(self,name,age,sex = "girl"):
        self.name = name
        self.age = age
        self.sex = sex
class Staff(Person):
    def __init__(self,name):
        super().__init__(name,20)
        self.salary = 8000
p1 = Person("秀秀",21)
p2 = Person("啾啾",23,"男")

s1 = Staff("咻咻")