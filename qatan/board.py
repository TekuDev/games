from hexagon import Hexagon, type

class Board():
    #Class of the Qatan board.
    def __init__(self):
        self.numbers = [2,3,3,4,4,5,5,6,6,8,8,9,9,10,10,11,11,12]
        self.hexagons = [Hexagon()] * 19
        self.thief = 0