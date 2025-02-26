import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
class application(App):
    def build(self):
        self.sm = ScreenManager()
        self.screen1 = Screen(name = 'screen_screen')
        layout = GridLayout(cols=1, spacing=10, size_hint_y =None)
        #layout1 = GridLayout(rows=1, spacing=10, size_hint_x =None)
        layout2 = GridLayout(cols=2, spacing=10, size_hint_y =None)
        s = Slider(min=-100, max=100, value=25, value_track=True, value_track_color=[0, 0.5, 1, 1])
        #layout1.bind(minimum_height = layout2.setter('height'))
        layout2.bind(minimum_height = layout2.setter('height'))
        layout.bind(minimum_height = layout.setter('height'))
        for i in range (100):
            layout2.add_widget(Button(text = str(i), size_hint_y=None, height = 100))
        #layout1.add_widget(s)
        #layout1.add_widget(Label(text = 'behold, scrolling'))
        root = ScrollView(size_hint=(1, None), size=(Window.width, Window.height), scroll_type = ['content'])
        #layout.add_widget(layout1)
        layout.add_widget(layout2)
        root.add_widget(layout)
        self.screen1.add_widget(root)
        self.sm.add_widget(self.screen1)
        return self.sm
if __name__ == '__main__':
   myApp = application()
   myApp.run()