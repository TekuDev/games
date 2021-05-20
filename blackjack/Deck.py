import random

class Deck():
    """docstring for Deck"""
    def __init__(self,nDecks):
        self.nDecks = nDecks
        self.cards = [4*nDecks] * 13
        print(self.cards)

    def getCard(self):
        done = False
        if not any(self.cards):
            self.shuffle()
        while not done:
            card = random.randint(0,12)
            if self.cards[card] != 0:
                self.cards[card] -= 1
                done = True
        card += 1
        if card == 11:
            card = "J"
        elif card == 12:
            card = "Q"
        elif card == 13:
            card = "K"
        elif card == 1:
            card = "As"
            
        return str(card)

    def shuffle(self):
        self.cards = [4*self.nDecks] * 13
        print("Shuffle!")

    def printCards(self):
    	for c in self.cards:
    		print(c, end=" ")
    	print()