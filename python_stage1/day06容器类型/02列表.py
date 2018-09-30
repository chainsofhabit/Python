"""
list(列表)
1.列表是python中的容器类型，有序的，可变的容器-可变指的是列表中的元素和元素的位置可变
有序：可以通过下标来获取元素   可变：可以进行增删改
2.元素指的是列表中的每一个内容,列表中的元素可以是任意类型的数据
一个列表中的元素类型可以不一样

"""
#1.列表的声明
#a.声明变量赋一个列表值
scores = [121,124,90,99]
print(scores,type(scores))

person = ['江',20,'死肥宅']
print(person)

#[]--->空列表
name = []
print(name,type(name))
#b.将其他数据类型转换成列表(只有序列才能转换：字符串和range，字典，元组，集合，生成式和迭代器)
chars = list('asdfafd')
print((chars))
numbers = list(range(10))
print(numbers)