#tuple(元组)
#元组就是不可变的列表 列表中除了和可变的相关的内容以外，其他的全部适用于元组
#不支持增，删，改  只支持和查相关的操作
#1.声明元组
tuple1 = (1, 2, 'asd', True, [1,2])
print(tuple1,type(tuple1))
#注意：如果要写一个元组元素个数是1字面量，需要在元素后面加逗号
t2 = (100,)
print(t2,type(t2),len(t2))
#()---->代表是空的元组
t3 = ()
print(t3,type(t3))

#2.查相关的
t3 = ('red','yellow','green','pink')
print(t3[1])
print(t3[0:3])
for item in t3:
    print(item)

#特殊操作
point = (100,200)
print(point[0],point[1])

#通过两个变量来获取元组中唯一的两个元素的值
x,y = point
print(x,y)
#通过在变量前加*，获取元组/列表中的一部分元素值，结果是一个列表
user = ('小胖',90,89,97,87,'男')
name,*score,sex = user
print(name,score,sex)

user1 = ('小江',67,68,69)
name,*score = user1
print(name,score)

#4,多个值之间用逗号隔开，对应的数据也是元组
a = 1,2,3,4  #相当于a = (1,2,3,4)
print(a,type(a))

x,y=100,200  #相当于x,y=100,200
print(x,y)