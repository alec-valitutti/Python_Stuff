##beta.py
##Alec Valitutti
##1/27/2020
##beta for ITCS1950

#UPDATES:

##ITCS SHOPPING LIST:
#####VARIABLES *
#####CONDITIONALS *
#####LOOPS *
#return*
#return para
#no return para*
#none*
#####TUPLES/LISTS *

#IMPORTS
import time
import random

#listing vars/bools/lists
inCombat = False
playerShop = False
generalDead = False

enemy1List = []
enemy1Health = []
enemy1Attack = []
enemyRoll = 0

camp1Items = ["Sword","Potion"]
camp2Items = ["Sabre","Potion"]
camp3Items = ["Great Axe","Super Potion"]
potionCount =2
superPotionCount = 2

dodgeChance = 0
killCount = 0

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
    playerInput = input().lower()

    while str("y") not in playerInput:
        invalidCommand()
        playerInput = input()
        
        if str("n") in playerInput:
            print("No")
            quitGame()
        playerInput = input().lower()
    else:
        print("Please enter your name.")

##BASE CLASSES FOR PLAYER/ENEMY
#PLAYER
class player(object):
    def __init__(self, character, health, attack, money):
        self.character = character
        self.health = health
        self.attack = attack
        self.money = money
playerCharacter = player("",5,2,10)

#ENEMY
class enemy(object):
    def __init__(self,name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
enemyMonster = enemy("",0,0)

##CHARACTER FUNCTIONS  
def characterStats(player):
    global myName
    print("________________________________________")
    print("")
    print("Here are your stats, " + myName + ":")
    print ("You have", playerCharacter.health, "health")
    print ("you have", playerCharacter.attack, "attack")
    print ("you have", playerCharacter.money, "coins")



###CAMP FUNCTIONS
def camp1():
    inCombat = False
    time.sleep(2)
    print("The sun is setting... it's time to return home to camp.")
    time.sleep(2)
    print("You return from the battlefield to camp.")
    time.sleep(4)
    if inCombat == False:
        playerShop = True
        print("You go speak to the quartermaster for equiptment.")
        time.sleep(2)
        print("'Hello there! You look like you could use some new equiptment! This is what i have!")
        
    while playerShop == True:
        if camp1Items == []:
            print("I have nothing else to sell. Thanks!")
            time.sleep(2)
            break
        print("________________________________________")
        print()
        print(camp1Items)
        print("________________________________________")
        print("Type '*itemYouWant*' to purchase an item. Type 'Leave' to leave.")
        print("Your gold:", playerCharacter.money)
        print("Your health:", playerCharacter.health)
        print("Your attack:", playerCharacter.attack)
        print("________________________________________")
        playerInput=input()
        if playerInput in ("Leave", "leave","l","L"):
            print("Okay, see you later!")
            playerShop = False
            time.sleep(2)
            break
        if playerInput in ("Sword","sword","s","S") and "Sword" in camp1Items:
            print("The sword costs 20 gold, do you want that?")
            playerInput = input()

            if playerInput in ("y","Y","Yes","yes") and playerCharacter.money >= 20:
                print("Here is your new sword. You gain two attack")
                playerCharacter.money -=20
                playerCharacter.attack +=2
                camp1Items.remove("Sword")
                time.sleep(2)
                
            if playerInput in ("y","Y","Yes","yes")and playerCharacter.money <= 20:
                print("sorry you dont have enough to cover it")
                time.sleep(2)
                
            if playerInput in ("n","N","no","No"):
                print("Okay nevermind then!")
                time.sleep(2)
                
        if playerInput in ("Potion","potion","p","P") and "Potion" in camp1Items:
            print("The potion costs 15 gold, do you want that?")
            playerInput = input()

            if playerInput in ("y","Y","Yes","yes") and playerCharacter.money >= 15:
                print("Here is your new potion. You gain two health")
                playerCharacter.money -=15
                playerCharacter.health +=2
                camp1Items.remove("Potion")
                time.sleep(2)
                
            if playerInput in ("y","Y","Yes","yes")and playerCharacter.money <= 15:
                print("sorry you dont have enough to cover it")
                time.sleep(2)
                
            if playerInput in ("n","N","no","No"):
                print("Okay nevermind then!")
                time.sleep(2)

def camp2():
    inCombat = False
    time.sleep(2)
    print("The sun is setting... it's time to return home to camp.")
    time.sleep(4)
    print("You return from the battlefield to camp.")
    time.sleep(2)
    if inCombat == False:
        playerShop = True
        print("You go speak to the quartermaster for equiptment.")
        time.sleep(2)
        print("'Hello there! You look like you could use some new equiptment! This is what i have!")
        
    while playerShop == True:
        if camp2Items == []:
            print("I have nothing else to sell. Thanks!")
            time.sleep(2)
            break
        print("________________________________________")
        print()
        print(camp2Items)
        print("________________________________________")
        print("Type '*itemYouWant*' to purchase an item. Type 'Leave' to leave.")
        print("Your gold:", playerCharacter.money)
        print("Your health:", playerCharacter.health)
        print("Your attack:", playerCharacter.attack)
        print("________________________________________")
        playerInput=input()
        if playerInput in ("Leave", "leave","l","L"):
            print("Okay, see you later!")
            playerShop = False
            time.sleep(2)
            break
        if playerInput in ("Sabre","sabre","s","S") and "Sabre" in camp2Items:
            print("The sabre costs 40 gold, do you want that?")
            playerInput = input()

            if playerInput in ("y","Y","Yes","yes") and playerCharacter.money >= 40:
                print("Here is your new sabre. You gain four attack")
                playerCharacter.money -=40
                playerCharacter.attack +=4
                camp2Items.remove("Sabre")
                time.sleep(2)
                
            if playerInput in ("y","Y","Yes","yes")and playerCharacter.money <= 40:
                print("sorry you dont have enough to cover it")
                time.sleep(2)
                
            if playerInput in ("n","N","no","No"):
                print("Okay nevermind then!")
                time.sleep(2)
                
        if playerInput in ("Potion","potion","p","P") and "Potion" in camp2Items:
            global potionCount
            print("The potion costs 15 gold, do you want that?")
            playerInput = input()

            if playerInput in ("y","Y","Yes","yes") and playerCharacter.money >= 15:
                print("Here is your new potion. You gain two health")
                playerCharacter.money -=15
                playerCharacter.health +=2
                potionCount -=1
                if potionCount == 0:
                    camp2Items.remove("Potion")
                time.sleep(2)
                
            if playerInput in ("y","Y","Yes","yes")and playerCharacter.money <= 15:
                print("sorry you dont have enough to cover it")
                time.sleep(2)
                
            if playerInput in ("n","N","no","No"):
                print("Okay nevermind then!")
                time.sleep(2)
def camp3():
    global superPotionCount
    inCombat = False
    time.sleep(2)
    print("The sun is setting... it's time to return home to camp.")
    time.sleep(4)
    print("You return from the battlefield to camp.")
    time.sleep(2)
    if inCombat == False:
        playerShop = True
        print("You go speak to the quartermaster for equiptment.")
        time.sleep(2)
        print("'Hello there! You look like you could use some new equiptment! This is what i have!")
        
    while playerShop == True:
        if camp3Items == []:
            print("I have nothing else to sell. Thanks!")
            time.sleep(2)
            break
        print("________________________________________")
        print()
        print(camp3Items)
        print("________________________________________")
        print("Type '*itemYouWant*' to purchase an item. Type 'Leave' to leave.")
        print("Your gold:", playerCharacter.money)
        print("Your health:", playerCharacter.health)
        print("Your attack:", playerCharacter.attack)
        print("________________________________________")
        playerInput=input()
        if playerInput in ("Leave", "leave","l","L"):
            print("Okay, see you later!")
            playerShop = False
            time.sleep(2)
            break
        if playerInput in ("Great Axe","Great Axe","g","G") and "Great Axe" in camp3Items:
            print("The Great Axe costs 80 gold, do you want that?")
            playerInput = input()

            if playerInput in ("y","Y","Yes","yes") and playerCharacter.money >= 80:
                print("Here is your new Great Axe. You gain eight attack")
                playerCharacter.money -=80
                playerCharacter.attack +=8
                camp3Items.remove("Great Axe")
                time.sleep(2)
                
            if playerInput in ("y","Y","Yes","yes")and playerCharacter.money <=80 and "Great Axe" in camp3Items:
                print("sorry you dont have enough to cover it")
                time.sleep(2)
                
            if playerInput in ("n","N","no","No"):
                print("Okay nevermind then!")
                time.sleep(2)
                
        if playerInput in ("Super Potion","Super Potion","p","P","s","S") and "Super Potion" in camp3Items:
            print("The Super Potion costs 30 gold, do you want that?")
            playerInput = input()

            if playerInput in ("y","Y","Yes","yes") and playerCharacter.money >= 30:
                print("Here is your new Super Potion. You gain four health")
                playerCharacter.money -=15
                playerCharacter.health +=4
                superPotionCount -=1
                if superPotionCount == 0:
                    camp3Items.remove("Super Potion")
                time.sleep(2)
                
            if playerInput in ("y","Y","Yes","yes")and playerCharacter.money <= 30 and "Super Potion" in camp3Items:
                print("sorry you dont have enough to cover it")
                time.sleep(2)
                
            if playerInput in ("n","N","no","No"):
                print("Okay nevermind then!")
                time.sleep(2)

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
    print("attack = a")
    print("dodge = d")
    print("stats = s")
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
        if playerCharacter.health <= 0:
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
    enemy1Health.append(2)
    enemy1Health.append(3)
    enemy1List.append("Warrior")
    enemy1List.append("Mage")
    enemy1List.append("Rogue")

def enemyChange2():
    del enemy1List[:]
    del enemy1Attack[:]
    del enemy1Health[:]
    enemy1List.append("Warlord")
    enemy1List.append("Assasin")
    enemy1List.append("Summoner")
    enemy1Attack.append(3)
    enemy1Attack.append(4)
    enemy1Health.append(4)
    enemy1Health.append(5)

def enemyChange3():
    del enemy1List[:]
    del enemy1Attack[:]
    del enemy1Health[:]
    enemy1List.append("Firelord Warrior")
    enemy1List.append("Beastmaster")
    enemy1List.append("Dark Sage")
    enemy1Attack.append(8)
    enemy1Attack.append(9)
    enemy1Health.append(8)
    enemy1Health.append(9)

def finalBoss():
    del enemy1List[:]
    del enemy1Attack[:]
    del enemy1Health[:]
    enemy1List.append("General Warleader")
    enemy1Attack.append(10)
    enemy1Health.append(20)

def fightingFunction():
    global inCombat
    global generalDead
    inCombat = True
    if playerCharacter.health <=0:
        playerDead()
    playerInput = input()
    if inCombat == True:
        if playerCharacter.health <=0:
            playerDead()
        while playerInput not in ("a","d","attack","dodge","s","S","stats","Stats") :
            invalidCommand()
            playerInput = input()
        while inCombat:
            if playerInput in ("s","S","stats","Stats"):
                characterStats(player)
                combatOptions()
                playerInput = input()
            if str('d') in playerInput:
                global dodgeChance
                dodgeChance = random.randint(0,9)
                if dodgeChance >7:
                    print("you dodge the attack")
                    dodgeChance = ''
                    combatOptions()
                    playerInput = input()
                else:
                    print("You fail to dodge the attack")
                    monsterAttack()
                    if playerCharacter.health <= 0:
                        playerDead()
                    dodgeChance = ''
                    combatOptions()
                    playerInput = input()     
                
            if str('a') in playerInput:
                if enemyMonster.name == "General Warleader":
                    randomNumber = random.randint(0,6)
                    if randomNumber <=2:
                        print("The general throws an axe at you!")
                        dodgeChance = random.randint(0,9)
                        time.sleep(2)
                        if dodgeChance >=4:
                            print("you dodge the axe!")
                        else:
                            print("You were hit by the axe! You take 5 damage!")
                            playerCharacter.health -=5
                            time.sleep(2)
                if playerCharacter.health <=0:
                    playerDead()
                playerAttack()
                if enemyMonster.health >0:
                    monsterAttack()
                    playerInput = input()
                else:
                    deadMonster()
                    playerLoot()
                    if enemyMonster.name == "General Warleader":
                        generalDead = True
                    break
def playerLoot():
    if enemyMonster.name == "Warrior":
        playerCharacter.money += 15
        print("You gain 15 coins.")
        randomNumber = random.randint(0,5)
        if randomNumber <=3:
            print("The Warrior dropped a cracked sword. You pick it up. You gain one attack")
            time.sleep(2)
            playerCharacter.attack +=1
        if randomNumber >=4:
            print("The Warrior dropped a half empty potion. You pick it up. You gain one health")
            time.sleep(2)
            playerCharacter.health +=1
    if enemyMonster.name == "Rogue":
        playerCharacter.money += 30
        print("You gain 30 coins.")
        randomNumber = random.randint(0,5)
        if randomNumber <=3:
            print("The Rogue dropped a cracked sword. You pick it up. You gain one attack")
            time.sleep(2)
            playerCharacter.attack +=1
        if randomNumber >=4:
            print("The Rogue dropped a half empty potion. You pick it up. You gain one health")
            time.sleep(2)
            playerCharacter.health +=1
    if enemyMonster.name == "Mage":
        playerCharacter.money += 10
        print("You gain 10 coins.")
        randomNumber = random.randint(0,5)
        if randomNumber <=3:
            print("The Mage dropped a Potion. You pick it up. You gain two health")
            time.sleep(2)
            playerCharacter.health +=2
        if randomNumber ==5:
            print("The Mage dropped a health scroll. You pick it up. You gain five health")
            time.sleep(2)
            playerCharacter.health +=5

    if enemyMonster.name == "Summoner":
        playerCharacter.money += 20
        print("You gain 40 coins.")
        randomNumber = random.randint(0,10)
        if randomNumber <=3:
            print("The Summoner dropped a Combat Scroll. You pick it up. You gain three attack")
            time.sleep(2)
            playerCharacter.attack +=3
    if enemyMonster.name == "Warlord":
        playerCharacter.money += 50
        print("You gain 40 coins.")
        randomNumber = random.randint(0,10)
        if randomNumber <=3:
            print("The Warlord dropped a Combat Scroll. You pick it up. You gain three attack")
            time.sleep(2)
            playerCharacter.attack +=3
    if enemyMonster.name == "Assasin":
        playerCharacter.money += 30
        print("You gain 30 coins.")
        randomNumber = random.randint(0,10)
        if randomNumber <=3:
            print("The Assasin dropped a Combat Scroll. You pick it up. You gain three attack")
            time.sleep(2)
            playerCharacter.attack +=3
    print("________________________________________")

def deadMonster():
    global killCount
    killCount +=1
    print('kc = ', killCount)
    print("You have defeated the", enemyMonster.name,".")
    time.sleep(2)
    
### ENEMY RANDOMIZER/UNIQUE ATTACKS
def enemyNameRandomizer():
    global dodgeChance
    global enemyRoll
    enemyMonster.name = random.choice(enemy1List)
    enemyMonster.health = random.choice(enemy1Health)
    enemyMonster.attack = random.choice(enemy1Attack)
    print("you encounter a(n)", enemyMonster.name, "with ", enemyMonster.health, "health and ",  enemyMonster.attack, "Attack")
    if enemyMonster.name =="Dark Sage":
        enemyRoll = random.randint(0,5)
        if enemyRoll <= 2:
            time.sleep(2)
            print("The Dark Sage channels ancient power. He hurls a dark storm at you!")
            time.sleep(2)
            dodgeChance = random.randint(0,9)
            if dodgeChance >7:
                print("you dodge the attack")
                time.sleep(2)
            else:
                print("You were hit by the Dark storm! You have been Confused! You lose some attack and health.")
                playerCharacter.health -= 1
                playerCharacter.attack -=2
                time.sleep(2)
                print("Your stats are now:",playerCharacter.health,"health and",playerCharacter.attack,"attack")
                time.sleep(2)
            
        if enemyRoll == 5:
            time.sleep(2)
            print("The Dark Sage channels ancient energy, granting him extra health and attack.")
            time.sleep(4)
            enemyMonster.health += 4
            enemyMonster.attack +=4
            print("The Dark Sage's stats are now", enemyMonster.health, "health and ",  enemyMonster.attack, "Attack" )
            time.sleep(2)
            
    if enemyMonster.name =="Beastmaster":
        random.randint(0,5)
        if enemyRoll <= 2:
            print("The Beastmaster sends his hounds after you!")
            time.sleep(2)
            dodgeChance = random.randint(0,9)
            if dodgeChance >7:
                print("you dodge the hounds!")
                time.sleep(2)
            else:
                print("You have been bitten by one of the hounds!")
                time.sleep(2)
                playerCharacter.health -=2
                print("Your stats are now:",playerCharacter.health,"health and",playerCharacter.attack,"attack")
                time.sleep(2)
    if enemyMonster.name =="Firelord Warrior":
        random.randint(0,5)
        if enemyRoll <= 2:
            time.sleep(2)
            print("The Firelord Warrior shouts and throws a fireball at you!")
            time.sleep(2)
            dodgeChance = random.randint(0,9)
            if dodgeChance >5:
                print("you dodge the fireball")
                time.sleep(2)
            else:
                print("You have been hit by the fireball, you have been burned! You lose health and attack.")
                time.sleep(2)
                playerCharacter.health -=3
                playerCharacter.attack -=1
                print("Your stats are now:",playerCharacter.health,"health and",playerCharacter.attack,"attack")
                time.sleep(2)
    if enemyMonster.name == "General Warleader":
        enemyRoll = random.randint(0,7)
        if enemyRoll <= 3:
            time.sleep(2)
            print("The General channels his inner power, he gains attack and health!")
            time.sleep(2)
            enemyMonster.health += 10
            enemyMonster.attack +=5
            print("The General's stats are now", enemyMonster.health, "health and ",  enemyMonster.attack, "Attack" )
            dodgeChance = random.randint(0,9)
            time.sleep(2)
        
    if playerCharacter.health <= 0:
        playerDead()

###STORY COMMANDS
def introStory():
    print("You are a warrior in the great general's army.")
    time.sleep(2)
    print("He has issued all of his loyal subjects to fight and take down the other general at all costs.")
    time.sleep(2)
    print("You prepare yourself for the upcoming battle.")
    time.sleep(2)

def returnBattleStory():
    print("You prepare yourself for the upcoming battle.")
    time.sleep(2)
    print("You return to the battlefield.")
    time.sleep(2)

def endCredits():
    print("You take a sigh of relief upon slaying the general.")
    time.sleep(2)
    print("You return back to camp")
    time.sleep(4)
    print("You report to your general and inform him of the news")
    time.sleep(2)
    print('You have done well, and for that, we will send you home. Thank you for your courage.')
    time.sleep(2)
    print("You climb abord the ship and sail home!")
    time.sleep(2)
    
###UTILITY COMMANDS
def replay():
    print("do you want to play again?")
    answer = answerYN()
    while answer not in ("y","Y","n","N"):
        print("Please enter a valid command. 'y' for yes, 'n' for no.")
        answer = answerYN()
    if answer =="y":
        main()
    if answer == "n":
        quitGame()
def answerYN():
    answer = input().lower()
    return answer

def invalidCommand():
        print("Please enter a valid command")
        print(" ")
        print("what would you like to do?")

def quitGame() :
    print("Okay, have a nice day!")
    time.sleep(2)
    quit()

def main():
    introStory()
    while killCount <=3:
        enemyList1()
        monsterEncounter()
    camp1()
    returnBattleStory()
    while killCount >=4 and killCount <7:
        enemyChange2()
        monsterEncounter()
    camp2()
    returnBattleStory()
    while killCount>=7 and killCount <=9:
        enemyChange3()
        monsterEncounter()
    camp3()
    returnBattleStory()
    while killCount>=10 and generalDead == False:
        finalBoss()
        monsterEncounter()
        if generalDead == True:
            break
    endCredits()
##################################################GAME START##################################
introCredits()
introFunction()
myName = input()
characterStats(player)
main()
replay()
