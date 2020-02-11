import pygame, sys
from settings import *
from pygame.locals import *
from meteors import meteors, add_meteor_row, exploded_meteors_list
from spacecraft import craft, lunched_shots
from playerstats import player_stats

print('Space craft game initialized.')

pygame.init()
# pygame.font.init()
fpsClock = pygame.time.Clock()

#Caption
pygame.display.set_caption('pygame test')

#variables
meteor_vector = [0,1]
old_player_points = player_stats.level

# draw first line of meteors
add_meteor_row()

#Main Loop
while True:

    if player_stats.health <= 0:
        break

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
        if meteors.meteors_list[-1].y > grid_y:
            add_meteor_row()
    except:
        print(meteors.meteors_list[-1].y)

    #draw geometries
    exploded_meteors_list.draw() # maybe change to traverse later on ??
    meteors.traverse(call_function='draw',)
    lunched_shots.draw()
    craft.draw()

    # update position of geometries
    if old_player_points + 15 < player_stats.points:
        old_player_points = player_stats.points
        player_stats.level += 1
        meteor_vector = [meteor_vector[0],meteor_vector[1]+.5]
    meteors.traverse(call_function='move', vector=meteor_vector)

    # handle collisions
    meteors.traverse(call_function='colision', colision_items=lunched_shots)

    #draw text
    player_stats.draw()


    # UPDATE SURFACE
    pygame.display.update()
    fpsClock.tick(FPS) # control speed or FPS
