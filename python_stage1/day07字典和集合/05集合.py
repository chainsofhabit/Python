#集合(set)
#集合是python中一种容器类型；无序的，可变的,值唯一

#1.声明一个集合
set1 = {1,'asd',100}
print(set1,type(set1))
#将其他序列转换成集合，自带去重功能
set2 = set('asdeeasaxe')
print(set2)
#容器类型不能成为集合中的内容
set3 = {10,3.14,True,'abc'}
print(set3)

# 2.查（获取集合中的元素）
#集合是不能单独获取其中的某一个元素的
#遍历获取每一个元素
for item in set3:
    print(item)

#3.增（添加元素）
#a. 集合.add(元素)
set3.add('nice')
print(set3)

#b.集合1.update(集合2)：将集合2中的元素添加到集合1中
set3.update({1,2,3})
print(set3)

#4.删 集合.remove(元素)
set3.remove('abc')
print(set3)

#删除所有元素
set3.clear()
print(set3)

#6.数学相关的集合运算
#a.判断包含情况：集合1>=集合2：判断集合1中是否包含集合2（或者是<=）
print({1, 2, 3, 4, 5}>={2, 3, 1})

#b.求并集|
set1 = {1,2,3,4,5,6}
set2 = {1,2,14,15,16}
print(set1|set2)



#c.求交集 &
print(set1 & set2)

#d.求差集:-
print(set1 - set2)

#e.求补集^
#求两个集合中除了公共部分以外的部分
print(set1 ^ set2)