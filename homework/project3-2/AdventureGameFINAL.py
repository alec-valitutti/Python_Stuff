##project3.py
##A
##4/3/2020


######################################################################################################################################################

import pygame, time, random, os,sys

def textWrite(text,font,color,surface,x,y):
    textobj = font.render(text,1,color)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    surface.blit(textobj,textrect)

#menus#####################################################################################################################################################
    
def mainMenu():
    global textFont
    screen.fill((0,0,0))
    
    menuImg = pygame.image.load('data/sprites/mainMenu1.png').convert()


    menu1 =True
    while menu1:

        screen.blit(menuImg, (0,0))
        textWrite('Adventure Game!',textFont,(00,0,00),screen,200,100)
        textWrite('Press '"1"' to Play',textFont,(0,0,0),screen,220,300)
        textWrite('Press '"2"' to Quit',textFont,(0,0,0),screen,500,300)
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_1 :
                    menu1 = False
                if event.key == pygame.K_2 :
                    print('quit')
                    exit()
            if event.type ==pygame.QUIT:
                print('quit')
                exit()

        pygame.display.flip()
        clock.tick(FPS)

#player//npc//#####################################################################################################################################################
class Player(pygame.sprite.Sprite):
    global facingLeft
    global facingRight
    
    images = ['data/sprites/char1.png',
              'data/sprites/char1.png',
              'data/sprites/char1.png',
              'data/sprites/char2.png',
              'data/sprites/char2.png',
              'data/sprites/char2.png',
              'data/sprites/char1.png',
              'data/sprites/char1.png',
              'data/sprites/char1.png',
              'data/sprites/char2.png',
              'data/sprites/char2.png',
              'data/sprites/char2.png']

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('data/sprites/char1.png')
        self.rect = self.image.get_rect()
        self.health =5
        self.rect.x= 0
        self.rect.y=0
        self.repeat =-1
    def update(self):
        global facingLeft
        global facingRight
        self.image = pygame.image.load(Player.images[self.repeat])
        self.repeat += 1
        if self.repeat ==12:
            self.repeat =-1
        
        global gravity
        key = pygame.key.get_pressed()
        self.rect.y+=gravity

        if key[pygame.K_d]:
            facingLeft=False
            facingRight =True
            self.rect.x +=5
        if key[pygame.K_a]:
            facingLeft =True
            facingRight = False
            self.rect.x -=5

           ############################################### 
        if key[pygame.K_e]:
            global s1
            if facingLeft == True:

                s1 = Sword((P1.rect.x+18,P1.rect.y))
                s1.image = pygame.transform.flip(s1.image,True,False)
                weaponGroup.add(s1)

            if facingRight == True:
                s1 = Sword((P1.rect.x+25,P1.rect.y))
                weaponGroup.add(s1)

        if self.rect.x <= 0:
            self.rect.x = 0

        if self.rect.x >= SCR_WID:
            self.rect.x = SCR_WID
            
        if self.rect.y >= SCR_HEI-30:
            self.rect.y =SCR_HEI-31
        if self.health ==0:
            dead()
        
class Sword(pygame.sprite.Sprite):
    global fasingLeft
    global facingRight
    
    def __init__(self,pos):
        
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('data/sprites/sword3.png')
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def update(self):

        if facingLeft ==True:
            self.rect.x -=10
        if facingRight ==True:
            self.rect.x +=10

#enemy########################################################################################################################################################
class Enemy(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('data/sprites/char2.png')
        self.rect = self.image.get_rect()
        self.movespeed = 2
        self.health =5
        self.rect.x,self.rect.y = x,y
        
    def update(self):
        global floor
        global gravity
        jump = random.randint(0,100)
        move =random.randint(0,100)
        grounded =False

        #bounding
        if self.rect.x<=0:
            jump=random.randint(100,500)
            self.rect.x=jump
        if self.rect.x >= SCR_HEI:
            jump=random.randint(100,500)
            self.rect.x=jump
            
        #GRAVITY
        self.rect.y+=gravity
        if self.rect.y >= SCR_HEI-30:
            self.rect.y = SCR_HEI-floor
            grounded =True
        if jump <2 and grounded == True:
            self.rect.y -=60
            grounded = False
            
        #movement
        if move <20 and grounded ==True:
            self.rect.x +=1
        if move >80 and grounded ==True:
            self.rect.x -=1
        if 40<=move<=50 and grounded == True:
            self.rect.x +=2
        if 50<=move<=60 and grounded == True:
            self.rect.x -=2
            
        #col
        if pygame.sprite.groupcollide(playerGroup,enemyGroup,0,False):
            run = random.randint(0,9)
            P1.health -=1
            if run <=4:
                self.rect.x -= 60
                self.rect.y -= 90
            else:
                self.rect.x+=60
                self.rect.y -= 90

        if pygame.sprite.groupcollide(weaponGroup,enemyGroup,1,False):
            self.health -=1
            print(self.health)
            
        if self.health <=0:
            enemyGroup.remove(e1)
            print(enemyGroup)
            self.health =5

            print(enemyGroup)

        if len(enemyGroup)==0:
            spawner()
            self.health =5



def spawner():
    randX=random.randint(100,500)
    randY = random.randint(200,375)
    if len(enemyGroup)==0:
        print('enemyGroup ==0')
        e1= Enemy(randX,randY)
        enemyGroup.add(e1)
               
#utility#####################################################################################################################################################

def dead():
    print('you died')
    exit()



#groups######################################################################################################################################################
playerGroup = pygame.sprite.Group(())
P1 = Player()
playerGroup.add(P1)

enemyGroup = pygame.sprite.Group(())
e1 = Enemy(300,100)
enemyGroup.add(e1)

weaponGroup = pygame.sprite.Group(())


facingLeft =False
facingRight = True
#global######################################################################################################################################################

SCR_WID, SCR_HEI = 640,480
screen = pygame.display.set_mode((SCR_WID, SCR_HEI))
pygame.display.set_caption("Adventure Game!")

pygame.font.init()
textFont = pygame.font.Font("data/font/PressStart2P-Regular.ttf", 16)
clock = pygame.time.Clock()
FPS =60
pygame.mixer.init(48000,16,2,4096)
floor =31
gravity =5

#global######################################################################################################################################################


def game():
    while True:
        global Sword

        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                print('quit')
                exit()

        screen.fill((0,77,0))
        playerGroup.draw(screen)
        playerGroup.update()
        enemyGroup.draw(screen)
        enemyGroup.update()

        weaponGroup.draw(screen)
        weaponGroup.update()


        pygame.display.flip()
        clock.tick(FPS)

#main######################################################################################################################################################

def main():
    mainMenu()
    game()

main()

