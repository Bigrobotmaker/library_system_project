import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.slider import Slider
class application(App):
    def build(self):
        layout = BoxLayout(orientation = 'vertical')
        s = Slider(min=-100, max=100, value=25)
        for i in range (0,10):
            layout.add_widget(Button(text = 'button')(pos_hint=('right':i)))
        layout.add_widget(s)
        return layout
if __name__ == '__main__':
   myApp = application()
   myApp.run()