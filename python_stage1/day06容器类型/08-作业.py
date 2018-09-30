#1.已知一个列表，求列表中心元素
list1 = [1,2,3,4,5,6,7,8,9]
a = len(list1)
if a % 2 != 0:
    print(list1[a // 2])
else:
    print(list[a // 2],list[a // 2 - 1])


#2.已知一个列表，求所有元素和
# count = 0
# for item in list1:
#     count += item
# print(count)
# 3.已知一个列表，输出所有下标是奇数的元素
# list2 = []
# for x in range(len(list1)):
#     if x%2 != 0:
#         list2.append(list1[x])
# print(list2)
#4.已知一个列表，输出所有元素中，值为奇数的元素
# for item in list1:
#     if item %2 != 0:
#         print(item,end = ' ')

# 5.已知一个列表，将所有的元素乘以2
# list3 = []
# item1 = 1
# for item in list1:
#     item1 = int(item*2)
#     list3.append(item1)
# print(list3)
# for index in range(len(list1)):
#     list1[index] *= 2
# print(list1)
# 6.已知一个列表，将所有元素加到第一个元素中
#sun(序列)：python内置的求序列中元素的和的方法
list1[0] = sum(list1)
print(list1)

# count = 0
# for item in list1:
#     count += item
# del list1[0]
# list1.insert(0,count)
# print(list1)
list1[0] = list1[:]
print(list1)
#7.已知一个列表A，将奇数位置元素存到B列表中，偶数元素存到C列表中

# list4 = []
# list5 = []
# for x in range(len(list1)):
#     if x%2 == 0:
#         list5.append(list1[x])
#     else:
#         list4.append(list1[x])
# print(list4)
# print(list5)
#
# # 8.把A列表的前5个元素复制到B列表中
# list6 = []
# list6 = list1[0:5]
# print(list6)
#
# 9.有一个长度是10的列表，按递增排列，用户输入一个数，插入适当位置
list7 = [1,3,5,7,9,11,13,15,17,20]
number = int(input('请输入一个数：'))
# list7.append(number)
# list7.sort()
# print(list7)
for index in range(len(list7)):
    if list7[index]>number:
        list7.insert(index,number)
        break
else:
    list7.append(number)
print(list7)
# # 10.实现列表的count方法的功能
# list8 = [1,2,'a','asd','a']
# print(list8.count('a'))

#11. 实现列表的extend方法的功能
# list8.extend([100,102])
# print(list8)

#12.实现列表的index方法
# index1 = list8.index('asd')
# print(index1)