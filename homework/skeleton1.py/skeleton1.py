##Skeleton1.py
##Alec Valitutti
##1/27/2020
##skeleton 1 for ITCS1950


##ITCS SHOPPING LIST:
#####VARIABLES
#####CONDITIONALS
#####LOOPS
#####FUNCTIONS 1-4
#####TUPLES/LISTS

#IMPORTS
import time
import random

#listing vars/bools/lists
inCombat = False
attackCommands = ('a','d','attack','Attack','dodge','Dodge')

enemy1List = []
enemy1Health = []
enemy1Attack = []

dodgeChance = 0
killCount = 7

##INTRO FUNCTIONS
def introCredits() :
    print("________________________________________")
    print(" ")
    print("The Great Battle!")
    print("Made By: Alec Valitutti")
    print("________________________________________")
    print(" ")
    time.sleep(2)

def introFunction():
    print("Hello and welcome to 'The Great Battle', do you want to play?")
    playerInput = input()
    playerInput.casefold()

    while str("y") not in playerInput:
        invalidCommandText()
        
        if str("n") in playerInput:
            print("No")
            quitGame()
        playerInput = input()
    else:
        print("Please enter your name.")

##BASE CLASSES FOR PLAYER/ENEMY
#PLAYER
class player:
    def __init__(self, character, health, attack,kills):
        self.character = character
        self.health = health
        self.attack = attack
        self.kills = kills
playerCharacter = player("",6,6,0)

#ENEMY
class enemy:
    def __init__(self,name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
enemyMonster = enemy("",0,0)

##CHARACTER FUNCTIONS  
def characterStats() :
    global myName
    print("________________________________________")
    print("")
    print("Here are your stats, " + myName + ":")
    print ("You have", playerCharacter.health, "health")
    print ("you have", playerCharacter.attack, "attack")
   
###COMBAT FUNCTIONS
    
def playerDead():
    print("You died. What a shame.")
    time.sleep(2)
    quit()

def combatOptions():
    print("________________________________________")
    print("")
    print("what would you like to do, "  + myName +"?")
    print("________________________________________")
    print("")
    print("attack")
    print("dodge")
    print("________________________________________")
    
def playerAttack() :
    enemyMonster.health -= playerCharacter.attack
    print("you deal", playerCharacter.attack, "damage")
    time.sleep(2)

def monsterAttack() :
    if enemyMonster.health >0:
        playerCharacter.health -= enemyMonster.attack
        print("you take", enemyMonster.attack, "damage")
        print("You have", playerCharacter.health, "health remaining")
        if playerCharacter.health == 0:
            playerDead()
        time.sleep(2)
        combatOptions()

def monsterEncounter() :
    print("")
    print("________________________________________")
    print("")
    enemyNameRandomizer()
    combatOptions()
    fightingFunction()

def enemyList1():
    enemy1Attack.append(1)
    enemy1Attack.append(2)
    enemy1Attack.append(3)
    enemy1Health.append(2)
    enemy1Health.append(3)
    enemy1List.append("Warrior")
    enemy1List.append("Mage")
    enemy1List.append("Rogue")

def enemyChange2():
    enemy1List.clear()
    enemy1Attack.clear()
    enemy1Health.clear()
    enemy1List.append("Warlord")
    enemy1List.append("Assasin")
    enemy1List.append("Summoner")
    enemy1Attack.append(3)
    enemy1Attack.append(4)
    enemy1Health.append(4)
    enemy1Health.append(5)

def enemyChange3():
    enemy1List.clear()
    enemy1Attack.clear()
    enemy1Health.clear()
    enemy1List.append("Firelord Warrior")
    enemy1List.append("Beastmaster")
    enemy1List.append("Dark Sage")
    enemy1Attack.append(8)
    enemy1Attack.append(9)
    enemy1Health.append(8)
    enemy1Health.append(9)
    

def fightingFunction():
    global inCombat
    inCombat = True
    playerInput = input()
    if inCombat == True:
        while playerInput not in attackCommands :
            print("Please use a valid input")
            playerInput = input()
        while inCombat:
            if str('d') in playerInput:
                global dodgeChance
                dodgeChance = random.randint(0,9)
                if dodgeChance >4:
                    print("you dodge the attack")
                    dodgeChance = ''
                    combatOptions()
                    playerInput = input()
                else:
                    print("You fail to dodge the attack")
                    monsterAttack()
                    dodgeChance = ''
                    combatOptions()
                    playerInput = input()
                
            if str('a') in playerInput:
                playerAttack()
                if enemyMonster.health >0:
                    monsterAttack()
                    playerInput = input()
                else:
                    deadMonster()
                    break
    
def deadMonster():
    global killCount
    killCount +=1
    print('kc = ', killCount)
    print("You have defeated the", enemyMonster.name,".")
    time.sleep(2)

def enemyNameRandomizer():
    enemyMonster.name = random.choice(enemy1List)
    enemyMonster.health = random.choice(enemy1Health)
    enemyMonster.attack = random.choice(enemy1Attack)
    print("you encounter a(n)", enemyMonster.name, "with ", enemyMonster.health, "health and ",  enemyMonster.attack, "Attack")

#################Loot example###############
##    if enemyMonster.name == "skeleton":
##        inCombat = False
##        playerCharacter.experience +=25
##        randomNumber = random.choice(randomNumber1_10)
##        if randomNumber == 1:
##            print("The skeleton dropped a cracked sword. You pick it up.")
##            time.sleep(2)
##            playerCharacter.attack +=1
##        if randomNumber == 0:
##            print("The skeleton dropped a half empty potion. You pick it up.")
##            time.sleep(2)
##            playerCharacter.health +=1

###UTILITY COMMANDS
def invalidCommandText():
        print("Please enter a valid command")
        print(" ")
        print("what would you like to do?")


def invalidCommand():
        print("Please enter a valid command")
        print(" ")
        print("what would you like to do?")
        playerInput = input()

def quitGame() :
    print("Okay, have a nice day!")
    time.sleep(2)
    quit()

##################################################GAME START##################################
introCredits()
introFunction()
myName = input()
characterStats()
while killCount <3:
    enemyList1()
    monsterEncounter()
while killCount >=3:
    enemyChange2()
    monsterEncounter()
while killCount>7:
    enemyChange3()
    monsterEncounter()
