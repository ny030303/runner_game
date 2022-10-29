import pygame, pytmx

from layer import Layer
class Level(object):
    def __init__(self, fileName):
        #Create map object from PyTMX
        self.mapObject = pytmx.load_pygame(fileName)
        
        #Create list of layers for map
        self.layers = []
        
        #Amount of level shift left/right
        self.levelShift = 0
        
        #Create layers for each layer in tile map
        for layer in range(len(self.mapObject.layers)):
            self.layers.append(Layer(index = layer, mapObject = self.mapObject))
    
    #Move layer left/right
    def shiftLevel(self, shiftX):
        self.levelShift += shiftX
        
        for layer in self.layers:
            for tile in layer.tiles:
                tile.rect.x += shiftX
    
    #Update layer
    def draw(self, screen):
        for layer in self.layers:
            layer.draw(screen)