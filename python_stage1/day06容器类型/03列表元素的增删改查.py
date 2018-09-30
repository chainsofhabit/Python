#查：获取列表元素
#a.获取单个元素:列表[下标],下标是不能越界的
movie_names = ['死亡飞车','速度与激情','金刚狼','黑客帝国']
print(movie_names[1])
print(movie_names[-1])
#b.获取部分元素(切片)：列表[下标1:下标2]/列表[::]
#结果是列表
#步进为正从前往后取，为负从后往前取
print(movie_names[1:3])
print(movie_names[-1:-4:-1])
print(movie_names[:3])
print(movie_names[2:])
print(movie_names[:])

#c.遍历(一个一个的获取每个元素)
#可以将列表直接放到for循环的in的后边
#循环过程中for后面的变量取得是列表中的每个元素
for item in movie_names:
    print(item)
#写一个列表来保存六个学生的成绩，统计成绩在80以上的人数
list1 = [80,79,81,78,82,76]
count = 0
for item in list1:
    if item > 80:
        count += 1
print(count)

#2.改
#语法：列表名[下标] = 新值  通过下标获取元素然后重新赋值
person = ['马',20,'money']
person[1] = 18
print(person)

#增(添加列表元素)
#列表中元素的个数发生改变后，列表中每个元素的下标会重新分配
#a.列表.append(元素)  在列表最后添加
person.append('男')
print(person)
#b.列表.insert(下标，元素):在指定的下标前取插入一个元素
person.insert(0,'007')
print(person)
#输入5个学生成绩，并且保存在一个列表里

# list2 = []
# for x in range(5):
#     score = int(input('输入学生成绩：'))
#     list2.append(score)
# print(list2)
# 4.删除列表中的元素
# a.del列表[下标]--->根据下标删除列表中的元素
# del语句是python中删除数据的语法，可以删除任何数据：del变量(删除变量) del列表(删除整个列表)
balls = ['羽毛球','乒乓球','网球','桌球','篮球','足球']
del balls[1]
print(balls)

#b.列表.remove(元素)---->删除列表中的值
#如果元素在列表中有多个，只删除最前面的一个
balls.remove('足球')
print(balls)

#c.列表.pop(下标) ----->将列表中下标对应的元素取出来
ball = balls.pop(2)   #将下标为2的元素取出来保存到ball中
print(balls,ball)

#将一个保存成绩的列表中，成绩低于60分的全部删除
#[78,59,40,90,89,45,69,30]
list3 = [78,59,40,90,89,45,69,30]
for item in list3[:]:
    if item < 60:
        list3.remove(item)
print(list3)
#注意:以后遍历列表的元素的时候，我们一般遍历他的拷贝值([:])
a = 10
b = a
print(a,b)
a = 100
print(a,b)
#引用类型赋值是
a1 = [1,2]
b1 = a1