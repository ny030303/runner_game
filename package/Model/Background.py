from random import random
import pygame
from GameMain import SCREEN_HEIGHT, SCREEN_WIDTH

class Background(pygame.sprite.Sprite):
    """ This class represents a simple block the player collects. """
 
    def __init__(self, bgInfo, wPos):
        """ Constructor, create the image of the block. """
        super().__init__()
        self.bgInfo = bgInfo
        self.imgWSize = int (bgInfo["width"]) * 3
        
        self.image = pygame.image.load("./images/PNG/environment/layers/"+bgInfo["url"])
        self.image = pygame.transform.scale(self.image, (self.imgWSize, SCREEN_HEIGHT)) # 이미지 스케일링
        self.rect = self.image.get_rect()
        if wPos == 0: self.rect.x = 0
        elif wPos == 1: self.rect.x = self.imgWSize
        elif wPos == 2: self.rect.x = - (self.imgWSize)
 
    def reset_pos(self):
        """ Called when the block is 'collected' or falls off
            the screen. """
        # self.rect.y = random.randrange(-300, -20)
        # self.rect.x = random.randrange(SCREEN_WIDTH)
        self.rect.x = - (self.imgWSize)
    
    #Move layer left/right
    def shiftLevelX(self, shiftX):
        self.levelShiftX += shiftX
        
        for layer in self.layers:
            for tile in layer.tiles:
                tile.rect.x += shiftX
 
    def update(self):
        """ Automatically called when we need to move the block. """
        if self.rect.x > SCREEN_WIDTH:
            self.reset_pos()
        # self.rect.x = int (self.bgInfo["speed"]) + self.rect.x
        # print(self.bgInfo["name"] + ": " + str(self.rect.x))