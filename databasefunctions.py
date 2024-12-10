import sqlite3
def addbook(title, author, genre, id, copies):
    connection = sqlite3.connect("Testinventory.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS inventory (title TEXT NOT NULL, author TEXT NOT NULL, genre TEXT NOT NULL, id TEXT NOT NULL PRIMARY KEY, copies TEXT NOT NULL)")
    cursor.execute('INSERT INTO inventory VALUES ("' + title + '", "' + author + '", "' + genre + '", "' + id + '", "' + copies + '")')
    connection.commit()
    return('mission complete')