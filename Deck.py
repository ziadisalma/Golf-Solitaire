import random
from Card import Card

class Deck:
    # A constructor which calls functions that generate the set of 52 cards and shuffles them. 
    # We also create an empty list that represent the deck
    def __init__(self):
        self.deckList = []
        self.generateDeck()
        self.shuffle()
        self.drawCard() 
        self.cardsLeft()

    '''
    shuffles the deck of cards by making 150 random swaps
    '''
    def shuffle(self):
        
        # this function uses random swaps to shuffle the deck of cards after they are generated.
        # PSEUDOCODE FOR THIS METHOD
        # repeat the following (indented lines of code) 150 times:

            # declare a variable called index1 and assign it to a random integer between 0 and (the length of the deck of Cards - 1)
            # declare a variable called index2 and assign it to a random integer between 0 and (the length of the deck of Cards - 1)

            # declare a variable called temp and assign it to the element of the deck of Cards located at index1
            # set the element of the deck of Cards located at index1 to the element of the deck located at index2
            # set the element of the deck of Cards located at index2 to temp

        for i in range(150):
            index1= random.randint(0, len(self.deckList)-1)
            index2= random.randint(0, len(self.deckList)-1)

            temp = self.deckList[index1]
            self.deckList[index1]=self.deckList[index2]
            self.deckList[index2] = temp
    '''
    generates a deck of un-shuffled cards
    '''
    # this function generates the 52 Card instances in the deck, stores them in a list, and “stores” that list as a property of the instance.

    def generateDeck(self):
        # create a list that contains 4 suits
        # for a value from 1 to 14 not including 14
            # for a suit in the list of suits created
                #create a card instance
                # add the 13*4 = 52 cards created to the deck 
        suitsList = ['♠','♣','♥','♦']
        for val in range(1,14):
            for suit in suitsList:
                cards = Card(val, suit)
                self.deckList.append(cards)

    
                




    

    '''
    # this function draws a card from the deck and return a card object
    '''
    def drawCard(self):
        # if there are cards remaining in the deck
            # remove the top card from the deck 
            # return it 
        # if there are no cards left
            # display "No remaining cards in the deck" on the terminal
        if self.cardsLeft()>0:
            card = self.deckList.pop(0)
            return card
            
        else:
            print("No remaining cards in the deck")
     
        
        
    
    '''
    # this function returns the number of cards left in the deck as an int
    '''
    def cardsLeft(self):
        # return the length of deckList
        return len(self.deckList)