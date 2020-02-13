import pygame, sys
from settings import *
from space_travel_loop import space_travel_loop
from menu_loop import menu_loop
print('Space craft game initialized.')

pygame.init()


#Caption
pygame.display.set_caption('Spacecraft Insanity')


#Main Loop
while True:
    menu_loop()
    space_travel_loop()
