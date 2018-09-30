import pygame
from random import randint
pygame.init()
window = pygame.display.set_mode((600, 600))
window.fill((255, 255, 255))
pygame.display.flip()
#球的圆心坐标
x1 = 100
y1 = 100
x2 = 50
y2 = 50
x3 = 200
y3 = 250
r1 = 25
r2 = 25
r3 = 25
add1 = 4
add2 = add5 = 3
add3 = 1
add4 = add6 = 2

#游戏循环
while True:
    #将之前的球覆盖
    window.fill((255,255,255))

    #延迟
    pygame.time.delay(10)
    #不断的画圆
    pygame.draw.circle(window,(255,0,0),(x1,y1),r1)
    pygame.draw.circle(window, (255, 0, 0), (x2, y2), r2)
    pygame.draw.circle(window, (255, 0, 0), (x3, y3), r3)
    pygame.display.update()

    #改变y值让圆在垂直方向移动
    y1 += add1
    x1 += add2
    y2 += add3
    x2 += add4
    y3 += add5
    x3 += add6

    # r += add
    # if r>=120 or r<=20:
    #     add *= -1
    #边界检测
    if y1 >= 575 or y1<=25:
        add1 *= -1
    if x1>= 575 or x1<=25:
        add2 *= -1
    if y2 >= 575 or y2 <= 25:
        add3 *= -1
    if x2 >= 575 or x2 <= 25:
        add4 *= -1
    if y3 >= 575 or y3 <= 25:
        add5 *= -1
    if x3 >= 575 or x3 <= 25:
        add6 *= -1
    if (x2-x1)**2+(y1-y2)**2 <= (r1+r2)**2:
        # x1 = x1+x2
        # x2 = x1-x2
        # x1 = x1-x2
        # y1 = y1 + y2
        # y2 = y1 - y2
        # y1 = y1 - y2
        x1,x2 = x2,x1
        y1,y2 = y2,y1
    if (x3 - x1) ** 2 + (y1 - y3) ** 2 <= (r1 + r3) ** 2:
        x1,x3 = x3,x1
        y1,y3 = y3,y1
    if (x3 - x2) ** 2 + (y2 - y3) ** 2 <= (r2 + r3) ** 2:
        x2,x3 = x3,x2
        y2,y3 = y3,y2

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.circle(window, (randint(0, 255), randint(0, 255), \
                                        randint(0, 255)), event.pos, randint(50, 100))
            pygame.display.flip()
            pygame.display.update()

# import pygame
# from random import randint
# pygame.init()
# window = pygame.display.set_mode((500,500))
# window.fill((255,255,255))
# pygame.display.flip()
# # r = randint(20,30)
# add1 = 3
# add2 = 2
# while True:
#
#     pygame.time.delay(20)
#     for event in pygame.event.get():
#
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             pygame.draw.circle(window,(randint(0,255),randint(0,255),randint(0,255)),\
#                                event.pos,20)
#             # pygame.display.flip()
#             # print()
#             circle_x,circle_y = event.pos
#             circle_x += add1
#             circle_y += add2
#             if circle_y >= 480 or circle_y <=20:
#                 add2 *= -1
#             if circle_x >= 480 or circle_x <=20:
#                 add1 *= -1
#             pygame.display.flip()
#         elif event.type == pygame.QUIT:
#             exit()



