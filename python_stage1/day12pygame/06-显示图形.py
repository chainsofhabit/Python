import pygame
from math import pi
pygame.init()
window = pygame.display.set_mode((500,500))
window.fill((255,255,255))

"""
1.画直线
def line(Surface, color, start_pos, end_pos, width=1)
Surface:画在哪
color：线的颜色
start_pos：起点
end_pos：终点
width=1：线的宽度
"""
pygame.draw.line(window,(255,0,0),(50,50),(400,50),8)

pygame.draw.line(window,(255,0,0),(50,50),(50,400),8)
"""
2.画线段（折线）
def lines(Surface, color, closed, pointlist, width=1)
Surface：画在哪
color：线的颜色
closed：是否闭合（是否连接起点和终点）
pointlist：点对应的列表
width
"""

pygame.draw.lines(window,(255,0,0),True,[(100,200),(250,120),(20,450)],6)

"""
3.画圆
def circle(Surface, color, pos, radius, width=0)
Surface：画哪
color：颜色
pos：圆心坐标
radius：半径
width：线宽  0-->填充
"""
pygame.draw.circle(window,(255,255,0),(250,250),100,2)

"""
4画矩形
def rect(Surface, color, Rect, width=0)
Surface：画哪
color：颜色
Rect：范围（元组，元组中的四个元素，分别是x,y,width,height）
width:线宽
"""
pygame.draw.rect(window,(220,255,100),(0,0,50,100))
"""
5.画多边形
def polygon(Surface, color, pointlist, width=0)
"""
pygame.draw.polygon(window,(0,255,200),[(100,200),(50,450),(150,300)])
"""
6.画椭圆
def ellipse(Surface, color, Rect, width=0)
"""
pygame.draw.ellipse(window,(200,200,250),(100,100,300,200))

"""
7.画弧线
def arc(Surface, color, Rect, start_angle, stop_angle, width=1)
start_angle:0-2pi
stop_angle:
"""
pygame.draw.arc(window,(200,100,120),(200,200,150,150),0,pi/2)
#展示内容
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()