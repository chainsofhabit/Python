import re
from re import findall

# 1. 写一个正则表达式判断一个字符串是否是ip地址
# 规则：一个ip地址由4个数字组成，每个数字之间用.连接。每个数字的大小是0-255
# 255.189.10.37   正确
# 256.189.89.9    错误
ip = input("请输入ip地址：")
re_str = r"((\d|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])\.){3}(\d|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])"
# re_str = r"(((\d{1,2})|(1\d{1,2})|(2[0-4]\d)|(25[0-5]))\.){3}((\d{1,2})|(1\d{1,2})|(2[0-4]\d)|(25[0-5]))"
result = re.fullmatch(re_str,ip)
if result:
    print("ip地址合法")
else:
    print("ip地址不合法")


# 2. 计算一个字符串中所有的数字的和
# 例如：字符串是：‘hello90abc 78sjh12.5’ 结果是90+78+12.5 = 180.5
re_str = r"[+-]?\d+\.\d+|[+-]?\d+"
# re_str = r"\d+[.]\d+|[1-9]\d*"
list1 = findall(re_str,"hel10lo90abc 78sjh12.5")
count = 0
for item in list1:
    count += float(item)
print("数字的和为：%.1f" % count)
# 3. 验证输入的内容只能是汉字
re_str = r"[\u4E00-\u9FA5]+"
string = input("输入内容：")
result = re.fullmatch(re_str,string)
if result:
    print("全是汉字！")
else:
    print("有非汉字！")
# 4. 电话号码的验证
# re_str = r"(13|14|15|17|18)[0-9]{9}"
# number = input("输入电话号码：")
# result = re.fullmatch(re_str,number)
# if result:
#     print("号码正确！")
# else:
#     print("号码错误！")
# 5. 简单的身份证号的验证
re_str  = r"[1-9]\d{5}[1-2]\d{3}(0[1-9]|1[0-2])(0[1-9]|[1-2][0-9]|3[0-1])\d{3}([0-9]|x|X)"
number1 = input("请输入身份证号：")
result = re.fullmatch(re_str,number1)
if result:
    print("身份证号正确！")
else:
    print("身份证号不正确！")