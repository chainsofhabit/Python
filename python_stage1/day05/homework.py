# number = '00005345'
# print(number.lstrip('0'))
# number = '2abd00076686'
# #字符串1.lstrip(字符串2)：
# #从字符串1的第一个开始，判断字符是否在字符串2中，如果在就删除这个字符，
# #然后再看下一个字符是否在字符串2中，依次类推，直到字符串1中的字符不在字符串2中为止
# #如果字符串1中的第一个字符就不在字符串2中，就一个字符都不用删
# print(number.lstrip('adb0'))



# import math
# x = 101
# count = 0
# while x <= 200:
# 	for y in range(2,math.sqrt(x)):
# 		if x%y != 0:
# 			count += 1
# 			print(x)

# 	x += 1

#1.求裴波那契数列中第n个数的值:1,1,2,3,5,8,13,21,34
#n=1和n=2时，第n个数=1
#当n>=3,第n个数 = 第n-1个数+第n-2个数
'''
num1 = 1
num2 = 1
number = num1+num2

'''
# n = int(input('请输入获取第几个数:'))
# if n ==1 or n ==2:
# 	print(1)
# num1 = 1
# num2 = 1
# current = 0   #当前数
# #求出第n个和第n个前面所有的数
# for index in range(3,n+1):
# 	#当前数等于前面第一个数加前面第两个数
# 	current = num1 + num2
# 	num1 = num2
# 	num2 = current
# print(current)


# 判断101到200之间有多少个素数，并输出所有的素数。判断素数的方法：用一个数分别除2到sqrt(这个数)，如果能被整除，则表明这个数不是素数，反之是素数
# count = 0
# for x in range(101,200):
# 	for y in range(2,x):
# 		if x % y == 0:
# 			break
# 	else:
# 		count += 1
# 		print(x,end = ' ')
# print('一共有%d个素数'%(count))


# for x in range(101,200):
# 	count = 0
# 	for y in range(2,x):
# 		if x%y ==0:
# 			count += 1
# 			break
# 	if count == 0:
# 		print(x,end = ' ')

n = int(input('输入所求的第几个数：'))
fz = 2
fm = 1
num = 0
for index in range(1,n):
	num = fz + fm
	fm = fz
	
	fz = num
print('第%d个数是:%d/%d' % (n,fz,fm))