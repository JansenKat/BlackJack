import random

suites = ['Spade','Heart','Club','Diamond']
values = {'Ace':[11,1],'Two':[2],'Three':[3],'Four':[4],'Five':[5],'Six':[6],'Seven':[7],'Eight':[8],'Nine':[9],'Ten':[10],'Jack':[10],'Queen':[10],'King':[10]}

class Card():
    def __init__(self,suit,value):
        self.suit = suit
        self.face = value
        self.worth = values[value]
        self.visible = True
        return
    
    def show(self):
        return f'{self.face} of {self.suit}s'

class Deck():
    def __init__(self,decks=1):
        self.deck = []
        for i in range(decks):
            for s in suites:
                for v in values.keys():
                    self.deck.append(Card(s,v))
        self.shuffle_deck()
        return

    def create_deck(self,decks):
        self.deck = []
        for i in range(decks):
            for s in suites:
                for v in values.keys():
                    self.deck.append(Card(s,v))
    
    def shuffle_deck(self):
        random.shuffle(self.deck)
        return
        
    def draw(self):
        return self.deck.pop(0)