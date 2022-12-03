from random import random
from unicodedata import name
import pygame

from GameMain import MAP_COLLISION_LAYER, SCREEN_HEIGHT, SCREEN_WIDTH

BEE_IMAGE_ARR = [
    {
        "name": "bee",
        "url": 'images/PNG/sprites/enemies/bee/bee-',
        "size": 8
    }
]
        
class Bee(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.img_num = 0
        self.img_frame = 1
        
        self.load_img()
        self.rect = self.image.get_rect()
        
        # (100 / 이미지 수) / 100 = (100 / 이미지 수 * 100)
        self.animation_time = round(100 / (BEE_IMAGE_ARR[self.img_num]["size"] * 100), 2)

        # mt와 결합하여 animation_time을 계산할 시간 초기화
        self.current_time = 0
        # self.reset_pos()
        self.changeX = 0
        self.changeY = 0
        self.direction = "right"
        
         #Players current level, set after object initialized in game constructor
        self.currentLevel = None
        self.reset_pos(x,y)
 
    def reset_pos(self,x,y):
        """ Called when the block is 'collected' or falls off
            the screen. """
        self.rect.y = 31*y
        self.rect.x = 31*x
    
    def load_img(self):
        self.image = pygame.image.load(str(BEE_IMAGE_ARR[self.img_num]["url"])+str(int(self.img_frame)) + '.png')
        self.image = self.image.subsurface(6, 0, 31, 39) # 좌표
        self.image = pygame.transform.scale(self.image, (31*1.5, 39*1.5)) # 이미지 스케일링
        
    def draw_frame_img(self):
        if self.img_frame > BEE_IMAGE_ARR[self.img_num]["size"]: self.img_frame = 1
        if self.img_frame % 1 == 0: 
            self.load_img()
            if self.direction == "left":
                self.image = pygame.transform.flip(self.image, True, False)
        
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
        
    def update(self, mt):
        # loop time 경과가 animation_time을 넘어서면 새로운 이미지 출력 
        self.current_time += mt
        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.draw_frame_img()
            
            self.img_frame += 1
            if self.img_frame > int(BEE_IMAGE_ARR[self.img_num]["size"]):
                self.img_frame = 1
        else:
            
            # print(self.img_frame)
            self.draw_frame_img()