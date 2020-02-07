
'''
Meteors are stored as a linked list with root and last node.
Nodes have two pointers. One to next and one to previous node.
'''

import pygame, sys
from settings import *
from colisions import detect_colision
# from spacecraft import lunched_shots


class Meteor(object):
    def __init__(self, x=30, y=30, wx=5, wy=5, color=(255,255,255)):
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
        if self.color != colors['black']:
            for i in kwargs['colision_items'].shots:
                if detect_colision(self, i) != None:
                    kwargs['colision_items'].remove_item(i)
                    self.color = colors['black']


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
            self.root_node.previous_meteor = meteor_node
            meteor_node.next_meteor = self.root_node
        else:
            self.last_node = meteor_node
        self.root_node = meteor_node

    #moves each meteor one step lower.
    def traverse(self, node=None, **kwargs):
        if node is None:
            node = self.root_node
        if self.root_node is not None:
            if 'call_function' in kwargs:

                if 'call_function' in kwargs:
                    getattr(
                        node.meteor,
                        kwargs['call_function']
                    )(**kwargs)

                #update metheors position
                # if kwargs['call_function']=='move':
                #     getattr(node.meteor, kwargs['call_function'])(kwargs['vector'])

                # handle colision
                # if kwargs['call_function']=='colision':
                #     colision_exists = getattr(
                #         node.meteor,
                #         kwargs['call_function'])(
                #             kwargs['colision_items']
                #         )
                #     if colision_exists:
                #         node.meteor.color = colors['black']
            if node.next_meteor != None:
                self.traverse(node=node.next_meteor, **kwargs)

    def draw_meteors(self):
        if self.root_node != None :
            current_node = self.root_node
            current_node.meteor.draw()
            while current_node.next_meteor != None:
                current_node = current_node.next_meteor
                current_node.meteor.draw()


class MeteorNode(object):
    def __init__(self, meteor=None):
        self.meteor = meteor if meteor != None else Meteor()
        self.next_meteor = None
        self.previous_meteor = None


def add_meteor_row():
    for i in range(8):
        add_meteor()


def add_meteor():
    if meteors.get_root() != None:
        if meteors.get_root().meteor.x < 260:
            meteors.push(
                MeteorNode(
                    Meteor(x=(meteors.get_root().meteor.x+40))
                )
            )
        else:
            #new line of meteors
            meteors.push(
                MeteorNode(
                    Meteor(x=30)
                )
            )
    else:
        # First Meteor added to the Meteors
        meteors.push(MeteorNode(
            Meteor()
        ))


meteors = Meteors()
