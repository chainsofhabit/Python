"""
1.json文件
标准格式：a.只有一个数据 b.数据必须是json支持的数据类型
数据类型：对象（字典），数组（列表），字符串（双引号），数字，布尔（true,false）,null
json数据和python之间的转换关系
python模块中的方法：load,loads,dump,dumps
异常捕获
try-except-finally
"""
import pygame
#1初始化游戏模块
pygame.init()
#创建游戏窗口
#display.set_mode(窗口大小）：创建一个窗口并且返回
#窗口大小：是一个元组；并且元组中需要两个值分别表示宽度和高度
window = pygame.display.set_mode((400,500))

#让游戏一直运行，直到点击关闭按钮才结束
while True:
    #获取游戏中产生的所有事件
    for event in pygame.event.get():
        #type判断事件的类型
        if event.type == pygame.QUIT:
            exit()   #退出程序