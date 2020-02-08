
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
        self.root_node = None
        self.last_node = None

    def get_last(self):
        return self.last_node

    def get_root(self):
        return self.root_node

    def push(self, meteor_node):
        if self.root_node!=None:
            self.root_node.previous_node = meteor_node
            meteor_node.next_node = self.root_node
        else:
            self.last_node = meteor_node
        self.root_node = meteor_node


    def traverse(self, node=None, **kwargs):
        if node is None:
            node = self.root_node
        if self.root_node is not None:
            # call functino on the meteor
            if 'call_function' in kwargs:
                if 'call_function' in kwargs:
                    getattr(
                        node.meteor,
                        kwargs['call_function']
                    )(**kwargs)

            if node.next_node != None:
                self.traverse(node=node.next_node, **kwargs)

    def remove_item(self, meteor_node):
        if meteor_node == self.root_node:
            self.get_root = meteor_node.next_node
            meteor_node.next_node.previous_node = None
        elif meteor_node == self.last_node:
            self.last_node = meteor_node.previous_node
            meteor_node.previous_node.next_node = None
        else:
            meteor_node.previous_node.next_node = meteor_node.next_node
            meteor_node.next_node.previous_node = meteor_node.previous_node
        del meteor_node.meteor
        del meteor_node


    def draw_meteors(self):
        if self.get_root() != None :
            current_node = self.get_root()
            while current_node.next_node != None:
                current_node.meteor.draw()
                current_node = current_node.next_node
            self.get_last().meteor.draw()
            # check if meteors left the game area
            if current_node.meteor.y > game_area[1]:
                player_stats.set(-1, 'points')
                self.remove_item(current_node)
            # else:
            #     current_node.meteor.draw()

class MeteorNode(object):
    def __init__(self, meteor=None):
        self.meteor = meteor if meteor != None else Meteor()
        self.next_node = None
        self.previous_node = None


def add_meteor_row():
    # add first in the row
    add_meteor(x=grid_x, y=0)
    # add rest meteors
    root_meteor_x = meteors.get_root().meteor.x
    while root_meteor_x + meteor_x + grid_x <= game_area[0]:
        add_meteor(x=root_meteor_x + meteor_x + grid_x, y=0)
        root_meteor_x = meteors.get_root().meteor.x



def add_meteor(x,y):
    if meteors.get_root():
        root_meteor = meteors.get_root().meteor
        meteors.push(
            MeteorNode(
                Meteor(
                    x=x
                )
            )
        )
    else:
        # First Meteor added to the row
        meteors.push(MeteorNode(
            Meteor(x=x)
        ))

global meteors
meteors = Meteors()
