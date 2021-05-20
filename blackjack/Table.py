from enum import Enum
from Player import Player
from Deck import Deck

class State(Enum):
    SET_BET = 1
    DEAL_CARD = 2
    PLAYER_TURN = 3
    BANCA_TURN = 4
    RESOLVE_ROUND = 5
    FINISH = 6

class Table():
    """docstring for Table"""
    def __init__(self, nDecks, money, objective, nHands2shuffle):
        self.deck = Deck(nDecks)
        self.player = Player(money, objective)
        self.nHands2shuffle = nHands2shuffle
        self.bancaHand = 0
        self.playerCards = []
        self.bancaCards = []
        self.state = State.SET_BET
        self.handsPlayed = 0
        self.playerHasBlackJack = False
        
    def reset(self):
        self.playerHasBlackJack = False
        self.bancaHand = 0
        self.playerCards = []
        self.bancaCards = []
        self.player.reset()

    def card(self):
        # Deal the new card and recalculate the hand value
        newcard = self.deck.getCard()
        if newcard not in ("10","J","Q","K","As"):
            self.player.currentHand += int(newcard)
        elif newcard in ("10","J","Q","K"):
            self.player.currentHand += 10
        elif (self.player.currentHand+11) > 21:
            self.player.currentHand += 1
            newcard = "1"
        else:
            self.player.currentHand += 11
        
        self.playerCards.append(newcard)
        
        if self.player.currentHand > 21 and "As" in self.playerCards:
            index = self.playerCards.index("As")
            self.playerCards.remove("As")
            self.player.currentHand -= 10
            self.playerCards.insert(index, "1")
        
        # Evaluate if the player hand is > 21
        if self.player.currentHand > 21:
            self.state = State.RESOLVE_ROUND
        elif self.player.currentHand == 21:
            self.state = State.BANCA_TURN
        
        
    def double(self):
        #Restrictions
        #Double option is only available if the player has 2 cards
        if len(self.playerCards) > 2:
            print("Double option is only available if the player has 2 cards")
            return
        
        #Double option is only available if the player has 9, 10 or 11
        if self.player.currentHand not in (9,10,11):
            print("Double option is only available if you have 9, 10 or 11")
            return
        
        #Double option
        #Double the bet if you can
        if (self.player.money - self.player.currentBet) < 0:
       	    print("You don't have enough money to double")
            return
        #else:
        self.player.money -= self.player.currentBet
        self.player.currentBet += self.player.currentBet
        
        # Deal the new card and recalculate the hand value
        newcard = self.deck.getCard()
        if newcard not in ("10","J","Q","K","As"):
            self.player.currentHand += int(newcard)
        elif newcard in ("10","J","Q","K"):
            self.player.currentHand += 10
        elif (self.player.currentHand+11) > 21:
            self.player.currentHand += 1
            newcard = "1"
        else:
            self.player.currentHand += 11
        
        self.playerCards.append(newcard)
        
        if self.player.currentHand > 21 and "As" in self.playerCards:
            index = self.playerCards.index("As")
            self.playerCards.remove("As")
            self.player.currentHand -= 10
            self.playerCards.insert(index, "1")
        
        # Evaluate if the player hand is > 21
        if self.player.currentHand > 21:
            self.state = State.RESOLVE_ROUND
        else:
            self.state = State.BANCA_TURN

    def fold(self):
        self.state = State.BANCA_TURN

    def playerTurn(self):
        option = int(input("1-Card 2-Double 3-Fold 4-Exit "))
        if option == 1:
            self.card()
        elif option == 2:
            self.double()
        elif option == 3:
            self.fold()
        elif option == 4:
            self.reset()
            self.state = State.FINISH
        else:
            print("Wrong option, you have to write 1, 2, 3 or 4 ")

    def bancaTurn(self):
        if self.bancaHand < 17:
            newcard = self.deck.getCard()
            if newcard not in ("10","J","Q","K","As"):
                self.bancaHand += int(newcard)
            elif newcard in ("10","J","Q","K"):
                self.bancaHand += 10
            elif (self.bancaHand+11) > 21:
                self.bancaHand += 1
                newcard = "1"
            else:
                self.bancaHand += 11
            
            self.bancaCards.append(newcard)
        
        if self.bancaHand > 21 and "As" in self.bancaCards:
            index = self.bancaCards.index("As")
            self.bancaCards.remove("As")
            self.bancaHand -= 10
            self.bancaCards.insert(index, "1")
        
        if self.bancaHand >= 17:
            self.state = State.RESOLVE_ROUND
            

    def resolveState(self):
        if self.state == State.SET_BET:
            if self.player.money == 0:
                print("GAME OVER")
                self.reset()
                self.state = State.FINISH
                return
                
            if self.handsPlayed == self.nHands2shuffle:
            	self.deck.shuffle()

            self.playerCards = []
            self.bancaCards = []
            self.bancaHand = 0
            self.player.currentHand = 0

            bet = int(input("Introduce the bet for the next round (-1 to exit) "))
            if bet == -1:
                self.state = State.FINISH
            elif bet <= self.player.money:
                self.player.setBet(bet)
                self.player.money -= bet
                self.state = State.DEAL_CARD
            else:
                print("You cannot bet more than money you have")

        elif self.state == State.DEAL_CARD:
        	
            self.handsPlayed += 1

            card = self.deck.getCard()
            if card not in ("10","J","Q","K","As"):
                self.player.currentHand += int(card)
            elif card in ("10","J","Q","K"):
                self.player.currentHand += 10
            elif (self.player.currentHand+11) > 21:
                self.player.currentHand += 1
            else:
                self.player.currentHand += 11
                
            self.playerCards.append(card)

            card = self.deck.getCard()
            if card not in ("10","J","Q","K","As"):
                self.bancaHand += int(card)
            elif card in ("10","J","Q","K"):
                self.bancaHand += 10
            elif (self.bancaHand+11) > 21:
                self.bancaHand += 1
            else:
                self.bancaHand += 11
                
            self.bancaCards.append(card)

            card = self.deck.getCard()
            if card not in ("10","J","Q","K","As"):
                self.player.currentHand += int(card)
            elif card in ("10","J","Q","K"):
                self.player.currentHand += 10
            elif (self.player.currentHand+11) > 21:
                self.player.currentHand += 1
            else:
                self.player.currentHand += 11
                
            self.playerCards.append(card)
            
            if self.player.currentHand == 21:
                self.playerHasBlackJack = True
                self.state = State.BANCA_TURN
            else:
                self.state = State.PLAYER_TURN

        elif self.state == State.PLAYER_TURN:
            self.playerTurn()

        elif self.state == State.BANCA_TURN:
            self.bancaTurn()

        elif self.state == State.RESOLVE_ROUND:
            if self.player.currentHand > 21:
                print("The hand is over")
            elif self.playerHasBlackJack and self.bancaHand != 21:
                print("Black Jack!!!!!")
                self.player.money += self.player.currentBet*2+self.player.currentBet/2
                
            elif self.bancaHand > 21 or self.player.currentHand > self.bancaHand:
                print("Player win the round")
                self.player.money += self.player.currentBet*2
                
            elif self.player.currentHand == self.bancaHand:
                print("Push")
                self.player.money += self.player.currentBet
                
            else:
                print("Player lose this round")
            
            self.reset()
            self.state = State.SET_BET

        else:
            print("Wrong state "+self.state)

    def printTable(self):
        print("--------------------------------------")
        #banca
        print(str(self.bancaHand) + " = ", end="")
        for c in self.bancaCards:
            print(c + " ", end="")
        print(": banca")

        #player
        print(str(self.player.currentHand) + " = ", end="")
        for c in self.playerCards:
            print(c + " ", end="")
        print(": player")
        print("Player money: "+str(self.player.money))
        print("Player bet: "+str(self.player.currentBet))

        #options
        print("--------------------------------------")