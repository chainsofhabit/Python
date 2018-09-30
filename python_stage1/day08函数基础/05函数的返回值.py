"""
1.返回值：函数的返回值就是return关键字后面的表达式的值，就是函数调用表达式的结果
2.python中所有的函数都有返回值，默认是None（没有return）
说明:
a.如果函数体中没有return，函数的返回值就是None
b.调用函数的语句就是函数调用表达式
"""

#写一个函数，打印'hello'
#1.没有return

def func1():
    print('hello')

#声明一个变量re来保存函数调用后的结果
#func1()
re = func1()
print(re)

#2.return关键字（return只能写在函数体中）
"""
a.确定返回值
b.结束函数（函数中只要遇到return，函数就直接结束）
c.单独的return相当于return None
"""
def func2(n):
    print(n)
    return 100
    print('=====')
re = func2(10)
print(re)


def func3():
    if False:
        return 20
print(func3())

"""
注意，看一个函数的返回值是多少，不是看函数中有没有return，而是看函数的执行过程中有没有遇到return
遇到了才是return后面的结果，否则就是None
"""

#练习：写一个函数，判断一个数是否是偶数，如果是返回True,否则返回False

def func4(x):

    if x % 2 ==0:
        return True
    else:
        return False
x = int(input('输入一个整数:'))
print(func4(x))



"""
什么时候函数需要返回值：只要实现函数的功能会产生新的数据，就通过返回值将新的数据返回
而不是打印他
"""
#练习：
#1. 写一个函数，统计一个列表中浮点数的个数
def count_of_float(list1):
    count = 0
    for item in list1:
        if isinstance(item,float):
            count += 1
    return count
result = count_of_float([3.14,True,4.0,90])
print(re)
#2.写一个函数，将一个数字列表中所有的元素的值都变成原来的2倍
def double_list(list2):
    for index in range(len(list2)):
        list2[index] *= 2
    return list2
# list2 = [1,2,34,56]
# double_list(list2)
# print(list2)

result = double_list([3,4,5,6])
print(result)
#3.写一个函数，获取指定元素对应的下标
def indexs(list4:list,item):
    index_list = []
    for index in range(len(list4)):
        if list4[index] == item:
            index_list.append(index)
    return index_list
all_index = indexs([10,'abc',89,40,10,56],10)
print(all_index)

#将第二个10换成121
list4 = [10,'abc',89,40,10,56]
all_index = indexs(list4,10)
list4[all_index[1]] = 121
print(list4)


#补充：判断一个值是否是指定的类型
#isinstance(值，类型)
def count_float(list):
    count = 0
    list = [3.14,2,4.0]
    for item in list:
        if isinstance(item,float):
            count += 1
    return count
geshu = count_float(list)
print(geshu)


