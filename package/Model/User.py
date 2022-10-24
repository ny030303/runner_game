from random import random
import pygame
from GameMain import SCREEN_HEIGHT, SCREEN_TILE, SCREEN_WIDTH

class User(pygame.sprite.Sprite):
    """ This class represents a simple block the player collects. """
 
    def __init__(self):
        """ Constructor, create the image of the block. """
        super().__init__()
        self.img_frame = 1
        self.image = pygame.image.load('images\PNG\sprites\player\player-idle\player-idle-'+str(self.img_frame) + '.png')
        self.image = pygame.transform.scale(self.image, (SCREEN_TILE, SCREEN_TILE)) # 이미지 스케일링
        self.rect = self.image.get_rect()
        
        self.reset_pos()
 
    def reset_pos(self):
        """ Called when the block is 'collected' or falls off
            the screen. """
        self.rect.y = 0
        self.rect.x = 0
 
    def update(self):
        # """ Automatically called when we need to move the block. """
        self.img_frame += 1
        if self.img_frame > 9: self.img_frame = 1
        self.image = pygame.image.load('images\PNG\sprites\player\player-idle\player-idle-'+ str(self.img_frame) + '.png')
        self.image = pygame.transform.scale(self.image, (50, 50)) # 이미지 스케일링
        self.rect = self.image.get_rect()
 