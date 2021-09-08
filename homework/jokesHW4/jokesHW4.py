#JokesHW4.py
# Alec Valitutti \\ 01/13/2020
#Function : This tells jokes based on input \
#modified joke program

print("Hello! What is your name?")
myName = input()

print("Would you like to hear a joke, " + myName + "?")
answer = input()

if answer == "yes" :
    print('What do you get when you cross a snowman with a vampire?')
    answer = input()

    if answer == "frostbite" :
        print('correct!')
    else :
            print ("Frostbite! Type 'next' for the next joke")
        
    nextJoke1 = input()
    if nextJoke1 == "next" :
        print("What do dentists call an astronaut's cavity?")
        answer = input()
        answer == "A black hole"
        if answer == "A black hole" :
                print('correct!')
        else :
            print ("A black hole! Type 'next' for the next joke")

    nextJoke1 = input()
    if nextJoke1 == "next" :
        print('Knock knock.')
        answer = input()
        answer == "Whose there"
        if answer == "whose there" :
                print('Interrupting cow.')
        answer = input()
        answer == "Interrupting cow who"
        if answer == "Interrupting cow who" :
             print('Interrupting cow wh', end='')
             print('-MOO!')
else :
    print("Okay then, have a nice day!")
