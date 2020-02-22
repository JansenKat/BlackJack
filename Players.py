class Player():
    def __init__(self,deck):
        self.hand = []
        for i in range(2):
            self.hand.append(deck.draw())
        self.gen_score()
        return
    
    def show_hand(self):
        out = '| '
        for card in self.hand:
            out += card.show() + ' | '
        print(f"Your hand is {out}")
        #print(f"Total value is {self.score}")
        return
    
    def gen_score(self):
        self.score = 0
        # self.show_hand()
        sorted_hand = sorted(self.hand, key=lambda x: x.worth[0], reverse=True)
        for card in sorted_hand:
            if len(card.worth)>1:
                if (21 - self.score) < card.worth[0]:
                    card.worth.pop(0)
            self.score += card.worth[0]
        return self.check_score()

    def add_card(self,deck):
        self.hand.append(deck.draw())
        self.gen_score()
        return 

    def hit(self,deck):
        while (self.gen_score()):
            self.show_hand()
            hit = input("Do you want to hit? y/n ")
            if hit != 'y':
                break
            self.add_card(deck)
        return self.score <= 21
    
    def check_score(self):
        check = True
        if self.score == 21:
            print("Win!")
            check =  False
        elif self.score > 21:
            print("Busted!")
            check =  False
        return check


class Dealer(Player):

    def __init__(self,deck):
        self.hand = []
        for i in range(2):
            card = deck.draw()
            if i == 0:
                card.visible = False
            self.hand.append(card)
        self.gen_score()
        self.show_hand()
        return
    
    def show_hand(self):
        out = '| '
        for card in self.hand:
            if card.visible:
                out += card.show()
            else:
                out += 'Hidden'
            out += ' | '
        print(f"Dealer has {out}")
        return
    
    def hit(self,deck):
        while self.score <= 16:
            print("Dealer hits: " + self.hand[-1].show())
            self.add_card(deck)
        return self.score <= 21