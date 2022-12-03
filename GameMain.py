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
        self.currentLevelNumber = 1
        self.currentBgNumber = 0
        
        # 게임시작, 게임오버 버튼 이미지
        self.btn_start = pygame.image.load("images\PNG\environment\gamestart.png")
        self.btn_start = pygame.transform.scale(self.btn_start, (700, 280))
        self.btn_over = pygame.image.load("images\PNG\environment\gameover.png")
        self.btn_over = pygame.transform.scale(self.btn_over, (700, 280))
        
        self.start_game = False
        
        # Create sprite lists
        self.all_sprites_list = pygame.sprite.Group()
        
        # Create your Level (first level is 1)
        self.levels = [] 
        self.levels.append(package.Level(fileName = "./Resources/level1.tmx"))
        self.levels.append(package.Level(fileName = "./Resources/level2.tmx"))
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
    
    def check_swipe_level(self):
        # print(self.player.starCount )
        if self.player.starCount > self.currentLevelNumber:
            self.currentLevelNumber += 1
            self.currentLevel = self.levels[self.currentLevelNumber]
            self.player.currentLevel = self.currentLevel
            self.player.reset_pos()
    
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
                    self.player.goRight()
                elif event.key == pygame.K_UP:
                    if self.player.climbimg != False:
                            self.player.climb_up()
                    else:
                        self.player.jump()
                elif event.key == pygame.K_DOWN:
                    if self.player.climbimg != False:
                        self.player.climb_down()
                    elif self.player.isHitLadderY != False and self.player.isHitLadderX == False:
                        # ladder-top 위일때 다운
                        self.player.swipe_climb_mode(self.player.isHitLadderY)
                        self.player.climb_down()
                    else:
                        self.player.duck()
                elif event.key == pygame.K_SPACE: # 스페이스바를 누르면 게임시작 버튼이 사라지고 게임시작 플래그 True로 변경
                    if not self.start_game and not self.game_over:
                        self.btn_start = pygame.transform.scale(self.btn_start, (0, 0))
                        self.start_game = True
                elif self.start_game and self.game_over: # 시작버튼 눌림 상태에 게임오버 상태
                    print("대충 리셋하라는 뜻")
                    self.__init__()
                        
            elif event.type == pygame.KEYUP:
                        
                if event.key == pygame.K_LEFT and self.player.changeX < 0:
                    self.player.stopX()
                elif event.key == pygame.K_RIGHT and self.player.changeX > 0:
                    self.player.stopX()

                if self.player.img_num == 1 and event.key == pygame.K_UP and self.player.changeY < 0:
                    self.player.stopY()
                elif self.player.img_num == 1 and event.key == pygame.K_DOWN and self.player.changeY > 0:
                    self.player.stopY()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.game_over:
                    self.__init__()
        return False
    
    def checkGameOver(self):
        if self.player.hp <= 0:
            self.game_over = True
            
    def run_logic(self, mt):
        """
        This method is run each time through the frame. It
        updates positions and checks for collisions.
        """
        if not self.game_over:
            # Move all the sprites
            self.all_sprites_list.update(mt=mt)
            self.currentLevel.update(mt)
            self.check_swipe_level()
 
    def display_frame(self, screen):
        """ Display everything to the screen for the game. """
        # screen.fill((255,255,255))
 
        if self.game_over:
            self.player.hud_draw(screen)
            # font = pygame.font.Font("Serif", 25)
            center_x = (SCREEN_WIDTH // 2) - (self.btn_over.get_width() // 2)
            center_y = (SCREEN_HEIGHT // 2) - (self.btn_over.get_height() // 2)
            screen.blit(self.btn_over, [center_x, center_y])
 
        if not self.game_over:
            self.currentBg.draw(screen)
            if self.start_game:
                self.all_sprites_list.draw(screen)
                self.currentLevel.draw(screen)
                self.player.draw(screen)
            
                self.player.hud_draw(screen)
            
        self.start_display(screen)
        
        pygame.display.flip()

    def start_display(self, screen):
        center_x = (SCREEN_WIDTH // 2) - (self.btn_start.get_width() // 2)
        center_y = (SCREEN_HEIGHT // 2) - (self.btn_start.get_height() // 2)
        screen.blit(self.btn_start, [center_x, center_y])
                
            
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
 
        # Pause for the next frame
        # clock.tick(30)
        # 밀리초를 초로 변경
        mt = clock.tick(60) / 1000
        
        # Update object positions, check for collisions
        
        if game.start_game:
            game.run_logic(mt)
        
        game.checkGameOver()
        # Draw the current frame
        game.display_frame(screen)
 
    # Close window and exit
    pygame.quit()
 
# Call the main function, start up the game
if __name__ == "__main__":
    main()