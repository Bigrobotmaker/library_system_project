import sqlite3
def addbook(title, author, genre, id, copies):
    inuse = False
    cursor.execute('SELECT id FROM availablebooks')
    taken = cursor.fetchall()
    for used in taken:
        if ','.join(used) == id:
           inuse = True
    if inuse == True:
        print("invalid id (already in use)")
    else:
        cursor.execute('INSERT INTO availablebooks VALUES ("' + title + '", "' + author + '", "' + genre + '", "' + id + '", "' + copies + '")')
        connection.commit()
def removebook(id):
    cursor.execute('DELETE FROM availablebooks\nWHERE id = "' + id + '"')
    connection.commit()
def addcopy(id):
    cursor.execute('SELECT * FROM availablebooks)\nWHERE id = "' + id + '"')
    book = cursor.fetchall()
connection = sqlite3.connect("Currentinventorytest.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS availablebooks (title TEXT, author TEXT, genre TEXT, id TEXT NOT NULL PRIMARY KEY, copies TEXT)")
cursor.execute("CREATE TABLE IF NOT EXISTS borrowedbooks (title TEXT, author TEXT, genre TEXT, id TEXT, copies TEXT, loanedto TEXT, due TEXT)")
addbook('one piece vol 2', 'oda', 'action manga', '1', '1')
cursor.execute('SELECT * FROM availablebooks')
rows = cursor.fetchall()
for row in rows:
    print(row)
connection.close()