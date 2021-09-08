##project3.py
##A
##4/3/2020


######################################################################################################################################################

import pygame, time, random, os,sys


######################################################################################################################################################

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname)
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()

def textWrite(text,font,color,surface,x,y):
    textobj = font.render(text,1,color)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    surface.blit(textobj,textrect)
    
######################################################################################################################################################

class Enemy(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("sprites/char2.png")
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
            p1.health -=1
            if run <=4:
                self.rect.x -= 60
                self.rect.y -= 90
            else:
                self.rect.x+=60
                self.rect.y -= 90



class Player(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("sprites/char1.png")
        self.movespeed = 2
        self.health = 5
        self.rect.x,self.rect.y =x,y

    def update(self):
        key = pygame.key.get_pressed()
        pg =pygame
        enemyDead = False
        global floor
        global gravity

        #move on x
        if key[pg.K_a]:
            self.rect.x -= 2 *self.movespeed
            global facingLeft
            global facingRight
            facingLeft =True
            facingRight = False
        if key[pg.K_d]:
            self.rect.x += 2 *self.movespeed
            facingLeft =False
            facingRight = True
            
        if self.rect.x <0:
            self.rect.x =0
        if self.rect.x >= SCR_WID:
            self.rect.x = SCR_WID

        #move on y + GRAVITY
        self.rect.y+=gravity
        if self.rect.y >= SCR_HEI-30:
            self.rect.y = SCR_HEI-floor
        #jumping
        if self.rect.y == SCR_HEI-floor:
            grounded =True
        else:
            grounded =False
        if key[pg.K_SPACE]and grounded == True:
            self.rect.y -=60
            jumping = True
            grounded= False

        #weapon
        if key[pg.K_e]:
            
            if facingLeft == True:
                sword.image = pygame.transform.flip(sword.image,True,False)
                weaponGroup.add(sword)

            if facingRight == True:
                sword.image = sword.image
                weaponGroup.add(sword)

        if sword.rect.x >=SCR_WID:
            weaponGroup.add(sword)
        if pygame.sprite.groupcollide(weaponGroup,enemyGroup,1,False):
            enemyGroup.remove(e1)
            enemyDead =True
            
        if enemyDead:
            enemyGroup.add(e2)
        #death
        if self.health ==0:
            dead()

class Sword(pygame.sprite.Sprite):
    global facingLeft
    global facingRight

    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("sprites/sword3.png")
        self.rect.center = pos

    def update(self):

        if facingLeft ==True:
            self.rect.x -=10
        if facingRight ==True:
            self.rect.x +=10


        #self.rect.y+=5
        if self.rect.y >= SCR_HEI-30:
            self.rect.y = SCR_HEI-floor

def dead():
    print('you died')
    exit()
    
######################################################################################################################################################
    
def mainMenu():
    key = pygame.key.get_pressed()
    pg =pygame
    menu =True
    while menu:
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                print('quit')
                exit()

        
        screen.fill((0,77,200))

        pygame.display.flip()
        clock.tick(FPS)

######################################################################################################################################################

facingLeft =False
facingRight = True
           
SCR_WID, SCR_HEI = 640,480
screen = pygame.display.set_mode((SCR_WID, SCR_HEI))
pygame.display.set_caption("Adventure Game!")

pygame.font.init()
textFont = pygame.font.SysFont("PressStart2P-Regular",16)

floor =31
gravity=5

clock = pygame.time.Clock()
FPS =60

pygame.mixer.init(48000,16,2,4096)

playerGroup = pygame.sprite.Group(())
p1 = Player(500,400)
weaponGroup = pygame.sprite.Group(())

enemyGroup = pygame.sprite.Group(())
e1 = Enemy(400,30)
e2 = Enemy(400,30)


playerGroup.add(p1)
enemyGroup.add(e1)

######################################################################################################################################################

def main():
    pg=pygame
    key = pygame.key.get_pressed()
    while True:
        global sword
        sword = Sword((p1.rect.x+25,p1.rect.y))
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                print('quit')
                exit()

        screen.fill((0,77,0))
        textWrite('yo',textFont,(200,90,200),screen,100,100)
        playerGroup.draw(screen)
        playerGroup.update()
        weaponGroup.draw(screen)
        weaponGroup.update()
        enemyGroup.draw(screen)
        enemyGroup.update()
        if key[pg.K_e]:
            exit()
        pygame.display.flip()
        clock.tick(FPS)
        
#mainMenu()
main()
