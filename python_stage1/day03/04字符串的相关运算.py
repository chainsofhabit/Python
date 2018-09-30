# 1. + 运算符 
'''

python支持两个字符串相加,其效果就是将两个字符串拼接在一起，产生一个新的字符串
注意：如果+的一边是字符串，那么另一边也必须是字符串
'''
print('asd'+'123')
str1 = 'world'
newstr = 'hello' + ' ' + str1
print(newstr)

# 2.* 运算符
'''
字符串*整数:字符串重复多次
'''
print('abc'*2)
# 3 所有的比较运算符
str2 = 'asd'
print('asd' == str2)
#比较大小
"""
str1 > str2;str1 < str2
让str1中的每一位字符分别和str2中的每一位字符依次比较，直到不同为止，再看不同字符中谁的编码值大或小

"""
print('asdf' > 'ad')
print('江秀成'>'王建平' )
print(ord('江'),ord('王'))

# 4 in 和 not in
"""
str1 in str2:判断str1是否在str2中
结果是布尔值
"""
print('asd' in 'asdfgfh')
print('asd' in 'awsedrf')
print('f' not in 'python') 

# 5 获取字符串长度
# 字符串的长度指的是字符串中字符的个数
# len()内置函数
str3 = 'jiangxiucheng'
print(len(str3))

# 空串
str4 = ''
str5 = ""
print(len(str4),len(str5))
print(str3[-1],str3[len(str3)-1])

# 6.阻止转义
# 在字符串的最前面添加r/R可以阻止转义
print('a\nb')
print(r'a\nb',R'a\nb\\')