import random

#standard variables
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}
game_on = True

class Card():

    def __init__(self,suits,ranks):
        self.suits = suits
        self.ranks = ranks
        self.values = values[ranks]

    def __str__(self):
        return f'The card is the {self.ranks} of {self.suits}'

class Deck():

    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit,rank))
        
    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()
    
class Player():

    def __init__(self,name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        self.all_cards.pop(0)

    def add_cards(self,new_cards):
        self.all_cards.append(new_cards)
    
    def hand_value(self):
        #calculates value of player's hand
        for cards in self.all_cards:
            self.hand += cards.value
            return self.hand

    def __str__(self):
        #returns value of player's cards on the table
        return f'{self.name} has {self.hand}'

#add account class

dealer = Player('CPU')
player = Player(input('Please Enter your name: '))
new_deck = Deck()
new_deck.shuffle

while True:
    choice = input('Do you wish to play a round of blackjack? ')
    if choice  == 'yes':
        deal = True
        while game_on:
            if deal == True:
                for x in range(0,2):
                    dealer.add_cards(new_deck.deal_one)
                    print(dealer.all_cards[x])
                    player.add_cards(new_deck.deal_one)
                    print(player.all_cards[0])
                deal = False
            print(player)
            hit_choice = input('Would you like to hit or stay?: ')
            if hit_choice == 'hit':
                player.add_cards(new_deck.deal_one)
                print(player.all_cards[0])
                print(player)
            else:
                if dealer.hand_value <= player.hand_value:
                    dealer.add_cards(new_deck.deal_one)
                    print(dealer.all_cards[0])
                else:
                    pass
            
            if player.hand_value <= 21:
                if player.hand_value > dealer.hand_value:
                    print('Player wins!')
                if player.hand_value <= dealer.hand_value:
                    print('Dealer wins!')
            elif player.hand_value > 21 or dealer.hand_value > 21:
                winner = min(player.hand_value, dealer.hand_value)
                print(f'{winner} has won due to bust')
    else:
        print('Lameo bitch')
        break

    

