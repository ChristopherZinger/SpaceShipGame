import pygame, sys
from settings import *
from meteors import meteors
from playerstats import player_stats

class SpaceCraft(object):
    def __init__(self,game_area, color):
        self.x = 150
        self.y = game_area[1] - 20
        self.wy = 8
        self.wx = 8
        self.color = color
        self.vector = [0,0]
        self.display_surface = DISPLAYSURF

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
        pygame.draw.rect(
            self.display_surface,
            self.color,
            (self.x, self.y, self.wx, self.wy)
        )

    def shot(self):
        if player_stats.get('amunition') > 0:
            player_stats.set(-1, 'amunition')
            lunched_shots.push(CraftShot(self.x, self.y))


class CraftShot(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.wx = 2
        self.wy = 2
        self.color = colors['light-green']
        self.display_surface = DISPLAYSURF

    def draw(self):
        pygame.draw.rect(
            self.display_surface,self.color,
            (self.x, self.y, self.wx, self.wy)
        )
        self.y -= 5
        if self.y < 0:
            lunched_shots.remove_item(self)


class LunchedShots():
    def __init__(self):
        self.shots = []

    def push(self, shot):
        self.shots.append(shot)

    def remove_item(self,item):
        self.shots.remove(item)
        del item

    def draw(self):
        if len(self.shots) > 0:
            for i in self.shots:
                i.draw()


craft = SpaceCraft(game_area, colors['light-green'])
global lunched_shots
lunched_shots = LunchedShots()
