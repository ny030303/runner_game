import sys
import pygame
import package

#### pygame에 사용되는 전역변수 선언
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 720
SCREEN_TILE = 75

class GameMain(object):
    
    def __init__(self):
        self.game_over = False
 
        # Create sprite lists
        self.all_sprites_list = pygame.sprite.Group()
        
        # Create the player
        self.player = package.UserController()
        self.background = package.BackgroundController()
        self.all_sprites_list.add(self.background.all_bg_list)
        self.all_sprites_list.add(self.player.all_user_list)
        
    def process_events(self):
        """ Process all of the events. Return a "True" if we need
            to close the window. """
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
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
            
 
    def display_frame(self, screen):
        """ Display everything to the screen for the game. """
        screen.fill((255,255,255))
 
        if self.game_over:
            # font = pygame.font.Font("Serif", 25)
            font = pygame.font.SysFont("serif", 25)
            text = font.render("Game Over, click to restart", True, (0,0,0))
            center_x = (SCREEN_WIDTH // 2) - (text.get_width() // 2)
            center_y = (SCREEN_HEIGHT // 2) - (text.get_height() // 2)
            screen.blit(text, [center_x, center_y])
 
        if not self.game_over:
            self.all_sprites_list.draw(screen)
 
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
        clock.tick(10)
 
    # Close window and exit
    pygame.quit()
 
# Call the main function, start up the game
if __name__ == "__main__":
    main()