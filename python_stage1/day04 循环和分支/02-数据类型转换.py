#int,float,bool,str
#数据类型的自动转换
a = 10  #整型(int)
b = 12.5  #浮点型(float)
result = a + b  #会自动将整型a转换成浮点型，然后再计算
print(type(result))

result2 = a + True  #会自动将布尔True转换成整型
print(result2,type(result2))

# 2.强制转换
# 基本语法：类型名(需要转换的数据)

#1.将其他数据转换成int类型
#浮点型，布尔和部分字符串可以转换

print(int(12.25))  #浮点型转换成整型，去掉小数点和小数点后的数
print(int(True),int(False))  #bool转换成int
#去掉字符串的引号后，字符串的内容本身就是一个整数的时候才能转换成整数
print(int('123'))

#2.将其他的数据类型转换成Float类型
'''
整数，布尔和部分字符串可以转换
'''
print(float(100))  #int 转换成float在后面加小数点和小数
print(float(True),float(False))
#去掉引号后字符串的内容本身就是一个整数或者浮点数的时候，才能转换成浮点数

print(float(2e3))

#3.将其他的数据类型转换成bool
'''
所有的数据类型的数据都可以转换成bool
数字中除了0是False，其他的都是True
字符串中出了空串其他的都是True
总结：所有为空，为0的值全部都是False,否则就是True
'''
print(bool(-100))
print(bool(0))
print(bool('asd'),bool('True'))
print(bool(''))
print(bool(None))

#4.其他类型转换成字符串
'''
所有的数据都可以转换成字符串，转换的时候就是在数据外面加引号

'''
print(str(1234))



number = 12344
print('它是%d位数'%len(str(number)))
print(str(number)[-1::-1])
# for index in 

# for i in range(100,1000):
# 	a = i//100
# 	b = i//10%10
# 	c = i%10
# 	if i == a^3 + b^3 + c^3:
# print(i)
# i = 100
# while i < 1000:
# 	a = i//100
# 	b = i//10%10
# 	c = i%10
# 	if i == (a**3 + b**3 + c**3):
# 		print(i)
# 	i += 1
import math
x = 101
count = 0
while x <= 200:
	for y in range(2,math.sqrt(x)):
		if x%y != 0:
			count += 1
			print(x)

	x += 1