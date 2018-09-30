import re

"""
1.正则表达式中的转义和字符串中的转义字符没有任何关系，
在python中的字符串前加r阻止的是字符串转义，不能阻止正则表达式的转义

2.在正则表达式中可以通过在有特殊意义的符号前加\来表示符号本身
\+  \.  \*  \?  \\  \( \)  \[ \]    \^   \$    \|
注意：
a.- 只有在中括号中的两个字符之间才有特殊的意义
b.如果特殊符号放到中括号中作为字符集的内容，
那么除了- 在两个字符之间以外，其他的都不需要转义
c.\ 不管在哪都需要转义 ^放在中括号的最前面需要转义
"""
re_str = r"a\+"
print(re.fullmatch(re_str,"a+"))
re_str = r"\+a"
print(re.fullmatch(re_str,"+a"))
re_str = r"\\w-a"
print(re.fullmatch(re_str,"\w-a"))
re_str = r"\(\d{3}"
print(re.fullmatch(re_str,"(234"))

re_str = r'[\^.?*]mbc\\'
print(re.fullmatch(re_str, '?mbc\\'))

