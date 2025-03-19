import sqlite3
import datetime
from datetime import date
def addbook(title, author, genre, id, copies):
    connection = sqlite3.connect("Testinventory.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS inventory (title TEXT NOT NULL, author TEXT NOT NULL, genre TEXT NOT NULL, id TEXT NOT NULL PRIMARY KEY, copies TEXT NOT NULL)")
    try:
        data = (title,author,genre,id,copies)
        cursor.execute('INSERT INTO inventory VALUES (?, ?, ?, ?, ?)', data)
        connection.commit()
    except:
        return('ID in use')
    return('book successfully added')
def passcheck(username):
    connection = sqlite3.connect("Testinventory.db")
    cursor = connection.cursor()
    uname = (username,)
    try:
        cursor.execute('SELECT password FROM users\nWHERE username = ?', uname)
        password = cursor.fetchall()
        password = ','.join(password[0])
        cursor.execute('UPDATE users SET loggedin = "True" WHERE username = ?', uname)
        connection.commit()
        return password
    except:
        connection.commit()
        return("password not recognised")
def removebook(id):
    connection = sqlite3.connect("Testinventory.db")
    cursor = connection.cursor()
    try:
        di = (id,)
        cursor.execute('DELETE FROM Borrowed WHERE id = ?',di)
        cursor.execute('DELETE FROM inventory WHERE id = ?',di)
        connection.commit()
    except:
        return('ID is not in use')
    return('book successfully deleted')
def register(u,p,c):
    connection = sqlite3.connect("Testinventory.db")
    cursor = connection.cursor()
    if p == c:
        try:
            userdata = (u,p)
            cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT NOT NULL PRIMARY KEY, password TEXT NOT NULL, loggedin TEXT NOT NULL)")
            cursor.execute('INSERT INTO users VALUES (?, ?, "' + "False" + '")',userdata)
            connection.commit()
        except:
            return('username in use')
        return('registration successful')
    else:
        return('passwords do not match')
def borrow(id, date):
    connection = sqlite3.connect("Testinventory.db")
    cursor = connection.cursor()
    idcursor = connection.cursor()
    usercursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS Borrowed (title TEXT NOT NULL,\n author TEXT NOT NULL,\n genre TEXT NOT NULL,\n id TEXT NOT NULL REFERENCES inventory(id) ON DELETE CASCADE,\n user TEXT NOT NULL,\n dateout DATE NOT NULL,\n due DATE NOT NULL,\n borrowid TEXT NOT NULL PRIMARY KEY)")
    try:
        di = (id,)
        cursor.execute('SELECT title, author, genre, copies FROM inventory\nWHERE id = ?',di)
        usercursor.execute('SELECT username FROM users WHERE loggedin = "' + "True" + '"')
        username = usercursor.fetchall()
        username = (username[0])[0]
        info = cursor.fetchall()
        title = (info[0])[0]
        author = (info[0])[1]
        genre = (info[0])[2]
        idcursor.execute('SELECT borrowid FROM Borrowed')
        borrowed = idcursor.fetchall()
        borrowid = 0
        for i in borrowed:
            try:
                if int((borrowed[0])[i]) >= borrowid:
                    borrowid = int((borrowed[0])[i]) + 1
            except:
                borrowid = 1
        dateout = date.split(',')
        dateout2 =(dateout[0] + '-' + dateout[1] + '-' + dateout[2])
        today = datetime.date.today()
        if int((info[0])[3]) > 0:
            cursor.execute('INSERT INTO borrowed VALUES ("' + title + '", "' + author + '", "' + genre + '", "' + id + '", "' + username + '", "' + str(today) + '","' + dateout2 + '", "' + str(borrowid) + '")')
            cursor.execute('UPDATE inventory SET copies ="' + str(int((info[0])[3]) - 1) + '" WHERE id = "' + id + '"')
            connection.commit()
            connection.close()
            return("borrowing successful")
        else:
            return("no copies available, try again later")
    except:
        return('ID not recognised')
def logoutset():
    connection = sqlite3.connect("Testinventory.db")
    cursorget = connection.cursor()
    cursorupdate = connection.cursor()
    cursorget.execute('SELECT username FROM users\nWHERE loggedin = "' + "True" + '"')
    username = cursorget.fetchall()
    username = (username[0])[0]
    cursorupdate.execute('UPDATE users SET loggedin = "False" WHERE username = "' + username + '"')
def returnbook(title):
    try:
        data = (title,)
        connection = sqlite3.connect("Testinventory.db")
        cursor = connection.cursor()
        usercursor = connection.cursor()
        copycursor = connection.cursor()
        usercursor.execute('SELECT username FROM users WHERE loggedin = "' + "True" + '"')
        name = usercursor.fetchall()
        uname = (name[0])[0]
        cursor.execute('SELECT borrowid FROM borrowed WHERE title = ? AND user = "' + uname + '"', data)
        id = cursor.fetchall()
        num = len(id)
        if num == 1:
            cursor.execute('DELETE FROM borrowed WHERE title = ? AND user = "' + uname + '"', data)
        else:
            cursor.execute('DELETE FROM borrowed WHERE title = ? AND user = "' + uname + '" AND borrowid = "' + (id[0])[0] + '"', data)
        copycursor.execute('SELECT id, copies FROM inventory\nWHERE title = "' + title + '"')
        ids = copycursor.fetchall()
        bookid = (ids[0])[0]
        cursor.execute('UPDATE inventory SET copies ="' + str(int((ids[0])[1]) + 1) + '" WHERE id = "' + bookid + '"')
        connection.commit()
        return('Return successful')
    except:
        return('You have not borrowed a book with that title')
def changecopies(ID, Copies):
    connection = sqlite3.connect("Testinventory.db")
    cursor = connection.cursor()
    try:
        data = (ID,Copies)
        cursor.execute('UPDATE inventory SET copies = ? WHERE id = ?', data)
    except:
        return('Error, ID is not in inventory')
    return('inventory succesfully updated')
def viewborrowed():
    connection = sqlite3.connect("Testinventory.db")
    cursor = connection.cursor()
    try:
        cursor.execute('SELECT title, id, user, dateout FROM borrowed')
        info = cursor.fetchall()
        print(info)
        return(info)
    except:
        connection.close()
        return('there are no currently borrowed books')
def getresults(title, genre, author):
    try:
        data = (title, author, genre)
        connection = sqlite3.connect("Testinventory.db")
        cursor = connection.cursor()
        if title == '':
            title = '%'
        if genre == '':
            genre = '%'
        if author == '':
            author = '%'
        cursor.execute('SELECT title, author, genre, id, copies FROM inventory\nWHERE title LIKE ? AND author LIKE ? AND genre LIKE ?', data)
        results = cursor.fetchall()
        if results == []:
            return('no books match the criteria')
        else:
            return(results)
    except:
        connection.close()
        return('no books match the criteria')