# coding: UTF-8
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.graphics import *
from const import Const

class GameScreen(Screen):
    u'''ゲーム画面クラス。ダイスを表示し、タップすると振る。'''
    def __init__(self, data, **kwargs):
        super(GameScreen, self).__init__(**kwargs)
        self.data = data
    
    def on_enter(self):
        u'''画面を開いたときの処理。ダイス用のラベルを追加する。'''
        y = Const.Y_BASE
        for die in self.data.cup:
            L = Label(text=str(die.pip), font_size=Const.FONT_SIZE, color='white', y=y)
            with L.canvas:
                Color(255, 0, 255)
                #Rectangle()
            self.add_widget(L)
            y -= Const.Y_SUBTRACT
    
    def on_touch_down(self, touch):
        u'''画面を開いたときの処理。ダイスを振り直す。'''
        return super().on_touch_down(touch)

    def on_leave(self):
        u'''画面を閉じたときの処理。ウィジェットを消す。'''
        self.clear_widgets()
