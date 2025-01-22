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
    cursor.execute("CREATE TABLE IF NOT EXISTS Borrowed (title TEXT NOT NULL, author TEXT NOT NULL, genre TEXT NOT NULL, id TEXT NOT NULL PRIMARY KEY, user TEXT NOT NULL, due TEXT NOT NULL)")
    cursor.execute('SELECT title FROM inventory\nWHERE id = "' + id + '"')
    title = cursor.fetchall()
    title = ','.join(title[0])
    cursor.execute('SELECT author FROM inventory\nWHERE id = "' + id + '"')
    author = cursor.fetchall
    author = ','.join(str(author))
    cursor.execute('SELECT genre FROM inventory\nWHERE id = "' + id + '"')
    genre = cursor.fetchall
    genre = ','.join(str(genre))
    print(title)
    print(author)
    print(genre)
    cursor.execute('INSERT INTO borrowed VALUES ("' + title + '", "' + author + '", "' + genre + '", "' + id + '", "' + user + '", "' + date + '")')
    return("borrowing successful")
