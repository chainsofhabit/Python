def func1():
    for x in range(10):
        return x
print(func1(),type(func1()),type(func1))
#1.yield关键字
"""
只要函数中有yield关键字，那么这个函数就会变成一个生成器
a.函数中有yield的函数，在调用函数的时候不再是获取返回值，
而是产生一个生成器,生成器对象中保留的是函数体
b.当通过next获取生成器中的数据的时候，才会执行函数体，执行到yield为止，
并且将yield后面的结果作为生成的数据返回，同时记录结束的位置，
下次再调用next的时候，从上次结束的位置接着往后执行
"""

def func2():
    print('abc')
    for x in range(10):
        yield x
        print('aaa')

#注意：函数中只要有yield不管yield会不会执行到，函数的调用结果都是生成器
def func3(x):
    print('asd')
    if  x > 10:
        yield 100
    return 20
print(func2(),type(func2()),type(func2))
#这的func2()是一个生成器
gen = func2()
print(next(gen))
print(next(gen))
print(next(gen))
print('=======')
#练习：写一个生成器，可以产生斐波那契数列（可以无限生成）
#1,1,2,3,5,8,13,21,34....
def fei():
    yield 1
    yield 1
    a = 1
    b = 1
    while True:
        yield a+b
        a,b = b,a+b

gen = fei()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

#生成器和生成式产生的对象就是迭代器
#将列表转换成迭代器对象
iter1 = iter([1,2,3,4])
print(iter1)

print(next(iter1))
print(next(iter1))
for item in iter1:
    print(item)
