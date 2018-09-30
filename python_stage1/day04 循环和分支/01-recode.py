#字符串的格式化
"""
'格式符'% (格式符对应的值)'
说明
%s---字符串
%d---整数
%f---浮点数
%c----字符
"""
first_name = '王'
last_name = '静'
age = 18
name = first_name + last_name
print(name)
#用字符串的格式化
#hello,XXX! 今年X岁
newstr = 'hello,%s%s! 今年%d岁' % (first_name,last_name,age)
print(newstr)

money = 999
newstr = '金额是：%.2f元'  % money
print(newstr)
#使用变量保存学生的名字，年龄和成绩
name = '李华'
age = 20
grade = 90
newstr2 = '%s今年%d岁，他的语文成绩是%.1f分' % (name,age,grade)
print(newstr2)
numbers = 1
for i in range(0,20):
	numbers *= 2
print(numbers)

summation = 0
num = 1
while num <= 100:
	if (num%3==0 or num%7==0) and num%21!=0:
		summation += 1
	num += 1
print(summation)


sum = 0
for num in range(1,101):

	sum +=num
print('所有数的和为:%d'%(sum))
print('所有数的和为:%.2f'%(sum/100))