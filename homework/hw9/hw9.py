#hw9.py
#Alec Valitutti
#2/27/2020
#card deal edit for hw9
#create 3 more players ... deal cards ...

#exercise methods flip, after every card move display the contents of the hands
#and the deck.

class Card(object):
    """ A playing card. """
    RANKS = ["A", "2", "3", "4", "5", "6", "7",
             "8", "9", "10", "J", "Q", "K"]
    SUITS = ["c", "d", "h", "s"]
    
    def __init__(self, rank, suit):
        self.rank = rank 
        self.suit = suit

    def __str__(self):
        rep = self.rank + self.suit
        return rep
    
class Unprintable_Card(Card):
    def __str__(self):
        return "<unprintable>"
    
class Positionable_Card(Card):
    def __init__(self, rank, suit, face_up = True):
      super(Positionable_Card, self).__init__(rank, 
                                              suit)
      self.is_face_up = face_up
    def __str__(self):
      if self.is_face_up:
           rep = super(Positionable_Card, self).__str__()
      else:
           rep = "XX"
      return rep

    def flip(self):
        self.is_face_up = not self.is_face_up

class Hand(object):
    """ A hand of playing cards. """
    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
           rep = ""
           for card in self.cards:
               rep += str(card) + "  "
        else:
            rep = "<empty>"
        return rep

    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)
        
class Deck(Hand):
    """ A deck of playing cards. """
    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS: 
                self.add(Card(rank, suit))

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal(self, hands, per_hand = 1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print ("Out of cards!")



def main():
    card1 = Card(rank = "A", suit = "c")
    card2 = Card(rank = "2", suit = "c")
    card3 = Card(rank = "3", suit = "c")
    card4 = Card(rank = "4", suit = "c")
    card5 = Card(rank = "5", suit = "c")
##    print (card1)  # Ac
##    print (card2)  # 2c
##    print (card3)  # 3c
##    print (card4)  # 4c
##    print (card5)  # 5c
##    my_hand = Hand()
##    print (my_hand)  # <empty>
##    my_hand.add(card1)
##    my_hand.add(card2)
##    my_hand.add(card3)
##    my_hand.add(card4)
##    my_hand.add(card5)
##    print (my_hand)  # Ac 2c 3c 4c 5c
##    your_hand = Hand()
##    my_hand.give(card1, your_hand)
##    my_hand.give(card2, your_hand)
##    print (your_hand)  # Ac 2c
##    print (my_hand)    # 3c 4c 5c
##    my_hand.clear()
##    print (my_hand)   # <empty>
##    print("Following output is for deck")
##    deck1 = Deck()
##    print(deck1)
##    deck1.add(card5)
##    print(deck1)
##    print("the following is for give example")
##    deck2 = Deck()
##    deck1.give(card5,deck2)
##    print(deck1)
##    print(deck2)
##    deck2.clear()
##    deck1.populate()
##    print(deck1)
##    deck1.shuffle()
##    print(deck1)
##    my_hand.clear()
##    your_hand.clear()
##    hands = [my_hand,your_hand]
##    print("the follwoing is for deal")
##    deck1.deal(hands,2)
##    print(my_hand)
##    print(your_hand)
##    print("remaining cards in the deck")
##    print(deck1)
##    up1 = Unprintable_Card("I love ITCS 195", "frank")
##    print(up1)
##    pc1 = Positionable_Card("I love ITCS 1950", "frank")
##    print(pc1)
##    pc1.flip()
##    print(pc1)
    
    player1 = Hand()
    player2 = Hand()
    player3 = Hand()
    player4 = Hand()

    dealerFlip = Positionable_Card(2,"c")
    hands = [player1,player2,player3,player4]
    deck1 = Deck()
    deck1.populate()
    deck1.shuffle()
    deck1.deal(hands,2)
    
    print(deck1)
    print(player1)
    print(player2)
    print(player3)
    print(player4)
    print("____")
    dealerFlip.flip()
    print(dealerFlip)

    deck1.deal(hands,1)
    print(player1)
    print(player2)
    print(player3)
    print(player4)
    print(deck1)

    player1.clear()
    player2.clear()
    player3.clear()
    player4.clear()

    print(player1)
    print(player2)
    print(player3)
    print(player4)

    card6 = Card(rank ="a",suit ="6")
    card7 = Card("s","2")
    card8 = Card("h","10")
    card9 = Card("c","3")

    player1.add(card6)
    player2.add(card7)
    player3.add(card8)
    player4.add(card9)

    print(player1)
    print(player2)
    print(player3)
    print(player4)

    player1.give(card6,player2)
    print(player1)
    print(player2)

    player1.clear()
    player2.clear()
    player3.clear()
    player4.clear()

    deck1.shuffle()
    deck1.deal(hands,10)
    print(player1)
    print(player2)
    print(player3)
    print(player4)
    print(deck1)
    
    

main()







    

