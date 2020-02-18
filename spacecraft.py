import pygame, sys
from settings import *
from playerstats import player_stats
from base_obj import BaseObj, ListOfObjects
from random import choice
from colisions import left_game_area

class SpaceCraft(BaseObj):
    def __init__(self,game_area, color):
        super().__init__(
            x=150, y=game_area[1] - 70,
            wx=25, wy=25
        )
        self.vector = [0,0]
        self.display_surface = DISPLAYSURF
        self.image = pygame.image.load('maps/spaceship.bmp')

    def handle_arrows(self, direction=None):
        # accelerate ship movement and detect if ship
        # is exiting the game area.
        if direction != None:
            if direction == 'left':
                self.vector[0] += -.5 if self.vector[0] > -6 else 0
            if direction == 'right':
                self.vector[0] += .5 if self.vector[0] < 6 else 0
        else:
            if self.vector[0] == 0:
                return
            self.vector[0] += .5 if self.vector[0] < 0  else -.5

    def move(self):
        area_limit = [0, game_area[0]-self.wx]
        if self.x > area_limit[0] and self.x < area_limit[1]:
            self.x += self.vector[0]
            self.y += self.vector[1]
        else:
            x = self.vector[0]
            self.vector[0] = self.vector[0]*(-1) if self.vector[0] > 0 else abs(self.vector[0])
            self.x = 1 if self.x <1 else area_limit[1]-1

    def draw(self):
        self.move()
        DISPLAYSURF.blit(self.image, (self.x, self.y))

    def shot(self,type):
        if player_stats.get('amunition') <= 0: return
        if type == 'normal':
                player_stats.set(-1, 'amunition')
                lunched_shots.add(CraftShot(self.x+int(self.wx/2), self.y))
        if type == 'double':
                player_stats.set(-2, 'amunition')
                lunched_shots.add(CraftShot(self.x, self.y))
                lunched_shots.add(CraftShot(self.x+self.wx-2, self.y))

    def explode(self):
        #lunch exploded meteor Animation
        for i in range(100):
            craft_pieces.add(
                CraftPiece(self.x,self.y)
            )


class CraftPiece(BaseObj):
    def __init__(self, x, y,):
        size = choice([ i for i in range(5) ])
        super().__init__(x=x,y=y, wx=size, wy=size)
        self.display_surface = DISPLAYSURF
        self.color = [255,255,255]
        #generate vector
        vector_choice = [i for i in range(-8,8)]
        vector_choice.remove(0)
        self.vector = [choice(
            vector_choice
        ) for i in range(2)]

    def move(self):
        #update color
        self.color[2] = self.color[2]-15 if self.color[2] >= 15 else 0
        if self.color[2] == 0 and self.color[1]-15 >= 0:
            self.color[1] -= 15
            if self.color[1] > 15 and self.color[0] > 5:
                self.color[0] -= 5

        # update positon
        self.x += self.vector[0]
        self.y += self.vector[1]
        if left_game_area(self):
            craft_pieces.remove_item(self)
            del self

    def draw(self,**kwargs):
        pygame.draw.rect(
            self.display_surface,
            self.color,
            (self.x, self.y, self.wx, self.wy)
        )
        self.move()


# class CraftPieces(object):
#     def __init__(self):
#         self.list = []
#
#     def add(self,item):
#         self.list.append(item)
#
#     def draw(self, **kwargs):
#         if len(self.list) > 0:
#             for i in self.list:
#                 i.draw()
#
#     def remove_item(self, item):
#         self.list.remove(item)


class CraftShot(BaseObj):
    def __init__(self, x, y, type='normal'):
        super().__init__(x=x, y=y, wx=2, wy=2)
        self.color = (255,255,255,0)
        self.display_surface = DISPLAYSURF
        self.shot_type = type

    def draw(self, **kwargs):
        #draw a bullet that looks like a short gradient
        for i in range(10):
            color = (0, (255-(i*25)), (255-(i*25)))
            pygame.draw.rect(
                self.display_surface, color,
                (self.x, self.y+(i*2), self.wx, self.wy)
            )
        self.y -= 5
        if self.y < 0:
            lunched_shots.remove_item(self)


global lunched_shots
craft_pieces = ListOfObjects()
craft = SpaceCraft(game_area, colors['light-green'])
lunched_shots = ListOfObjects()
