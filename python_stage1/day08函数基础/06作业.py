#1编写一个函数，求1+2+3+....+N
# def func1():
#     count = 0
#     for x in range(1,N+1):
#         count += x
#     print(count)
# N = int(input('输入一个整数N:'))
# func1()

#2.编写一个函数，求多个数中的最大值
# def func2(*num):
#     a = 0
#     for item in num:
#         if a < item:
#             a=item
#     print('最大值为：%d' % a)
# func2(10,9,50,30,20,121)


#3.编写一个函数，实现摇色子的功能，打印n个色子的点数和
# import random
# def func3():
#     count = 0
#     n = int(input('几个色子点数相加:'))
#     for x in range(n):
#         point = random.randint(1,6)
#         count += point
#     print('%d个色子点数相加的和为：%d' % (n,count))
# func3()

#4.编写一个函数，交换指定字典的key和value 例如：{'a':1,'b':2,'c':3}----
def exchange(dict1):
    dict2 = {}
    for x in dict1:
        dict2[dict1[x]] = x
    return dict2
dict1 = {'a':1,'b':2,'c':3}
print(exchange(dict1))
#5.编写一个函数，求三个数中的最大值
def func5(*nums):
    a = 0
    for item in nums:
        if a < item:
            a=item
    print('最大值为：%d' % a)

func5(10,90,45)


#6.编写一个函数，提取指定字符串中的所有的字母，然后拼接在一起后打印出来
#例如:'12a@bc$%1d--'---->打印'abcd'

def get_str(str1):
    new_str = ''
    for item in range(len(str1)):
        if str1[item].isalpha():
            new_str += str1[item]
    return new_str


print(get_str('12a@bc$%1d--'))

#7.写一个函数，求多个数的平均值
def average(*number):
    count = 0
    for item in number:
        count += item
    avg = count/(len(number))
    print('平均值为：%.2f' % avg)
average(10,89,12)

#8写一个函数，默认值求10的阶乘，也可以求其他数的阶乘

def factorial(a = 10):
    count = 1
    for x in range(1,a+1):
        count *= x
    print('阶乘为：%d' % count)
factorial(5)

#9.写一个函数可以对多个数进行不同的运算
"""
例如：operation('+',1,2,3)---> 求1+2+3的结果
      operation('-',10,9)---> 求10-9的结果
      operation('*',2,4,8，10)---> 求2*4*8*10的结
"""
