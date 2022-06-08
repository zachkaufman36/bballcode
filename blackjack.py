import random

#standard variables
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'One':1, 'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
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
        self.hand = 0

    def remove_one(self):
        self.all_cards.pop(0)

    def add_cards(self,new_cards):
        self.all_cards.append(new_cards)
        self.hand += new_cards.values
    
    def hand_reset(self):
        self.hand = 0

    def __str__(self):
        #returns value of player's cards on the table
        return f'{self.name} has {self.hand}'

class Account():

    def __init__(self,balance = 500):
        self.balance = balance

    def deposit(self,deposit):
        self.balance += deposit
        return self.balance
    
    def withdraw(self,withdraw):
        if withdraw > self.balance:
            return f'Your balance is {self.balance}, pick a number below that'
        else:
            self.balance -= withdraw
            return withdraw
    
    def __str__(self):
        return f'Your balance is {self.balance}'


dealer = Player('CPU')
player = Player(input('Please Enter your name: '))
new_deck = Deck()
new_deck.shuffle()
bet = Account()

while True:
    choice = input('Do you wish to play a round of blackjack? ')
    if choice  == 'yes':
        game_on = True
        deal = True
        while game_on:
            wdw = int(input('Place buy in: '))
            money = bet.withdraw(wdw)
            print(bet.balance)
            if deal == True:
                for rmvl in range(len(player.all_cards)):
                    player.remove_one()
                player.hand_reset()
                print(player)
                for rmvl in range(len(dealer.all_cards)):
                    dealer.remove_one()
                dealer.hand_reset()
                print(dealer)
                x = 0
                for x in range(0,2):
                    dealer.add_cards(new_deck.deal_one())
                    player.add_cards(new_deck.deal_one())
                    if player.all_cards[x].ranks == 'Ace':
                        choose = input('Choose between One or Ace: ')
                        player.all_cards[x].ranks = choose
                    else:
                        pass
                    print(f'The player has {player.all_cards[x]}')
                print(f'The dealer has {dealer.all_cards[0]}')
                deal = False
            print(player)
            hit_choice = input('Would you like to hit or stay?: ')
            while hit_choice == 'hit':
                wdw2 = int(input('Place bet to proceed: '))
                money += bet.withdraw(wdw2)
                x += 1
                player.add_cards(new_deck.deal_one())
                if player.all_cards[x].ranks == 'Ace':
                    choose = input('Choose between One or Ace: ')
                    player.all_cards[x].ranks = choose
                else:
                    pass
                print(player.all_cards[x])
                print(player)
                if player.hand > 21:
                    print(f'{dealer.name} has won due to bust')
                    money = 0
                    print(bet.balance)
                    game_on = False
                    break
                hit_choice = input('Would you like to hit or stay?: ')
            else:
                y = 0
                while dealer.hand <= player.hand:
                    y += 1
                    dealer.add_cards(new_deck.deal_one())
                    print(f'The dealer draws {dealer.all_cards[y]}')
                    if dealer.hand > 21:
                        bet.deposit((money*2))
                        print(f'{player.name} has won due to bust')
                        print(bet.balance)
                        print(dealer)
                        game_on = False
                        break
                else:
                    pass
            
            if player.hand <= 21 and dealer.hand <= 21:
                if player.hand > dealer.hand:
                    bet.deposit((money*2))
                    print('Player wins!')
                    print(bet.balance)
                    break
                if player.hand <= dealer.hand:
                    print('Dealer wins!')
                    money = 0
                    print(dealer)
                    print(bet.balance)
                    break           
    else:
        print('Lameo bitch')
        break

    

