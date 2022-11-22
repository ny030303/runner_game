import pygame, pytmx
import package

from package.Model.Layer import Layer

class Level(object):
    def __init__(self, fileName):
        #Create map object from PyTMX
        self.mapObject = pytmx.load_pygame(fileName)
        
        #Create list of layers for map
        self.layers = []
        
        #Create list of enemys for map
        self.enemys = []
        
        #Amount of level shift left/right
        self.levelShiftX = 0
        self.levelShiftY = 0
        
        #Create layers for each layer in tile map
        for layer in range(len(self.mapObject.layers)):
            self.layers.append(Layer(index = layer, mapObject = self.mapObject))
            
        #Create Enemys
        self.enemys.append(package.Bee())
        
        self.shiftLevelY(-31*4)
        
    #Move layer left/right
    def shiftLevelX(self, shiftX):
        self.levelShiftX += shiftX
        
        # layer shift X
        for layer in self.layers:
            for tile in layer.tiles:
                tile.rect.x += shiftX
        
        # enemy shift X
        for enemy in self.enemys:
            enemy.rect.x += shiftX
                
    #Move layer up/down
    def shiftLevelY(self, shiftY):
        self.levelShiftY += shiftY
        
        # layer shift Y
        for layer in self.layers:
            for tile in layer.tiles:
                tile.rect.y += shiftY
        # enemy shift Y   
        for enemy in self.enemys:
            enemy.rect.y += shiftY
            
            
    def update(self):
        for enemy in self.enemys:
            enemy.update()
    
    #Update layer
    def draw(self, screen):
        for layer in self.layers:
            layer.draw(screen)
        
        for enemy in self.enemys:
            enemy.draw(screen)