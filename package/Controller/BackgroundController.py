import pygame
import package
from package.Model.Background import Background

class BackgroundController():
    def __init__(self):
        self.img_url_list = [
            {
                "name": "bg1",
                "url": "background.png",
                "width": 192,
                "speed": 1
            },
            {
                "name": "bg2",
                "url": "middleground.png",
                "width": 384,
                "speed": 2
            }
        ]
        self.all_bg_list = pygame.sprite.Group()
        self.init()
    
    def init(self):
        for i in range(0, len(self.img_url_list)):
            self.all_bg_list.add(Background(self.img_url_list[i], 0))
            self.all_bg_list.add(Background(self.img_url_list[i], 1))
            self.all_bg_list.add(Background(self.img_url_list[i], 2))
            
    def update(self):
        print("here!")
        
        