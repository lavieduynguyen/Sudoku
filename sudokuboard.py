from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget


class SudokuBoard(GridLayout):
    def __init__(self, puzzle=None, **kwargs):
        super().__init__(**kwargs)
        self.cols = 11
        self.rows = 11
        for i in range(9):
            count = 0
            for j in range(9):
                if count == 3:
                    self.add_widget(VerticalSeparator())
                    count = 0
                self.add_widget(Label(text=('0')))
                count += 1


class SudokuSquare(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class VerticalSeparator(Widget):
    pass


class HorizontalSeparator(Widget):
    pass

