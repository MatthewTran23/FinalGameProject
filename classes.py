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
        for tile in self.title_list:
            # to draw the img import
            screen.blit(tile[0], tile[1])

class Player():
    def __inti__(self, x ,y):
        # list of img assets
        self.images_right = []
        self.images_left = []
        self.index = 0
        # use self.counter to track speed of player animation
        self.counter = 0
        # for loop to load multiple imgs
        for num in range(1,5):
            img_right = pygame.image.load(f'PLACEHOLDER')
            img_right = pygame.transform.scale(img_right,(40,80))
            # flip the img right for left using pygame 
            img_left = pygame.transform.flip(img_right, True, False)
            # to not overide use append function. add to list
            self.images_right.append(img_right)
            self.images_left.append(img_left)
        # use the first img from the images_right list whe first loaded in
        self.image = self.images_right[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel_y = 0
        self.jumped = False
        self.direction = 0

    def update(self):
        dx = 0
        dy = 0
        walk_cooldown = 5
        
        # movement inputs based on key presses
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and self.jumped == False:
            self.vel.y = -15
            self.jumped = True
        if key[pygame.K_SPACE] == False:
            self.jumped = False
        if key[pygame.K_LEFT]:
            dx -= 5
            # counter +1 only if movement keys are pressed 
            self.counter +=1
            self.direction = -1
        if key[pygame.K_RIGHT]:
            dx += 5
            # counter +1 only if movement keys are pressed 
            self.counter +=1
            self.direction = 1
        # if statement to reset the image's animation if keys not pressed
        if key[pygame.K_LEFT] == False and key[pygame.K_RIGHT]== False:
            self.counter = 0 
            self.index = 0
            if self.direction == 1:
                self.images = self.images_right[self.index]
            if self.direction == -1:
                self.images = self.images_left[self.index]

        # animatio update. if statement to slow down the animation
        if self.counter > walk_cooldown:
            self.counter = 0 
            self.index +=1 
            # if statement to make sure that the sprite resets once it exceeds the length of the list
            if self.index >= len(self.images_right):
                    self.index = 0
            if self.direction == 1:
                self.images = self.images_right[self.index]
            if self.direction == -1:
                self.images = self.images_left[self.index]

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