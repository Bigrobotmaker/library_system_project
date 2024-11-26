import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
class application(App):
   def build(self):
      layout = GridLayout(cols=1)
      layout.add_widget(Label(text='please enter your username and password'))
      self.tinput = TextInput(multiline=False, text = 'Username')
      self.pinput = TextInput(multiline=False, text = 'Password')
      layout.add_widget(self.tinput)
      layout.add_widget(self.pinput)