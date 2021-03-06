#1.什么是字符串
"""
用单引号或者双引号括起来的字符集就是字符串
'asdfd21@#$$中文',"a  kar98k"
字符串中每个独立的单元叫字符，例如'k','a','r','9','8'等就是字符


"""
name = '哈士奇'
# 2.转义字符
"""
说明：python中没有字符类型，若果要表示字符，就是用一个长度是1的字符串表示，如'1','a'
长度指的就是字符串中字符的个数，如'asd0',长度是4
转义字符：通过\将一些特殊的字符转换成具有特殊功能或特殊意义的字符
常见的转义字符：\n --->换行  \t ---->制表符(相当于tab键)
\\ ---->\ ;\'---';\"-----"

"""
poem = '床前明月光，\n疑似地上霜。'

print(poem)
str1 = 'abc\\bcd'
print(str1)

str2 = 'sdb\'123'
print(str2)
str3 = 'abc\"123"asd'
print(str3)
#3.Unicode编码
"""
python中字符的编码采用的是Unicode编码
Unicode是采用两个字节对一个字符进行编码(2^15)能够将世界上所有的符号进行编码
Unicode编码中包含了ASCII码
将字符转换成指定的数值，这个过程就是编码(编码的目的是方便计算机存储)
将数值转换成对应的符号的过程就是反编码(解码)

"""
#1).将Unicode码转换成字符：Python内置函数 chr(编码)
print(chr(0xA000))
print(chr(0xA100))
print(chr(0x4e60))
#2).将字符转换成Unicode编码：ord(字符)
code1 = ord('王')
print(hex(code1))





#字符串[下标1:下标2:步进]
#从下标1开始获取 每次下标值增加步进值，没增加一次取一个字符，知道取到下标2前为止
#注意：步进如果是正数，那么下标1对应的字符的位置一定要在下标2对应的位置的前面
#如果步进是负数，下标1对应的位置要在下标2对应的位置的后面
#下标2对应的字符是取不到的
str4 = 'hello python'
print(str4[0:5:2])
print(str4[-1:5:-1])

#下标的省略
'''
切片的时候，下标1和下标2是可以省略的
下标1省略：默认从开头开始获取(开始可能是字符串的第一个字符，也可能是字符串的最后一个字符)

'''
str5 = 'good good study day day up'
print(str5[:4])
print(str5[:4:2])
'''
下标2省略，从下标1的位置开始获取 获取到结束(结束可能是字符串的最后，也可能是字符串的开头位置)
'''
print(str5[3:])
print(str5[3::-1])
print(str5[:])
print(str5[::-1])
#要求将一个字符串中所有奇数位上的字符获取出来(位数从0开始算)
print(str5[1::2])