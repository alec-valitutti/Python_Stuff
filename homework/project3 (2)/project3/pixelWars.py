##pixelWars.py
##Alec valitutti
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
    global mainmenu
    global optionsmenu
    global aboutmenu
    global boss1
    global game1
    hp1  = pygame.image.load('data/sprites/healthpack.png')
    enemies = pygame.image.load('data/sprites/e1_idle_1.png')
    screen.fill((0,0,0))
    menuImg = pygame.image.load('data/sprites/mainMenu1.png').convert()
    menu1 =True
    enemyGroup.add(Dummy)
    playerGroup.add(P1)
    boss1 = Boss(2000,SCR_HEI-180)

    while menu1:
        P1.health =10
        if pygame.mixer.music.get_busy() == 0:
            pygame.mixer.music.play(-1)
        screen.blit(menuImg, (0,0))
        textWrite('Pixel Wars!',textFontBig,(00,0,00),screen,200,100)
        if mainmenu:
            textWrite('Press '"1"' to Play',textFont,(0,0,0),screen,200,300)
            textWrite('Press '"2"' for controls',textFont,(0,0,0),screen,200,350)
            textWrite('Press '"3"' for gameplay/about this project',textFont,(0,0,0),screen,200,400)
            textWrite('_________________________',textFont,(0,0,0),screen,200,450)
            textWrite('Press '"4"' to Quit',textFont,(0,0,0),screen,200,500)

        if optionsmenu:
            textWrite('Press '"A"' to move left',textFont,(0,0,0),screen,200,300)
            textWrite('Press '"D"' to move right',textFont,(0,0,0),screen,200,350)
            textWrite('Press '"W"' to jump',textFont,(0,0,0),screen,200,400)
            textWrite('Press '"E"' to shoot',textFont,(0,0,0),screen,200,450)
            textWrite('Press '"ESCAPE"' to pause',textFont,(0,0,0),screen,200,500)
            textWrite('_________________________',textFont,(0,0,0),screen,200,550)
            textWrite('Press '"3"' for gameplay/about this project',textFont,(0,0,0),screen,200,600)
            textWrite('Press '"TAB"' to go back',textFont,(0,0,0),screen,200,660)
            
        if aboutmenu:
            textWrite('You are tasked with defeating as many enemies as possible',textFont,(0,0,0),screen,200,300)
            textWrite('Try to defeat the boss after the waves of enemies',textFont,(0,0,0),screen,200,350)
            textWrite('Pick up health packs from fallen enemies to continue your mission',textFont,(0,0,0),screen,200,400)
            textWrite('_________________________',textFont,(0,0,0),screen,200,450)
            textWrite('Version 0.1',textFont,(0,0,0),screen,200,500)
            textWrite('_________________________',textFont,(0,0,0),screen,200,550)
            textWrite('Gameplay: Alec Valitutti',textFont,(0,0,0),screen,200,600)
            textWrite('Graphics: Alec Valitutti',textFont,(0,0,0),screen,200,650)
            textWrite('Sound: Alec Valitutti',textFont,(0,0,0),screen,200,700)
            textWrite('Contact: unbounddesigns1@gmail.com',textFont,(0,0,0),screen,200,750)
            textWrite('_________________________',textFont,(0,0,0),screen,200,800)
            textWrite('Press '"2"' for controls',textFont,(0,0,0),screen,200,850)
            textWrite('Press '"TAB"' to go back',textFont,(0,0,0),screen,200,900)
            
        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_TAB and optionsmenu:
                    optionsmenu = False
                    mainmenu = True
                    aboutmenu =False

                if event.key == pygame.K_TAB and aboutmenu:
                    aboutmenu = False
                    optionsmenu = False
                    mainmenu = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1 and mainmenu:
                    menu1 = False #plays game
                    groupClear()
                    game1 = True
                if event.key == pygame.K_4  and mainmenu:

                    pygame.mixer.music.fadeout(1000)
                    exit()
                if event.key == pygame.K_2 :
                    optionsmenu = True
                    mainmenu =False
                    aboutmenu = False

                if event.key == pygame.K_3 :
                    optionsmenu = False
                    mainmenu =False
                    aboutmenu = True

            if event.type ==pygame.QUIT:
                exit()
                
        weaponGroup.draw(screen)
        weaponGroup.update()
        
        enemyGroup.draw(screen)
        enemyGroup.update()
        
        bossGroup.draw(screen)
        bossGroup.update()

        playerGroup.draw(screen)
        playerGroup.update() 

        eWeaponGroup.draw(screen)
        eWeaponGroup.update()
        
        Items.draw(screen)
        Items.update()

        pygame.display.flip()
        
        clock.tick(FPS)

def pauseMenu():
    
    global game1
    global mainmenu1
    global pausemenu

    pygame.mixer.music.pause()
    pauseImg = pygame.image.load('data/sprites/pause.png').convert_alpha()
    pauseImg = pygame.transform.scale(pauseImg,(1920,1020))
    screen.blit(pauseImg,(0,0))
    textWrite('Game Paused',textFontBig,(0,0,0),screen,200,250)
    textWrite('Press '"1"' to continue playing',textFont,(0,0,0),screen,200,400)
    textWrite('Press '"2"' to return to the main menu',textFont,(0,0,0),screen,200,450)
    textWrite('Press '"3"' to quit',textFont,(0,0,0),screen,200,500)

    
    
    while pausemenu == True:

        
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    pausemenu = False
                    pygame.mixer.music.unpause()
                if event.key == pygame.K_2:
                    mainmenu1 = True
                    game1 = False
                    pausemenu = False
                    pygame.mixer.music.unpause()
                    groupClear()

                if event.key == pygame.K_3:
                    pygame.mixer.music.fadeout(1000)
                    exit()
    
        pygame.display.update()
        clock.tick(FPS)

#UI stuff#############################################################################################################################################
class healthBar(pygame.sprite.Sprite):

    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('data/sprites/healthBar.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        if P1.health >=10:
            healthBar1.image = pygame.transform.scale(self.image,(160,20))
        if 9>=P1.health >=8:
            healthBar1.image = pygame.transform.scale(self.image,(128,20))
        if 7>=P1.health >=6:
            healthBar1.image = pygame.transform.scale(self.image,(96,20))
        if 5>=P1.health >=4:
            healthBar1.image = pygame.transform.scale(self.image,(64,20))
        if 3>=P1.health >=2:
            healthBar1.image = pygame.transform.scale(self.image,(32,20))
        if P1.health ==1:
            healthBar1.image = pygame.transform.scale(self.image,(16,20))
        if P1.health ==0:
            healthBar1.image = pygame.transform.scale(self.image,(1,20))

class staminaBar(pygame.sprite.Sprite):

    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('data/sprites/staminabar.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    def update(self):
        global counter
        if counter ==10:
            staminaBar1.image = pygame.transform.scale(self.image,(160,20))
        if counter ==8:
            staminaBar1.image = pygame.transform.scale(self.image,(128,20))
        if counter ==6:
            staminaBar1.image = pygame.transform.scale(self.image,(96,20))
        if counter ==4:
            staminaBar1.image = pygame.transform.scale(self.image,(64,20))
        if counter ==2:
            staminaBar1.image = pygame.transform.scale(self.image,(32,20))
        if counter ==1:
            staminaBar1.image = pygame.transform.scale(self.image,(1,20))

#Items############################################################################################################################################################

class healthPack(pygame.sprite.Sprite):

    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('data/sprites/healthpack.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.heal = 5
        
    def update(self):
        global gravity
        if pygame.sprite.groupcollide(Items,playerGroup,1,False):
            pygame.mixer.Sound.play(healthpickup)
            P1.health +=self.heal

        if self.rect.y >= SCR_HEI-63:
            self.rect.y =SCR_HEI-64

        self.rect.y +=gravity

#bullets################################################################################################################################

         
class Bullet(pygame.sprite.Sprite):
    def __init__(self,player,x,y,velx):
        super().__init__()
        self.player=player
        self.image=pygame.image.load('data/sprites/bullet.png')
        self.rect=self.image.get_rect()
        self.rect.x= P1.rect.x
        self.rect.y= P1.rect.y
        self.velx= velx
        self.last = pygame.time.get_ticks()
      
    def update(self):
        now=pygame.time.get_ticks()
        self.rect.x+=self.velx

        if now-self.last>300:
         self.kill()

class Bullet1(pygame.sprite.Sprite):
    def __init__(self,enemy,x,y,velx):
        super().__init__()
        self.enemy=enemy
        self.image=pygame.image.load('data/sprites/bullet1.png')
        self.rect=self.image.get_rect()
        self.rect.x= x
        self.rect.y= y
        self.velx= velx
        self.last = pygame.time.get_ticks()
      
    def update(self):
        now=pygame.time.get_ticks()
        self.rect.x+=self.velx
        hits= pygame.sprite.groupcollide(weaponGroup,enemyGroup,1,False)

        if now-self.last>200 or hits:
         self.kill()

class Bomb(pygame.sprite.Sprite):
    def __init__(self,enemy,x,y,velx):
        super().__init__()
        self.enemy=enemy
        self.image=pygame.image.load('data/sprites/bomb.png')
        self.rect=self.image.get_rect()
        self.rect.x= x
        self.rect.y= y
        self.velx= velx
        self.last = pygame.time.get_ticks()
      
    def update(self):
        now=pygame.time.get_ticks()
        self.rect.x+=self.velx
        hits= pygame.sprite.groupcollide(weaponGroup,enemyGroup,1,False)

        if now-self.last>1000 or hits:
         self.kill()

class Dynamite(pygame.sprite.Sprite):
    def __init__(self,enemy,x,y,velx):
        super().__init__()
        self.enemy=enemy
        self.image=pygame.image.load('data/sprites/dynamite.png')
        self.rect=self.image.get_rect()
        self.rect.x= x
        self.rect.y= y
        self.velx= velx
        self.last = pygame.time.get_ticks()
      
    def update(self):
        now=pygame.time.get_ticks()
        self.rect.x+=self.velx
        hits= pygame.sprite.groupcollide(weaponGroup,enemyGroup,1,False)

        if now-self.last>1000 or hits:
         self.kill()

#player//npc//#####################################################################################################################################################
   
class Player(pygame.sprite.Sprite):
    global facingLeft
    global facingRight

    Idle = ['data/sprites/p_idle_1.png',
              'data/sprites/p_idle_1.png',
              'data/sprites/p_idle_1.png',
              'data/sprites/p_idle_1.png',
              'data/sprites/p_idle_1.png',
              'data/sprites/p_idle_1.png',
              'data/sprites/p_idle_2.png',
              'data/sprites/p_idle_2.png',
              'data/sprites/p_idle_2.png',
              'data/sprites/p_idle_2.png',
              'data/sprites/p_idle_2.png',
              'data/sprites/p_idle_2.png',
              'data/sprites/p_idle_1.png',
              'data/sprites/p_idle_1.png',
              'data/sprites/p_idle_1.png',
              'data/sprites/p_idle_1.png',
              'data/sprites/p_idle_1.png',
              'data/sprites/p_idle_1.png',
              'data/sprites/p_idle_2.png',
              'data/sprites/p_idle_2.png',
              'data/sprites/p_idle_2.png',
              'data/sprites/p_idle_2.png',
              'data/sprites/p_idle_2.png',
              'data/sprites/p_idle_2.png']

    walk = ['data/sprites/p_walk_1.png',
              'data/sprites/p_walk_1.png',
              'data/sprites/p_walk_1.png',
              'data/sprites/p_walk_1.png',
              'data/sprites/p_walk_1.png',
              'data/sprites/p_walk_1.png',
              'data/sprites/p_walk_2.png',
              'data/sprites/p_walk_2.png',
              'data/sprites/p_walk_2.png',
              'data/sprites/p_walk_2.png',
              'data/sprites/p_walk_2.png',
              'data/sprites/p_walk_2.png',
              'data/sprites/p_walk_3.png',
              'data/sprites/p_walk_3.png',
              'data/sprites/p_walk_3.png',
              'data/sprites/p_walk_3.png',
              'data/sprites/p_walk_3.png',
              'data/sprites/p_walk_3.png',
              'data/sprites/p_walk_4.png',
              'data/sprites/p_walk_4.png',
              'data/sprites/p_walk_4.png',
              'data/sprites/p_walk_4.png',
              'data/sprites/p_walk_4.png',
              'data/sprites/p_walk_4.png']

    def __init__(self,x,y):

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('data/sprites/p_idle_1.png')
        self.rect = self.image.get_rect()
        self.health =10
        self.rect.x= x
        self.rect.y=y
        self.repeat =-1
        self.jump =0
        self.last = 0
    def update(self):
        
        global facingLeft
        global facingRight
        global idle
        global walk
        global grounded
        global gravity
        global counter
        global canJump
        global negative
        global pausemenu
        self.last +=1
        self.jump +=1
        if self.health >=10:
            self.health =10
        key = pygame.key.get_pressed()
        #animations
 
        if idle ==True and facingRight:
            walk =False
            facingLeft =False
            self.image = pygame.image.load(Player.Idle[self.repeat])

        if idle == True and facingLeft:
            walk = False
            facingRight =False
            self.image = pygame.image.load(Player.Idle[self.repeat])
            P1.image = pygame.transform.flip(P1.image,True,False)

        if walk == True and facingRight:
            idle =False
            facingLeft =False
            self.image = pygame.image.load(Player.walk[self.repeat])

        if walk == True and facingLeft:
            idle =False
            facingRight =False
            self.image = pygame.image.load(Player.walk[self.repeat])
            P1.image = pygame.transform.flip(P1.image,True,False)

        self.repeat += 1
        if self.repeat ==24:
            self.repeat =-1
        
        idle = True

        #movement
                 
        key = pygame.key.get_pressed()
        self.rect.y+=gravity

        if key[pygame.K_d]:

            facingLeft=False
            facingRight =True
            self.rect.x +=5
            idle =False
            walk = True
            if self.last>15000:
                footstep.play()
                self.last = 0
        if key[pygame.K_a]:
            facingLeft =True
            facingRight = False
            idle = False
            walk =True
            if self.last>15000:
                footstep.play()
                self.last = 0
            
            self.rect.x -=5
        if counter >=5:
            negative = 1
        if counter <=4:
            negative = -1
            
        if key[pygame.K_w]:

            if counter>=0 and canJump:

                if grounded:
                    counter-=1
                    self.rect.y -=45
                    
                if facingLeft and canJump:
                    self.rect.x -=6
                if facingRight and canJump:
                    self.rect.x+=6
            if self.jump>28 and grounded:    
                jump.play()
                self.jump =0
                             
        if counter <=0 and canJump:
            canJump =False
            
        if canJump == False:
            counter+=1
            if self.rect.y >= SCR_HEI-82:
                canJump = True
        if self.rect.y >= SCR_HEI-82:
            counter+=1
        if counter>=10:
            counter = 10

        #weapon
        self.last +=1000
        if key[pygame.K_e]:
            now = pygame.time.get_ticks()
            if facingRight == True and self.last>10000:
                s1 = Bullet(P1,110,110,30)
                weaponGroup.add(s1)
                pygame.mixer.Sound.play(gunshot)

                self.last =0

            if facingLeft == True and self.last>10000:
                s1 = Bullet(P1,0,0,-30)
                weaponGroup.add(s1)
                pygame.mixer.Sound.play(gunshot)

                self.last =0
                
        #bounding     
        if self.rect.x <= 0:
            self.rect.x = 0

        if self.rect.x >= SCR_WID:
            self.rect.x = SCR_WID
            
        if self.rect.y >= SCR_HEI-80:
            grounded = True
            self.rect.y =SCR_HEI-81

        if self.health <=0:
            dead()

class Dummy(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('data/sprites/dummy.png')
        self.rect = self.image.get_rect()
        self.movespeed = 2
        self.health =5
        self.repeat =-1
        self.last = 0
        self.rect.x,self.rect.y = x,y

    def update(self):
        global floor
        global gravity
        global eGrounded
        grounded =False
        
        self.rect.y+=gravity
        if self.rect.y >= SCR_HEI-80:
            self.rect.y = SCR_HEI-81
            grounded =True
            eGrounded =True

        if pygame.sprite.groupcollide(weaponGroup,enemyGroup,1,False):
            hitSound.play()
            randomNum = random.randint(1,100)
            if randomNum <9:
                randomX =random.randint(100,1500)

                healthpack1 = healthPack(randomX,Dummy.rect.y-700)
                Items.add(healthpack1)

class Boss(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('data/sprites/boss.png')
        self.image = pygame.transform.scale(self.image,(256,168))
        self.rect = self.image.get_rect()
        self.movespeed = 2
        self.health =5
        self.repeat =-1
        self.last = 0
        self.rect.x,self.rect.y = x,y

    def update(self):
        global floor
        global gravity
        global eGrounded
        grounded =False
        self.rect.y+=gravity
        shoot = random.randint(0,2000)

        if pygame.sprite.groupcollide(weaponGroup,bossGroup,1,False):
            boss1.health -=1
            hitSound.play()

        if pygame.sprite.groupcollide(eWeaponGroup,playerGroup,1,False):
            P1.health -=1
            hitSound.play()
        
        if shoot<=10:
            if self.rect.x > P1.rect.x:
                bomb1 = Bomb(boss1,boss1.rect.x,boss1.rect.y+85,-10)
                eWeaponGroup.add(bomb1)
                pygame.mixer.Sound.play(gunshotE)

        if 11<=shoot<=21:
            if self.rect.x > P1.rect.x:
                dynamite1 = Dynamite(boss1,boss1.rect.x,boss1.rect.y+85,-10)
                eWeaponGroup.add(dynamite1)
                pygame.mixer.Sound.play(gunshotE)

        if P1.rect.x<self.rect.x and self.rect.x !=1500:
                self.rect.x +=1
        if self.rect.x>1500:
            self.rect.x -=5
        if self.rect.y >= SCR_HEI-180:
            self.rect.y =SCR_HEI-179
            grounded =True
            eGrounded =True

        if self.health <= 0:
            global bossSpawn
            pygame.sprite.Sprite.kill(boss1)
            bossGroup.remove(boss1)
            bossSpawn-=3
            spawner()


class Enemy(pygame.sprite.Sprite):
    Idle = ['data/sprites/e1_idle_1.png',
              'data/sprites/e1_idle_1.png',
              'data/sprites/e1_idle_1.png',
              'data/sprites/e1_idle_1.png',
              'data/sprites/e1_idle_1.png',
              'data/sprites/e1_idle_1.png',
              'data/sprites/e1_idle_2.png',
              'data/sprites/e1_idle_2.png',
              'data/sprites/e1_idle_2.png',
              'data/sprites/e1_idle_2.png',
              'data/sprites/e1_idle_2.png',
              'data/sprites/e1_idle_2.png',
              'data/sprites/e1_idle_1.png',
              'data/sprites/e1_idle_1.png',
              'data/sprites/e1_idle_1.png',
              'data/sprites/e1_idle_1.png',
              'data/sprites/e1_idle_1.png',
              'data/sprites/e1_idle_1.png',
              'data/sprites/e1_idle_2.png',
              'data/sprites/e1_idle_2.png',
              'data/sprites/e1_idle_2.png',
              'data/sprites/e1_idle_2.png',
              'data/sprites/e1_idle_2.png',
              'data/sprites/e1_idle_2.png']

    walk = ['data/sprites/e1_walk_1.png',
              'data/sprites/e1_walk_1.png',
              'data/sprites/e1_walk_1.png',
              'data/sprites/e1_walk_1.png',
              'data/sprites/e1_walk_1.png',
              'data/sprites/e1_walk_1.png',
              'data/sprites/e1_walk_2.png',
              'data/sprites/e1_walk_2.png',
              'data/sprites/e1_walk_2.png',
              'data/sprites/e1_walk_2.png',
              'data/sprites/e1_walk_2.png',
              'data/sprites/e1_walk_2.png',
              'data/sprites/e1_walk_3.png',
              'data/sprites/e1_walk_3.png',
              'data/sprites/e1_walk_3.png',
              'data/sprites/e1_walk_3.png',
              'data/sprites/e1_walk_3.png',
              'data/sprites/e1_walk_3.png',
              'data/sprites/e1_walk_4.png',
              'data/sprites/e1_walk_4.png',
              'data/sprites/e1_walk_4.png',
              'data/sprites/e1_walk_4.png',
              'data/sprites/e1_walk_4.png',
              'data/sprites/e1_walk_4.png']

    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('data/sprites/e1_idle_1.png')
        self.rect = self.image.get_rect()
        self.movespeed = 2
        self.health =5
        self.repeat =-1
        self.last = 0
        self.rect.x,self.rect.y = x,y
        
    def update(self):
        global floor
        global gravity
        global eGrounded
        grounded =False
        jump = random.randint(0,100)
        move =random.randint(0,100)
        self.last +=1

        if self.last >15 and eGrounded:
            footstep.play()
            self.last =0

        self.image = pygame.image.load(self.Idle[self.repeat])

        if self.rect.x < P1.rect.x:
            self.image = pygame.image.load(self.walk[self.repeat])

        if self.rect.x > P1.rect.x:
            self.image = pygame.image.load(self.walk[self.repeat])
            self.image = pygame.transform.flip(self.image,True,False)

        if self.rect.x < P1.rect.x+10:

            self.rect.x +=2
        if self.rect.x > P1.rect.x+10:

            self.rect.x -=2

        self.repeat +=1
            
        #GRAVITY
        self.rect.y+=gravity
        if self.rect.y >= SCR_HEI-80:
            self.rect.y = SCR_HEI-81
            grounded =True
            eGrounded =True
        else:
            eGrounded =False
        if jump <2 and grounded == True:
            self.rect.y -=60
            grounded = False
            
        #col
        if pygame.sprite.spritecollide(P1,enemyGroup,0,False):
            run = random.randint(0,9)
            P1.health -=1
            hitSound.play()
            if run <=4:
                self.rect.x -= 60
                self.rect.y -= 90
            else:
                self.rect.x+=60
                self.rect.y -= 90

        if pygame.sprite.spritecollide(e1,weaponGroup,1,False):
            pygame.mixer.Sound.play(hitSound)
            e1.health -=1
            
        if self.health <= 0:

            pygame.sprite.Sprite.kill(e1)
            enemyGroup.remove(e1)
            global kc
            kc +=1
            spawner()

        if self.repeat ==24:
            self.repeat =-1
            
class Enemy1(pygame.sprite.Sprite):

    Idle = ['data/sprites/e_idle_1.png',
              'data/sprites/e_idle_1.png',
              'data/sprites/e_idle_1.png',
              'data/sprites/e_idle_1.png',
              'data/sprites/e_idle_1.png',
              'data/sprites/e_idle_1.png',
              'data/sprites/e_idle_2.png',
              'data/sprites/e_idle_2.png',
              'data/sprites/e_idle_2.png',
              'data/sprites/e_idle_2.png',
              'data/sprites/e_idle_2.png',
              'data/sprites/e_idle_2.png',
              'data/sprites/e_idle_1.png',
              'data/sprites/e_idle_1.png',
              'data/sprites/e_idle_1.png',
              'data/sprites/e_idle_1.png',
              'data/sprites/e_idle_1.png',
              'data/sprites/e_idle_1.png',
              'data/sprites/e_idle_2.png',
              'data/sprites/e_idle_2.png',
              'data/sprites/e_idle_2.png',
              'data/sprites/e_idle_2.png',
              'data/sprites/e_idle_2.png',
              'data/sprites/e_idle_2.png']

    walk = ['data/sprites/e_walk_1.png',
              'data/sprites/e_walk_1.png',
              'data/sprites/e_walk_1.png',
              'data/sprites/e_walk_1.png',
              'data/sprites/e_walk_1.png',
              'data/sprites/e_walk_1.png',
              'data/sprites/e_walk_2.png',
              'data/sprites/e_walk_2.png',
              'data/sprites/e_walk_2.png',
              'data/sprites/e_walk_2.png',
              'data/sprites/e_walk_2.png',
              'data/sprites/e_walk_2.png',
              'data/sprites/e_walk_3.png',
              'data/sprites/e_walk_3.png',
              'data/sprites/e_walk_3.png',
              'data/sprites/e_walk_3.png',
              'data/sprites/e_walk_3.png',
              'data/sprites/e_walk_3.png',
              'data/sprites/e_walk_4.png',
              'data/sprites/e_walk_4.png',
              'data/sprites/e_walk_4.png',
              'data/sprites/e_walk_4.png',
              'data/sprites/e_walk_4.png',
              'data/sprites/e_walk_4.png']

    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('data/sprites/e_idle_1.png')
        self.rect = self.image.get_rect()
        self.movespeed = 2
        self.health =5
        self.repeat =-1
        self.last = 0
        self.rect.x,self.rect.y = x,y
        
    def update(self):
        global floor
        global gravity
        global left
        global right
        global up
        global down
        global eGrounded
        jump = random.randint(0,100)
        move =random.randint(0,100)
        grounded =False
        self.last +=1

        if self.last >15 and eGrounded:
            footstep.play()
            self.last =0

        if self.rect.x < P1.rect.x and eGrounded:
            self.image = pygame.image.load('data/sprites/e_idle_1.png')
        if self.rect.x > P1.rect.x and eGrounded:
            self.image = pygame.image.load('data/sprites/e_idle_1.png')
            self.image = pygame.transform.flip(self.image,True,False)
        #movement
        self.rect.y+=gravity
        if self.rect.y >= SCR_HEI-80:
            self.rect.y = SCR_HEI-81
            grounded =True
            eGrounded = True
        else:
            eGrounded =False
            
        #movement
            
        if self.rect.y >= SCR_HEI-81 and right ==True:

            self.image = pygame.image.load(self.walk[self.repeat])
            if self.rect.x > P1.rect.x and eGrounded:
                self.image = pygame.transform.flip(self.image,True,False)
            self.rect.x+=5

        if self.rect.x >=SCR_WID - 20 and up==True:
            right=False
            self.rect.y-=gravity+5

            
        if self.rect.y <=5 and left ==True:
            up =False
            self.rect.y -=gravity
            self.rect.x -=5

            if self.rect.x <=0:
                left =False
                down = True
                
        if self.rect.x <=0 and down ==True:
            self.rect.y+=-10

        
        if self.rect.y >=SCR_HEI-100:
            right=True
            up=True
            left =True

        shoot = random.randint(0,1000)
        if shoot<=20:
            if self.rect.x < P1.rect.x:
                
                eW1 = Bullet1(e2,self.rect.x,self.rect.y+20,30)
                eWeaponGroup.add(eW1)
                pygame.mixer.Sound.play(gunshotE)
            if self.rect.x > P1.rect.x:
                eW1 = Bullet1(e2,self.rect.x,self.rect.y+20,-30)
                eWeaponGroup.add(eW1)
                pygame.mixer.Sound.play(gunshotE)

        if pygame.sprite.groupcollide(eWeaponGroup,playerGroup,1,False):
            P1.health -=1
            hitSound.play()
                
        #col
        if pygame.sprite.spritecollide(P1,enemyGroup1,0,False):
            run = random.randint(0,9)
            P1.health -=1
            hitSound.play()
            
            if run <=4:
                self.rect.x -= 60
                self.rect.y -= 90
            else:
                self.rect.x+=60
                self.rect.y -= 90

        if pygame.sprite.groupcollide(weaponGroup,enemyGroup1,1,False):
            pygame.mixer.Sound.play(hitSound)
            e2.health -=1
            
        if self.health <= 0:
            pygame.sprite.Sprite.kill(e2)
            enemyGroup1.remove(e2)
            spawner()
            global kc
            kc+=1
        self.repeat +=1
        if self.repeat ==24:
            self.repeat =-1       
class Enemy2(pygame.sprite.Sprite):

    Idle = ['data/sprites/e2_idle_1.png',
              'data/sprites/e2_idle_1.png',
              'data/sprites/e2_idle_1.png',
              'data/sprites/e2_idle_1.png',
              'data/sprites/e2_idle_1.png',
              'data/sprites/e2_idle_1.png',
              'data/sprites/e2_idle_2.png',
              'data/sprites/e2_idle_2.png',
              'data/sprites/e2_idle_2.png',
              'data/sprites/e2_idle_2.png',
              'data/sprites/e2_idle_2.png',
              'data/sprites/e2_idle_2.png',
              'data/sprites/e2_idle_1.png',
              'data/sprites/e2_idle_1.png',
              'data/sprites/e2_idle_1.png',
              'data/sprites/e2_idle_1.png',
              'data/sprites/e2_idle_1.png',
              'data/sprites/e2_idle_1.png',
              'data/sprites/e2_idle_2.png',
              'data/sprites/e2_idle_2.png',
              'data/sprites/e2_idle_2.png',
              'data/sprites/e2_idle_2.png',
              'data/sprites/e2_idle_2.png',
              'data/sprites/e2_idle_2.png']

    walk = ['data/sprites/e2_walk_1.png',
              'data/sprites/e2_walk_1.png',
              'data/sprites/e2_walk_1.png',
              'data/sprites/e2_walk_1.png',
              'data/sprites/e2_walk_1.png',
              'data/sprites/e2_walk_1.png',
              'data/sprites/e2_walk_2.png',
              'data/sprites/e2_walk_2.png',
              'data/sprites/e2_walk_2.png',
              'data/sprites/e2_walk_2.png',
              'data/sprites/e2_walk_2.png',
              'data/sprites/e2_walk_2.png',
              'data/sprites/e2_walk_3.png',
              'data/sprites/e2_walk_3.png',
              'data/sprites/e2_walk_3.png',
              'data/sprites/e2_walk_3.png',
              'data/sprites/e2_walk_3.png',
              'data/sprites/e2_walk_3.png',
              'data/sprites/e2_walk_4.png',
              'data/sprites/e2_walk_4.png',
              'data/sprites/e2_walk_4.png',
              'data/sprites/e2_walk_4.png',
              'data/sprites/e2_walk_4.png',
              'data/sprites/e2_walk_4.png']

    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('data/sprites/e2_idle_1.png')
        self.rect = self.image.get_rect()
        self.movespeed = 2
        self.health =5
        self.repeat =-1
        self.rect.x,self.rect.y = x,y
        self.last = 0

        self.lastShot = pygame.time.get_ticks()
        
    def update(self):
            
        global floor
        global gravity
        global lefta
        global righta
        global eGrounded

        grounded =False
        self.last +=1

        if self.last >15 and eGrounded:
            footstep.play()
            self.last =0

        self.image = pygame.image.load(self.walk[self.repeat])
        if self.rect.x > P1.rect.x:
            self.image = pygame.transform.flip(self.image,True,False)

        #GRAVITY
        self.rect.y+=gravity
        if self.rect.y >= SCR_HEI-80:
            self.rect.y = SCR_HEI-81
            grounded =True
            eGrounded = True
        else:
            eGrounded = False
            
        now = pygame.time.get_ticks()
            
        #movement
        if self.rect.y >= SCR_HEI-81 and righta == True:
            self.rect.x+=5
            self.rect.x =self.rect.x
            if self.rect.x >= SCR_WID-16:
                righta =False
                lefta =True

        if self.rect.y >= SCR_HEI-81 and lefta == True:
            self.rect.x-=5
            self.rect.x =self.rect.x
            if self.rect.x <=0:
                righta =True
                lefta = False

        shoot = random.randint(0,1000)
        if shoot<=20:
            if self.rect.x < P1.rect.x:
                
                eW1 = Bullet1(e3,self.rect.x,self.rect.y,30)
                eWeaponGroup.add(eW1)
                pygame.mixer.Sound.play(gunshotE)
            if self.rect.x > P1.rect.x:
                eW1 = Bullet1(e3,self.rect.x,self.rect.y,-30)
                eWeaponGroup.add(eW1)
                pygame.mixer.Sound.play(gunshotE)

        if pygame.sprite.groupcollide(eWeaponGroup,playerGroup,1,False):
            P1.health -=1
            hitSound.play()
                
        #col
        if pygame.sprite.spritecollide(P1,enemyGroup2,0,False):
            run = random.randint(0,9)
            P1.health -=1
            hitSound.play()
            if run <=4:
                self.rect.x -= 60
                self.rect.y -= 90
            else:
                self.rect.x+=60
                self.rect.y -= 90

        if pygame.sprite.groupcollide(weaponGroup,enemyGroup2,1,False):
            pygame.mixer.Sound.play(hitSound)

            e3.health -=1
            
        if self.health <= 0:
            pygame.sprite.Sprite.kill(e3)
            enemyGroup2.remove(e3)

            global kc
            kc +=1
            spawner()

        self.repeat +=1
        if self.repeat ==24:
            self.repeat =-1

def spawner():
    global kc
    global e1
    global e2
    global e3
    global bossSpawn
    global boss1
    randX=random.randint(100,1800)
    randY = random.randint(600,900)
    randomNum = random.randint(0,10)
    
    if kc<= 2 and len(enemyGroup)== 0:
        enemyGroup.empty()
        e1= Enemy(randX,randY)
        enemyGroup.add(e1)
        if randomNum <=3:
            healthpack1 = healthPack(randX,randY -400)
            Items.add(healthpack1)

    if kc ==3 and len(enemyGroup1)== 0:
        enemyGroup1.empty()
        e2 =Enemy1(randX,randY)
        enemyGroup1.add(e2)
        
        if randomNum <=3:
            healthpack1 = healthPack(randX,randY -400)
            Items.add(healthpack1)

    if kc >=4 and len(enemyGroup2)== 0:
        enemyGroup2.empty()
        e3 =Enemy2(randX,randY)
        enemyGroup2.add(e3)
        kc=0
        bossSpawn +=1
        if randomNum <=3:
            healthpack1 = healthPack(randX,randY -400)
            Items.add(healthpack1)
            
    if bossSpawn >=3 and len(bossGroup)== 0:
        boss1 = Boss(2000,SCR_HEI-180)
        bossGroup.add(boss1)

#utility#####################################################################################################################################################

def dead():
    global game1
    global menu1
    groupClear()
    game1 = False
    menu1 = True

def groupClear():
    global kc
    global bossSpawn
    kc =0
    bossSpawn = 0
    enemyGroup.empty()
    enemyGroup1.empty()
    enemyGroup2.empty()
    Items.empty()
    playerGroup.empty()
    weaponGroup.empty()
    eWeaponGroup.empty()
    bossGroup.empty()
    
#global######################################################################################################################################################

SCR_WID, SCR_HEI = 1920,1020
screen = pygame.display.set_mode((SCR_WID, SCR_HEI))
pygame.display.set_caption("Pixel Wars!")

pygame.font.init()
textFont = pygame.font.Font("data/font/PressStart2P-Regular.ttf", 16)
textFontBig = pygame.font.Font("data/font/PressStart2P-Regular.ttf", 48)
clock = pygame.time.Clock()
FPS =60
pygame.mixer.init(48000,16,2,4096)

pygame.mixer.set_num_channels(24)


backgroundImg = pygame.image.load('data/sprites/ground.png').convert()
backgroundImg_Copy = backgroundImg.copy()
backgroundImg_Copy = pygame.transform.scale(backgroundImg_Copy,(1920,1020))

hitSound = pygame.mixer.Sound('data/sound/hit1.wav')
footstep = pygame.mixer.Sound('data/sound/footstep.wav')
jump = pygame.mixer.Sound('data/sound/jump.wav')
gunshot = pygame.mixer.Sound('data/sound/gunshot1.wav')
healthpickup = pygame.mixer.Sound('data/sound/heal.wav')
jumpE = pygame.mixer.Sound('data/sound/jump.wav')
gunshotE = pygame.mixer.Sound('data/sound/gunshot2.wav')
footstepE = pygame.mixer.Sound('data/sound/footstep.wav')

music1 = pygame.mixer.music.load('data/sound/music.wav')

#groups######################################################################################################################################################
playerGroup = pygame.sprite.Group(())

P1 = Player(0,SCR_HEI-100)
Dummy= Dummy(1700, 1000)

boss1 = Boss(2000,SCR_HEI-180)

playerGroup.add(P1)

enemyGroup = pygame.sprite.Group(())
enemyGroup1 = pygame.sprite.Group(())
enemyGroup2 = pygame.sprite.Group(())
bossGroup = pygame.sprite.Group(())

eWeaponGroup = pygame.sprite.Group(())

weaponGroup = pygame.sprite.Group(())

healthBar1 = healthBar(20,10)

staminaBar1 = staminaBar(20,40)

UI_Health= pygame.sprite.Group(())
UI_Stamina= pygame.sprite.Group(())

UI_Health.add(healthBar1)
UI_Stamina.add(staminaBar1)

healthpack1 = healthPack(0,0)

Items= pygame.sprite.Group(())

#conditions######################################################################################################################################################
kc =0
bossSpawn=0

floor =81
gravity =15

idle=True
walk=False
facingLeft =False
facingRight = True
grounded = False
counter =10
canJump = True
negative =1

facingLeftE =False
facingRightE = True

up=True
down=False
left=True
right=True
lefta=False
righta=True
eGrounded = False

mainmenu = True
optionsmenu = False
aboutmenu = False
pausemenu = False

game1= False
#global######################################################################################################################################################

def game():
    
    global game1
    global pausemenu
    playerGroup.add(P1)
    
    while game1:
        
        key = pygame.key.get_pressed()
        


        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                exit()
        spawner()

        screen.blit(backgroundImg_Copy,(0,0))
        playerGroup.draw(screen)
        playerGroup.update()

        Items.draw(screen)
        Items.update()

        bossGroup.draw(screen)
        bossGroup.update()
        
        enemyGroup.draw(screen)
        enemyGroup.update()

        enemyGroup1.draw(screen)
        enemyGroup1.update()

        enemyGroup2.draw(screen)
        enemyGroup2.update()
        
        weaponGroup.draw(screen)
        weaponGroup.update()

        eWeaponGroup.draw(screen)
        eWeaponGroup.update()

        UI_Health.draw(screen)
        UI_Health.update()
        UI_Stamina.draw(screen)
        UI_Stamina.update()

        if key[pygame.K_ESCAPE] and pausemenu == False:
            pausemenu = True
            pauseMenu()
            
        pygame.display.flip()
        clock.tick(FPS)

#main######################################################################################################################################################

def main():
    while True:
        mainMenu()
        game()

main()

