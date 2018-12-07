import sqlite3

def create():
    DB_FILE = "data/database.db"

    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    #Creating our tables in our database
    c.execute("CREATE TABLE IF NOT EXISTS users (name TEXT PRIMARY KEY, pass TEXT);")
    c.execute("CREATE TABLE IF NOT EXISTS book_faves (user TEXT, type TEXT, title TEXT, author TEXT, description TEXT, date TEXT, amazon TEXT);")
    c.execute("CREATE TABLE IF NOT EXISTS movie_faves (user TEXT, type TEXT, title TEXT, poster TEXT, description TEXT, date TEXT);")
    c.execute("CREATE TABLE IF NOT EXISTS game_faves (user TEXT, type TEXT, title TEXT);")
    c.execute("CREATE TABLE IF NOT EXISTS music_faves (user TEXT, type TEXT, title TEXT, artist TEXT, album TEXT, date TEXT, lyrics TEXT);")

    db.commit()
    db.close()

def viewFavorites(user):
    print("something")

def checkAccts():
    DB_FILE = "data/database.db"
    db = sqlite3.connect(DB_FILE)
    u = db.cursor()
    u.execute("CREATE TABLE IF NOT EXISTS users (name TEXT, pwd TEXT);")
    u.execute("SELECT name, pass FROM users;")
    x = u.fetchall()
    db.close()
    return x

def createAcct(uname,pwd):
    DB_FILE = "data/database.db"
    db = sqlite3.connect(DB_FILE)
    u = db.cursor()
    u.execute("INSERT INTO users values(?,?);", (uname, pwd))
    db.commit()
    db.close()

def getFaves(type,username):
    DB_FILE = "data/database.db"
    db = sqlite3.connect(DB_FILE)
    u = db.cursor()
    u.execute("CREATE TABLE IF NOT EXISTS "+type+"_faves (user TEXT, isbn TEXT);")
    u.execute("SELECT * from "+type+"_faves WHERE "+type+"_faves.user == (?);", (username,))
    x = u.fetchall()
    db.close()
    return x

def addBook(user,media_type,title,author,description,date,amazon):
    DB_FILE = "data/database.db"
    db = sqlite3.connect(DB_FILE)
    u = db.cursor()
    u.execute('INSERT INTO book_faves VALUES (?,?,?,?,?,?,?);', (user, media_type, title, author, description, date, amazon))
    db.commit()
    db.close()

def addMovie(user, media_type, title, poster, description, date):
    DB_FILE = "data/database.db"
    db = sqlite3.connect(DB_FILE)
    u = db.cursor()
    u.execute('INSERT INTO movie_faves VALUES (?,?,?,?,?,?);', (user, media_type, title, poster, description, date))
    db.commit()
    db.close()

def addMusic(user, media_type, title, artist, album, date, lyrics):
    DB_FILE = "data/database.db"
    db = sqlite3.connect(DB_FILE)
    u = db.cursor()
    u.execute('INSERT INTO music_faves VALUES (?,?,?,?,?,?,?);', (user, media_type, title, artist, album, date, lyrics))
    db.commit()
    db.close()

def addGame(user, media_type, title):
    DB_FILE = "data/database.db"
    db = sqlite3.connect(DB_FILE)
    u = db.cursor()
    u.execute('INSERT INTO game_faves VALUES (?,?,?);', (user, media_type, title))
    db.commit()
    db.close()

def getBook(user,title,author):
    DB_FILE = "data/database.db"
    db = sqlite3.connect(DB_FILE)
    u = db.cursor()
    u.execute('SELECT * FROM book_faves WHERE user = (?) AND title = (?) AND author = (?);', (user, title, author))
    x = u.fetchall()
    db.commit()
    db.close()
    return x

def getMovie(user, title, date):
    DB_FILE = "data/database.db"
    db = sqlite3.connect(DB_FILE)
    u = db.cursor()
    u.execute('SELECT * FROM movie_faves WHERE user = (?) AND title = (?) AND date = (?);', (user, title, date))
    x = u.fetchall()
    db.commit()
    db.close()
    return x

def getMusic(user,title, artist):
    DB_FILE = "data/database.db"
    db = sqlite3.connect(DB_FILE)
    u = db.cursor()
    u.execute('SELECT * FROM music_faves WHERE user = (?) AND title = (?) AND artist = (?);', (user, title, artist))
    x = u.fetchall()
    db.commit()
    db.close()
    return x

def getGame(user, title):
    DB_FILE = "data/database.db"
    db = sqlite3.connect(DB_FILE)
    u = db.cursor()
    u.execute('SELECT * FROM game_faves WHERE user = (?) AND title = (?);', (user, title))
    x = u.fetchall()
    db.commit()
    db.close()
    return x

def deleteFave(user,media_type,title):
    DB_FILE = "data/database.db"
    db = sqlite3.connect(DB_FILE)
    u = db.cursor()
    u.execute("SELECT * from "+media_type+"_faves WHERE "+media_type+"_faves.title = ? AND user=?;", (title,user,))
    x = u.fetchall()
    print(x)
    if len(x)==0:
        return
    u.execute("DELETE FROM "+media_type+"_faves WHERE title = ? AND user=?",(title,user))
    db.commit()
    db.close()
