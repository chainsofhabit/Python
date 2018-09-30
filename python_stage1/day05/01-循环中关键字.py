import random
#python 控制台输入函数 input(提示信息)
'''
1.程序遇到input，会停下来，等到输入完成后才会执行后面的代码（阻塞线程）
2.输入结束：遇到return就结束
3.获取到输入的内容的类型是字符串（不管输入的是什么）

'''

name = input('请输入名字:')
number = input('请输入一个数字:')

print(name,number,type(name))

#break、continue、else
'''
break:程序执行过程中只要遇到break就结束/跳出包含break的最近的一个循环
'''
#练习；随机生成一个数，然后去猜，直到猜到为止
number = random.randint(0,100)
count = 0
while True:
	num = input('请输入一个数字(0-100):')
	count += 1
	if int(num) == number:
		print('恭喜你猜对了！%d' % (number))
		if count > 7:
			print('回家养猪去')
		elif count >3:
			print('还可以')
		else:
			print('nice')
		break    #循环结束
	else:
		if int(num) > number:
			print('大了')
		else:
			print('小了')



#计算1000以内，不能被15整除的和
sum = 0
for x in range(1000):
	if x%15 == 0:
		continue
	sum += x

print(sum)

# else:python中的循环的最后可以添加else语句
'''
for 变量 in 序列:
	循环体
else:
	循环结束后要执行的代码


while 条件语句:
	循环体
else:
	循环结束后要执行的代码
注意:写到else里面的语句，和写在循环外边的区别是，break的时候else中内容不会执行
'''

for x in range(5):
	print(x,end = ' ')
else:
	print('结束')


n = 1
while n>5:
	print(n)
	n += 1
else:
	print('结束')
