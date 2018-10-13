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

class Deck():
	"""docstring for Deck"""
	def __init__(self,nDecks):
		self.nDecks = nDecks
		self.cards = [4*nDecks] * 13
		print(self.cards)

	def getCard(self):
		card = random.randint(0,12)
		return str(card)

	def shuffle(self):
		self.cards = [4*self.nDecks] * 13

class Table():
	"""docstring for Table"""
	def __init__(self, nDecks, money, objective, nHands2shuffle):
		self.deck = Deck(nDecks)
		self.player = Player(money, objective)
		self.nHands2shuffle = nHands2shuffle
		self.bancaHand = 0
		self.isPlayerTurn = True
		self.playerCards = []
		self.bancaCards = []
		self.state = State.SET_BET

	def card(self):
		pass

	def double(self):
		pass

	def fold(self):
		self.state = State.BANCA_TURN

	def playerTurn(self):
		option = int(input("1-Card 2-Double 3-Fold "))
		if option == 1:
			table.card()
		elif option == 2:
			table.double()
		elif option == 3:
			table.fold()
		else:
			print("Wrong option, you have to write 1,2 or 3 ")

	def bancaTurn(self):
		pass

	def resolveState(self):
		if self.state == State.SET_BET:
			self.playerCards = []
			self.bancaCards = []
			bet = int(input("Introduce the bet for the next round "))
			self.player.setBet(bet)
			self.state = State.DEAL_CARD

		elif self.state == State.DEAL_CARD:
			card = self.deck.getCard()
			self.player.currentHand += int(card)
			self.playerCards.append(card)

			card = self.deck.getCard()
			self.bancaHand += int(card)
			self.bancaCards.append(card)

			card = self.deck.getCard()
			self.player.currentHand += int(card)
			self.playerCards.append(card)
			self.state = State.PLAYER_TURN

		elif self.state == State.PLAYER_TURN:
			self.playerTurn()

		elif self.state == State.BANCA_TURN:
			self.bancaTurn()
			self.state = State.RESOLVE_ROUND

		elif self.state == State.RESOLVE_ROUND:
			self.state = State.SET_BET

		else:
			print("Wrong state "+self.state)

	def printTable(self):
		print("--------------------------------------")
		#banca
		print(str(self.bancaHand) + " ", end="")
		for c in self.bancaCards:
			print(c + " ", end="")
		print(": banca")

		#player
		print(str(self.player.currentHand) + " ", end="")
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
