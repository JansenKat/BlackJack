from Deck import Deck
from Players import Player, Dealer
from Hand import Hand

def start(yn):
    if yn == 'y':
        decks = int(input("How many decks do you want to play with? "))
        if decks>0:
            main(decks)
        else:
            print('Invalid deck value')
    else:
        "Very Well. Have a good day."
        return

def main(decks):
    d = Deck(decks)
    p = Player(d)
    if not p.check_score():
        return
    h = Dealer(d)
    if not h.check_score():
        return
    p.hit(d)
    h.hit(d)
    if p.score > h.score:
        print("Player Wins!")
    else:
        print("Dealer Wins")
    return


if __name__ == "__main__":
    main(1)
#     start_input = input("Do you want to play BlackJack? y/n ")
#     start(start_input)