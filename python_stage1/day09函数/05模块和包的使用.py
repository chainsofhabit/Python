
"""
封装：
函数：对实现某一特定功能的代码段的封装
模块：对变量，函数，类进行封装
模块：一个py文件就是一个模块
"""
# def multipy(*numbers):
#     sum1 = 1
#     for item in numbers:
#         sum1 *= item
#     return sum1
# print(multipy(1,2,5))
"""
1.怎么使用其他模块的内容
a. import 模块
通过模块.内容的形式去使用模块中的内容（能够使用的是全局变量，函数，类）
b. from 模块 import 模块中的内容
可以直接使用模块中的内容

c.from 模块  import * ---->
"""
#导入系统的math模块
# import math

#导入自定义的my_list模块
# a.
import my_list
#使用模块中的全局变量
print(my_list.empty)
num = my_list.count([1,2,3,4,3,1,3])
print(num)
from my_list import count
print(count([1,2,3,4,3,1,3]))

#c.
from math import *
print(pi)
print(sqrt(4))

"""
2.重命名
import 模块 as 新名字
from 模块 import 内容 as 新名字 
"""

import random as RAN
print(RAN.randint(1,10))

from datetime import date as DateClass
print(DateClass.today())

"""
每个模块都有一个__name__属性，这个属性的值默认就是当前模块的文件名
当当前模块正在被执行（直接在当前这个模块中点了run）的时候__name__属性的值是'__main__'
在一个模块中将不希望被其他模块导入的代码写在if __name__=='__main__'中
建议：函数的声明，类的声明一般写在if的外面，其他的写在if 的里面（想要被外部使用的全局变量也可以写在外面）

"""
# import my_model
# from my_model import func1()
# print(func1)

