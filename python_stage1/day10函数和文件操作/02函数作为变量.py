"""
在python中，函数就是一种特殊的类型
"""
#
# if __name__ == '__main__':
#     a = 10
#     b = a
#     #申明一个函数func
#
# #2.函数作为列表元素
# list1 = [a,'10',100]
# list2 = []
# list3 = []
# for x in range(10):
#     def func2():
#         print(x+y)
#     list2.append(func2)
#     list3.append(func2(x))
# #list2中每个元素都是函数
# print(list2)
# print(list3)
#
# #list2[0]就是一个函数
# func = list2[0]
# print(func(100))
#
# #调用list中下标对应是1的函数并且传参为10
# list2[1](10)
# #直接将函数作为列表的元素
# # funcs = [func1]
# # funcs[0]()
#
# #将函数作为字典的值
# # def sub(*nums):
# #     if not
# operation = {'+':lambda x,y:x+y,'-':lambda x,y:x-y,'*':lambda x,y:x*y}
# result = operation['+'](10,20)
# print(result)

#函数作为函数的参数（回调函数）
def clean_kitchen(time):
    print('在%s，做厨房清洁服务' % time)
    print('收费300元')
    return 300
def clean_floor(time):
    print('在%s，做地板清洁服务' % time)
    print('收费200元')
    return 200
def call_service(time:str,service):
    service(time)
#将函数作为参数，传给其他函数
call_service('上午10点',clean_kitchen)
call_service('下午2点',clean_floor)
print('=============')
#5.函数作为函数的返回值
def operation(operator:str):
    if operator == '+':
        def sum1(*nums):
            count = 0
            for num in nums:
                count += num
            print(count)
        #将求和的函数返回
        return sum1
    elif operator == '*':
        def sum1(*nums):
            count = 1
            for num in nums:
                count *= num
            print(count)
        #将求和的函数返回
        return sum1

operation('+')(1,2,3)
operation('*')(3,4,5)