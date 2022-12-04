import pygame
import package
from package.Model.Background import Background

from GameMain import MAP_COLLISION_LAYER, SCREEN_HEIGHT, SCREEN_WIDTH
class BackgroundController():
    def __init__(self, levelNum):
        self.img_url_list = [
            {
                "name": "bg1",
                "url": "background.png",
                "width": 190,
                "num": 0,
                "speed": 1
            },
            {
                "name": "bg2",
                "url": "middleground.png",
                "width": 384,
                "speed": 2
            }
        ]
        
        self.img_url_list2 = [
            {
                "name": "bg1",
                "url": "background2.png",
                "width": 190,
                "num": 0,
                "speed": 1
            },
            {
                "name": "bg2",
                "url": "middleground2.png",
                "width": 384,
                "speed": 2
            }
        ]
        
        self.bgShiftX = 0
        
        # self.all_bg_list = []
        # self.all_bg_list.append(pygame.sprite.Group())
        # self.all_bg_list.append(pygame.sprite.Group())
        
        self.bg1List = pygame.sprite.Group()
        self.bg2List = pygame.sprite.Group()
        self.init(levelNum)
    
    def init(self, levelNum):
        if levelNum == 0:
            self.bg1List.add(Background(self.img_url_list[0], 0))
            self.bg1List.add(Background(self.img_url_list[0], 1))
            self.bg1List.add(Background(self.img_url_list[0], 2))
            
            self.bg2List.add(Background(self.img_url_list[1], 0))
            self.bg2List.add(Background(self.img_url_list[1], 1))
            self.bg2List.add(Background(self.img_url_list[1], 2))
        else:
            self.bg1List.add(Background(self.img_url_list2[0], 0))
            self.bg1List.add(Background(self.img_url_list2[0], 1))
            self.bg1List.add(Background(self.img_url_list2[0], 2))
            
            self.bg2List.add(Background(self.img_url_list2[1], 0))
            self.bg2List.add(Background(self.img_url_list2[1], 1))
            self.bg2List.add(Background(self.img_url_list2[1], 2))
            
    def update(self):
        print("here!")
    
    #Move layer left/right
    def shiftBgX(self, shiftX, mt):
        self.bgShiftX += shiftX
        # print(shiftX)
        tmp_bgs = self.bg1List.sprites()
        # print(' #0 ' , tmp_bgs[0].rect.x, tmp_bgs[0].bgInfo["speed"], tmp_bgs[1].rect.x, tmp_bgs[1].bgInfo["speed"], tmp_bgs[2].rect.x, tmp_bgs[2].bgInfo["speed"])
        for bg in tmp_bgs:
            # print(' #0 ' , bg.bgInfo["num"], bg.rect.x, "shiftX:", shiftX)
            if shiftX > 0:
                bg.moveX(float(bg.bgInfo["speed"]))
            elif shiftX < 0:
                bg.moveX(-(float(bg.bgInfo["speed"])))                
            
            if (bg.rect.x) < -(bg.imgWSize + 200):
                bg.rect.x += (bg.imgWSize*3)
            if (bg.rect.x) > (960 + 200):
                bg.rect.x -= (bg.imgWSize*3)
            # if (bg.rect.x) == - bg.imgWSize:
            #     bg.rect.x = bg.imgWSize
            # elif (bg.rect.x) == - bg.imgWSize:
            #     bg.rect.x = bg.imgWSize
            
        tmp_bgs = self.bg2List.sprites()
        for bg in tmp_bgs:
            if shiftX > 0:
                bg.moveX(float(bg.bgInfo["speed"]))
            elif shiftX < 0:
                bg.moveX(- (float(bg.bgInfo["speed"])))                
                
            if (bg.rect.x) < -(bg.imgWSize + 200):
                bg.rect.x += (bg.imgWSize*3)
            if (bg.rect.x) > (960 + 200):
                bg.rect.x -= (bg.imgWSize*3)
                    
        
    #Update layer
    def draw(self, screen):
        self.bg1List.draw(screen)
        self.bg2List.draw(screen)
        
        