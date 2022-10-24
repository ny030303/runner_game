import pygame
import package
from package.Model.User import User

class UserController():
    def __init__(self):
        self.all_user_list = pygame.sprite.Group()
        self.all_user_list.add(User())
 
    # def update(self):
    #     print("here!")