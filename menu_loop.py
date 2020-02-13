import pygame, sys
from settings import *
from pygame.locals import *
from playerstats import player_stats
from space_travel_loop import space_travel_loop
from meteors import meteors
import pygame, sys
from settings import *
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
            pygame.quit()
            sys.exit()
        if choice == self.options[2][0]:

            pass
            # TODO:
            # create instruction page

def game_over_loop():
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
                    for option in menu.options:
                        if option[1]=='active':
                            return menu.choice(option[0])

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
