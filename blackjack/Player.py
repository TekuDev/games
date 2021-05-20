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