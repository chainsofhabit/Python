#计算机中常用的进制有:二进制、八进制、十进制、十六进制

#十进制:
#1.十进制的基数：0,1,2,3,4,5,6,7,8,9 进位：逢10进1
#十进制数的每一位：3456 = 10^0*6+10^1*5+10^2*4+10^3*3

#二进制 基数:0,1 例如110 10100 进位：逢2进1
#二进制上的每一位 1011 = 2^0*1 + 2^1*1 + 2^2*0 + 2^3*1 =11(十进制)
#八进制 基数：0,1,2,3,4,5,6,7 逢8进1
#八进制数上的每一位 123 = 8^0*3 + 8^1*2 + 8^2*1 = 83(十进制)
#十六进制：基数：0-9  A-F 逢16进1
#十六进制数上的每一位 123 = 16^0*3 + 16^1*2 = 16^2*1 = 291(十进制)

#进制间的转换
#1.二进制、八进制、十六进制转换为十进制
#进制数^位数(从零开始)*每一位上的值得和
# 1011 = 2^0*1 + 2^1*1 + 2^2*0 + 2^3*1 =11(十进制)

#123 = 8^0*3 + 8^1*2 + 8^2*1 = 83(十进制)

#八进制、十六进制转换我二进制
#将一位的八进制转换成三位的二进制
#将一位的十六进制转换成四位的二进制
#123(8)--->001010011(2)
#123(16)--->000100100011(2)
#二进制转换成八进制 十六进制
#将三位的二进制转换成一位的八进制，将四位的二进制转换成一位的十六进制
# 4,十进制转换成二进制 相除取余法
# python对进制的支持
#python支持整数的二进制、八进制、十六进制
#python中二进制、八进制、十六进制的表示
#二进制:0b
#将其他的数据转换成二进制   bin()
print(0b11)
print(bin(20))  
#八进制:0o
#将其他数据转换成八进制  oct()
print(0o11)
print(oct(20))  
#十六进制：0x
#将其他数据转换成十六进制  hex()

print(0xaf)
print(hex(20))  