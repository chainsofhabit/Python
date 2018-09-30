#判断一个数是否是偶数的写法
number = 13
if number % 2 ==0:
	print('偶数')

if not number % 2:
	print('偶数')

if number % 2:
	print('奇数')

#判断一个字符串是否为空串
#01.
str1 = 'asd'
if str1 == '':
	print('是空串')
else:
	print('不是空串')

#02.
if len(str1) == 0:
	print('是空串')
else:
	print('不是空串')

#03.
if str1:
	print('不是空串')
else:
	print('是空串')

if not str1:
	print('是空串')
	