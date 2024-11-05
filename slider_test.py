import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.slider import Slider
class application(App):
    def build(self):
        layout = GridLayout(cols = 1)
        s = Slider(min=-100, max=100, value=25)
        for i in range (0,10):
            layout.add_widget(Button(text = 'button'))
        layout.add_widget(s)
    
       