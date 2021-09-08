#HW5.py
#alec valitutti
#1/30/2020
# callable functions for homework5

tup = ('George', 50)
scores = [["health",50], ["ammo", 25], ["weapon", "light sabre"]]
pizza = ["pizza",1]

def showHowmany(scores, item):
    i = scores.count(item)
    
    return i
def showScores(scores):
    for entry in scores:
        score, name = entry
        print( name, "\t", score)


def scoresCheck():
    print (scores)

def listAppend():
    print("Type what you want to add to the list! First add an object/item, then a quantity!")
    scores.append([input(),input()])
    print(scores)
    print("_______________________________________________________________________________________")

def listPrintSpecific():
    print("scores contains", len(scores),"entries.")
    print(scores[0][0])
    print(scores[0][1])
    print(scores[1][0])
    print(scores[1][1])
    print(scores[2][0])
    print(scores[2][1])
    print("_______________________________________________________________________________________")

def scoreIfStatement():
    print("This checks to see if a specific value in scores is equal to something")
    if scores[1][1] == 1500:
        print("Got one")
    else:
        print("scores [1][1] doesn't equal 1500")
    print("_______________________________________________________________________________________")
    
def newEntry():
    print("This adds an entry to this list!")
    showScores(scores)
    print("____________________________________________________________________________")
    print("Shemp is added to the list")
    name, score = ("Shemp", 175)
    entry = name, score
    scores.append(entry)
    showScores(scores)
    print("____________________________________________________________________________")


def listCount():
    print("This shows how many times 'x' is in your list")
    x = showHowmany(scores, tup)
    print(x)
    if x == 1:
        print("yep")
    else:
        print("nope")
def listCountAppend():
    print("if we append it to scores then it will return 1 and yes")
    scores.append(tup)
    x = showHowmany(scores, tup)
    print(x)
    if x == 1:
        print("yep")
    else:
        print("nope")

def listReverse():
    print("This reverses entries in list")
    print(scores)
    scores.reverse()
    print(scores)
    
def listPop():
    print("This removes a specific location that you define")
    print(scores)
    scores.pop([1][0])
    print(scores)

def listExtend():
    print("extends list by what you tell it to")
    print(scores)
    scores.extend(scores)
    print(scores)

def listInsert():
    print("lets you insert an entry and pick where it goes")
    print(scores)
    print("_____________")
    print("told it to go into the '2' spot")
    scores.insert(2,pizza)
    print(scores)

scoresCheck()
listPrintSpecific()
listAppend()
scoreIfStatement()
newEntry()
listCount()
listCountAppend()
listReverse()
listPop()
listExtend()
listInsert()
