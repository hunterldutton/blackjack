##Hunter Dutton
##Final Project - CS021
##BLACKJACK

#import random module
import random

#Name all cards in the deck
CARD_LIST=['Ace of Spades','Ace of Clubs','Ace of Diamonds','Ace of Hearts',
            'Two of Spades','Two of Clubs','Two of Diamonds','Two of Hearts',
            'Three of Spades','Three of Clubs','Three of Diamonds','Three of Hearts',
            'Four of Spades','Four of Clubs','Four of Diamonds','Four of Hearts',
            'Five of Spades','Five of Clubs','Five of Diamonds','Five of Hearts',
            'Six of Spades','Six of Clubs','Six of Diamonds','Six of Hearts',
            'Seven of Spades','Seven of Clubs','Seven of Diamonds','Seven of Hearts',
            'Eight of Spades','Eight of Clubs','Eight of Diamonds','Eight of Hearts',
            'Nine of Spades','Nine of Clubs','Nine of Diamonds','Nine of Hearts',
            'Ten of Spades','Ten of Clubs','Ten of Diamonds','Ten of Hearts',
            'Jack of Spades','Jack of Clubs','Jack of Diamonds','Jack of Hearts',
            'Queen of Spades','Queen of Clubs','Queen of Diamonds', 'Queen of Hearts',
            'King of Spades','King of Clubs','King of Diamonds','King of Hearts']

#Assign values to each card
CARD_VALUES={'Ace of Spades':11,'Ace of Clubs':11,'Ace of Diamonds':11,'Ace of Hearts':11,
              'Two of Spades':2,'Two of Clubs':2,'Two of Diamonds':2,'Two of Hearts':2,
              'Three of Spades':3,'Three of Clubs':3,'Three of Diamonds':3,'Three of Hearts':3,
              'Four of Spades':4,'Four of Clubs':4,'Four of Diamonds':4,'Four of Hearts':4,
              'Five of Spades':5,'Five of Clubs':5,'Five of Diamonds':5,'Five of Hearts':5,
              'Six of Spades':6,'Six of Clubs':6,'Six of Diamonds':6,'Six of Hearts':6,
              'Seven of Spades':7,'Seven of Clubs':7,'Seven of Diamonds':7,'Seven of Hearts':7,
              'Eight of Spades':8,'Eight of Clubs':8,'Eight of Diamonds':8,'Eight of Hearts':8,
              'Nine of Spades':9,'Nine of Clubs':9,'Nine of Diamonds':9,'Nine of Hearts':9,
              'Ten of Spades':10,'Ten of Clubs':10,'Ten of Diamonds':10,'Ten of Hearts':10,
              'Jack of Spades':10,'Jack of Clubs':10,'Jack of Diamonds':10,'Jack of Hearts':10,
              'Queen of Spades':10,'Queen of Clubs':10,'Queen of Diamonds':10,'Queen of Hearts':10,
              'King of Spades':10,'King of Clubs':10,'King of Diamonds':10,'King of Hearts':10}

def main():
    answer='YES'
    chip_total=100
    print('Welcome to Blackjack!')
    print('You have',chip_total,'chips.')
    while answer=='YES' and chip_total>0:
        bet_valid='No'
        turn=''
        turn_input=''
        dealer_turn=''
        total=0
        valid='No'
#validate the bet and chip total
        while bet_valid=='No':
            try:
                bet=int(input('How many chips would you like to bet? '))
                if 0<bet<=chip_total:
                    bet_valid='Yes'
                else:
                    print('Invalid response. Please try again.')
            except:
                print('Invalid response. Please try again.')
                bet_valid='No'
        player_card1=drawcard()
        player_card2=drawcard()
        dealer_card1=drawcard()
        dealer_card2=drawcard()
        total=CARD_VALUES[player_card1]+CARD_VALUES[player_card2]
        print('You drew a ',player_card1,' and a ',player_card2,' for a total of ',total,'.',sep='')
#test if a blackjack has been drawn
        player_blackjack=blackjack_test(player_card1,player_card2)
        dealer_blackjack=blackjack_test(dealer_card1,dealer_card2)
        if player_blackjack=='Blackjack' and dealer_blackjack=='Blackjack':
            print('The dealer drew a',dealer_card1,'and a',dealer_card2)
            print('Tie.')
        elif player_blackjack=='Blackjack' and dealer_blackjack=='No blackjack':
            print('The dealer drew a',dealer_card1,'and a',dealer_card2)
            print('Player wins.')
            chip_total+=bet
        elif player_blackjack=='No blackjack' and dealer_blackjack=='Blackjack':
            print('The dealer drew a',dealer_card1,'and a',dealer_card2)
            print('Dealer wins.')
            chip_total-=bet
#if a blackjack is not drawn, continue playing the game
        else:
            total=CARD_VALUES[player_card1]+CARD_VALUES[player_card2]
            print('The dealer drew a',dealer_card1,'and a face-down card.')
            while turn!='DONE':
                if total<21:
                    turn_input=userinput()
                    if turn_input=='HIT':
                        newcard=drawcard()
                        total+=CARD_VALUES[newcard]
                        if total==21:
                            turn='DONE'
                        print('You drew a ',newcard,' for a total of ',total,'.',sep='')
                    elif turn_input=='STAND':
                        turn='DONE'
                else:
                    turn='DONE'
                    print('You have busted.')
            dealer_total=CARD_VALUES[dealer_card1]+CARD_VALUES[dealer_card2]
            print('The dealer drew a',dealer_card1,'and a',dealer_card2)
            while dealer_turn!='DONE':
                if dealer_total<17:
                    newcard=drawcard()
                    dealer_total+=CARD_VALUES[newcard]
                    print('The dealer drew a ',newcard,' for a total of ',dealer_total,'.',sep='')
                else:
                    dealer_turn='DONE'
#determine winner and add/remove bet
            if total<21 and dealer_total<21:
                if total>dealer_total:
                    print('Player wins.')
                    chip_total+=bet
                elif dealer_total>total:
                    print('Dealer wins.')
                    chip_total-=bet
                elif dealer_total==total:
                    print('The player and the dealer have tied. No one wins.')
            elif total>21 and dealer_total<21:
                print('Player busted. Dealer wins.')
                chip_total-=bet
            elif total<21 and dealer_total>21:
                print('Dealer busted. Player wins.')
                chip_total+=bet
            elif total>21 and dealer_total>21:
                print('Both the dealer and the player busted. No one wins.')
        print('You have',chip_total,'chips.')
        if chip_total!=0:
            while valid=='No':
                try:
                    choice=str(input('Would you like to play again? (Yes/No)\n '))
                    choice_uppercase=choice.upper()
                    valid='Yes'
                except TypeError:
                    print('Invalid response. Please try again.')
                    valid='No'
                if choice_uppercase=='YES' or choice_uppercase=='NO':
                    if choice_uppercase=='YES':
                        answer='YES'
                    elif choice_uppercase=='NO':
                        answer='NO'
                elif choice_uppercase!='YES' or choice_uppercase!='NO':
                    valid='No'
                    print('Invalid response. Please try again.')
        elif chip_total==0:
            print('Sorry, but you are out of chips.')
            
        
#Returns a random card string
def drawcard():
    cardrange=random.randint(0,51)
    card=CARD_LIST[cardrange]
    return card

#Asks user whether they want to hit or stand
def userinput():
    valid='No'
    while valid=='No':
        try:
            choice=str(input('Would you like to hit or stand? '))
            choice_uppercase=choice.upper()
            valid='Yes'
        except TypeError:
            print('Invalid response. Please try again.')
            valid='No'
        if choice_uppercase=='HIT' or choice_uppercase=='STAND':
            valid='Yes'
            return choice_uppercase
        elif choice_uppercase!='HIT' or choice_uppercase!='STAND':
            valid='No'
            print('Invalid response. Please try again.')
        
        
#Tests whether or not a blackjack has been drawn
def blackjack_test(card1,card2):
    if CARD_VALUES[card1]==11 and CARD_VALUES[card2]==10:
        return 'Blackjack'
    elif CARD_VALUES[card1]==10 and CARD_VALUES[card2]==11:
        return 'Blackjack'
    else:
        return 'No blackjack'


main()
            
    
              
