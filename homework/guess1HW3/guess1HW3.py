#guess1HW3.py
#Programmer : Alec Valitutti
#Date: 01/13/2020
#Function : This is a Guess the Number game.

import random

guessesTaken = 0


print("Hello! What is your name?")
myName = input()

#change the game to be easy or hard
#ask if the user wants it to be easy or hard
#have two copies that make it easy or hard
print("Would you like the game to be easy or hard, " + myName + "?")
answer = input()

if answer == "easy" :
    number = random.randint(1, 20)
    print("Well, " + myName + ", I am thinking of a number between 1 and 20.")

    for guessesTaken in range(6):
        print("Take a guess.") # Four spaces in front of "print".
        guess = input()
        guess = int(guess)

        if guess < number:
            print("Your guess is too low.") # Eight spaces in front of "print"

        if guess > number:
            print("Your guess is too high.")

        if guess == number:
            break
if answer == "hard" :
        number = random.randint(1, 1000)
        print("Well, " + myName + ", I am thinking of a number between 1 and 1000.")

        for guessesTaken in range(2):
            print("Take a guess.") # Four spaces in front of "print".
            guess = input()
            guess = int(guess)

            if guess < number:
                print("Your guess is too low.") # Eight spaces in front of "print"

            if guess > number:
                print("Your guess is too high.")

            if guess == number:
                break


if guess == number:
    guessesTaken = str(guessesTaken + 1)
    print("Good job, " + myName + "! You guessed my number in " + guessesTaken + " guesses!")

if guess != number:
    number = str(number)
    print("Nope. The number I was thinking of was " + number + ".")


