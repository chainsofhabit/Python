import pygame
pygame.init()
window = pygame.display.set_mode((600, 600))
window.fill((255, 255, 255))
# pygame.display.flip()

image = pygame.image.load("./files/timg2.jpg")
#缩放
image = pygame.transform.rotozoom(image,0,0.5)
window.blit(image,(100,100))
#获取图片的宽度和高度
image_w,image_h = image.get_size()
pygame.display.flip()

#用来存储图片是否移动
flag = False
# 保存图片的坐标
image_x = 100
image_y = 100
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            #判断鼠标按下的位置是否在图片上
            m_x,m_y = event.pos
            if image_x<=m_x<=image_x+image_w and image_y<=m_y<=image_y+image_h:
                flag = True
        if event.type == pygame.MOUSEBUTTONUP:
            flag = False

        #鼠标移动事件
        #鼠标在移动并且flag是True
        if event.type == pygame.MOUSEMOTION and flag:

            #填充背景色，覆盖原来的内容
            window.fill((255,255,255))
            #鼠标移动的位置渲染图片
            center_x,center_y = event.pos
            image_x,image_y = center_x-image_w/2,center_y-image_h/2
            window.blit(image,(image_x,image_y))
            # 更新屏幕显示
            pygame.display.update()
