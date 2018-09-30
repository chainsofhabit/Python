# python为字符串提供了很多的内建函数
# 字符串.函数()
#注意：这些所有的函数的功能都不会影响原来的字符串，而是产生一个新的字符串
#1.capitalize()将字符串的第一个字符转换成大写
str1 = 'hello python'
newstr = str1.capitalize()
print(newstr)
# 2.center(width,fillchar)

#让字符串变成width对应的长度，原内容居中，剩余的内容使用fillchar的内容填充
#width - 整数；fillchar - 任意字符
print('asd'.center(10,'0'))

# 3 rjust(width,fillchar)
#让字符串变成width对应的长度，原内容靠右，剩余的 部分使用fillchar的值来填充
number = '1'
new_id = number.rjust(3,'0')
print(new_id)

#4.原字符串.count(str) 判断str值在原字符串中出现的次数
print('asdsdasaa'.count('a'))
#5 str1.join(str2)
#在str2中的每一个字符之间插入一个str1
print('1'.join('asdew00'))
#6.str1.replace(old,new)
#将str1中的old全部替换成new
new_str = 'sadsfsdgcv'.replace('d','*')
print(new_str)
#判断是否以start开头
str3 = 'startwithasdqwe'
str4 = 'asdqwer'
print(str3.startswith('s'))
print(str4.startswith('s'))
#判断是否以end结尾
str5 = 'zxcend'
print(str5.endswith('d'))
print(str5.endswith('en'))
#将字符串中的Tab符号转换成空格，tab符号默认的空格数是8
str6 = '	a 	we 	'
print(str6.expandtabs())
#如果字符串中至少有一个字符并且所有的字符都是字母或数字则返回True,否则返回False
str7 = '  '
str8 = '123swds'

print(str7.isalnum())
print(str8.isalnum())
#如果字符串中至少有一个字符并且所有字符都是字母则返回True,否则返回False
str9 = 'asWddfr'
print(str8.isalpha())
print(str9.isalpha())
#如果字符串中只包含数字则返回True否则返回False
str10 = '123556'
print(str8.isdigit())
print(str10.isdigit())
#如果字符串中包含至少一个区分大小写的字符并且所有的字符都是小写则返回True,否则返回FalseF
print(str9.islower())

print(str7.isspace())
#将字符串中的大写转换为小写，小写转换为大写
print(str9.swapcase())
#标题化字符串
print(str5.title())
#如果字符是标题化的则返回True否则返回False
print(str5.istitle())