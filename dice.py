#coding: utf-8
from numpy import random
from const import Const

class Dice():
    def __init__(self, sides):
        self.sides = sides
        self.pip = Const.DIE_MINIMUM
    
    def roll(self):
        self.pip = random.randint(Const.DIE_MINIMUM, self.sides + 1)
        return self.pip

class DiceFactory():
    def __init__(self):
        pass

    def create(self, sides):
        return Dice(sides)
