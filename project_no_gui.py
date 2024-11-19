import sqlite3
def addbook(title, author, genre, id, copies):
    cursor.execute('INSERT INTO availablebooks VALUES ("' + title + '", "' + author + '", "' + genre + '", "' + id + '", "' + copies + '")')
connection = sqlite3.connect("Currentinventory.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS availablebooks (title TEXT, author TEXT, genre TEXT, id TEXT, copies TEXT)")
cursor.execute("CREATE TABLE IF NOT EXISTS borrowedbooks (title TEXT, author TEXT, genre TEXT, id TEXT, copies TEXT, loanedto TEXT, due TEXT)")
addbook('one piece', 'oda', 'action manga', '0', '1')
cursor.execute('SELECT * FROM availablebooks\nWHERE title = "' + 'one piece' + '"')
rows = cursor.fetchall()
for row in rows:
    print(row)