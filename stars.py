# python modules
import pygame, sys
from random import randint, choice

#local imports
from base_obj import BaseObj
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

    def draw(self):
        self.move()
        pygame.draw.rect(
            self.display_surface,
            self.color,
            (self.x, self.y, self.wx, self.wy)
        )


class Stars(object):
    def __init__(self):
        self.stars_list = []

    def add_to_end(self, star):
        self.stars_list.append(star)

    def remove_item(self, star):
        self.stars_list.remove(star)

    def clear_list(self):
        self.stars_list = []

    def draw(self):
        for star in self.stars_list:
            star.draw()


def add_star_row(quantity=10):
    # add first in the row
    for i in range(randint(1,quantity)):
        add_star()


def add_star():
        stars.add_to_end(Star())


global stars
stars = Stars()
