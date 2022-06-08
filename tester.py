"""import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'One':1, 'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card():
    #creates individual cards
    def __init__(self,suits,ranks):
        self.suits = suits
        self.ranks = ranks
        self.values = values[ranks]

    def __str__(self):
        return self.ranks + ' of ' + self.suits

class Deck():
   
    def __init__(self):
         #creates empty list for cards to go into
        self.all_cards = []
        #fills list with created cards
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit,rank))
    #shuffles deck when called
    def shuffle(self):
        random.shuffle(self.all_cards)
    #deals one card from the deck
    def deal_one(self):
        return self.all_cards.pop()

class Player():
    #creates players    
    def __init__(self,name):
        self.name = name
        self.all_cards = []
        self.hand = 0     

    def remove_one(self):
        # Note we remove one card from the list of all_cards
        # We state 0 to remove from the "top" of the deck
        # We'll imagine index -1 as the bottom of the deck
        return self.all_cards.pop(0)
    
    def add_cards(self,new_cards):
        self.all_cards.append(new_cards)
        self.hand += new_cards.values

    def ace_as_one(self):
        self.hand -= 10

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards with value of {self.hand}'

new_deck = Deck()
human = Player('Jorge')
for x in range(52):
    human.add_cards(new_deck.deal_one())
    if human.all_cards[x].ranks == 'Ace':
        choose = input('Choose between One or Ace: ')
        if choose == 'One':
            human.ace_as_one()
            human.all_cards[x].ranks = choose
for y in range(52):
    if human.all_cards[y].ranks == 'Ace':
        print(human.all_cards[y])
print(human)
"""
i = 0
y = ['ace', 'squirrel', 5]
z = 22
if z > 21:
    for i in range(3):
        if y[i] == 'ace':
            z -= 10
            print(z)
            break
if z> 21:
    print(y)
