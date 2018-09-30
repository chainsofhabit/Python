from re import fullmatch,search,findall
"""
1.正则表达式就是用来检测字符串是否满足某种规则的工具
例如：1,.账号是手机号/邮箱/多少位由什么东西组成等
2.脏话替换成*等

正则表达式python对正则表达式的支持，提供了一个内置的模块:re
fullmatch(正则表达式，字符串)：判断整个字符串是否符合正则表达式

"""

#1）匹配任意字符
re_str = r"."
result = fullmatch(re_str,"a")
print(result)

#2 \w匹配字母数字下划线
#匹配一个字符串，前三位分别是abc最后两个是字母数字下划线
re_str = r"abc\w\w"
result = fullmatch(re_str,"abc2g")
print(result)

# 3）\s 匹配空白字符（空白指的是空格，制表符和回车等所有能产生空白的字符）
re_str = r'\w\w\w\s.'
result = fullmatch(re_str, 'hu2\t?')
print(result)

#4 \d 匹配一个数字字符
#匹配一个字符串，前三位是数字字符，最后一位是任意字符
re_str = r"\d\d\d."
result = fullmatch(re_str,"121#")
print(result)

#5 \b  检测是否是单词边界（单词的开头，单词的结尾）
#匹配一个字符串，前四位是when，第五时空白

re_str = r'when\b\swhere'
result = fullmatch(re_str, 'when where')
print(result)

re_str = r'abc\b'
result = fullmatch(re_str, 'abc')
print(result)


# \W 匹配一个非数字，字母，下划线的字符串
re_str = r"\W\w"
result = fullmatch(re_str,"!a")
print(result)

 # 6) ^ 检测字符串是否以给定的正则表达式开头
# 匹配一个字符串，是否以两个数字字符开头
re_str = r'^\d\d'
result = fullmatch(re_str, '23')
print(result)

result = search(r'^\d\d', '99abc11hkj')
print(result)

re_str = r'a\d$'
result = fullmatch(re_str, 'a8')
print(result)

result = search(re_str, 'a9aaa8')
print(result)

#9) \S 匹配非空白字符
re_str = r"\S\w\w\w"
result = fullmatch(re_str,"@a3f")
print(result)

# \D匹配一个非数字字符
#\b 检测非单词边界
#========================匹配次数===================

#1.[] 匹配中括号中出现的任意字符
#注意：一个中括号只匹配一个字符
#匹配一个3位的字符串，第一位是a/b/c后两位是数字

re_str = r"[abc]\d\d"
result = fullmatch(re_str,"c67")
print(result)

# - 在正则中的中括号的应用：如果将减号放在两个字符的中间，代表的是谁到谁
#要求一个字符串的第一个是1-8中的一个，后面两位是小写字母
re_str = r'[1-8][a-z][a-z]'
result = fullmatch(re_str, '2hn')
print(result)

re_str = r'[!+-][A-Z]'
result = fullmatch(re_str, '-D')
print(result)

#匹配一个四位的字符串，第一位不是大写字母，后三位是abc
#匹配一个字符串，最后一位是"b"，
re_str = r'[^A-Z\d]abc'
result = fullmatch(re_str, '#abc')
print(result)


#3) *匹配0次或者多次
#匹配一个字符串，最后一位是"b",b的前面有0个或多个a
re_str = r"a*b"
print(fullmatch(re_str,"aaab"))

# + 匹配一次或者多次（至少一次）
# 判断一个字符串是否是无符号的正整数

re_str = r"[1-9]+\d*"
print(fullmatch(re_str,'10'))

#5.？匹配零次或一次

re_str = r"@?\d+"
print(fullmatch(re_str,"@124455"))


re_str = r'[+-]?[1-9]+\d*'
print(fullmatch(re_str, '200'))



# 6)  {N} 匹配N次
re_str = r"\d{3}"
re_str = r"[a-zA-Z]{3}"
print(fullmatch(re_str,'aHh'))

#7) {N,} 至少匹配N次
re_str = r"\w{4,}"
print(fullmatch(re_str,"hanc_123"))

#8) {,N}最对匹配N次
re_str = r'a{,4}b'  # 'b', 'ab', 'aab', 'aaab','aaaab'
print(fullmatch(re_str, 'aaaab'))
#9）{M,N}
re_str = r'a{2,4}b'  # 'aab', 'aaab', 'aaaab'
print(fullmatch(re_str, 'aaab'))
# 注意：次数相关的操作，每次约束的次数符号前的前一个字符
#==========分之和分组============
#1)| 分之（相当于逻辑运算中的or）
# 匹配一个字符串是三个字母或者是三个数字
re_str = r"[a-zA-Z]{3}|\d{3}"
print(fullmatch(re_str,"abc"))
# "\d{3}[a-z]{2}"是分之中的第一个条件
re_str = r"\d{3}[a-z]{2}|[A-Z]{3}"
print(fullmatch(re_str,"ABC"))


#2)分组 通过加()来对正则条件进行分组
#两位数字两位字母出现3次
re_str = r"([a-z]{2}\d\d){3}"
print(fullmatch(re_str,"sa23er45gh67"))

#练习写一个正则表达式，能够匹配出字符串中所有的数字（包括整数和小数）
# "acx12.5fgd60,30kkk9sf0.12"
# re_str = r"[1-9]\d*[.]?\d*|0[.]\d+"
re_str = r"\d+[.]\d+|[1-9]\d*"
print(findall(re_str,"acx12.5fgd60,30kkk9sf0.12"))
#匹配一个字符串，按照一个数字一个字母的规律出现一次或多次
re_str = r"(\d[a-z])+"
print(fullmatch(re_str,"7a7f0h7d0g8h6k"))
#重复
# 可以通过\数字来重复匹配前面的括号中匹配的结果
re_str = r"(\d{2}[A-Z])=%\1\1"
print(fullmatch(re_str,"28M=%28M28M"))
re_str = r"(\d{3})-(\w{2})\1\2"
print(fullmatch(re_str,"123-aa123aa"))

#捕获
#按照完整的正则表达式去匹配，只捕获（）中的内容，只有在findall中有效
re_str = r"a(\d{3})b"
print(fullmatch(re_str,"a245b"))
print(findall(re_str,"a345b"))


#正则中的分支有短路操作：如果使用|去连接多个条件，前面的条件已经匹配出结果，那么后面的条件就不会去匹配了
# 练习：
# 用户名必须由字母，数字，或下划线构成且长度在6-20个字符之间
# QQ号是5-12的数字且首位不能为0
user_name = input("用户名：")
qq = input("QQ:")
if fullmatch(r"\w{6,20}",user_name):
    print("用户名合法")
else:
    print("用户名不合法")
if fullmatch(r"[1-9]\d{4,11}",qq):
    print("qq可用")
else:
    print("qq不可用")