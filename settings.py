import pygame, sys, os

BASE_DIR =  os.path.dirname(os.path.realpath(__file__))
print(BASE_DIR)

# Display settings
FPS = 60

window_size = (550,700)
game_area = (300,700)
DISPLAYSURF = pygame.display.set_mode(window_size)
DISPLAYSURFALPHA = DISPLAYSURF.convert_alpha()
#Colors
colors = {
    'cian': (0,255,255),
    'white': (255,255,255),
    'red': (255,0,0),
    'blue': (0,0,255),
    'green': (0,255,0),
    'black': (0,0,0),
    'light-green': (0, 255, 119),
    'gray': (70,70,70),
}

# grid
meteor_x = 10
meteor_y = 10

grid_x = 30
grid_y = 100

fpsClock = pygame.time.Clock()
meteors_in_row = int(game_area[0]/(grid_x+meteor_x))
