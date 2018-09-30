import pygame
pygame.init()
window = pygame.display.set_mode((500,500))
window.fill((255,255,255))

#图片相关
#1.加载图片
image = pygame.image.load("./files/timg2.jpg")


"""
形变：
a.缩放
transform.scale(缩放对象，目标大小)：将指定的对象缩放到指定的大小，会返回缩放后的对象
"""
new_image = pygame.transform.scale(image,(100,100))

"""
b.旋转缩放（指定缩放比例）
rotozoom(Surface,angle,scale)
Surface:旋转缩放对象
angle：旋转的角度(0-360)
scale：缩放比例
"""
new_image = pygame.transform.rotozoom(image,0,1)
"""
c.旋转
rotate(Surface,angle)
Surface:旋转缩放对象
angle：旋转的角度(0-360)
"""
# new_image = pygame.transform.rotate(image,45)
#2.渲染图片
window.blit(new_image,(100,100))

#3.展示内容
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()