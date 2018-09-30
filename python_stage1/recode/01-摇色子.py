from random import randint
count = 0
for _ in range(3):
    number = randint(1,6)
    count += number
    print("色子点数:",number)
print("点数和：",count)

#计算1+2+3+...+100
count1 = 0
for x in range(1,101):
    count1 += x
print("和为:%d" % count1)
#统计1-1000中能被3整除的数的个数
count2 = 0
for x in range(1,1001):
    if x % 3 == 0:
        count2 += 1
print("能被3整除的数有%d个" % count2)

list = [1,2,3,4,5]
for index in range(len(list)):
    list[index] *= 2
print(list)

get_value = lambda list1,index = 0:list1[index]/2
str = input("请输入字符串:")
def count_str():
    list1 = list(str)
    list2 = []
    number = len(str)
    for i in range(number):
        count = 0
        item  = list1[i]
        for item in list1:
            if item == list1[i]:
                count += 1
        list2.append(count)
    number = max(list2)
    print(number)
    x = list2.index(number)
    print(list1[x])
    # print(list1[count])
count_str()

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def getx(self):
        return self.x
    def gety(self):
        return self.y
class distance:
    def __init__(self,p1,p2):
        self.x = p1.getx()-p2.getx()
        self.y = p1.gety()-p2.gety()
        self.len = (self.x**2 + self.y**2)**0.5
    def getlen(self):
        print(self.len)

p1 = Point(0,0)
p2 = Point(3,4)
l = distance(p1,p2)
l.getlen()


