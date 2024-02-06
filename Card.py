class Card:
    # this constructor sets the Card's value and suit
    def __init__(self, value, suit):
        self.suit = suit
        self.value = value
        
    # this getter gets the card's suit
    def getSuit(self):
        return self.suit
    # this getter gets the card's value
    def getValue(self):
        return self.value

    # this string method returns a String representation of the card's suit and value
    def __str__(self):
        return str(self.suit)+ str(self.value)
    
        