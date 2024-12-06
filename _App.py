#coding: utf-8
from dice import DiceFactory
from const import Const

cup = []
for i in range(Const.NUM_OF_DICE):
    cup.append(DiceFactory().create(Const.SIX_SIDED))
    cup[-1].roll()

for die in cup:
    print(die.pip)