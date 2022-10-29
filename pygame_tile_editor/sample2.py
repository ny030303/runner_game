import pygame
from pytmx import load_pygame
import random


white = (255,255,255)


#create window
screenSize = (800,600)
screen = pygame.display.set_mode(screenSize)
pygame.display.set_caption("GameName")
screen.fill(white)

backgroundfile = pygame.image.load("./images/PNG/environment/layers/tileset.png")
gameMap = load_pygame("./package/Data/untitled.tmx")

#Original code    

#create a list of 2600 single tiles in first layer
images = []

for y in range(51):
    for x in range(80):
        image = gameMap.get_tile_image(x,y,0)
        images.append(image)

#blit all tiles onto the screen
i = 0 #runs from 0 to 2600

# print(images[1])
# if(images[1])
for y in range(51):
    for x in range(80):
        # print("i: " + str(images[i]))
        screen.blit(images[i],(x * 15, y * 15))
        i += 1

#Orginal code

#main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()