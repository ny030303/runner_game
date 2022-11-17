from random import random
from unicodedata import name
import pygame

from GameMain import MAP_COLLISION_LAYER, SCREEN_HEIGHT, SCREEN_WIDTH

BEE_IMAGE_ARR = [
    {
        "name": "idle",
        "url": 'images\PNG\sprites\enemies\bee\bee-',
        "size": 8
    }
]
        
class Bee(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.img_num = 0
        self.img_frame = 1
        # print(self.img_frame)
        self.image = pygame.image.load(str(BEE_IMAGE_ARR[self.img_num]["url"])+str(self.img_frame) + '.png')
        # self.image = self.image.subsurface(6, 0, 24, 32) # 좌표
        
        self.image = pygame.transform.scale(self.image, (24*2, 32*2)) # 이미지 스케일링
        self.rect = self.image.get_rect()
        
        # self.reset_pos()
        self.changeX = 0
        self.changeY = 0
        self.direction = "right"
        
        self.reset_pos()
 
    def reset_pos(self):
        """ Called when the block is 'collected' or falls off
            the screen. """
        self.rect.y = 31*10
        self.rect.x = 0
        
    def draw_frame_img(self):
        self.img_frame += 0.5
        # print(self.img_frame)
        if self.img_frame > BEE_IMAGE_ARR[self.img_num]["size"]: self.img_frame = 1
        if self.img_frame % 1 == 0: 
            self.image = pygame.image.load(str(BEE_IMAGE_ARR[self.img_num]["url"])+str(int(self.img_frame)) + '.png')
            # self.image = self.image.subsurface(6, 0, 24, 32)
            self.image = pygame.transform.scale(self.image, (24*2, 32*2)) # 이미지 스케일링
            if self.direction == "left": 
                self.image = pygame.transform.flip(self.image, True, False) # 좌우반전
        
    #Move right
    def goRight(self):
        self.direction = "right"
        self.running = True
        self.changeX = 5
    
    #Move left
    def goLeft(self):
        self.direction = "left"
        self.running = True
        self.changeX = -5
    
    #Stop moving
    def stop(self):
        self.running = False
        self.changeX = 0
        
    #Draw player
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
    def update(self):
        
        self.draw_frame_img()