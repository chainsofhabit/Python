def func1():
    print('good')
#将不希望被别的模块导入（执行）的代码块放到if语句中
if __name__=='__main__':
    print('!!',a)
    for x in range(10):
        print('!!',x)