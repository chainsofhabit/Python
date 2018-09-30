#字典(dict)
"""
1.字典是容器类型（序列），以键值对作为元素（字典里面存的数据全是以键值对的形式出现的）
{key:value,key2:value2...}
2.键值对: 键：值（key:value）
键（key）：要唯一，不可变的（数字，布尔，字符串和元组，推荐使用字符串）
值(value):可以不唯一，可以是任何类型的数据
3.字典是可变(增删改)：可变指的是字典中键值对的值和个数可变
"""
#1.声明字典
dict1 = {1: 100,'a':97,True:'布尔',(10,10):'start'}
print(dict1)

person1 = ['余婷',20,5,90]
person2 = {'name':'余婷','age':20,'work_age':5}
dict2 = {}    #空的字典
print(type(dict2))
#2.查(获取值)
# 获取字典的元素对应的值（字典存数据，实质是存的value，key是获取value的手段）
#字典[key]----通过key获取值
print(person2['name'],person2['age'])
#通过字典[key]获取value的时候，如果key不存在会发生KeyError异常
# print(person2['sex'])         #KeyError

#b.字典  get(key)
print(person2.get('age'))
#字典.get(key) 如果key不存在不会报错，返回None
print(person2.get('sex'))  #None----python中的特殊值，代表没有
print(person2.get('name2'))

#总结:确定key肯定存在的时候用[]语法获取value
#key值可能不存在，不存在的时候不希望报错，而是想要自己对他进行特殊处理的时候使用get获取value
person = {'name':'江晨','age':20,}

#c.遍历字典
dog = {'name':'旺财','color':'yellow','age':3}
for key in dog:
    # print(key,end = ' ')
    print(dog[key],end = ' ')


#3.改(修改key对应的value)
#字典[key] = 新值   (key是本来就存在)
dog['name'] = '大黄'
print(dog)

#4.增(添加键值对)
#字典[key] = 值   (key本来就不存在)
dog['type'] = '中华田园犬'
print(dog)


#5.删(删除键值对)
# a. del 字典[key]
del dog['age']
print(dog)

#b.字典.pop(key)
color = dog.pop('color')
new_dict = {'a':color}
print(color,dog)
print(new_dict)
