import random
import time

def displayIntro():
    print('''You are in a land full of dragons. In front of you,
you see four caves. In one cave, the dragon is friendly
and will share his treasure with you. In another cave, the dragon
is greedy and hungry, and will eat you on sight. The other two are a mystery....''')
    print()

def chooseCave():

    cave = ''
    while cave != '1' and cave != '2' and cave != '3' and cave != '4':
        print('Which cave will you go into? (1, 2,3 or 4)')
        cave = input()

    return cave

def checkCave(chosenCave):
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1, 4)
    print("_______________________________")
    print()
    if friendlyCave == 1:
         print('Gives you his treasure!')

    if friendlyCave == 2:
         print('Gobbles you down in one bite!')

    if friendlyCave == 3:
         print('Asks if you want him to do your taxes.')

    if friendlyCave == 4:
         print('Starts to talk about how exicted he is that he has a visitor.')
    print("_______________________________")
         
time.sleep(2)

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)

    print('Do you want to play again? (yes or no)')
    playAgain = input()
