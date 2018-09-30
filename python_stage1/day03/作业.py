'''
个性化消息: 将用户的姓名存到一个变量中，并向该用户显示一条消息。
\显示的消息应非常简单，如“Hello Eric, would you like to learn some Python today?”
'''
name1 = 'Tom'
print("Hello %s,would you like to learn some Python today" %name1)
"""
调整名字的大小写: 将一个人名存储到一个变量中，再以小写、大写和首字母大写的方式显示这个人名。
"""
name2 = 'summer'
print(name2.lower())    #全部小写
print(name2.upper())    #全部大写
print(name2.capitalize())   #首字母大写


str1 = 'Albert Einstein once said,'
str2 = '“A person who never made a mistake never tried anything new.”'
print(str1 + str2)


famous_person = 'Albert Einstein'
message = '“A person who never made a mistake never tried anything new.”'
print(famous_person + ' once said,' + message)

name3 = '\txiatian  \n'
print(name3)
print(name3.strip(),name3.lstrip(),name3.rstrip())
