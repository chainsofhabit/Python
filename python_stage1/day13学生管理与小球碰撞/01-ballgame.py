import pygame
import ball_color
from random import randint
"""
游戏功能，点击屏幕，在点击的地方产生一个球，球可以自由移动，撞到边界会弹回，撞到其他球会吃掉
 第一步：搭建游戏窗口
 第二步：点击屏幕产生球
 第三步：让球动起来（需要用列表来保存所有的球，需要用字典来保存每个球的信息）
"""
#全局变量
window_width = 500
window_height = 500

key_ball_color = "ball_color"
key_ball_center = "ball_center"
key_ball_radius = "ball_radius"

key_ball_xspeed = "ball_xspeed"
key_ball_yspeed = "ball_yspeed"

key_ball_alive = "ball_live"
all_ball = []  #保存所有的球
def ball_crash():
    """
    检测碰撞
    :return:
    """
    #去看屏幕上的每个球是否和其他的球圆心距小于等于半径和
    #拿第一个球
    for ball in all_ball:
        #拿另外的球
        for other in all_ball:
            if ball == other or ball[key_ball_alive] == False or other[key_ball_alive] == False:
                continue
            #判断两次拿到的球是否相撞
            x1,y1 = ball[key_ball_center]
            x2,y2 = other[key_ball_center]
            distance = ((x1-x2)**2 + (y1-y2)**2)**0.5
            if distance <= ball[key_ball_radius] + other[key_ball_radius]:
                #相撞后
                if randint(0,1):
                    ball[key_ball_radius] += int(other[key_ball_radius]*0.4)  #一个变大
                    # all_ball.remove(other)  #一个消失
                    other[key_ball_alive] = False
                else:
                    other[key_ball_radius] += int(ball[key_ball_radius] * 0.4)  # 一个变大
                    # all_ball.remove(other)  #一个消失
                    ball[key_ball_alive] = False


def draw_all_ball(window):
    pygame.time.delay(20)
    window.fill(ball_color.white)
    for ball in all_ball[:]:
        if ball[key_ball_alive]:
            pygame.draw.circle(window,ball[key_ball_color],
                               ball[key_ball_center],ball[key_ball_radius])
        else:
            all_ball.remove(ball)
    pygame.display.update()
def ball_move():
    """
    球动起来
    :return:
    """
    for ball in all_ball:
        ball_x,ball_y = ball[key_ball_center]
        new_x = ball_x + ball[key_ball_xspeed]
        new_y = ball_y + ball[key_ball_yspeed]


        if new_x < ball[key_ball_radius]:
            new_x = ball[key_ball_radius]
            ball[key_ball_xspeed] *= -1
        elif new_x > window_width - ball[key_ball_radius]:
            new_x = window_width - ball[key_ball_radius]
            ball[key_ball_xspeed] *= -1
        if new_y < ball[key_ball_radius]:
            new_y = ball[key_ball_radius]
            ball[key_ball_yspeed] *= -1
        elif new_y > window_height - ball[key_ball_radius]:
            new_y = window_height - ball[key_ball_radius]
            ball[key_ball_yspeed] *= -1
        ball[key_ball_center] = new_x,new_y
def creat_ball(window,pos):
    """
    在指定的位置产生一个颜色随机的球
    :param window:
    :param pos:
    :return:
    """
    balls_color = ball_color.rand_color()
    ball_center = pos
    ball_radius = randint(10,30)
    ball = {key_ball_color:balls_color,
            key_ball_center:ball_center,
            key_ball_radius:ball_radius,
            key_ball_xspeed:randint(-5,5),
            key_ball_yspeed:randint(-5,5),
            key_ball_alive:True
    }
    #保存球的信息
    all_ball.append(ball)
    pygame.draw.circle(window,balls_color,ball_center,ball_radius)
    pygame.display.update()
def main_game():
    """
    游戏主系统
    :return:
    """

    #初始化游戏
    pygame.init()
    window = pygame.display.set_mode((window_width,window_height))
    window.fill(ball_color.white)

    #进入游戏界面，默认显示的内容和要执行的操作写在这

    pygame.display.flip()
    #游戏循环
    while True:



        #游戏循环要执行的代码写在这....
        ball_move()
        draw_all_ball(window)
        ball_crash()
        #事件检测
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            #事件发生要执行的操作写在下面
            #鼠标按下
            elif event.type == pygame.MOUSEBUTTONDOWN:
                creat_ball(window,event.pos)





main_game()