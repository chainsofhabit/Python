"""
1.函数就是对实现某一特定功能的代码块的封装
2.函数的声明
def 函数名(形参列表):
    函数的说明文档
    函数体

3.函数的函数体只有在函数调用的时候才会执行

4.函数的调用
函数名（实参列表）

5.函数调用的过程
a.回到函数声明的位置
b.传参，用实参给形参赋值（一定要保证每个参数都要有值）
c.执行函数体
d.将返回值返回
e.回到函数调用的位置（这个时候函数调用表达式的结果就是返回值）

6.位置参数和关键字

7.参数可以有默认值
要求别人在使用这个函数的时候必须传参就不要默认值（这个时候类型在通过:类型名说明）

8.不定个数参数，在参数名前加*

9.返回值
python中所有的函数都有返回值
看一个函数的返回值；在执行的过程中，又没有执行到return语句
如果有，函数的返回值就是trturn后面的语句，没有就是None

return 关键字：确定返回值；结束函数
"""
#函数说明文档
def dowload(url):
    """
    通
    :param url:
    :return:
    """