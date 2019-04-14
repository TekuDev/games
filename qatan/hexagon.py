from enum import Enum

class type(Enum):
    NULL = 0
    MOUNTAIN = 1
    WOOD = 2
    GROUND = 3
    ANIMAL = 4
    FIELD = 5
    DESERT = 6

class Hexagon():
    #Class of Hexagon of the board
    def __init__(self):
        self.type = type.NULL
        self.number = 0
        self.hasThief = False