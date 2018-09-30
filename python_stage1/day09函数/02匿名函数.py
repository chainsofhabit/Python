"""
匿名函数本质还是函数，之前函数的所有内容都适用它
1.匿名函数的声明
函数名 =lambda  参数列表：返回值
2. 说明：
函数名：变量名
lambda:声明匿名函数的关键字
 3.调用
 匿名函数的调用和普通函数一样

"""
#写一个匿名函数计算两个数的和
#声明一个匿名函数
# my_sum = lambda x,y:x+y
# #调用匿名函数
# result = my_sum(121,129)
# print(result)

#练习，写一个匿名函数，获取指定列表指定下标的值得1/2

#匿名函数的参数可以设默认值
# get_num = lambda list1,index=0:list1[index]/2
# #位置参数
#
# # print(get_num([1,2,3,4,5],3))
# print(get_num([1,2,3,4,5]))
# #关键字参数
# print(get_num(index=1,list=[10,9,8,6]))

#练习：获取一个列表的所有元素的平均值和所有元素的和（sum函数可以计算一个序列的和）
list_operation = lambda list2:(sum(list2),sum(list2)/len(list2))
sum1,average = list_operation([1,32,3,6])
print(sum1,average)


#补充：python中的函数可以有多个返回值，就是在一个return后返回多个值，多个值之间用逗号隔开
def list_operation2(list2):
    return sum(list2),sum(list2)/len(list2)
print(list_operation2([1,2,3,4,5,6]))
