import pygame
#1.初始化游戏模块
pygame.init()
#2.创建窗口
window = pygame.display.set_mode((600,600))
#给窗口填充颜色
"""
fill(颜色)
颜色;计算机三原色（红，绿，蓝），每个颜色对应的值得范围是0-255，
可以通过改变三原色的值可以调配出不同的颜色
颜色值：是一个元组，元组中三个元素，分别代表红绿蓝（rgb）
(255,0,0)---red
(0,255,0)---green
(0,0,255)---blue

"""
window.fill((100,100,100))
"""
显示图片
"""
# pygame.load():获取本地图片,返回图片对象
image = pygame.image.load("./files/timg2.jpg")
# getsize()获取图片的大小，返回值为一个元组，有两个元素，分别是宽和高
image_width,image_height = image.get_size()

#渲染图片
"""
blit(渲染对象，位置)
位置：坐标（x，y），值的类型是元组，元组有两个元素分别对应x,y坐标
"""
window.blit(image,(600-image_width,600-image_height))
#展示内容
pygame.display.flip()

#3.游戏循环
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()