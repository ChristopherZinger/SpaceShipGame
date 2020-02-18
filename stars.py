# python modules
import pygame, sys
from random import randint, choice

#local imports
from base_obj import BaseObj, ListOfObjects
from settings import *
from colisions import left_game_area


class Star(BaseObj):
    def __init__(self):
        x = randint(0, game_area[0])
        wx = randint(1,3)
        super().__init__(x=x, y=0, wx=wx, wy=wx)
        color = randint(50,120)
        self.color = (color,color,color)
        self.display_surface = DISPLAYSURF
        self.vector = [
            0 if randint(0,100) < 70 else randint(0,4),
            randint(1,4)
        ]

    def destruct(self):
        # remove star form list and delete object
        stars.remove_item(self)
        del self

    def move(self,**kwargs):
        self.x += self.vector[0]
        self.y += self.vector[1]
        if left_game_area(self):
            stars.remove_item(self)
            del self

    def draw(self, **kwargs):
        self.move()
        pygame.draw.rect(
            self.display_surface,
            self.color,
            (self.x, self.y, self.wx, self.wy)
        )


def add_star_row(quantity=10):
    # add first in the row
    for i in range(randint(1,quantity)):
        stars.add(Star())


global stars
stars = ListOfObjects()
