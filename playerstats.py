import pygame, sys
from settings import *
pygame.font.init()
print(
    pygame.font.get_init(),
    pygame.font.get_default_font(),
    )


class PlayerStats(object):
    def __init__(self):
        self.level = 0
        self.amunition = 100
        self.health = 100
        self.points = 0
        self.font = pygame.font.Font('freesansbold.ttf', 20)

    def draw(self):
        text_points = self.font.render(
            'points: {}'.format(self.points),
            True,
            colors['white']
        )
        text_amunition = self.font.render(
            'amunition: {}'.format(self.amunition),
            True,
            colors['white']
        )
        DISPLAYSURF.blit(text_amunition,(350,50))
        DISPLAYSURF.blit(text_points,(350,150))

    def set(self, value=0, property=None):
        if property!=None:
            value += getattr(self, property)
            setattr(self, property, value)

    def get(self, property):
        if property != None:
            return getattr(self, property)


player_stats = PlayerStats()
