import pygame, pytmx

from package.Model.Tile import Tile


class Layer(object):
    def __init__(self, index, mapObject):
        #Layer index from tiled map
        self.index = index
        
        #Create gruop of tiles for this layer
        self.tiles = pygame.sprite.Group()
        
        #Reference map object
        self.mapObject = mapObject
        
        #Create tiles in the right position for each layer
        for x in range(self.mapObject.width):
            for y in range(self.mapObject.height):
                img = self.mapObject.get_tile_image(x, y, self.index)
                if img:
                    prop = self.mapObject.get_tile_properties(x, y, self.index)
                    if prop:
                        self.tiles.add(Tile(image = img, x = (x * self.mapObject.tilewidth), y = (y * self.mapObject.tileheight), type = prop["Type"]))
                    else:
                        self.tiles.add(Tile(image = img, x = (x * self.mapObject.tilewidth), y = (y * self.mapObject.tileheight)))

    #Draw layer
    def draw(self, screen):
        self.tiles.draw(screen)
