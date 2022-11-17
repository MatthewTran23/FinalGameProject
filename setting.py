# libraries
import pygame# import libraries and modules
import pygame as pg
from pygame.sprite import Sprite
from random import randint
# settings

# short hand for pygame vector for ease of use
vec = pg.math.Vector2

# game settings 
WIDTH = 500
HEIGHT = 720
FPS = 30
mpos = (0,0)

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)