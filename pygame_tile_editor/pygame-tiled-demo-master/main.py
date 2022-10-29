import pygame, pytmx
from level import Level
from player import Player

#Background color
BACKGROUND = (20, 20, 20)

SCREEN_WIDTH = 720
SCREEN_HEIGHT = 480

#Tiled map layer of tiles that you collide with
MAP_COLLISION_LAYER = 1

class Game(object):
    def __init__(self):
        #Set up a level to load
        self.currentLevelNumber = 0
        self.levels = []
        self.levels.append(Level(fileName = "resources/level1.tmx"))
        self.currentLevel = self.levels[self.currentLevelNumber]
        
        #Create a player object and set the level it is in
        self.player = Player(x = 200, y = 100)
        self.player.currentLevel = self.currentLevel
        
        #Draw aesthetic overlay
        self.overlay = pygame.image.load("resources/overlay.png")
        
    def processEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            #Get keyboard input and move player accordingly
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.goLeft()
                elif event.key == pygame.K_RIGHT:
                    self.player.goRight()
                elif event.key == pygame.K_UP:
                    self.player.jump()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and self.player.changeX < 0:
                    self.player.stop()
                elif event.key == pygame.K_RIGHT and self.player.changeX > 0:
                    self.player.stop()
            
        return False
        
    def runLogic(self):
        #Update player movement and collision logic
        self.player.update()
    
    #Draw level, player, overlay
    def draw(self, screen):
        screen.fill(BACKGROUND)
        self.currentLevel.draw(screen)
        self.player.draw(screen)
        screen.blit(self.overlay, [0, 0])
        pygame.display.flip()
        



def main():
    pygame.init()
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    pygame.display.set_caption("Pygame Tiled Demo")
    clock = pygame.time.Clock()
    done = False
    game = Game()
    
    while not done:
        done = game.processEvents()
        game.runLogic()
        game.draw(screen)
        clock.tick(60)
        
    pygame.quit()
    
main()
