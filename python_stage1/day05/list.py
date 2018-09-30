list = ['baidu','jianshu',234,121]
list[2] = 289  #替换列表中的第三个元素
print(list)

# del list[2]   #删除列表中的第三个元素,根据索引删除
# print(list)

list.remove(289)  #删除单个元素，删除首个符合条件的元素
print(list)

list.pop(0)  #删除单个或多个元素，按照索引删除
print(list)

list2 = ['asd','summer',234,121]
list2.append('jd')  #在末尾添加新对象
print(list2)

print(list2.count(121))  #统计出现次数
print(list2.index(121))  #找出第一个符合条件的元素的索引
list3 = [1,2,3]
list3.reverse()   #列表反转
print(list3)

print(max(list3))
#列表用[],元组用(),
tup1 = (121,34.56)
tup2 = ('run','abc')
tup3 = tup1 + tup2
print(tup3)
print(len(tup3))
#字典：字典是另一种可变容器模型，切可存储任意类型对象
#字典的每一个键值用冒号：分割，每个对用逗号分割，键必须是唯一的，值不一定是唯一的
dict = {'name':'wx','age':18,'school':'chengdu'}
print('年龄:',dict['age'])
dict['from'] = '内江'   #添加
dict['age'] = '19'     #修改
print(dict)