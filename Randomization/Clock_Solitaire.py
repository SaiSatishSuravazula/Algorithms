"""
Clock Solitaire:
Given a deck of 52 cards, shuffle it 7 times. This ensures that the deck follows the Uniform Distribution. Next,divide the deck into 13 groups of 4 cards each. Name the groups ‘A,2,3,....J,Q,K ’(Note that a group NEED NOT have ONLY the cards that match the group label. For example, group 2 need not have only 2s and so on).

The game progresses as follows:
Pick up a card from group ‘K’. Remove the card from ‘K’.
Go to the group matching the label of the card picked up from group ‘K’ and pick up a card from this group.
Continue the process.
The game stops if a particular group is empty and the player accesses it.
A player is declared winner if he accesses all the 52 cards before any of the groups is empty.

"""


import random

def Clock_Solitaire():
    deck = [i for i in range(52)]
    piles = [[] for i in range(13)]

    for i in range(7):
        random.shuffle(deck) #shuffled the deck seven times

    # Giving four cards to each of the piles
    k = 0
    for i in range(13):
        for j in range(4):
            piles[i].append(deck[k])
            j+=1
            k+=1

    #Now every pile had 4 cards

    #pick the initial card
    card_picked = piles[0].pop()

    #Play the game
    #Now traverse through the piles based on the card picked
    strike_count = 1
    while(piles[card_picked%13]):
        card_picked = piles[card_picked%13].pop()
        strike_count+=1

    if(strike_count == 52):
        return 1
    else: 
        return 0

n = int(input("Enter the number of times program to be executed: "))
wins = 0
for i in range(n):    
    wins += Clock_Solitaire()

print("Winning probability: ", wins/n)

