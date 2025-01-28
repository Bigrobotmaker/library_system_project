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
    connection = sqlite3.connect("Tempusers.db")
    cursor = connection.cursor()
    cursor.execute('SELECT password FROM users\nWHERE username = "' + username + '"')
    password = cursor.fetchall()
    password = ','.join(password[0])
    return password
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
    connection = sqlite3.connect("Tempusers.db")
    cursor = connection.cursor()
    if p == c:
        try:
            cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT NOT NULL PRIMARY KEY, password TEXT NOT NULL)")
            cursor.execute('INSERT INTO users VALUES ("' + u + '", "' + p + '")')
            connection.commit()
        except:
            return('username in use')
        return('registration successful')
    else:
        return('passwords do not match')
def borrow(id, date, user):
    connection = sqlite3.connect("Testinventory.db")
    cursor = connection.cursor()
    idcursor = connection.cursor
    cursor.execute("CREATE TABLE IF NOT EXISTS Borrowed (title TEXT NOT NULL, author TEXT NOT NULL, genre TEXT NOT NULL, id TEXT NOT NULL, user TEXT NOT NULL, due TEXT NOT NULL, borrowid TEXT NOT NULL PRIMARY KEY)")
    try:
        cursor.execute('SELECT title, author, genre, copies FROM inventory\nWHERE id = "' + id + '"')
        info = cursor.fetchall()
        title = (info[0])[0]
        author = (info[0])[1]
        genre = (info[0])[2]
        idcursor.execute('SELECT * FROM Borrowed')
        borrowed = idcursor.fetchall
        borrowid = 0
        for i in borrowed:
            borrowid = borrowid + 1
        if int((info[0])[3]) > 0:
            cursor.execute('INSERT INTO borrowed VALUES ("' + title + '", "' + author + '", "' + genre + '", "' + id + '", "' + user + '", "' + date + '", "' + str(borrowid) + '")')
            cursor.execute('UPDATE inventory SET copies ="' + str(int((info[0])[3]) - 1) + '" WHERE id = "' + id + '"')
            connection.commit()
            connection.close()
            return("borrowing successful")
        else:
            return("no copies available, try again later")
    except:
        connection.close()
        return('ID not recognised')
