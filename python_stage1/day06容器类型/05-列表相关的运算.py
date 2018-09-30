# +操作
# 列表1 + 列表2：将列表1中的元素和列表2中的元素依次合并，产生一个新的列表
a = [1,2]
list1 = a + ['asd',100]
print(list1,a)

# 2.* 操作
# 列表 * N:将列表1中的元素重复N次，产生一个新的列表
list2 = a * 3
print(list2)

#3.in / not in
# 元素 in 列表：判断一个元素是否在列表中
print(10 in [1,2,3,4,10])

#4.获取列表的长度
# len(序列)
print(len([1,2,34,5]))
name = ['羽毛球','乒乓球','网球','桌球','篮球','足球']
print(len(name))


#5.相关的方法
number = [1, 2.3, 1, 45, 1]
#5.1列表.count(元素)，统计指定元素在列表中有几个
print(number.count(1))
#5.2 列表.extend(序列)：将序列中的元素添加到列表中
number.extend([1000,200])
print(number)
number.extend('xwr')
print(number)

number.append([300,400])
print(number)

#5.3列表。index(元素)：获取指定元素在指定列表中第一次出现对应的下标
index1 = number.index(1)
print(index1)

#5.4列表.pop():将列表中最后一个元素从列表中取出来
item = number.pop()
print(item,number)

#5.5列表.reverse():将列表中的元素反序
number1 = [1,22,3,4]
number1.reverse()
print(number1)

# 5.6列表.sort():对列表元素进行排序(默认升序)
#列表.sort(reverse = True):对列表进行降序排序
number1.sort()
print(number1)

#列表.clear()：将列表中的元素全部清除

number1.clear()
print(number1)

#5.8列表.copy():将列表中的元素全部拷贝一份产生一个新的列表，相当于列表[:]
#这的拷贝是浅拷贝  浅拷贝只拷贝列表里的值
number2 = [1,2,3,45]
number3 = number2.copy()
print(number3)