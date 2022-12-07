# libraries
import pygame# import libraries and modules
import pygame, sys
import pygame as pg
from pygame.sprite import Sprite
from pygame.locals import *
from random import randint
# settings

# short hand for pygame vector for ease of use
vec = pg.math.Vector2

# game settings
WIDTH = 800
HEIGHT = 800
FPS = 60
screen= pg.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Penguin Run")
clock = pg.time.Clock()
mpos = (0,0)

# define color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0) 
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Background img Import
background = pygame.image.load('moutain_background2.png')

# tile size
tile_size = 50

# Level Map
level_map = [
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,1,0,0,1,0,1,0,0,0,0,0,0],
[0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0],
[0,0,0,0,1,1,1,1,0,1,0,0,0,0,0,0],
[0,0,0,0,1,0,0,1,0,1,0,0,0,0,0,0],
[0,0,0,0,1,0,0,1,0,1,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0],
[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
]
