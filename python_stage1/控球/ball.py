import pygame

key_color = 'color'
key_radius = 'radius'
key_pos = 'pos'
key_direction = 'direction'
key_xspeed = 'xspeed'
key_yspeed = 'yspeed'


if __name__ == '__main__':
    pygame.init()
    window = pygame.display.set_mode((400, 600))
    window.fill((255, 255, 255))

    main_ball = {
        key_color: (0, 255, 0),
        key_radius: 20,
        key_pos: (200, 300),
        key_direction: 'up',
        key_xspeed: 0,
        key_yspeed: -3
    }
    pygame.draw.circle(window, main_ball[key_color], main_ball[key_pos], main_ball[key_radius])
    pygame.display.flip()

    while True:

        # 移动
        center_x, center_y = main_ball[key_pos]
        new_x = center_x + main_ball[key_xspeed]
        new_y = center_y + main_ball[key_yspeed]
        main_ball[key_pos] = new_x, new_y
        # 重新画
        window.fill((255, 255, 255))
        pygame.draw.circle(window, main_ball[key_color], main_ball[key_pos], main_ball[key_radius])
        pygame.display.update()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == 273:
                    main_ball[key_yspeed] = -3
                    main_ball[key_xspeed] = 0
                elif event.key == 274:
                    main_ball[key_yspeed] = 3
                    main_ball[key_xspeed] = 0
                elif event.key == 275:
                    main_ball[key_yspeed] = 0
                    main_ball[key_xspeed] = 3
                elif event.key == 276:
                    main_ball[key_yspeed] = 0
                    main_ball[key_xspeed] = -3
