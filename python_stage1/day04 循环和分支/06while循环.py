'''
1.结构：
while 条件语句:
	循环体
2. 说明:
while:关键字
条件语句:结果是True或者False
循环体:要重复执行的代码

3.执行过程:
判断条件语句的结果是否为True 如果为True就执行循环体，
执行完循环体再判断条件语句是否为True，直到条件语句的结果为False为止
'''
i = 1
sum = 0
while i <= 100:
	sum += i
	i += 1
print(sum)
i = 1
sum = 0
while i <= 5:
	i += 1
	sum += i
	
print(sum,i)	

#for循环和while循环的比较
#for循环的循环次数是有限的，并且是固定(确定)的；while循环的循环次数不确定
#for循环：1.遍历序列中的值 2.循环次数确定
#while循环：1.死循环 2.循环次数不确定
#找大于10000的数中，第一个能够被23整除的数
x = 10001
while x % 23 != 0:
	x += 1
print(x)





# number = 0
# x = 1
# while x <= 100:
# 	if x%3 == 0:
# 		number += x
# 	x += 1
# print('1到100之间能被3整除的数的和为:%d'%number)



# number = 0
# x = 1
# while x <= 100:
# 	if x%7 != 0:
# 		number += x
# 	x += 1
# print('1到100之间不能被7整除的数的和为:%d'%number)