import pygame, sys
from settings import *
from pygame.locals import *
from meteors import meteors, add_meteor_row
from spacecraft import craft, lunched_shots
from playerstats import player_stats


pygame.init()
# pygame.font.init()
fpsClock = pygame.time.Clock()

#Caption
pygame.display.set_caption('pygame test')

# draw first line of meteors
add_meteor_row()

#Main Loop
while True:

    DISPLAYSURF.fill(colors['black'])
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            pass

        if event.type == KEYUP:
            # handle shoot
            if event.key == pygame.K_f:
                craft.shot('normal')
        if event.type == KEYUP:
            # handle shoot
            if event.key == pygame.K_SPACE:
                craft.shot('double')

    # handle key down
    pressed = pygame.key.get_pressed()
    # handle craft move left or right
    if pressed[pygame.K_LEFT] or pressed[pygame.K_RIGHT]:
        if pressed[pygame.K_LEFT]:
            craft.handle_arrows('left')
        if pressed[pygame.K_RIGHT]:
            craft.handle_arrows('right')
    else:
        craft.handle_arrows()

    # add new row of metheors
    try:
        if meteors.root_node.meteor.y > grid_y:
            add_meteor_row()
    except Exception as e:
        print('Error. main.py')
        print(e)

    #draw geometries
    meteors.traverse(call_function='draw',)
    lunched_shots.draw()
    craft.draw()

    # update position of geometries
    meteors.traverse(call_function='move', vector=[0,.5])

    # handle collisions
    meteors.traverse(call_function='colision', colision_items=lunched_shots)

    #draw text
    player_stats.draw()


    # UPDATE SURFACE
    pygame.display.update()
    fpsClock.tick(FPS) # control speed or FPS
