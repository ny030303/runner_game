import pygame
tmxdata = pytmx.TiledMap("map.tmx")

from pytmx import load_pygame
tmxdata = load_pygame("map.tmx")
image = tmx_data.get_tile_image(x, y, layer)
screen.blit(image, position)
tmxdata = TiledMap('level1.tmx')
props = txmdata.get_tile_properties(x, y, layer)
props = tmxdata.get_layer_by_name("dirt").properties
tmxdata = TiledMap.from_string(xml_string)