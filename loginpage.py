import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
class application(App):
   def build(self):
      self.sm = ScreenManager()
      self.layout = GridLayout(cols=1)
      self.layout1 = GridLayout(cols=1)
      self.layout2 = GridLayout(cols=2)
      self.registerlayout = GridLayout(cols=1)
      self.registerlayout1 = GridLayout(cols=1)
      self.registerlayout2 = GridLayout(cols=2)
      self.screen1 = Screen(name = 'login_screen')
      self.screen2 = Screen(name = 'register_screen')
      self.layout1.add_widget(Label(text='Welcome to the library system, please enter your username and password to log in\nIf you do not have an account please click register to make one', font_size='20sp'))
      self.tinput = TextInput(multiline=False, hint_text = 'Username')
      self.pinput = TextInput(multiline=False, hint_text = 'Password')
      self.layout1.add_widget(self.tinput)
      self.layout1.add_widget(self.pinput)
      self.layout2.add_widget(Button(text ='log in'))
      self.layout2.add_widget(Button(text = 'register', on_press = self.registerswap))
      self.layout.add_widget(self.layout1)
      self.layout.add_widget(self.layout2)
      self.screen1.add_widget(self.layout)
      self.sm.add_widget(self.screen1)
      self.registerlayout1.add_widget(Label(text='Please enter the username and password you would like to set'))
      self.tinput2 = TextInput(multiline=False, hint_text = 'Username')
      self.pinput2 = TextInput(multiline=False, hint_text = 'Password')
      self.registerlayout1.add_widget(self.tinput2)
      self.registerlayout1.add_widget(self.pinput2)
      self.registerlayout2.add_widget(Button(text ='Register'))
      self.registerlayout2.add_widget(Button(text = 'Back to login', on_press = self.registerswap))
      self.registerlayout.add_widget(self.registerlayout1)
      self.registerlayout.add_widget(self.registerlayout2)
      self.screen2.add_widget(self.registerlayout)
      self.sm.add_widget(self.screen2)
      return self.sm
   def registerswap(self, instance):
      if self.sm.current == 'login_screen':
         self.sm.current = 'register_screen'
      elif self.sm.current == 'register_screen':
         self.sm.current = 'login_screen'

if __name__ == '__main__':
   myApp = application()
   myApp.run()