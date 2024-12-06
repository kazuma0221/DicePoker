# coding: UTF-8
from dice import DiceFactory
from const import Const

class GameData():
    u'''ゲームデータの生成と受け渡し用のクラス。'''
    def __init__(self):
        u'''コンストラクタ。ダイスを作って適当に振る。'''
        self.cup = []
        for i in range(Const.NUM_OF_DICE):
            self.cup.append(DiceFactory().create(Const.SIX_SIDED))
            self.cup[-1].roll()
        # デバッグ用
        for die in self.cup:
            print(die.pip)