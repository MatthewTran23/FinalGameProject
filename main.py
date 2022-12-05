'''
Penguin Slide final Project

discription: a obsticle based platformer with the goal of making a user accesssable playing experience 

required files: sprites import, main.py, class.py, settings.py, function.py

libraries: pygame, more depends

Sources: 
    -https://www.pygame.org/docs/
    -https://www.geeksforgeeks.org/python-call-function-from-another-file/
    -https://opengameart.org/content/tux-bros

Construction Steps
    -Add needed libraries in all files
    -Make game loop in Main.py
    -Make classes in class.py
    -Add window and global variable settings in settings.py


'''
# import libraries and modules
import pygame
import pygame as pg
from pygame.sprite import Sprite
from random import randint
from setting import *
from classes import *
from functions import *

# instence of the world class
game_world = World(level_map)

player = Player(100, HEIGHT - 130)

# game loop
run = True
while run==True:

    clock.tick(FPS)
   
    # draw backgound
    screen.blit(background, (0,0))
    # call the method to draw the world 
    game_world.draw()
    
    player.update()

    draw_grid()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    
    pg.display.update()

    screen.fill(BLACK)

pg.quit()