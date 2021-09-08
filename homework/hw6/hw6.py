#hw6.py
#Alec Valitutti
#2/6/2020
#Dictionary program for homework

#notes: I am making a fighting game!

import time

player = {'health': 50,'attack':4,'strength':3}
enemy =  {'health': 10,'attack':1,'strength':1}

##print(dict(player))
##
##print(player['health'])
##print(player['attack'])
##print(player['strength'])
##
##player['health'] +=1
##player['attack'] +=1
##player['strength'] +=1
##
##print(player['health'])


#fighting functions
def fightOptions():
    print("Fight!")
    print("type 'f' to fight!")
    
def deadPlayer():
    print("The player is dead!")
    time.sleep
    quit()

def deadEnemy():
    print("The enemy is dead! You won!")
    time.sleep(2)
    quit()

def playerAttack():
    enemy['health'] -= player['attack']

def enemyAttack():
    player['health'] -= enemy['attack']

def combat():
    fightOptions()
    while enemy['health'] >0:
        playerInput = input()
        if str("f") in playerInput :
            print("player hits the enemy for ",player['attack'],"!")
            playerAttack()
            print("the enemy has", enemy['health']," health left.")
            if enemy['health'] <= 0:
                deadEnemy()
            if enemy['health'] > 0:
                enemyAttack()
                print("the enemy hits back for:",enemy['attack'])
                time.sleep(2)
                fightOptions()

#main    
def main():
    combat()
        
main()


