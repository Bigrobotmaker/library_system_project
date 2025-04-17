import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
import sqlite3
import databasefunctions
import datetime
from datetime import date
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
import hashlib
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
      self.mainpageS = GridLayout(cols=3)
      self.removepage = GridLayout(cols=2)
      self.borrowpage = GridLayout(cols=2)
      self.returnpage = GridLayout(cols=2)
      self.copypage = GridLayout(cols=2)
      self.parameters = GridLayout(cols=3)
      self.screen1 = Screen(name = 'login_screen')
      self.screen2 = Screen(name = 'register_screen')
      self.screen3 = Screen(name = 'admin_screen')
      self.screenB = Screen(name = 'bookadd_screen')
      self.screenR = Screen(name = 'bookremove_screen')
      self.screenS = Screen(name = 'student_screen')
      self.screenBR = Screen(name = 'borrow_screen')
      self.REscreen = Screen(name = 'return_screen')
      self.COscreen = Screen(name = 'copies_screen')
      self.searchscreen = Screen(name = 'parameters_screen')
#the above code initialises all the screens that the code needs
      self.layout1.add_widget(Label(text='Welcome to the OLA library system, please enter your username and password to log in\nIf you do not have an account please click register to make one', font_size='20sp'))
      self.tinput = TextInput(multiline=False, hint_text = 'Username')
      self.pinput = TextInput(multiline=False, hint_text = 'Password', password = True)
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
#code for the login screen, creates all the labels and buttons, adds them and adds the overall screen to the screen manager
      self.registerlayout1.add_widget(Label(text='Please enter the username and password you would like to set'))
      self.tinput2 = TextInput(multiline=False, hint_text = 'Username')
      self.pinput2 = TextInput(multiline=False, hint_text = 'Password', password = True)
      self.pcinput = TextInput(multiline=False, hint_text = 'confirm your password', password = True)
      self.verifyR = Label(text = '')
      self.registerlayout1.add_widget(self.verifyR)
      self.registerlayout1.add_widget(self.tinput2)
      self.registerlayout1.add_widget(self.pinput2)
      self.registerlayout1.add_widget(self.pcinput)
      self.registerlayout2.add_widget(Button(text ='Register', on_press = self.register))
      self.registerlayout2.add_widget(Button(text = 'Back to login', on_press = self.registerswap))
      self.registerlayout.add_widget(self.registerlayout1)
      self.registerlayout.add_widget(self.registerlayout2)
      self.screen2.add_widget(self.registerlayout)
      self.sm.add_widget(self.screen2)
#creates and constructs the registration screen 
      self.mainpage.add_widget(Label(text = ''))
      self.mainpage.add_widget(Label(text = 'Welcome', font_size='40sp'))
      self.mainpage.add_widget(Label(text = ''))
      self.mainpage.add_widget(Button(text = 'Add a book', on_press = self.bookaddswap))
      self.mainpage.add_widget(Button(text = 'Remove a book', on_press = self.bookremoveswap))
      self.mainpage.add_widget(Button(text = 'Log out', on_press = self.logout))
      self.mainpage.add_widget(Button(text = 'Change the number of copies a book has', on_press = self.copyswap))
      self.mainpage.add_widget(Button(text = 'See the status of borrowed books', on_press = self.listswap))
      self.screen3.add_widget(self.mainpage)
      self.sm.add_widget(self.screen3)
      #above code creates and constructs the admin's main screen
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
      self.bookadd.add_widget(Button(text = 'add to database', on_press = self.addbook(self.titleinput.text, self.author.text, self.genre.text, self.id.text, self.copies.text)))
      self.bookadd.add_widget(Button(text = 'return to admin', on_press = self.bookaddswap))
      self.screenB.add_widget(self.bookadd)
      self.sm.add_widget(self.screenB)
#creates the add book screen and adds it to screen manager
      self.mainpageS.add_widget(Label(text = ''))
      self.mainpageS.add_widget(Label(text = 'Welcome'))
      self.mainpageS.add_widget(Button(text = 'View a list of books', on_press = self.searchbook))
      self.mainpageS.add_widget(Button(text = 'Log out', on_press = self.logout))
      self.mainpageS.add_widget(Button(text = 'Return a book', on_press = self.returnswap))
      self.mainpageS.add_widget(Button(text = 'Borrow a book', on_press = self.borrowswap))
      self.screenS.add_widget(self.mainpageS)
      self.sm.add_widget(self.screenS)
#creates and adds the student home page
      self.removelabel = Label(text = 'Please remove a book here')
      self.removepage.add_widget(self.removelabel)
      self.Rid = TextInput(multiline=False, hint_text = 'The ID of the book you would like to remove')
      self.removepage.add_widget(self.Rid)
      self.removepage.add_widget(Button(text = 'remove book', on_press = lambda x:self.removebook(self.Rid.text)))
      self.removepage.add_widget(Button(text = 'return to admin', on_press = self.bookremoveswap))
      self.screenR.add_widget(self.removepage)
      self.sm.add_widget(self.screenR)
#creates and the screen for removing a book and adds it to the screen manager
      self.borrowconfirm = Label(text = '')
      self.BID = TextInput(multiline=False, hint_text = 'The ID of the book you would like to borrow')
      self.Returndate = TextInput(multiline=False, hint_text = 'when would you like to return the book?\n(write as year,month,day, for example, 2025,01,01)')
      self.borrowpage.add_widget(Label(text = 'please enter the ID of the book you would like to take out'))
      self.borrowpage.add_widget(self.borrowconfirm)
      self.borrowpage.add_widget(self.BID)
      self.borrowpage.add_widget(self.Returndate)
      self.borrowpage.add_widget(Button(text = 'back to main page', on_press = self.borrowswap))
      self.borrowpage.add_widget(Button(text = 'request to borrow the book', on_press = lambda x:self.borrow(self.BID.text, self.Returndate.text)))
      self.screenBR.add_widget(self.borrowpage)
      self.sm.add_widget(self.screenBR)
#the above code creates the page for borrowing a book and adds it to the screen manager
      self.returnconfirm = Label(text = '')
      self.REtitleinput = TextInput(multiline=False, hint_text = 'The title of the book you would like to return')
      self.returnpage.add_widget(Label(text = 'please enter the title of the book you are returning'))
      self.returnpage.add_widget(self.returnconfirm)
      self.returnpage.add_widget(self.REtitleinput)
      self.returnpage.add_widget(Label(text = ''))
      self.returnpage.add_widget(Button(text = 'back to main page', on_press = self.returnswap))
      self.returnpage.add_widget(Button(text = 'return book', on_press = lambda x:self.returnbook(self.REtitleinput.text)))
      self.REscreen.add_widget(self.returnpage)
      self.sm.add_widget(self.REscreen)
#the above code creates the page for returning a book and adds it to the screen manager
      self.idinput = TextInput(multiline = False, hint_text = 'the id of the book you would like to alter')
      self.copyinput =TextInput(multiline = False, hint_text = 'the number of copies of the book that the library has')
      self.copyconfirm = Label(text = '')
      self.copypage.add_widget(Label(text = 'please enter the ID of the book and the number of copies you want to change it to\nthis automaticaly updates when books are borrowed and returned'))
      self.copypage.add_widget(self.copyconfirm)
      self.copypage.add_widget(self.idinput)
      self.copypage.add_widget(self.copyinput)
      self.copypage.add_widget(Button(text = 'back to main page', on_press = self.copyswap))
      self.copypage.add_widget(Button(text = 'change number of copies', on_press = lambda x:self.changecopies(self.idinput.text, self.copyinput.text)))
      self.COscreen.add_widget(self.copypage)
      self.sm.add_widget(self.COscreen)
#the above code creates the page for changing the number of copies of a book and adds it to the screen manager
      self.searchtitle = TextInput(multiline = False, hint_text = "the title you would like to search for\n(leave blank for no specific title)")
      self.searchgenre = TextInput(multiline = False, hint_text = "the genre you would like to search for\n(leave blank for no specific genre)")
      self.searchauthor = TextInput(multiline = False, hint_text = "the author you would like to search for\n(leave blank for no specific author)")
      self.parameters.add_widget(Label(text = 'please enter the search parameters'))
      self.parameters.add_widget(Label(text = ''))
      self.parameters.add_widget(Label(text = ''))
      self.parameters.add_widget(self.searchtitle)
      self.parameters.add_widget(self.searchgenre)
      self.parameters.add_widget(self.searchauthor)
      self.parameters.add_widget(Button(text = 'return to main page', on_press = self.searchbook))
      self.parameters.add_widget(Label(text = ''))
      self.parameters.add_widget(Button(text = 'search', on_press = self.getresults))
      self.searchscreen.add_widget(self.parameters)
      self.sm.add_widget(self.searchscreen)
      return self.sm
#the above code creates the page for borrowing a book and adds it to the screen manager
   def registerswap(self, instance):
      if self.sm.current == 'login_screen':
         self.sm.current = 'register_screen'
         self.pinput.text = ''
      elif self.sm.current == 'register_screen':
         self.tinput2.text = ''
         self.pinput2.text = ''
         self.pcinput.text = ''
         self.sm.current = 'login_screen'
#function that swaps between register and login, as well as clearing the password fields and the login username field
   def copyswap(self, instance):
      if self.sm.current == 'admin_screen':
         self.sm.current = 'copies_screen'
      elif self.sm.current == 'copies_screen':
         self.sm.current = 'admin_screen'
#swaps between admin and copy
   def logincheck(self, instance):
      if self.tinput.text == 'Admin' and self.pinput.text == 'Password':
         self.sm.current = 'admin_screen'
      elif self.passcheck(self.tinput.text) == 'login success':
         self.sm.current = 'student_screen'
      else:
         self.verifyL.text = "Login failed - username or password is incorrect"
#if the username and password are the pre-set admin ones, swaps to admin home, otherwise calls the passchceck function with the contents of the username input, and if the result is a success it goes to the student home screen
   def register(self, instance):
      u = self.tinput2.text
      p = self.pinput2.text
      c = self.pcinput.text
      self.verifyR.text = databasefunctions.register(u,p,c)
   #calls the register function from databasefunctions with the inputs as whatever is stored in the textinput on the register page
   def bookaddswap(self, instance):
      if self.sm.current == 'admin_screen':
         self.sm.current = 'bookadd_screen'
      elif self.sm.current == 'bookadd_screen':
         self.returnlabel.text = 'please add a new book here'
         self.sm.current = 'admin_screen'
#swaps between add a book and admin screen
   def searchbook(self, instance):
      if self.sm.current == 'student_screen':
         self.sm.current = 'parameters_screen'
      elif self.sm.current == 'parameters_screen':
         self.sm.current = 'student_screen'
#swaps between student main screen and parameters
   def getresults(self, instance):
      results = databasefunctions.getresults(self.searchtitle.text, self.searchgenre.text, self.searchauthor.text)
      self.resultscreen = Screen(name = 'search_results_screen')
      self.resultview = GridLayout(cols=2,size_hint_y =None, spacing = 10)
      self.resultview.bind(minimum_height = self.resultview.setter('height'))
      self.searchscroll = ScrollView(size_hint=(1, None), size=(Window.width, Window.height), scroll_type = ['content'])
      self.resultview.add_widget(Label(text = 'results:', size_hint_y =None , height = 300))
      self.resultview.add_widget(Button(text = 'return to search page', on_press = self.viewresults, size_hint_y =None , height = 300)) 
      if results == 'no books match the criteria':
         self.resultview.add_widget(Label(text = 'no books match the criteria', height = 100))
      else:
         for item in range(0,len(results)):
            item = int(item)
            if ((results[item-1])[4]) != '1':
               self.resultview.add_widget(Label(text = ((results[item-1])[0]) + '\n By ' + ((results[item-1])[1]) + ' genre: ' + ((results[item-1])[2]) + '\n Book ID: ' + ((results[item-1])[3]) + '\n this book has ' + ((results[item-1])[4]) + ' copies left ', size_hint_y=None, height = 100))
            else:
               self.resultview.add_widget(Label(text = ((results[item-1])[0]) + '\n By ' + ((results[item-1])[1]) + ' genre: ' + ((results[item-1])[2]) + '\n Book ID: ' + ((results[item-1])[3]) + '\n this book has ' + ((results[item-1])[4]) + ' copy left', size_hint_y=None, height = 100))
      self.searchscroll.add_widget(self.resultview)
      self.resultscreen.add_widget(self.searchscroll)
      self.sm.add_widget(self.resultscreen)
      self.viewresults(instance)
#calls the getresults function from databasefunctions, then creates the scroll view and results screen, this is done seperately to properly show the results as they change while the program is running, the function also creates a label if there are no books that match the search criteria, the function it calls deletes the previous screen so it is re-created every time
   def viewresults(self, instance):
         if self.sm.current == 'parameters_screen':
            self.sm.current = 'search_results_screen'
         elif self.sm.current == 'search_results_screen':
            self.sm.current = 'parameters_screen'
            self.sm.remove_widget(self.resultscreen)
#switches between search results and parameters
   def bookremoveswap(self,instance):
      if self.sm.current == 'admin_screen':
         self.sm.current = 'bookremove_screen'
      elif self.sm.current == 'bookremove_screen':
         self.removelabel.text = 'please remove a book here'
         self.sm.current = 'admin_screen'
#swaps between the remove book screen and the admin screen
   def borrowswap(self,instance):
      if self.sm.current == 'student_screen':
         self.sm.current = 'borrow_screen'
      elif self.sm.current == 'borrow_screen':
         self.sm.current = 'student_screen'
#swaps between borrow screen and student home screen         
   def returnswap(self, instance):
      if self.sm.current == 'student_screen':
         self.sm.current = 'return_screen'
      elif self.sm.current == 'return_screen':
         self.sm.current = 'student_screen'
#swaps between return screen and student home screen  
   def listswap(self,instance):
      if self.sm.current == 'borrow_view_screen':
         self.sm.current = 'admin_screen'
         self.sm.remove_widget(self.scrollscreenB)
      elif self.sm.current == 'admin_screen':
         self.borrowedview = GridLayout(cols=2)
         self.viewborrowed()
         self.sm.current = 'borrow_view_screen'
#swaps between the view borrowed screen and admin home screen, also removes the screen when swapping away and calls a function to recreate it when swapping to it  
   def addbook(self, newtitle,newauthor,newgenre,newid,newcopies):
      self.returnlabel.text = databasefunctions.addbook(newtitle,newauthor,newgenre,newid,newcopies)
#calls function to add a book
   def removebook(self, RID):
      self.removelabel.text = databasefunctions.removebook(RID)
#calls function to remove a book
   def passcheck(self, username):
      if databasefunctions.passcheck(username) == hashlib.sha256((self.pinput.text).encode('utf-8')).hexdigest():
         return 'login success'
      else:
         return 'login failed'
#calls a function to check the password and returns success if it was successful and fail if the password did not match
   def logout(self, instance):
      self.sm.current = 'login_screen'
      self.pinput.text = ''
      self.pinput.text = ''
      databasefunctions.logoutset()
#logs someone out, sets their logged in status in the database with a function
   def borrow(self, ID, Date):
      self.borrowconfirm.text = databasefunctions.borrow(ID, Date)
#calls function to borrow a book
   def returnbook(self,title):
      self.returnconfirm.text = databasefunctions.returnbook(title)
#calls function to return a book
   def changecopies(self, ID, Copies):
      self.copyconfirm.text = databasefunctions.changecopies(ID, Copies)
#calls function to change the number of copies of a book
   def viewborrowed(self):
      info = databasefunctions.viewborrowed()
      self.scrollscreenB = Screen(name = 'borrow_view_screen')
      self.borrowedview = GridLayout(cols=2,size_hint_y =None, spacing = 10)
      self.borrowedview.bind(minimum_height = self.borrowedview.setter('height'))
      self.scrolling = ScrollView(size_hint=(1, None), size=(Window.width, Window.height), scroll_type = ['content'])
      self.borrowedview.add_widget(Label(text = 'these are the books which are currently borrowed', size_hint_y =None , height = 300))
      self.borrowedview.add_widget(Button(text = 'return to admin page', on_press = self.listswap, size_hint_y =None , height = 300)) 
      if info == 'there are no currently borrowed books':
         self.borrowedview.add_widget(Label(text = info, height = 100))
      else:
         for item in range(0,len(info)):
            item = int(item)
            self.borrowedview.add_widget(Label(text = ((info[item-1])[0]) + '\n book ID: ' + ((info[item-1])[1]) + '\n borrowed by ' + ((info[item-1])[2]) + '\n on ' + ((info[item-1])[3]) +'\n due ' + ((info[item-1])[4]), size_hint_y=None, height = 100))
      self.scrolling.add_widget(self.borrowedview)
      self.scrollscreenB.add_widget(self.scrolling)
      self.sm.add_widget(self.scrollscreenB)
#similarly to an above function, creates the scrolling page that lets you view the borrowed books, the page is re-created every time bo properly fill it with the labels after the number of borrowed books changes
if __name__ == '__main__':
   myApp = application()
   myApp.run()