import pygame
from random import randint
pygame.init()
window = pygame.display.set_mode((600, 600))
window.fill((0, 255, 255))

#游戏循环
while True:

    #所有的事件处理的入口就是for循环
    #for循环中的代码只有游戏事件发生后才会执行
    """
    事件的type：
    QUIT:关闭按钮被点击事件
    MOUSEBUTTONDOWN：鼠标按下事件
    MOUSEBUTTONUP：鼠标弹起
    MOUSEMOTION：鼠标移动
    KEYDOWN：键盘按下
    KEYUP：键盘弹起
    
    b.事件的pos ---鼠标事件发生的位置（坐标）
    
    c.事件的key----键盘事件被按的键对应的编码值
    """
    for event in pygame.event.get():
        #不同的事件发生后，对用type值不一样
        if event.type == pygame.QUIT:
            print("点击关闭按钮")
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)
            print("按下")
            pygame.draw.circle(window,(randint(0,255),randint(0,255),\
                                       randint(0,255)),event.pos,randint(50,100))
            pygame.display.flip()
        elif event.type == pygame.MOUSEBUTTONUP:
            print("弹起")
        # elif event.type == pygame.MOUSEMOTION:
        #     print("在动")
        elif event.type == pygame.KEYDOWN:
            print("按下去",chr(event.key))
        elif event.type == pygame.KEYUP:
            print("弹起来")
