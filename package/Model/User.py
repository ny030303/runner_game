from random import random
from unicodedata import name
import pygame

from GameMain import MAP_COLLISION_LAYER, SCREEN_HEIGHT, SCREEN_WIDTH

USER_IMAGE_ARR = [
    {
        "name": "idle",
        "url": 'images\PNG\sprites\player\player-idle\player-idle-',
        "size": 9
    },
    {
        "name": "climb",
        "url": 'images\PNG\sprites\player\player-climb\player-climb-',
        "size": 4
    },
    {
        "name": "duck",
        "url": 'images\PNG\sprites\player\player-duck\player-duck-',
        "size": 4
    },
    {
        "name": "fall",
        "url": 'images\PNG\sprites\player\player-fall\player-fall-',
        "size": 4
    },
    {
        "name": "hurt",
        "url": 'images\PNG\sprites\player\player-hurt\player-hurt-',
        "size": 2
    },
    {
        "name": "jump",
        "url": 'images\PNG\sprites\player\player-jump\player-jump-',
        "size": 4
    },
    {
        "name": "skip",
        "url": 'images\PNG\sprites\player\player-skip\player-skip-',
        "size": 8
    }
]

        
class User(pygame.sprite.Sprite):
    """ This class represents a simple block the player collects. """
 
    def __init__(self):
        super().__init__()
        self.img_num = 0
        self.img_frame = 1
        
        self.starCount = 0
        # print(self.img_frame)
        self.load_img()
        self.rect = self.image.get_rect()
        
        # (100 / 이미지 수) / 100 = (100 / 이미지 수 * 100)
        self.animation_time = round(100 / (USER_IMAGE_ARR[self.img_num]["size"] * 100), 2)

        # mt와 결합하여 animation_time을 계산할 시간 초기화
        self.current_time = 0
        
        self.hp = 3
        self.hud_img = pygame.image.load('images/PNG/sprites/misc/hud/hud-4.png')
        self.hud_img = pygame.transform.scale(self.hud_img, (150, 40))
        
        self.sound_hurt = pygame.mixer.Sound('./sound/hurt.ogg')
        
        # self.reset_pos()
        self.changeX = 0
        self.changeY = 0
        self.direction = "right"
        
        self.climbimg = False
        #Boolean to check if player is running, current running frame, and time since last frame change
        self.running = False
        self.runningFrame = 0
        self.runningTime = pygame.time.get_ticks()
        
        self.ducking = False
        
         # ladder top 부딛히면 tile 정보, 아니면 False
        self.isHitLadderX = False
        self.isHitLadderY = False
        
        #Players current level, set after object initialized in game constructor
        self.currentLevel = None
        self.currentBg = None
        
        self.hitedEnemy = None
        self.hitedItem = None
        
        self.reset_pos()
 
    def reset_pos(self):
        """ Called when the block is 'collected' or falls off
            the screen. """
        self.rect.y = 31*10
        self.rect.x = 31*3
    
    def load_img(self):
        
        self.image = pygame.image.load(str(USER_IMAGE_ARR[self.img_num]["url"])+str(int(self.img_frame)) + '.png')
        self.image = self.image.subsurface(6, 0, 24, 32)
        self.image = pygame.transform.scale(self.image, (24*2, 32*2)) # 이미지 스케일링
        
    def draw_frame_img(self):
        if self.img_frame > USER_IMAGE_ARR[self.img_num]["size"]: self.img_frame = 1
        if self.img_frame % 1 == 0: 
            self.load_img()
            if self.direction == "left":
                self.image = pygame.transform.flip(self.image, True, False)
    
    #Make player jump
    def jump(self):
        #Check if player is on ground
        # print(self.rect.y)
        file = "./sound/jump.ogg"
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        # sound_jump = pygame.mixer.Sound('./sound/jump.ogg')
        # sound_jump.play()
        self.rect.y += 2
        tileHitList = pygame.sprite.spritecollide(self, self.currentLevel.layers[MAP_COLLISION_LAYER].tiles, False)
        self.rect.y -= 2
        
        if len(tileHitList) > 0:
            self.img_num = 5
            self.changeY = -7
        
    #Move right
    def goRight(self):
        self.direction = "right"
        self.running = True
        self.changeX = 3
    
    #Move left
    def goLeft(self):
        self.direction = "left"
        self.running = True
        self.changeX = -3
    
    #Stop moving
    def stopX(self):
        self.running = False
        self.changeX = 0
    
    def stopY(self):
        self.running = False
        self.changeY = 0
        
    def duck(self):
        self.running = False
        self.changeX = 0
    
    def climb_up(self):
        self.direction = "up"
        self.running = True
        self.changeY = -5
    def climb_down(self):
        self.direction = "down"
        self.running = True
        self.changeY = 5
    
    def swipe_climb_mode(self, tile):
        print("change!")
        self.img_num = 1
        self.img_frame = 1
        self.stopX()
        self.stopY()
        self.rect.right = tile.rect.right
        # self.rect.bottom = tile.rect.bottom
        self.load_img()
        
    def unswipe_climb_mode(self, tile):
        print("unchange!")
        self.img_num = 0
        self.img_frame = 1
        self.stopX()
        self.stopY()
        self.rect.right = tile.rect.right
        # self.rect.bottom = tile.rect.bottom
        self.load_img()
        
    #Draw player
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        # screen.blit(self.image, (70, 90), self.rect)
        
    # hud 이미지 로드
    # 위의 draw 함수에서 hud 이미지를 blit 하도록 해봤는데, 마지막 이미지인 hud-1.png가 업데이트 되지 않은 채로 게임오버가 돼서 hud 이미지용 함수를 따로 생성함
    # GameMain의 display_frame 함수에서만 1번 호출됨
    def hud_draw(self, screen):
        screen.blit(self.hud_img, (0, 0))
        
    def getTileHitList(self):
        return pygame.sprite.spritecollide(self, self.currentLevel.layers[MAP_COLLISION_LAYER].tiles, False)
        
    def update(self, mt):
        # """ Automatically called when we need to move the block. """
        self.current_time += mt
        
        # 부딛힘 검사 전 초기화
        self.isHitLadderX = False
        self.isHitLadderY = False
        
        #Update player position by change
        if self.img_num != 1: # 사다리
            self.rect.x += self.changeX
        
        #Get tiles in collision layer that player is now touching
        tileHitList = pygame.sprite.spritecollide(self, self.currentLevel.layers[MAP_COLLISION_LAYER].tiles, False)
        
        #Move player to correct side of that block
        for tile in tileHitList:
            if tile.type == "ladder" or tile.type == "ladder-top":
                    if tile.type == "ladder-top": self.isHitLadderX = tile
                    # print("X in")
                    if self.img_num != 1 and self.climbimg == False:
                        self.swipe_climb_mode(tile)
                        # print(self.direction)
                        self.climbimg = tile
                        self.img_num = 1
            else:
                self.climbimg = False
                if self.changeX > 0:
                    self.rect.right = tile.rect.left
                else:
                    self.rect.left = tile.rect.right
        
        #Move screen if player reaches screen bounds
        if self.rect.right >= SCREEN_WIDTH - 400:
            difference = self.rect.right - (SCREEN_WIDTH - 400)
            self.rect.right = SCREEN_WIDTH - 400
            self.currentLevel.shiftLevelX(-difference)
            self.currentBg.shiftBgX(-difference, mt)
        
        #Move screen is player reaches screen bounds
        if self.rect.left <= 400:
            difference = 400 - self.rect.left
            self.rect.left = 400
            self.currentLevel.shiftLevelX(difference)
            self.currentBg.shiftBgX(difference, mt)
            
        if self.rect.bottom >= SCREEN_HEIGHT - 200:
            difference = self.rect.bottom - (SCREEN_HEIGHT - 200)
            self.rect.bottom = SCREEN_HEIGHT - 200
            self.currentLevel.shiftLevelY(-difference)
        
        #Move screen is player reaches screen bounds
        if self.rect.top <= 200:
            difference = 200 - self.rect.top
            self.rect.top = 200
            self.currentLevel.shiftLevelY(difference)
            
            
        #Update player position by change
        self.rect.y += self.changeY
        
        #Get tiles in collision layer that player is now touching
        tileHitList = pygame.sprite.spritecollide(self, self.currentLevel.layers[MAP_COLLISION_LAYER].tiles, False)
       
        #If there are tiles in that list
        if len(tileHitList) > 0:
            #Move player to correct side of that tile, update player frame
            for tile in tileHitList:
                
                if tile.type == "ladder" or tile.type == "ladder-top":
                    if tile.type == "ladder-top": self.isHitLadderY = tile
                else:
                    if self.changeY > 0:
                        self.rect.bottom = tile.rect.top
                        self.changeY = 1
                    else:
                        self.rect.top = tile.rect.bottom
                        self.changeY = 0
                    
                    
        #If there are not tiles in that list
        else:
            if self.img_num == 1:
                # print("falling stop plz,,,")
                self.stopX()
                self.stopY()
                self.img_num = 0
                self.climbimg = False
                self.load_img()
            else:
                #Update player change for jumping/falling and player frame
                self.changeY += 0.2
                if self.changeY > 0:
                    self.img_num = 3
                else:
                    self.img_num = 5
                    
        #If player is on ground and running, update running animation
        if self.running and self.changeY == 1 and self.img_num != 1:
                self.img_num = 6
        
        # ---Item---
        itemsHitList = pygame.sprite.spritecollide(self, self.currentLevel.items, False)
        
        if len(itemsHitList) > 0:
            for item in itemsHitList:
                if self.hitedItem == None:
                    print("item hit: ", item)
                    print("스테이지 전환", item)
                    file = "./sound/star.ogg"
                    pygame.mixer.init()
                    pygame.mixer.music.load(file)
                    pygame.mixer.music.play()
                    self.starCount += 1
                    self.hitedItem = item
        else:
            self.hitedItem = None
            
        # ---Enemy---
        enemyHitList = pygame.sprite.spritecollide(self, self.currentLevel.enemys, False)
        
        if len(enemyHitList) > 0:
            for enemy in enemyHitList:
                if self.hitedEnemy == None:
                    file = "./sound/hurt.ogg"
                    pygame.mixer.init()
                    pygame.mixer.music.load(file)
                    pygame.mixer.music.play()
                    for x in range(3, -1, -1):
                        if self.hp == x:
                            self.hud_img = pygame.image.load(('images/PNG/sprites/misc/hud/hud-')+str(int(x)) + '.png')
                            self.hud_img = pygame.transform.scale(self.hud_img, (150, 40))
                    self.hp -= 1
                    self.hitedEnemy = enemy
        else:
            self.hitedEnemy = None
        #----Stand-----
        # stand player
        if self.running == False and len(tileHitList) > 0 and self.img_num != 1:
            self.img_num = 0
                
            
        #When correct amount of time has passed, go to next frame
        if pygame.time.get_ticks() - self.runningTime > 50:
            self.runningTime = pygame.time.get_ticks()
            if self.runningFrame == 4:
                self.runningFrame = 0
            else:
                self.runningFrame += 1
                
        if self.running == False and self.img_num == 1:
            self.img_frame = 1
        else:
            # loop time 경과가 animation_time을 넘어서면 새로운 이미지 출력 
            if self.current_time >= self.animation_time:
                self.current_time = 0
                self.draw_frame_img()

                self.img_frame += 1
                if self.img_frame > int(USER_IMAGE_ARR[self.img_num]["size"]):
                    self.img_frame = 1
            else:
            
                # print(self.img_frame)
                self.draw_frame_img()