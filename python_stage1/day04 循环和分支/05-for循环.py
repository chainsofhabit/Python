#在完成某个功能的时候如果需要重复某个操作，就可以使用循环
#python中循环结构有两种：for循环，while循环
'''
1.for循环的结构：
for 变量名 in序列:
	循环体
说明:
a.for:关键字
b.变量名:和声明变量名时的变量名的要求是一样的
c.in:关键字
d.序列:容器(数据本身是由多个数据组成)，例如：字符串、列表、字典、元组、集合、range、生成式和生成器
e.循环体:需要重复执行的代码
执行过程:让变量去序列中取数据，一个一个取，取完为止，每取一个数据执行一次循环体

'''
for i in 'asef123':
	print(i)

#range函数是python中内置函数，作用是产生一定范围中的数字
'''
range(N):产生0~N-1的所有整数
range(N,M):产生N到M-1的所有整数
range(N,M,step):产生从N开始每step产生一个整数，到M-1之前
xrange是python2中的函数，python3用range代替
'''
print('--------------')
for x in range(9):
	print(x)

for y in range(10,16):
	print(y)

for a in range(1,11,2):
	print(a)

print('===========')
#计算1+2+3+4+.....+100
sum = 0
for num in range(1,101):

	sum +=num
print(sum)

#统计1~1000中能被3整除的个数
number = 0
for x in range(1,1001):
	if x%3 == 0:
		number += 1
print('能被3整除的数的个数:%d' %(number))
#注意：for循环中用来获取序列值得变量，在循环体不一定要使用
#如果不用，那么变量名可以声明为下划线_
number = 0
for x in range(1,101):
	if x%3 == 0:
		number += x
print(number)




# number = 0
# for x in range(1,101):
# 	if x%7 != 0:
# 		number += x
# print('1到100之间不能被7整除的数的和为:%d'%number)