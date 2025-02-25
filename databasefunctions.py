import sqlite3
def addbook(title, author, genre, id, copies):
    connection = sqlite3.connect("Testinventory.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS inventory (title TEXT NOT NULL, author TEXT NOT NULL, genre TEXT NOT NULL, id TEXT NOT NULL PRIMARY KEY, copies TEXT NOT NULL)")
    try:
        cursor.execute('INSERT INTO inventory VALUES ("' + title + '", "' + author + '", "' + genre + '", "' + id + '", "' + copies + '")')
        connection.commit()
        connection.close()
    except:
        connection.close()
        return('ID in use')
    return('book successfully added')
def passcheck(username):
    connection = sqlite3.connect("Testinventory.db")
    cursor = connection.cursor()
    try:
        cursor.execute('SELECT password FROM users\nWHERE username = "' + username + '"')
        password = cursor.fetchall()
        password = ','.join(password[0])
        cursor.execute('UPDATE users SET loggedin = "True" WHERE username = "' + username + '"')
        connection.commit()
        connection.close()
        return password
    except:
        connection.commit()
        connection.close()
        return("password not recognised")
def removebook(id):
    connection = sqlite3.connect("Testinventory.db")
    cursor = connection.cursor()
    try:
        cursor.execute('DELETE FROM inventory WHERE id = "' + id + '"')
        connection.commit()
        connection.close()
    except:
        connection.close()
        return('ID is not in use')
    return('book successfully deleted')
def register(u,p,c):
    connection = sqlite3.connect("Testinventory.db")
    cursor = connection.cursor()
    if p == c:
        try:
            cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT NOT NULL PRIMARY KEY, password TEXT NOT NULL, loggedin TEXT NOT NULL)")
            cursor.execute('INSERT INTO users VALUES ("' + u + '", "' + p + '", "' + "False" + '")')
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
    cursor.execute("CREATE TABLE IF NOT EXISTS Borrowed (title TEXT NOT NULL, author TEXT NOT NULL, genre TEXT NOT NULL, id TEXT NOT NULL, user TEXT NOT NULL, due TEXT NOT NULL, borrowid TEXT NOT NULL PRIMARY KEY)")
    try:
        cursor.execute('SELECT title, author, genre, copies FROM inventory\nWHERE id = "' + id + '"')
        usercursor.execute('SELECT username FROM users WHERE loggedin = "' + "True" + '"')
        username = usercursor.fetchall()
        username = (username[0])[0]
        info = cursor.fetchall()
        title = (info[0])[0]
        author = (info[0])[1]
        genre = (info[0])[2]
        idcursor.execute('SELECT id FROM Borrowed')
        borrowed = idcursor.fetchall()
        borrowid = 0
        for i in borrowed:
            try:
                if int((borrowed[0])[i]) >= borrowid:
                    borrowid = int((borrowed[0])[i]) + 1
            except:
                borrowid = 1
        if int((info[0])[3]) > 0:
            cursor.execute('INSERT INTO borrowed VALUES ("' + title + '", "' + author + '", "' + genre + '", "' + id + '", "' + username + '", "' + date + '", "' + str(borrowid) + '")')
            cursor.execute('UPDATE inventory SET copies ="' + str(int((info[0])[3]) - 1) + '" WHERE id = "' + id + '"')
            connection.commit()
            connection.close()
            return("borrowing successful")
        else:
            return("no copies available, try again later")
    except:
        connection.close()
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
        connection = sqlite3.connect("Testinventory.db")
        cursor = connection.cursor()
        usercursor = connection.cursor()
        copycursor = connection.cursor()
        usercursor.execute('SELECT username FROM users WHERE loggedin = "' + "True" + '"')
        name = usercursor.fetchall()
        uname = (name[0])[0]
        cursor.execute('SELECT borrowid FROM borrowed WHERE title = "' + title + '" AND user = "' + uname + '"')
        id = cursor.fetchall()
        num = len(id)
        if num == 1:
            cursor.execute('DELETE FROM borrowed WHERE title = "' + title + '" AND user = "' + uname + '"')
        else:
            cursor.execute('DELETE FROM borrowed WHERE title = "' + title + '" AND user = "' + uname + '" AND borrowid = "' + (id[0])[0] + '"')
        copycursor.execute('SELECT id, copies FROM inventory\nWHERE title = "' + title + '"')
        ids = copycursor.fetchall()
        bookid = (ids[0])[0]
        cursor.execute('UPDATE inventory SET copies ="' + str(int((ids[0])[1]) - 1) + '" WHERE id = "' + bookid + '"')
        connection.commit()
        connection.close()
        return('Return successful')
    except:
        connection.close()
        return('You have not borrowed a book with that title')
def changecopies(ID, Copies):
    connection = sqlite3.connect("Testinventory.db")
    cursor = connection.cursor()
    try:
        cursor.execute('UPDATE inventory SET copies = ' + Copies + ' WHERE id = "' + ID + '"')
    except:
        return('Error, ID is not in inventory')
    return('inventory succesfully updated')