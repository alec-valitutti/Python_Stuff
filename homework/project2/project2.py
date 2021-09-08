#project2.py
#Alec Valitutti
#3/28/2020
#Modified Pong game for project 2

import pygame
import time
import random

class Player():
        def __init__(self,side):
                if side == 'left':
                        self.x, self.y = 16, SCR_HEI/2
                else:
                        self.x, self.y = SCR_WID-16, SCR_HEI/2

                self.speed = 3
                self.padWid, self.padHei = 8, 64
                self.score = 0
                self.scoreFont = pygame.font.Font("imagine_font.ttf", 64)
       
        def scoring(self,side):
                global winner
                if side == 'left':
                        scoreBlit = self.scoreFont.render(str(self.score), 1, (255, 255, 255))
                        screen.blit(scoreBlit, (32, 16))
                        if self.score == 10:
                                pygame.mixer.music.stop()
                                time.sleep(1)
                                pygame.mixer.Sound.play(win1)
                                screen.blit(p1win,(0,0))
                                winner=0
                else:
                        scoreBlit = self.scoreFont.render(str(self.score), 1, (255, 255, 255))
                        screen.blit(scoreBlit, (SCR_HEI+92, 16))
                        if self.score == 10:
                                pygame.mixer.music.stop()
                                time.sleep(1)
                                pygame.mixer.Sound.play(win1)
                                screen.blit(p2win,(0,0))
                                winner =1
        def movement(self,side):
                if side == 'left':
                        keys = pygame.key.get_pressed()
                        if keys[pygame.K_w]:
                                self.y -= self.speed
                        elif keys[pygame.K_s]:
                                self.y += self.speed
               
                        if self.y <= 0:
                                self.y = 0
                        elif self.y >= SCR_HEI-64:
                                self.y = SCR_HEI-64
                else:

                        keys = pygame.key.get_pressed()
                        if keys[pygame.K_UP]:
                                self.y -= self.speed
                        elif keys[pygame.K_DOWN]:
                                self.y += self.speed
               
                        if self.y <= 0:
                                self.y = 0
                        elif self.y >= SCR_HEI-64:
                                self.y = SCR_HEI-64
        def draw(self):
                pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.padWid, self.padHei))
 
class Ball():
        def __init__(self):
                self.x, self.y = SCR_WID/2, SCR_HEI/2
                self.speed_x = -3
                self.speed_y = 3
                self.size = 8
       
        def movement(self):
                self.x += self.speed_x
                self.y += self.speed_y
 
                #wall col
                if self.y <= 20:
                        self.speed_y *= -1
                        pygame.mixer.Sound.play(wallCol1)
                elif self.y >= SCR_HEI-self.size-20:
                        self.speed_y *= -1
                        pygame.mixer.Sound.play(wallCol1)
                if self.x <= 0:
                        pygame.mixer.Sound.play(score1)
                        self.__init__()
                        enemy.score += 1
                        global backgroundCounter
                        backgroundCounter +=1
                elif self.x >= SCR_WID-self.size:
                        pygame.mixer.Sound.play(score1)
                        self.__init__()
                        self.speed_x = 3
                        player.score += 1
                        global backgroundCounter
                        backgroundCounter +=1

                ##wall col
                #paddle col
                #player
                for n in range(-self.size, player.padHei):
                        if self.y == player.y + n:
                                if self.x <= player.x + player.padWid:
                                        pygame.mixer.Sound.play(paddleCol1)
                                        self.speed_x *= -1
                                        break
                        n += 1
                #enemy
                for n in range(-self.size, enemy.padHei):
                        if self.y == enemy.y + n:
                                if self.x >= enemy.x - enemy.padWid:
                                        pygame.mixer.Sound.play(paddleCol1)
                                        self.speed_x *= -1
                                        break
                        n += 1
                ##paddle col
 
        def draw(self):
                pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, 8, 8))

musicPlaying =False
musicCounter = 1

def music():

        global musicPlaying
        global musicCounter
                
        if pygame.mixer.music.get_busy() == 0 and musicCounter ==1:
                pygame.mixer.music.load('music1.wav')
                pygame.mixer.music.play(3)
                musicCounter +=1

        if pygame.mixer.music.get_busy() == 0 and musicCounter ==2:
                pygame.mixer.music.load('music3.wav')
                pygame.mixer.music.play(3)
                musicCounter +=1

        if pygame.mixer.music.get_busy() == 0 and musicCounter ==3:
                pygame.mixer.music.load('music5.wav')
                pygame.mixer.music.play(-1)
                musicCounter +=1
def backMgr():
        if backgroundCounter <=2:
                screen.blit(bck1,(0,0))
        if 3<= backgroundCounter <=5:
                screen.blit(bck2,(0,0))
        if 6<= backgroundCounter <=8:
                screen.blit(bck7,(0,0))
        if 9<= backgroundCounter <=11:
                screen.blit(bck4,(0,0))
        if 12<= backgroundCounter <=14:
                screen.blit(bck5,(0,0))
        if 15<= backgroundCounter <=17:
                screen.blit(bck6,(0,0))
        if 18<= backgroundCounter <=100:
                screen.blit(bck3,(0,0))
                
def winMgr():
        global winner
        if winner ==0:
                screen.blit(p1win,(0,0))
                exit()
        if winner ==1:
                screen.blit(p2win,(0,0))
                exit()
                
SCR_WID, SCR_HEI = 640, 480
screen = pygame.display.set_mode((SCR_WID, SCR_HEI))
pygame.display.set_caption("Pong")
pygame.font.init()
clock = pygame.time.Clock()
FPS = 60

player = Player('left')
ball = Ball()
enemy = Player('right')

pygame.mixer.init(48000, 16, 2, 4096)

paddleCol1 = pygame.mixer.Sound('beep2.wav')
wallCol1 = pygame.mixer.Sound('beep3.wav')
score1 = pygame.mixer.Sound('beepScore.wav')
music1 = pygame.mixer.music.load('music1.wav')
win1 = pygame.mixer.Sound('win1.wav')

bck1 = pygame.image.load('background.png')
bck2 = pygame.image.load('background1.png')
bck3 = pygame.image.load('background2.png')
bck4 = pygame.image.load('background4.png')
bck5 = pygame.image.load('background5.png')
bck6 = pygame.image.load('background3.png')
bck7 = pygame.image.load('background7.png')
p1win = pygame.image.load('p1win.png')
p2win = pygame.image.load('p2win.png')

backgroundCounter =0

winner =2

def main():
        
        while True:
                winMgr()
                #process
                for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                        print ("Game exited by user")
                                        
                                        exit()
                music()
                ##process
                #logic
                ball.movement()
                player.movement('left')
                enemy.movement('right')
                screen.fill((0, 0, 0))
                backMgr()
                
                ##logic
                #draw      
                ball.draw()
                player.draw()
                player.scoring('left')
                enemy.draw()
                enemy.scoring('right')
                ##draw
                #_______
                pygame.display.flip()
                clock.tick(FPS)

main()
