#coding: utf-8
from kivyview.const import Const
from kivy.config import Config
Config.set('graphics', 'width', str(Const.WIDTH))
Config.set('graphics', 'height', str(Const.HEIGHT))

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, NoTransition
from GameScreen import GameScreen
from GameData import GameData

class DicePokerApp(App):
    u'''アプリのメインクラス。'''
    def build(self):
        data = GameData()
        sm = ScreenManager(transition = NoTransition())
        sm.add_widget(GameScreen(data, name = 'Game'))
        sm.current = 'Game'
        return sm

# 起動
if __name__ == '__main__':
    DicePokerApp().run()
