import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
import sqlite3
import databasefunctions
class application(App):
   def build(self):
      self.sm = ScreenManager()
      self.layout = GridLayout(cols=1)
      self.layout1 = GridLayout(cols=1)
      self.layout2 = GridLayout(cols=2)
      self.registerlayout = GridLayout(cols=1)
      self.registerlayout1 = GridLayout(cols=1)
      self.registerlayout2 = GridLayout(cols=2)
      self.bookadd = GridLayout(cols=2)
      self.mainpage = GridLayout(cols=3)
      self.screen1 = Screen(name = 'login_screen')
      self.screen2 = Screen(name = 'register_screen')
      self.screen3 = Screen(name = 'admin_screen')
      self.screenB = Screen(name = 'bookadd_screen')
      self.layout1.add_widget(Label(text='Welcome to the library system, please enter your username and password to log in\nIf you do not have an account please click register to make one', font_size='20sp'))
      self.tinput = TextInput(multiline=False, hint_text = 'Username')
      self.pinput = TextInput(multiline=False, hint_text = 'Password')
      self.verifyL = Label(text = '')
      self.layout1.add_widget(self.verifyL)
      self.layout1.add_widget(self.tinput)
      self.layout1.add_widget(self.pinput)
      self.layout2.add_widget(Button(text ='log in', on_press = self.logincheck))
      self.layout2.add_widget(Button(text = 'register', on_press = self.registerswap))
      self.layout.add_widget(self.layout1)
      self.layout.add_widget(self.layout2)
      self.screen1.add_widget(self.layout)
      self.sm.add_widget(self.screen1)
      self.registerlayout1.add_widget(Label(text='Please enter the username and password you would like to set'))
      self.tinput2 = TextInput(multiline=False, hint_text = 'Username')
      self.pinput2 = TextInput(multiline=False, hint_text = 'Password')
      self.verifyR = Label(text = '')
      self.registerlayout1.add_widget(self.verifyR)
      self.registerlayout1.add_widget(self.tinput2)
      self.registerlayout1.add_widget(self.pinput2)
      self.registerlayout2.add_widget(Button(text ='Register', on_press = self.register))
      self.registerlayout2.add_widget(Button(text = 'Back to login', on_press = self.registerswap))
      self.registerlayout.add_widget(self.registerlayout1)
      self.registerlayout.add_widget(self.registerlayout2)
      self.screen2.add_widget(self.registerlayout)
      self.sm.add_widget(self.screen2)
      self.mainpage.add_widget(Label(text = ''))
      self.mainpage.add_widget(Label(text = 'Welcome', font_size='40sp'))
      self.mainpage.add_widget(Label(text = ''))
      self.mainpage.add_widget(Button(text = 'Add a book', on_press = self.bookaddswap))
      self.mainpage.add_widget(Button(text = 'This page is under construction'))
      self.mainpage.add_widget(Label(text = ''))
      self.screen3.add_widget(self.mainpage)
      self.sm.add_widget(self.screen3)
      self.titleinput = TextInput(multiline=False, hint_text = 'Title')
      self.author = TextInput(multiline=False, hint_text = 'Author')
      self.genre = TextInput(multiline=False, hint_text = 'Genre')
      self.id = TextInput(multiline=False, hint_text = 'ID')
      self.copies = TextInput(multiline=False, hint_text = 'Number of copies')
      self.returnlabel = Label(text = 'please add a new book here', font_size='20sp')
      self.bookadd.add_widget(self.returnlabel)
      self.bookadd.add_widget(self.titleinput)
      self.bookadd.add_widget(self.author)
      self.bookadd.add_widget(self.genre)
      self.bookadd.add_widget(self.id)
      self.bookadd.add_widget(self.copies)
      self.bookadd.add_widget(Button(text = 'add to database', on_press = lambda x:self.addbook(self.titleinput.text, self.author.text, self.genre.text, self.id.text, self.copies.text)))
      self.bookadd.add_widget(Button(text = 'return to admin', on_press = self.bookaddswap))
      self.screenB.add_widget(self.bookadd)
      self.sm.add_widget(self.screenB)
      return self.sm
   def registerswap(self, instance):
      if self.sm.current == 'login_screen':
         self.sm.current = 'register_screen'
      elif self.sm.current == 'register_screen':
         self.sm.current = 'login_screen'
   def logincheck(self, instance):
      if self.tinput.text == 'Admin' and self.pinput.text == 'Password':
         self.sm.current = 'admin_screen'
      elif self.passcheck(self.tinput.text) == 'login success':
         self.sm.current = 'admin_screen'
      else:
         self.verifyL.text = "Login failed - username or password is incorrect"
   def register(self, instance):
      connection = sqlite3.connect("Tempusers.db")
      cursor = connection.cursor()
      cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT NOT NULL PRIMARY KEY, password TEXT NOT NULL)")
      u = self.tinput2.text
      p = self.pinput2.text
      cursor.execute('INSERT INTO users VALUES ("' + u + '", "' + p + '")')
      connection.commit()
   def bookaddswap(self, instance):
      if self.sm.current == 'admin_screen':
         self.sm.current = 'bookadd_screen'
      elif self.sm.current == 'bookadd_screen':
         self.returnlabel.text = 'please add a new book here'
         self.sm.current = 'admin_screen'
   def addbook(self, newtitle,newauthor,newgenre,newid,newcopies):
      self.returnlabel.text = databasefunctions.addbook(newtitle,newauthor,newgenre,newid,newcopies)
   def passcheck(self, username):
      if databasefunctions.passcheck(username) == self.pinput.text:
         return 'login success'
      else:
         return 'login failed'



if __name__ == '__main__':
   myApp = application()
   myApp.run()