import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
class application(App):
    def build(self):
        layout = GridLayout(rows=1, spacing=10)
        layout1 = GridLayout(rows=1, spacing=10)
        layout2 = GridLayout(rows=1, spacing=10)
        s = Slider(min=-100, max=100, value=25, value_track=True, value_track_color=[0, 0.5, 1, 1])
        for i in range (0,10):
            layout2.add_widget(Button(text = 'button'))
        layout1.add_widget(s)
        root = ScrollView(size_hint=(0.2, None), bar_pos_x = 'bottom', scroll_type = ['content'], size=(Window.width, Window.height), bar_margin = 1, do_scroll_y = False, bar_color = [0, 1, 0, 1])
        layout.add_widget(layout2)
        #layout.add_widget(layout1)
        root.add_widget(layout)
        return root
if __name__ == '__main__':
   myApp = application()
   myApp.run()