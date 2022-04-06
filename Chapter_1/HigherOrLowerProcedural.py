import random

# card constants

SUIT_TUPLE = ('Spades', 'Hearts', 'Clubs', 'Diamonds')
RANK_TUPLE = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen','King')


NUMBER_OF_CARDS = 8

# Pass in a deck and this function returns a random card from the deck
def getCard(deckListIn):
    thisCard = deckListIn.pop()
    return thisCard

# Pass in a deck and this function returns a shuffled copy of the deck
def shuffle(deckListIn):
    deckListOut = deckListIn.copy()
    random.shuffle(deckListOut)
    return deckListOut


# main code
print('Welcome to Higher or Lower.')
print('You have to choose whether the next card to be shown will be higher or lower than the current card.')
print('Getting it right adds 20 points; get it wrong and you lose 15 points.')
print('You have 50 points to start.')
print()

starting_deck_List = []
for suit in SUIT_TUPLE:
    for thisValue, rank in enumerate(RANK_TUPLE):
        cardDict = {'rank': rank, 'suit': suit, 'value': thisValue + 1}
        starting_deck_List.append(cardDict)

score = 50

while True: # play multiple games
    print()
    game_Deck_List = shuffle(starting_deck_List)
    current_card_Dict = getCard(game_Deck_List)
    current_card_rank = current_card_Dict['rank']
    current_card_value = current_card_Dict['value']
    current_card_suit = current_card_Dict['suit']
    print('Starting card is:', current_card_rank + ' of ' + current_card_suit)
    print()


    for cardNumber in range(0, NUMBER_OF_CARDS):  # play one game of this many cards
        answer = input(('Will the next card be higher or lower than the ' + 
                               current_card_rank + ' of ' + 
                               current_card_suit + '?  (enter h or l): '))
        answer = answer.casefold() # force lower case
        next_card_dict = getCard(game_Deck_List)
        next_card_rank = next_card_dict['rank']
        next_card_suit = next_card_dict['suit']
        next_card_value = next_card_dict['value']
        print('Next card is:', next_card_rank + ' of ' + next_card_suit)
        
        # Checks if the user presses the 'h' for higher if so the score will add up with 20
        # other than that it will retract 15
        if answer == 'h':
            if next_card_value > current_card_value:
                print('You got it right, it was higher')
                score = score + 20
            else:
                print('Sorry, it was not higher')
                score = score - 15          
        # Otherwise it checks if the user presses the 'l' for lower if so the score will add up with 20
        # otherwise it will retract -15 of the score.
        elif answer == 'l':
            if next_card_value < current_card_value:
                score = score + 20
                print('You got it right, it was lower')

            else:
                score = score - 15
                print('Sorry, it was not lower')

        print('Your score is:', score)
        print()
        current_card_rank = next_card_rank
        current_card_value = next_card_value  # don't need current suit

    # Checks if the user want to quit the program
    go_Again = input('To play again, press ENTER, or "q" to quit: ')
    if go_Again == 'q':
        break

print('OK bye')