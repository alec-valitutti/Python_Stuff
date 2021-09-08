#hw12.py
#alec valitutti
#3/20/20
#adding 2nd player1 to cube game


import pygame, sys, random
from pygame.locals import *

# Set up pygame.
pygame.init()
mainClock = pygame.time.Clock()

# Set up the window.
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Input')

# Set up the colors.
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
MYCOLOR = (30,140,200)

# Set up the player1/2 and food data structure.
foodCounter = 0
NEWFOOD = 40
FOODSIZE = 20
player1 = pygame.Rect(100, 300, 50, 50)
player2 = pygame.Rect(300, 100, 50, 50)
foods = []
for i in range(20):
    foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE), random.randint(0, WINDOWHEIGHT - FOODSIZE), FOODSIZE, FOODSIZE))

# Set up movement variables.
moveLeft = False
moveRight = False
moveUp = False
moveDown = False

moveLeft1 = False
moveRight1 = False
moveUp1 = False
moveDown1 = False

MOVESPEED = 6


# Run the game loop.
while True:
    # Check for events.
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            # Change the keyboard variables. player1
            if event.key == K_LEFT:
                moveRight = False
                moveLeft = True
            if event.key == K_RIGHT:
                moveLeft = False
                moveRight = True
            if event.key == K_UP:
                moveDown = False
                moveUp = True
            if event.key == K_DOWN:
                moveUp = False
                moveDown = True

            if event.key == K_KP0:
                player1.top = random.randint(0, WINDOWHEIGHT - player1.height)
                player1.left = random.randint(0, WINDOWWIDTH - player1.width)
                
            #player2
            if event.key == K_a:
                moveRight1 = False
                moveLeft1 = True
            if event.key == K_d:
                moveLeft1 = False
                moveRight1 = True
            if event.key == K_w:
                moveDown1 = False
                moveUp1 = True
            if event.key == K_s:
                moveUp1 = False
                moveDown1 = True
                
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

            if event.key == K_e:
                player2.top = random.randint(0, WINDOWHEIGHT - player1.height)
                player2.left = random.randint(0, WINDOWWIDTH - player1.width)
                
            if event.key == K_LEFT or event.key == K_a:
                moveLeft = False
                moveLeft1 = False
            if event.key == K_RIGHT or event.key == K_d:
                moveRight = False
                moveRight1 = False
            if event.key == K_UP or event.key == K_w:
                moveUp = False
                moveUp1 = False
            if event.key == K_DOWN or event.key == K_s:
                moveDown = False
                moveDown1 = False

        if event.type == MOUSEBUTTONUP:
            foods.append(pygame.Rect(event.pos[0], event.pos[1], FOODSIZE, FOODSIZE))

    foodCounter += 1
    if foodCounter >= NEWFOOD:
        # Add new food.
        foodCounter = 0
        foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE), random.randint(0, WINDOWHEIGHT - FOODSIZE), FOODSIZE, FOODSIZE))

    # Draw the white background onto the surface.
    windowSurface.fill(WHITE)

    # Move the player1.
    if moveDown and player1.bottom < WINDOWHEIGHT:
        player1.top += MOVESPEED
    if moveUp and player1.top > 0:
        player1.top -= MOVESPEED
    if moveLeft and player1.left > 0:
        player1.left -= MOVESPEED
    if moveRight and player1.right < WINDOWWIDTH:
        player1.right += MOVESPEED

    if moveDown1 and player2.bottom < WINDOWHEIGHT:
        player2.top += MOVESPEED
    if moveUp1 and player2.top > 0:
        player2.top -= MOVESPEED
    if moveLeft1 and player2.left > 0:
        player2.left -= MOVESPEED
    if moveRight1 and player2.right < WINDOWWIDTH:
        player2.right += MOVESPEED

    # Draw the player1 onto the surface.
    pygame.draw.rect(windowSurface, BLACK, player1)
    pygame.draw.rect(windowSurface, MYCOLOR, player2)

    # Check if the player1 has intersected with any food squares.
    for food in foods[:]:
        if player1.colliderect(food):
            foods.remove(food)

    for food in foods[:]:
        if player2.colliderect(food):
            foods.remove(food)

    # Draw the food.
    for i in range(len(foods)):
        pygame.draw.rect(windowSurface, GREEN, foods[i])

    # Draw the window onto the screen.
    pygame.display.update()
    mainClock.tick(40 )
