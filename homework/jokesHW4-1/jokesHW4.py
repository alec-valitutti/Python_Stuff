#JokesHW4.py
# Alec Valitutti \\ 01/13/2020
#Function : This tells jokes based on input \
#modified joke program
import time

print("Hello! What is your name?")
myName = input()

print("Would you like to hear a joke, " + myName + "?")
answer = input()

if answer == "yes" or answer == "Yes"  :
    print('What do you get when you cross a snowman with a vampire?')
    answer = input()

    if answer == "frostbite" or answer == "Frostbite" :
        print("correct! Type 'next' for the next joke")
    else :
            print ("Frostbite! Type 'next' for the next joke")
        
    nextJoke1 = input()
    if nextJoke1 == "next" or nextJoke1 == "Next" :
        print("What do dentists call an astronaut's cavity?")
        answer = input()
        answer == "A black hole"
        if answer == "A black hole" or answer == "a black hole" or answer == "A Black Hole" :
                print("correct! Type 'next' for the next joke")
        else :
            print ("A black hole! Type 'next' for the next joke")

    nextJoke1 = input()
    if nextJoke1 == "next" or nextJoke1 == "Next"  :
        print('Knock knock.')
        answer = input()
        answer == "Whose there"
        if answer == "Whose there" or answer == "whose there" :
                print('Interrupting cow.')
        answer = input()
        answer == "Interrupting cow who"
        if answer == "Interrupting cow who" or answer == "interrupting cow who" :
             print('Interrupting cow wh', end='')
             print('-MOO!')
             time.sleep(1)
             print("___________________________")
             print("Have a nice day!")
             time.sleep(1)
             quit()
else :
    print("Okay then, have a nice day!")
    time.sleep(1)
    quit()
