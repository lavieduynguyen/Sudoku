import kivy
kivy.require('1.10.0')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.dropdown import DropDown
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen, ScreenManager

from sudokuboard import SudokuBoard


class GameScreen(Screen):
    pass


class SolverScreen(Screen):
    pass


class HelpScreen(Screen):
    pass


class CreditsScreen(Screen):
    pass


class MenuScreen(Screen):
    pass


class Numpad(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 3
        self.rows = 3
        for i in range(self.cols * self.rows):
            button = Button(text=str(i + 1))
            button.font_size = button.height * 0.25
            self.add_widget(button)


class ColorFilter(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.spacing = 8
        self.padding = 10
        self.cols = 8
        self.rows = 5
        for i in range(20):
            self.add_widget(CheckBox(active=True, size_hint=(None, None), height=20, width=20))
            self.add_widget(Button(size_hint=(0.5, None),size_hint_max_x=60, height=20))


class SudokuApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(GameScreen(name='game'))
        sm.add_widget(HelpScreen(name='help'))
        sm.add_widget(CreditsScreen(name='credits'))
        sm.current = 'menu'
        return sm


if __name__ == '__main__':
    SudokuApp().run()