from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
class MyGame(App):
    def build(self):
        return GridLayout()
class MyGame(App):
    def build(self):
        grid = GridLayout()
        for i in range(4):
            for j in range(4):
                label = Label(text="2" if random.random() > 0.1 else "4")
                grid.add_widget(label)
        return grid

MyGame()
