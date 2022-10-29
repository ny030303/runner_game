from random import random
from unicodedata import name
import pygame

from GameMain import MAP_COLLISION_LAYER, SCREEN_HEIGHT, SCREEN_WIDTH

USER_IMAGE_ARR = [
    {
        "name": "idle",
        "url": 'images\PNG\sprites\player\player-idle\player-idle-',
        "size": 9
    },
    {
        "name": "climb",
        "url": 'images\PNG\sprites\player\player-climb\player-climb-',
        "size": 4
    },
    {
        "name": "duck",
        "url": 'images\PNG\sprites\player\player-duck\player-duck-',
        "size": 4
    },
    {
        "name": "fall",
        "url": 'images\PNG\sprites\player\player-fall\player-fall-',
        "size": 4
    },
    {
        "name": "hurt",
        "url": 'images\PNG\sprites\player\player-hurt\player-hurt-',
        "size": 2
    },
    {
        "name": "jump",
        "url": 'images\PNG\sprites\player\player-jump\player-jump-',
        "size": 4
    },
    {
        "name": "skip",
        "url": 'images\PNG\sprites\player\player-skip\player-skip-',
        "size": 8
    }
]

class User(pygame.sprite.Sprite):
    """ This class represents a simple block the player collects. """
 
    def __init__(self):
        super().__init__()
        self.img_num = 0
        self.img_frame = 1
        self.image = pygame.image.load(str(USER_IMAGE_ARR[self.img_num]["url"])+str(self.img_frame) + '.png')
        self.image = pygame.transform.scale(self.image, (90, 90)) # 이미지 스케일링
        self.rect = self.image.get_rect()
        
        # self.reset_pos()
        self.changeX = 0
        self.changeY = 0
        self.direction = "right"
        
        #Boolean to check if player is running, current running frame, and time since last frame change
        self.running = False
        self.runningFrame = 0
        self.runningTime = pygame.time.get_ticks()
        
        self.ducking = False
        
        #Players current level, set after object initialized in game constructor
        self.currentLevel = None
        
        self.reset_pos()
 
    def reset_pos(self):
        """ Called when the block is 'collected' or falls off
            the screen. """
        self.rect.y = 31*10
        self.rect.x = 0
        
    def draw_frame_img(self):
        self.img_frame += 0.5
        # print(self.img_frame)
        if self.img_frame > USER_IMAGE_ARR[self.img_num]["size"]: self.img_frame = 1
        if self.img_frame % 1 == 0:
            self.image = pygame.image.load(str(USER_IMAGE_ARR[self.img_num]["url"])+str(int(self.img_frame)) + '.png')
            self.image = pygame.transform.scale(self.image, (90, 90)) # 이미지 스케일링
            if self.direction == "left":
                self.image = pygame.transform.flip(self.image, True, False)
            # self.rect = self.image.get_rect()
    
    #Make player jump
    def jump(self):
        #Check if player is on ground
        print(self.rect.y)
        self.rect.y += 2
        tileHitList = pygame.sprite.spritecollide(self, self.currentLevel.layers[MAP_COLLISION_LAYER].tiles, False)
        self.rect.y -= 2
        
        if len(tileHitList) > 0:
            self.img_num = 5
            self.changeY = -6 
        
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
    
    def duck(self):
        self.running = False
        self.changeX = 0
        
    #Draw player
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
    def update(self):
            # """ Automatically called when we need to move the block. """
            #Update player position by change
        
        
        # print(self.changeX, ", ", self.changeY)
        self.rect.x += self.changeX
        
        #Get tiles in collision layer that player is now touching
        tileHitList = pygame.sprite.spritecollide(self, self.currentLevel.layers[MAP_COLLISION_LAYER].tiles, False)
        
        #Move player to correct side of that block
        for tile in tileHitList:
            if self.changeX > 0:
                self.rect.right = tile.rect.left
            else:
                self.rect.left = tile.rect.right
        
        #Move screen if player reaches screen bounds
        if self.rect.right >= SCREEN_WIDTH - 400:
            difference = self.rect.right - (SCREEN_WIDTH - 400)
            self.rect.right = SCREEN_WIDTH - 400
            self.currentLevel.shiftLevelX(-difference)
        
        #Move screen is player reaches screen bounds
        if self.rect.left <= 400:
            difference = 400 - self.rect.left
            self.rect.left = 400
            self.currentLevel.shiftLevelX(difference)
            
        if self.rect.bottom >= SCREEN_HEIGHT - 400:
            difference = self.rect.bottom - (SCREEN_HEIGHT - 400)
            self.rect.bottom = SCREEN_HEIGHT - 400
            self.currentLevel.shiftLevelY(-difference)
        
        #Move screen is player reaches screen bounds
        if self.rect.top <= 200:
            difference = 200 - self.rect.top
            self.rect.top = 200
            self.currentLevel.shiftLevelY(difference)
            
            
        #Update player position by change
        self.rect.y += self.changeY
        
        #Get tiles in collision layer that player is now touching
        tileHitList = pygame.sprite.spritecollide(self, self.currentLevel.layers[MAP_COLLISION_LAYER].tiles, False)
       
        #If there are tiles in that list
        if len(tileHitList) > 0:
            #Move player to correct side of that tile, update player frame
            for tile in tileHitList:
                if self.changeY > 0:
                    self.rect.bottom = tile.rect.top
                    self.changeY = 1
                    
                else:
                    self.rect.top = tile.rect.bottom
                    self.changeY = 0
        #If there are not tiles in that list
        else:
            #Update player change for jumping/falling and player frame
            self.changeY += 0.2
            if self.changeY > 0:
                self.img_num = 3
            else:
                self.img_num = 5
        
        #If player is on ground and running, update running animation
        if self.running and self.changeY == 1:
                self.img_num = 6
        
        
        #-------------
        # stand player
        if self.running == False and len(tileHitList) > 0:
            self.img_num = 0
            
            
        #When correct amount of time has passed, go to next frame
        if pygame.time.get_ticks() - self.runningTime > 50:
            self.runningTime = pygame.time.get_ticks()
            if self.runningFrame == 4:
                self.runningFrame = 0
            else:
                self.runningFrame += 1
        self.draw_frame_img()