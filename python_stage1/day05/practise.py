#1.控制台输入年龄，根据年龄输出不同的提示(例如:老年人，青壮年，成年人，未成年，儿童)


# age = int(input('请输入年龄:'))
# if age >= 60:
# 	print('老年人')
# elif age >= 30:
# 	print('青壮年')
# elif age >= 18:
# 	print('成年人')
# elif age >= 6:
# 	print('未成年')
# else:
# 	print('儿童')

#计算5的阶乘 5!的结果是 

# i = 1
# for x in range(1,6):
# 	i *= x
# print('5!的结果是:%d' %i)

#3.求1+2!+3!+...+20!的和

# number = 0
# for x in range(1,21):
# 	i = 1
# 	for y in range(1,x+1):
# 		i *= y
# 	number += i
# print(number)

#4.计算 1+1/2!+1/3!+1/4!+...1/20!
# number = 0
# for x in range(1,21):
# 	i = 1
# 	for y in range(1,x+1):
# 		i *= y
# 		a = 1/i
# 	number += a
# print(number)


#5.循环输入大于0的数字进行累加，
#直到输入的数字为0，就结束循环，
#并最后输出累加的结果

# count = 0
# while True:
# 	number = int(input('输入一个数:'))
# 	if number == 0:
# 		break
# 	else:
# 		count += number
# print(count)


#输入三个整数x,y,z，请把这三个数由小到大输出
# number = input('输入三个整数:')
# number_list = list(map(int,list(number)))
# #list将数字转换为字符串
# number_list.sort()
# print('排序后：%s' % number_list)


#.这是经典的"百马百担"问题，有一百匹马，驮一百担货，大马驮3担，中马驮2担，两只小马驮1担，问有大，中，小马各几匹
for x in range(0,34):
	for y in range(0,50):
		z = 100-x-y
		if x*3+y*2+z/2 == 100:
			print('大马%d匹，中马%d匹，小马%d匹' % (x,y,z))
#我国古代数学家张邱建在《算经》中出了一道“百钱买百鸡”的问题，题意是这样的： 5文钱可以买一只公鸡，3文钱可以买一只母鸡，1文钱可以买3只雏鸡。现在用100文钱买100只鸡，那么各有公鸡、母鸡、雏鸡多少只？请编写程序实现
for i in range(20):
	for j in range(33):
		k = 100-i-j
		if 5*i+3*j+k/3 == 100:
			print('公鸡%d只，母鸡%d只，雏鸡%d只' % (i,j,k))
#小明单位发了100元的购物卡，小明到超市买三类洗化用品，洗发水（15元），香皂（2元），牙刷（5元）。要把100元整好花掉，可如有哪些购买结合？
for a in range(7):
	for b in range(51):
		for c in range(21):
			if a*15+b*2+c*5 == 100:
				print('洗发水%d瓶，香皂%d块，牙刷%d个' % (a,b,c))

# i = int(input('输入一个整数:'))
# while i>0:
# 	print('*'*i)
# 	i -=1
# i = int(input('输入一个整数(奇数)：'))
# for x in range(i+1):
# 	if x%2==0:
# 		continue
# 	else:
# 		str = '*'*x
# 		print(str.center(i,' '))

#乘法表
# for i in range(1,10):
# 	for j in range(1,i+1):
# 		num = i*j
# 		print('%d*%d=%d\t' % (j,i,num),end = "")
# 	print('\n')



# 求s=a+aa+aaa+aaaa+aa...a的值，
#其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，
# 几个数相加有键盘控制。
# 1.程序分析：关键是计算出每一项的值

# i = int(input('输入一个整数：'))
# j = int(input('几个数相加：'))
# count = 0
# x = 0
# for a in range(j):

# 	x = i+x*10
# 	count += x
# print(count)



