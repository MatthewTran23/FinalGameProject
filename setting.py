# libraries
import pygame# import libraries and modules
import pygame, sys
import pygame as pg
from pygame.sprite import Sprite
from random import randint
# settings

# short hand for pygame vector for ease of use
vec = pg.math.Vector2

# game settings 
WIDTH = 1600
HEIGHT = 800
FPS = 30
screen= pg.display.set_mode((WIDTH,HEIGHT))
clock = pg.time.Clock()
mpos = (0,0)

# define color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0) 
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Level Map
level_map = [
'                       ',
'                       ',
'                       ',
'                       ',
'                       ',
'                       ',
'                       ',
'                       ',
'                       ',
'                       ',
'                       ',
'                       ',
'                       ']

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    
    screen.fill(BLACK)