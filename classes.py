# import libraries and modules
import pygame
import pygame as pg
from pygame.sprite import Sprite
from random import randint
from setting import *

# Classes
class World():
    def __init__(self, data):
        # list to store the data from the construction of the world
        self.title_list = []    
        # load images
        ice_img = pygame.image.load("PLACEHOLDER")

        # this loop will load in a img then scale that by the tile size and make a rectangle from that
        row_count = 0
        for row in data:
            # varable allow for for loop know where to put tile from the world_data information
            col_count = 0 
            for tile in row:
                if tile ==1:
                    img = pygame.transform.scale(ice_img, tile_size, tile_size)
                    # gives imported image convert it into rectangle object to store its information used later for collision 
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    # save both img_rect and the img in a touple
                    tile = (img, img_rect)
                    # use append function from python to add to list
                    self.title_list.append(tile)
                col_count += 1
            row_count += 1
    # draw method
    def draw(self):
        for tile in self.tile_list:
            # to draw the img import
            screen.blit(tile[0], tile[1])

class Player():
    def __inti__(self, x ,y):
        # load the player image. will be penguin 
        img = pygame.image.load("PLACEHOLDER")
        self.image = pygame.transform.scale(img,(40,80))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel_y = 0
        self.jumped = False

    def update(self):
        dx = 0
        dy = 0
        
        # movement inputs
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and self.jumped == False:
            self.vel.y = -15
            self.jumped = True
        if key[pygame.K_SPACE]:
            self.jumped = False
        if key[pygame.K_LEFT]:
            dx -= 5
        if key[pygame.K_RIGHT]:
            dx += 5

        # add gravity
        self.vel_y += 1
        if self.vel_y > 10:
            self.vel.y = 10
        dy += self.vel_y

        # update player cordinates
        self.rect.x += dx
        self.rect.y +=dy

        # Make sure player not fall through Screen
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
            dy = 0
        
        screen.blit(self.image, self.rect)