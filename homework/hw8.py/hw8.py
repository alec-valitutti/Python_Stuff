#hw8.py
#Alec Valitutti
#2/10/2020 -2/19/2020
#class practice

#2 atrib added color and str
#modify critter class to have private and public access to them
#validate the inputs

class Critter(object):#defining a class
    """a vitural pet"""
    total = 0
    def __init__(self,name,numOfLegs,mood,color,strength):#constructor
        print("a new critter has been born!")
        self.name = name #member of instance
        self.legs = numOfLegs #member of instance
        self.__mood = mood #private member/atrib
        self.__color = color
        self.__str = strength
        Critter.total = Critter.total +1
    def __str__(self):
        rep = "critter object \n"
        rep += "name:" + self.name +"\n"
        rep +="legs:" + str(self.legs) +'\n'
        return rep

    def get_str(self):
        return self.__str
    
    def set_str(self,new_strength):
        if type(new_strength) == str:
            print("cant be string only int")
            new_strength = str(new_strength)
        else:
            self.__str = new_strength
    strength = property(get_str,set_str)

    def get_color(self):
        return self.__color
    def set_color(self,new_color):
        if new_color == "":
            print("Critter's name can't be an empty string")
        else:
            self.__color = new_color
            print("color change successful")
    color=property(get_color,set_color)
    
    def get_name(self):
        return self.__name
    
    def set_name(self,new_name):
        if new_name =="":
            print("Critter's name can't be an empty string")
        else:
            self.__name = new_name
            print("name change successful")
    name=property(get_name,set_name)

    def publicMethod(self):
        print("This is a public method.")
        self.__private_Method()
        
    def __private_Method(self):
        print("This is a private method.")
        
    def updateName(self,nName):
        self.name = nName
        
    def updateColor(self,nColor):
        self.color = nColor

    def intLegs(self,val):
        if self.legs== val:
            return self.name
        else:
            return "nope"

    def talk(self):#defining a method
        print("hi i'm ", self.name,"I have", self.legs, "Legs.")
        print("right now i feel", self.__mood,".")
        
def legTest(List,nom):
    foundOne = ""
    for crit in List:
        foundOne = crit.intLegs(nom)
        print(foundOne)
        if foundOne!="nope":
            break
    return foundOne

def main():
    foundOne = ""
    crit1 = Critter("george",4,"happy","orange",5)
    print(crit1) 
    crit1.talk()#method

##    crit2 = Critter("mary",2)
##    print(crit2)
##    #crit2.talk()#method
##
##    crit3 = Critter("bob",3)
##    print(crit3)
##    #crit3.talk()#method
##    
##    crit4 = Critter("jack",8)
##    print(crit4)
##    #crit4.talk()#method


    crit5 = Critter("Dave",7,"sad","blue",100)
    print(crit5.color)
    print(crit5)
    crit5.updateName("r2d2")
    print(crit5)
    crit5.talk()
    crit5.publicMethod()
    crit5.set_name("")
    crit5.set_name("bobby")
    crit5.set_color("green")
    crit5.set_str(5)
    print(crit5.strength)
    crit5.set_str("pizza")
    print(crit5.strength)
    print(crit5.color)
    crit5.updateColor("red")
    print(crit5.color)

##    Critters = [crit1,crit2,crit3,crit4]
##    critter = legTest(Critters,3)
##    print("The following critter has 3 legs:" + critter)
##    print(Critter.total)
##    print(crit1.total)




main()
