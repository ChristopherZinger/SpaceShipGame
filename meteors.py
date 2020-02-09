
'''
Meteors are stored as a linked list with root and last node.
Nodes have two pointers. One to next and one to previous node.
'''

import pygame, sys
from settings import *
from colisions import detect_colision
from playerstats import player_stats


class Meteor(object):
    def __init__(self, x=grid_x, y=0, wx=meteor_x, wy=meteor_y, color=(255,255,255)):
        self.x = x
        self.y = y
        self.wy = wy
        self.wx = wx
        self.color = color
        self.display_surface = DISPLAYSURF

    def move(self,**kwargs):
        if 'vector' in kwargs:
            self.x += kwargs['vector'][0]
            self.y += kwargs['vector'][1]
        ## TODO:
        # check if meteor left the game space
        # if yes remove object and decrease palyer points

    def draw(self):
        pygame.draw.rect(
            self.display_surface,
            self.color,
            (self.x, self.y, self.wx, self.wy)
        )

    def colision(self, **kwargs):
        for i in kwargs['colision_items'].shots:
            if detect_colision(self, i) != None:
                player_stats.set(2, 'amunition')
                player_stats.set(1, 'points')
                #remove bullet from lunched_shots
                kwargs['colision_items'].remove_item(i)
                # find meteors node and remove it all together.
                '''
                # TODO:
                following code should be integrated into meteors.traverse()
                '''
                node = meteors.root_node
                if self == node.meteor:
                    meteors.remove_item(node)
                    return
                while node.next_node != None:
                    node = node.next_node
                    if self == node.meteor:
                        meteors.remove_item(node)
                        break



class Meteors(object):
    def __init__(self):
        self.meteors_list = []

    def append(self, meteor):
        # if meteor.__class__.__name__ == 'Meteor':
        self.meteors_list.append(meteor)

    def traverse(self, **kwargs):
        if 'call_function' in kwargs:
            for i in self.meteors_list:
                    getattr(
                        self.meteors_list[i],
                        kwargs['call_function']
                    )(**kwargs)

    def remove_item(self, meteor):
        self.meteors_list.remove(meteor)


def add_meteor_row():
    # add first in the row
    add_meteor(x=grid_x, y=0)
    # add rest meteors
    root_meteor_x = meteors.meteors_list[0].x
    while root_meteor_x + meteor_x + grid_x <= game_area[0]:
        add_meteor(x=root_meteor_x + meteor_x + grid_x, y=0)
        root_meteor_x = meteors.meteors_list[0].meteor.x


def add_meteor(x,y):
        meteors.append(
            Meteor(
                x=x
            )
        )

global meteors
meteors = Meteors()
