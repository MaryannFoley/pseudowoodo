import sqlite3

def create():
    DB_FILE = "data/database.db"

    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    #Creating our tables in our database
    c.execute("CREATE TABLE IF NOT EXISTS users (name TEXT PRIMARY KEY, pass TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS book_faves (user TEXT, isbn TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS movie_faves (user TEXT, movie_id TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS games_faves (user TEXT, game_id TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS music_faves (user TEXT, music_id TEXT)")

def
