import pygame
import package
# from package.Model.Level import Level

#### pygame에 사용되는 전역변수 선언
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 720
SCREEN_TILE = 75

#Tiled map layer of tiles that you collide with
MAP_COLLISION_LAYER = 0

class GameMain(object):
    
    def __init__(self):
        self.game_over = False
        #Set up a level to load
        self.currentLevelNumber = 0
        self.currentBgNumber = 0
 
        # Create sprite lists
        self.all_sprites_list = pygame.sprite.Group()
        
        # Create your Level (first level is 1)
        self.levels = [] 
        self.levels.append(package.Level(fileName = "./Resources/level1.tmx"))
        self.currentLevel = self.levels[self.currentLevelNumber]
        
         # Create the background
        self.bgs = [] 
        self.bgs.append(package.BackgroundController())
        self.currentBg = self.bgs[self.currentBgNumber]
        
        # self.bee.currentLevel = self.currentLevel
        # self.bee.currentBg = self.currentBg
        
        # Create the player
        self.player = package.User()
        self.player.currentLevel = self.currentLevel
        self.player.currentBg = self.currentBg
        
        
        # self.all_sprites_list.add(self.background.all_bg_list)
        self.all_sprites_list.add(self.player)
    def process_events(self):
        """ Process all of the events. Return a "True" if we need
            to close the window. """
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            elif event.type == pygame.KEYDOWN:
                tileHitList = self.player.getTileHitList()
                for tile in tileHitList:
                    if tile.type == "ladder":
                        try:
                            self.player.swipe_climb_mode(self.player.climbimg)
                        except:
                            print('ERR: climb mode was not swiped')
                            
                if event.key == pygame.K_LEFT:
                    self.player.goLeft()
                elif event.key == pygame.K_RIGHT:
                    print(self.player.climbimg)
                    self.player.goRight()
                elif event.key == pygame.K_UP:
                    if self.player.climbimg != False:
                            self.player.climb_up()
                    else:
                        self.player.jump()
                elif event.key == pygame.K_DOWN:
                    if self.player.climbimg != False:
                            self.player.climb_down()
                    else:
                        self.player.duck()
            elif event.type == pygame.KEYUP:
                        
                if event.key == pygame.K_LEFT and self.player.changeX < 0:
                    self.player.stopX()
                elif event.key == pygame.K_RIGHT and self.player.changeX > 0:
                    self.player.stopX()

                if self.player.img_num == 1 and event.key == pygame.K_UP and self.player.changeY < 0:
                    self.player.stopY()
                elif self.player.img_num == 1 and event.key == pygame.K_DOWN and self.player.changeY > 0 :
                    self.player.stopY()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.game_over:
                    self.__init__()
        return False
 
    def run_logic(self):
        """
        This method is run each time through the frame. It
        updates positions and checks for collisions.
        """
        if not self.game_over:
            # Move all the sprites
            self.all_sprites_list.update()
            self.currentLevel.update()
            
 
    def display_frame(self, screen):
        """ Display everything to the screen for the game. """
        # screen.fill((255,255,255))
 
        if self.game_over:
            # font = pygame.font.Font("Serif", 25)
            font = pygame.font.SysFont("serif", 25)
            text = font.render("Game Over, click to restart", True, (0,0,0))
            center_x = (SCREEN_WIDTH // 2) - (text.get_width() // 2)
            center_y = (SCREEN_HEIGHT // 2) - (text.get_height() // 2)
            screen.blit(text, [center_x, center_y])
 
        if not self.game_over:
            self.currentBg.draw(screen)
            self.all_sprites_list.draw(screen)
            self.currentLevel.draw(screen)
            self.player.draw(screen)
 
        pygame.display.flip()
        
def main():
    """ Main program function. """
    # Initialize Pygame and set up the window
    pygame.init()
 
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
 
    pygame.display.set_caption("My Game")
    pygame.mouse.set_visible(False)
 
    # Create our objects and set the data
    done = False
    clock = pygame.time.Clock()
    game = GameMain()
 
    # Main game loop
    while not done:
 
        # Process events (keystrokes, mouse clicks, etc)
        done = game.process_events()
 
        # Update object positions, check for collisions
        game.run_logic()
 
        # Draw the current frame
        game.display_frame(screen)
 
        # Pause for the next frame
        clock.tick(30)
 
    # Close window and exit
    pygame.quit()
 
# Call the main function, start up the game
if __name__ == "__main__":
    main()