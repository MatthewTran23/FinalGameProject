'''
Penguin Slide final Project

discription: a obsticle based platformer with the goal of making a user accesssable playing experience 

required files: sprites import, main.py, class.py, settings.py, function.py

libraries: pygame, more depends

Sources: 
    -https://www.pygame.org/docs/
    -https://www.geeksforgeeks.org/python-call-function-from-another-file/
    -https://opengameart.org/content/tux-bros

Art Credit:
    -https://opengameart.org/content/polar-bear-platformer
    -https://caz-creates-games.itch.io/cute-penguin-sprite-idle-run-attack
    -https://omniclause.itch.io/spikes

Construction Steps
    -Add needed libraries in all files
    -Make game loop in Main.py
    -Make classes in class.py
    -Add window and global variable settings in settings.py

'''
# import libraries and module
import pygame
import pygame as pg
from pygame.sprite import Sprite
from random import randint
from setting import *
from classes import *
from functions import *

# game loop
while run == True:
    clock.tick(FPS)
    if menu == True:
        keys = pg.key.get_pressed()
        # draw backgound
        screen.blit(background, (0,0))
        draw_text("Penguin Run", 18, BLACK, WIDTH/2, HEIGHT / 2- 50)
        draw_text("SPACE to start", 18, BLACK, WIDTH/2, (HEIGHT /2)+50)
        if keys[pg.K_SPACE]:
            menu = False   
    if menu == False:
        # draw backgound
        screen.blit(background, (0,0))
        # call the method to draw the world 
        game_world.draw()
        spike_group.draw(screen)
        door_group.draw(screen)
        # player update method called
        player.update()

        ## draw lose text with if conditions
        draw_text("HEALTH: " + str(player.health), 35, WHITE, 150, HEIGHT / 24)
        if player.health <= 0:
            draw_text("YOU LOSE", 50, RED, WIDTH / 2, 320)
            player.playerkill()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    pg.display.update()

    screen.fill(BLACK)

pg.quit()