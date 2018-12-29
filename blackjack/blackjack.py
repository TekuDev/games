#!/usr/bin/python3

import random 
from enum import Enum

class State(Enum):
    SET_BET = 1
    DEAL_CARD = 2
    PLAYER_TURN = 3
    BANCA_TURN = 4
    RESOLVE_ROUND = 5
    FINISH = 6


#Clases
class Player():
    """docstring for Player"""
    def __init__(self, money = 0, objective = 0):
        self.money = money
        self.objective = objective
        self.currentHand = 0
        self.currentBet = 0

    def setBet(self, bet):
        self.currentBet = bet
        
    def reset(self):
        self.currentHand = 0
        self.currentBet = 0

class Deck():
    """docstring for Deck"""
    def __init__(self,nDecks):
        self.nDecks = nDecks
        self.cards = [4*nDecks] * 13
        print(self.cards)

    def getCard(self):
        done = False
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

    def printCards(self):
    	for c in self.cards:
    		print(c, end=' ')
    	print()

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
        
    def reset(self):
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
        else:
            self.player.currentHand += 11
        
        self.playerCards.append(newcard)
        
        # Evaluate if the player hand is > 21
        if self.player.currentHand > 21:
            self.state = State.RESOLVE_ROUND
        
        
    def double(self):
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
        else:
            self.player.currentHand += 11
        
        self.playerCards.append(newcard)
        
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
            table.card()
        elif option == 2:
            table.double()
        elif option == 3:
            table.fold()
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
            else:
                self.bancaHand += 11
            
            self.bancaCards.append(newcard)
        
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
            
            self.state = State.PLAYER_TURN

        elif self.state == State.PLAYER_TURN:
            self.playerTurn()

        elif self.state == State.BANCA_TURN:
            self.bancaTurn()

        elif self.state == State.RESOLVE_ROUND:
            if self.player.currentHand > 21:
                print("The hand is over")
            elif self.player.currentHand == 21 and self.bancaHand != 21:
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


        


#Main:

print("Reading configuration")
#Read configuration
#number of decks
#initial player money
#money objective to end the game
#number of hands without shuffle
config_file = open("config.txt", 'r')
config_ndecks = int(config_file.readline())
print("nDecks: "+str(config_ndecks))
config_initialmoney = int(config_file.readline())
print("Initial money: "+str(config_initialmoney))
config_objectivemoney = int(config_file.readline())
print("Objective money: "+str(config_objectivemoney))
config_nhands2shuffle = int(config_file.readline())
print("nHands2shuffle: "+str(config_nhands2shuffle))
config_file.close()

table = Table(config_ndecks,config_initialmoney,config_objectivemoney,config_nhands2shuffle)

table.printTable()
while(table.state != State.FINISH):
    table.resolveState()
    table.printTable()
    if table.player.money >= table.player.objective:
        print("Winner winner chicken dinner")
        table.state = State.FINISH
