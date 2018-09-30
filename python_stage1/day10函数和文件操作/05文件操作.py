"""
1.程序中不管操作任何文件，不管怎么操作，
过程都是：打开文件 -> 操作（读或写） -> 关闭文件
2.做数据持久化，本地化，都要使用文件来保存数据
（数据库文件，txt文档，json文件，plist,xml文件等，二进制文件（图片，视频，音频等））
程序中通过变量，列表，字典等保存的数据，在程序结束后都会被销毁的
"""

"""
1.打开文件
open(文件地址，打开方式，encoding=编码方式)
文件地址：告诉open函数要打开的是哪个文件，填文件路径，可以填绝对路径，也可以填相对路径
绝对路径：C:/Users/Administrator/Desktop/a.txt
相对路径：./相对路径（相对于当前文件所在的目录）
          ../相对路径（相对于当前文件所在的目录的上一层目录）
b.打开方式，获取文件的内容以读的形式打开，往文件中写内容就以写的内容打开
'r' ---> 读（默认值）,读出来的内容以文本形式返回
'rb' /'br' ---> 读，读出来的内容以二进制（bytes）的形式返回
'w'--> 写，写文本到文件中
'wb'/'bw'--> 写，写二进制数据到文件中
'a' ---> 写  追加

c.编码方式：以文本的形式读和写的时候才需要设置编码方式
utf-8:万国码
gbk:只支持中文

d.open函数的返回值是被打开的文件对象

2.关闭文件
文件对象.close()

"""
#1.文本文件
# f1 = open('/Python/.txt',encoding='utf-8')
# f2 = open('./test.txt','rb')
# f = open('../test.txt','r',encoding='utf-8')

#2.关闭文件
# f1.close()
# f2.close()
# f.close()

#3.操作文件
#a.读操作
#读文件中的内容，一行一行读写，读完为止
f = open('./test.txt','r',encoding='utf-8')
content = f.readline()
while content:
    print('line',content)
    content = f.readline()

f.close()


#b.写操作
"""
write(写的内容)
'w'-->写操作，完全覆盖原文件的内容
'a'--->写操作，在原文件的内容后去追加新的内容
"""
f = open('./test.txt','w',encoding='utf8')
f.write('程序员的诗')
f.close()

#文件不存在的情况
"""
当以读的形式打开文件的时候，如果文件不存在，程序会崩溃，报错
当以写的形式打开一个不存在的文件的时候，会自动创建一个新的文件
"""
f = open('./test2.txt','w',encoding='utf8')
f.write('诗和远方')
f.close()

#练习：统计一个模块执行的次数
f = open('./number',encoding='utf-8')

