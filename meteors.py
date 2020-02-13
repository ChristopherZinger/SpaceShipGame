
'''
Meteors are stored as a linked list with root and last node.
Nodes have two pointers. One to next and one to previous node.
'''
# python modules
import pygame, sys
from random import randint, choice
import time

#local imports
from colisions import detect_colision, left_game_area
from base_obj import BaseObj
from playerstats import player_stats
from settings import *
from spacecraft import craft


class Meteor(BaseObj):
    def __init__(self, x=grid_x, y=0, wx=meteor_x, wy=meteor_y,  color=(255,255,255)):
        super().__init__(x=x, y=y, wx=wx, wy=wy)
        self.color = color
        self.display_surface = DISPLAYSURF

    def destruct(self):
        #lunch exploded meteor Animation
        for i in range(randint(7,15)):
            exploded_meteors_list.add(
                ExplodedMeteor(self.x,self.y)
            )
        # remove meteor form list and delete object
        meteors.remove_item(self)
        del self

    def move(self,**kwargs):
        if 'vector' in kwargs:
            self.x += kwargs['vector'][0]
            self.y += kwargs['vector'][1]
        if left_game_area(self):
            meteors.remove_item(self)
            player_stats.points -= 1
            del self

    def draw(self, **kwargs):
        pygame.draw.rect(
            self.display_surface,
            self.color,
            (self.x, self.y, self.wx, self.wy)
        )

    def colision(self, **kwargs):
        # check for colision with player's spaceship
        if detect_colision(self, craft):
            player_stats.health -= 10
            self.destruct()
            return
        # check for colision with shots
        for i in kwargs['colision_items'].shots:
            if detect_colision(self, i) != None:
                player_stats.set(2, 'amunition')
                player_stats.set(1, 'points')
                #remove bullet from lunched_shots
                kwargs['colision_items'].remove_item(i)
                self.destruct()
                return



class Meteors(object):
    def __init__(self):
        self.meteors_list = []

    def add_to_end(self, meteor):
        # if meteor.__class__.__name__ == 'Meteor':
        self.meteors_list.append(meteor)

    def traverse(self, **kwargs):
        if 'call_function' in kwargs:
            for meteor in self.meteors_list:
                    getattr(
                        meteor,
                        kwargs['call_function']
                    )(**kwargs)

    def remove_item(self, meteor):
        self.meteors_list.remove(meteor)

    def clear_list(self):
        self.meteors_list = []


class ExplodedMeteor(BaseObj):
    def __init__(self,x,y):
        super().__init__(x=x,y=y,wx=2,wy=2)
        self.color = colors['gray']
        self.display_surface = DISPLAYSURF
        #generate vector
        vector_choice = [i for i in range(-5,5)]
        vector_choice.remove(0)
        self.vector = [choice(
            vector_choice
        ) for i in range(2)]

    def move(self):
        self.x += self.vector[0]
        self.y += self.vector[1]
        if left_game_area(self):
            exploded_meteors_list.remove_item(self)
            del self

    def draw(self):
        pygame.draw.rect(
            self.display_surface,
            (255,255,255),
            (self.x, self.y, self.wx, self.wy)
        )
        self.move()


class ExplodedMeteorsList(object):
    def __init__(self):
        self.list = []

    def add(self,item):
        self.list.append(item)

    def draw(self):
        if len(self.list) > 0:
            for i in self.list:
                i.draw()
    def remove_item(self, item):
        self.list.remove(item)


def add_meteor_row():
    # add first in the row
    margin_right = (meteor_x*1.2)
    margin_left = 50
    x_offset = randint(margin_left, (meteor_x + grid_x)*3)
    add_meteor(x_offset, y=0)
    # add rest meteors
    previous_meteor_x = meteors.meteors_list[-1].x
    x_offset = previous_meteor_x + randint(margin_left, (meteor_x + grid_x)*3)
    while x_offset + margin_right  <= game_area[0]:
        add_meteor(x=x_offset, y=0)
        previous_meteor_x = meteors.meteors_list[-1].x
        x_offset = previous_meteor_x + randint(margin_left, (meteor_x + grid_x)*3)


def add_meteor(x,y):
        meteors.add_to_end(
            Meteor(
                x=x
            )
        )


global meteors, exploded_meteors_list
meteors = Meteors()
exploded_meteors_list = ExplodedMeteorsList()
