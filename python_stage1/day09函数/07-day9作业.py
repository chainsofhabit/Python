#1.写一个函数将一个指定的列表中的元素逆序(例如[1, 2, 3] -> [3, 2, 1])
# (注意：不要使用列表自带的逆序函数)
def reverse_list(list1:list):
    list2 = []
    n = len(list1)
    for index in range(n):
        list2.append(list1[n-1-index])
    return list2

print(reverse_list([1,3,4,6,5]))
#2.写一个函数，提取出字符串中所有奇数位上的字符
def get_str(str1:str):
    str2 = ''
    str2 += str1[1::2]
    return str2
print(get_str('asdfre3$%#&%'))
# 3.写一个匿名函数，判断指定的年是否是闰年
leap_year = lambda year:(year % 4 == 0 & year % 100 != 0 or year % 400 ==0)
result = leap_year(2000)
if result is True:
    print('闰年')
else:
    print('不是闰年')


#4
def str(n):
    if n == 1:
        print('@')
        return
    str(n-1)
    print('@'*n)
str(4)

#5.写函数，检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。


