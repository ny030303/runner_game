import pygame
import package
from package.Model.Background import Background

from GameMain import MAP_COLLISION_LAYER, SCREEN_HEIGHT, SCREEN_WIDTH
class BackgroundController():
    def __init__(self):
        self.img_url_list = [
            {
                "name": "bg1",
                "url": "background.png",
                "width": 192,
                "speed": 0.2
            },
            {
                "name": "bg2",
                "url": "middleground.png",
                "width": 384,
                "speed": 0.4
            }
        ]
        self.bgShiftX = 0
        
        self.all_bg_list = []
        self.all_bg_list.append(pygame.sprite.Group())
        self.all_bg_list.append(pygame.sprite.Group())
        self.init()
    
    def init(self):
        for i in range(0, len(self.img_url_list)):
            self.all_bg_list[i].add(Background(self.img_url_list[i], 0))
            self.all_bg_list[i].add(Background(self.img_url_list[i], 1))
            self.all_bg_list[i].add(Background(self.img_url_list[i], 2))
            self.all_bg_list[i].add(Background(self.img_url_list[i], 3))
            self.all_bg_list[i].add(Background(self.img_url_list[i], 4))
            
    def update(self):
        print("here!")
    
    #Move layer left/right
    def shiftBgX(self, shiftX):
        self.bgShiftX += shiftX
        # print(shiftX)
        for i in range(0, len(self.img_url_list)):
            for bg in self.all_bg_list[i]:
                # print(float(bg.bgInfo["speed"]))
                if 0.4 == float(bg.bgInfo["speed"]):
                    bg.moveX(shiftX*float(bg.bgInfo["speed"]))
                    
        
    #Update layer
    def draw(self, screen):
        for i in range(0, len(self.img_url_list)):
            for bg in self.all_bg_list[i]:
                if bg.rect.x > (bg.imgWSize*2):
                    bg.rect.x = - (bg.imgWSize*2)
                elif bg.rect.x < - (bg.imgWSize*2):
                    bg.rect.x = (bg.imgWSize*2)
        
            self.all_bg_list[i].draw(screen)
        
        