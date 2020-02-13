import pygame, sys
from settings import *
pygame.font.init()



class PlayerStats(object):
    def __init__(self):
        self.level = 0
        self.amunition = 100
        self.health = 100
        self.points = 0
        self.font = pygame.font.Font('freesansbold.ttf', 20)

    def draw(self):
        text_points = self.font.render(
            'Points: {}'.format(self.points),
            True,
            colors['white']
        )
        text_amunition = self.font.render(
            'Amunition: {}'.format(self.amunition),
            True,
            colors['white']
        )
        text_health = self.font.render(
            'Health: {}'.format(self.health),
            True,
            colors['red']
        )
        text_next_level = self.font.render(
            'next level: {}pt'.format((self.level * 15) + 15),
            True,
            colors['white']
        )
        for i in range(int(self.health/2)):
            pygame.draw.rect(
                DISPLAYSURF,
                colors['red'],
                (350+(i*2), 280, 1, 25)
            )
        text_level = self.font.render(
            'level: {}'.format(self.level),
            True,
            colors['light-green']
        )
        DISPLAYSURF.blit(text_amunition,(350,50))
        DISPLAYSURF.blit(text_points,(350,150))
        DISPLAYSURF.blit(text_health,(350,250))
        DISPLAYSURF.blit(text_level,(350,350))
        DISPLAYSURF.blit(text_next_level,(350,450))

    def set(self, value=0, property=None):
        if property!=None:
            value += getattr(self, property)
            setattr(self, property, value)

    def get(self, property):
        if property != None:
            return getattr(self, property)

    def clear_results(self):
        self.level = 0
        self.amunition = 100
        self.health = 100
        self.points = 0


player_stats = PlayerStats()
