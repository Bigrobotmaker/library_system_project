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