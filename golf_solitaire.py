from Card import Card
from Deck import Deck



    
'''

displays a grid of cards arranged in 7x5 col/row formatted like this:
[   [row1, row2, row3...],  <-col1
    [row1, row2, row3...],  <-col2
    [row1, row2, row3...],  <-col3
    ...
]

params:
    grid - a 2D list in the format shown above

returns:
    None (output from this function is printed)

'''
def displayGrid(grid):

    #generate and display the index header for the grid
    headerStr = ""
    for row in range(7):
        headerStr += " \t" + str(row) + "\t "
    print(headerStr)
    print()

    #proces through each of the rows in reverse because we need to print top to bottom (ie last index to first)
    for row in range(4, -1, -1):

        #generate the full string for a row before printing it
        rowStr = "|\t"
        for col in range(7):
            #create an index offset so that cards are always aligned at the top
            offset = 5 - len(grid[col])
            rowIdx = row - offset

            #as long as the row index is valid, get the data for that particular card
            if(rowIdx >=0):
                rowStr += str(grid[col][rowIdx]) + "\t|\t"
            
            #otherwise print an empty space
            else:
                rowStr += "  \t|\t"
            
        #print the completed row and a row separator
        print(rowStr)
        print()





'''
Initializes a grid of cards for golf solitaire

params:
    deck - an instance of the deck class to draw cards from

returns:
    a 2D list of card objects formatted in a 7x5 configuration for 7 columns and 5 rows
'''
# this function takes a Deck object as an argument and removes cards from that deck and returns a 2D list of Card objects formatted in a 7x5 configuration for 7 columns and 5 rows. This function generates the main grid of cards used in the game. Each sublist in the 2D list should be considered to be one of the columns. 

def initGrid(deck):
    # create an empty list called grid
    grid = [] 
    # we create 7 empty lists that represent columns  
    for i in range(7):
        column = []
        # we will draw 5 cards and add them to each list = column 
        #add the columns to the grid
    # store the grid
        for x in range(5):
            cardsDrawn = deck.drawCard()
            column.append(cardsDrawn)
        grid.append(column)
    return grid



'''
Checks whether the grid is empty (ie the grid is a list containing only empty lists). Example is below:

    [ [], [], [], [], [], [], [] ] <--- This grid is empty
    [ [Card, Card], [], [], [Card], [], [], [] ] <--- This grid is NOT empty

params:
    grid - a 2D list in the format shown above

returns:
    True if the grid is empty
    False if the grid is not empty

'''
# which takes a grid (2D list) of Card objects as an argument and returns True if the grid is empty (i.e., the game is won) and False if the grid is not empty (i.e., the game is not won). A grid is considered empty if the sublists that contain Cards have no Card objects left in them.
def checkWin(grid):
    # for each column in the grid
        # if the length of the column list is different than 0
            # return False, the user hasn't won
    # return false if no so they're all empty 
    for i in range(7):
        if len(grid[i]) != 0:
            return False
    return True

    




'''
Calculates the abs between the values of two cards
params:
    card1 - instance of the Card class
    card2 - instance of the Card class

returns:
    the absolute value between the two cards (accounting for A/J/Q/K)

'''
# this function  takes 2 Card objects and returns the absolute value of the difference between the two values of the two cards.
def compareCards(card1, card2):
    # the difference is equal to the absolute value of the value of the first card minus the value of the second card, we find the value using the getter used in Card class.
    # store the difference 
    dif = abs(card1.getValue()-card2.getValue())
    return dif


'''
Main game function

params:
    none

returns:
    none

'''
def main():
    #generate the deck of cards
    my_deck = Deck()
    #setting up the grid of cards
    grid = initGrid(my_deck)
    #shuffling the cards
    my_deck.shuffle()
    #displaying the grid
    displayGrid(grid)
    # we start the game with no wastecard so the wastecard is None
    wastecard = None
    #set the question to an empty string
    question = ""
    #While the player has not lost the game 
    while checkWin(grid) == False:
        
        #ask the user what they want to do : draw card from deck, select card from grid, or quit the game
        question = input("Enter the number of the column which card you want to remove or click 'd' to take card from deck or click 'q' to quit: ")
        #display grid for player to keep track of what they're doing
        displayGrid(grid)
        # if the user decided to quit then diplay "You have quit the game" on the terminal
        if question == "q":
            print("You have quit the game")
        # else if the user decides to draw a card from the deck make that card the wastecard
        #display what the wastecard is on the terminal
        elif question == "d":
            wastecard = my_deck.drawCard()
            print("the wastecard is:", wastecard)
        # else if the user selects a card from a column between 0 and 6
            # assign that card to variable called selectedCard
            # if there is no waste card or if the abs difference between the value of the selected card and that of the wastecard is 1:
                #remove that card from the grid
                # make that card the wastecard
                #display grid to see the card removed
                #display what the wastecard is on the terminal
            # if there abs difference is different than 1 and there is a wastecard
                # display what the wastecard was 
                # ask the user to try different card 
        
        
        
        elif int(question)>=0 and int(question)<=6:
            selectedCard = grid[int(question)][0]
            if wastecard == None or compareCards(selectedCard, wastecard)==1 or (selectedCard.getValue()== 13 and wastecard.getValue()== 1) or (selectedCard.getValue()== 1 and wastecard.getValue()== 13):
                selectedCard = grid[int(question)].pop(0)
                wastecard = selectedCard
                displayGrid(grid)
                print("the wastecard is:", wastecard)
                
            else:
                print("the wastecard is still:", wastecard)
                print("try a different card")
        
        # if the user has won:
            # display "Congrats you have won the game!" on the terminal
        if checkWin(grid) == True:
            print("Congrats you have won the game!")
        
            

            
            
        

            
        
        
        
        
       


        
            


            

        

        

        
    
    

            
            



if __name__ == "__main__":
    main()









