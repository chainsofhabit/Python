import pygame

pygame.init()
window = pygame.display.set_mode((600, 600))
window.fill((255, 255, 255))
pygame.display.flip()
#球的圆心坐标
x = 100
y = 100
r = 20
add1 = 4
add2 = 3
#游戏循环
while True:
    #将之前的球覆盖
    window.fill((255,255,255))

    #延迟
    pygame.time.delay(10)
    #不断的画圆
    pygame.draw.circle(window,(255,0,0),(x,y),r)
    pygame.display.update()

    #改变y值让圆在垂直方向移动
    y += add1
    x += add2

    # r += add
    # if r>=120 or r<=20:
    #     add *= -1
    #边界检测
    if y >= 580 or y<=20:
        add1 *= -1
    if x>= 580 or x<=20:
        add2 *= -1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
