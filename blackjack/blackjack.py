#!/usr/bin/python3

import random


#Clases
class Player():
	"""docstring for Player"""
	def __init__(self, money = 0, objective = 0):
		self.money = money
		self.objective = objective
		self.currentHand = 0
		self.currentBet = 0

class Deck():
	"""docstring for Deck"""
	def __init__(self,nDecks):
		self.nDecks = nDecks
		self.cards = [4*nDecks] * 13

	def getCard(self):
		pass

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

	def card(self):
		pass

	def double(self):
		pass

	def fold(self):
		pass

	def bancaTurn(self):
		pass

	def printTable(self):
		print("--------------------------------------")
		#banca
		print(str(self.bancaHand) + " ", end="")
		for c in self.bancaCards:
			print(c + " ", end="")
		print("as banca")

		#player
		print(str(self.player.currentHand) + " ", end="")
		for c in self.playerCards:
			print(c + " ", end="")
		print("as player")
		print("Player money: "+str(self.player.money))
		print("Player bet: "+str(self.player.currentBet))

		#options
		print("1-Card 2-Double 3-Fold")
		print("--------------------------------------")


		


#Main:

print("Reading configuration")
#Read configuration
#number of decks
#initial player money
#money objective to end the game
#number of hands without shuffle
config_ndecks = int(input())
print("nDecks: "+str(config_ndecks))
config_initialmoney = int(input())
print("Initial money: "+str(config_initialmoney))
config_objectivemoney = int(input())
print("Objective money: "+str(config_objectivemoney))
config_nhands2shuffle = int(input())
print("nHands 2 shuffle: "+str(config_nhands2shuffle))

table = Table(config_ndecks,config_initialmoney,config_objectivemoney,config_nhands2shuffle)

table.printTable()

option = input("Select 1,2,3 in player mode or enter in banca mode. 4 to exit")
if option != '':
	option = int(option)
while(option != 4):
	if option == 1:
		table.card()
	elif option == 2:
		table.double()
	elif option == 3:
		table.fold()
	else:
		table.bancaTurn()

	option = input("Select 1,2,3 in player mode or enter in banca mode. 4 to exit")
	if option != '':
		option = int(option)