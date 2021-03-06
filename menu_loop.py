import pygame, sys
from settings import *
from pygame.locals import *
from playerstats import player_stats
from space_travel_loop import space_travel_loop
from meteors import meteors, exploded_meteors_list
import pygame, sys
from settings import *
from spacecraft import craft, craft_pieces, lunched_shots
from random import randint
from stars import stars, add_star_row

pygame.font.init()

class Menu(object):
    def __init__(self):
        self.font = pygame.font.Font('freesansbold.ttf', 20)
        self.options = [
            [
                'Play',
                'active',
                (75, 150),
            ],
            [
                'Instructions',
                'inactive',
                (75, 200)
            ],
            [
                'Exit',
                'inactive',
                (75, 250)
            ],
        ]

    def draw(self):
        for option in self.options:
            DISPLAYSURF.blit(
                self.font.render(
                    option[0],
                    True,
                    colors['white'] if option[1] != 'active' else colors['cian']
                ),
                option[2]
            )

    def choice(self,choice):
        if choice == self.options[0][0]:
            player_stats.clear_results()
            meteors.clear_list()
            space_travel_loop()

        if choice == self.options[1][0]:
            pass
            # TODO:
            # create instruction page

        if choice == self.options[2][0]:
            pygame.quit()
            sys.exit()


def game_over_animation_loop():
    #variables
    meteor_vector = [0,1]

    craft.explode()

    #Main Loop
    for i in range(120):
        DISPLAYSURF.fill(colors['black'])
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # add background start row
        if randint(1,10) < 7 :
            add_star_row(3)

        #draw geometries
        stars.traverse(call_function='draw')
        exploded_meteors_list.traverse(call_function='draw')
        meteors.traverse(call_function='draw',)
        lunched_shots.traverse(call_function='draw')
        craft_pieces.traverse(call_function='draw')

        # update position of geometries
        meteors.traverse(call_function='move', vector=meteor_vector)

        # handle collisions
        meteors.traverse(call_function='colision', colision_items=lunched_shots)

        #draw text
        player_stats.draw()

        # UPDATE SURFACE
        pygame.display.update()
        fpsClock.tick(FPS) # control speed or FPS


def game_over_loop():
    game_over_animation_loop()
    i = 0
    while True:
        i+=1
        if i > 500:
            break

        DISPLAYSURF.fill(colors['black'])
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == pygame.K_RETURN:
                    menu_loop()

        # print game over
        DISPLAYSURF.blit(
            pygame.font.Font('freesansbold.ttf', 20).render(
                'Game Over',
                True,
                colors['white']
            ),
            (75,200),
        )
        #draw
        player_stats.draw()

        # UPDATE SURFACE
        pygame.display.update()
        fpsClock.tick(FPS) # control speed or FPS
    menu_loop()


def menu_loop():
    while True:
        DISPLAYSURF.fill(colors['black'])
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                # handle arow up
                if event.key == pygame.K_UP:
                    for i, item in enumerate(menu.options):
                        if menu.options[i][1] == 'active' and i != 0:
                            menu.options[i-1][1] = 'active'
                            menu.options[i][1] = 'inactive'
                            break

                # handle arrow down
                if event.key == pygame.K_DOWN:
                    for i, item in enumerate(menu.options):
                        if menu.options[i][1] == 'active' and i != len(menu.options)-1:
                            menu.options[i+1][1] = 'active'
                            menu.options[i][1] = 'inactive'
                            break
                if event.key == pygame.K_RETURN:
                    for option in menu.options:
                        if option[1]=='active':
                            return menu.choice(option[0])


        #draw
        player_stats.draw()
        menu.draw()

        # UPDATE SURFACE
        pygame.display.update()
        fpsClock.tick(FPS) # control speed or FPS

menu = Menu()
