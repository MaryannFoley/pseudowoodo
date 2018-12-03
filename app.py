import json
import os
import random
import sqlite3
import urllib
from urllib.parse import urlparse

from flask import flash,Flask,request,render_template,session,url_for,redirect

from util import BooksAPI, scrambler

DB_FILE = "database.db"

db = sqlite3.connect(DB_FILE)
c = db.cursor()

#Creating our tables in our database
c.execute("CREATE TABLE IF NOT EXISTS users (name TEXT PRIMARY KEY, pass TEXT)")
c.execute("CREATE TABLE IF NOT EXISTS book_faves (user TEXT, isbn TEXT)")
c.execute("CREATE TABLE IF NOT EXISTS movie_faves (user TEXT, movie_id TEXT)")
c.execute("CREATE TABLE IF NOT EXISTS games_faves (user TEXT, game_id TEXT)")
c.execute("CREATE TABLE IF NOT EXISTS music_faves (user TEXT, music_id TEXT)")

app = Flask(__name__)
app.secret_key=os.urandom(32)

#==================================== HOME ====================================

@app.route("/")
def home():
    print(session)
    if session.get('username'):
        return render_template('home.html')
    return render_template('login.html')

#=============================== REGISTER/LOGIN ===============================

@app.route("/create_account", methods=['POST'])
def create_account():
    db = sqlite3.connect(DB_FILE)
    u = db.cursor()
    u.execute("CREATE TABLE IF NOT EXISTS users (name TEXT, pwd TEXT)")
    uname = request.form["new_username"]
    pwordA = request.form["new_password"]
    pwordB = request.form["confirm_password"]
    u.execute("SELECT name, pass FROM users");
    for person in u:
        if uname==person[0]: #checks if your username is unique
            flash("Username taken")# username already exists
            return render_template("register.html")
    if pwordA != pwordB:
        flash("Passwords don\'t match") # given passwords don't match
        return render_template("register.html")
    else:
        u.execute("INSERT INTO users values(?,?)", (uname, pwordA))
    db.commit();
    db.close();
    return redirect(url_for("home"))

@app.route("/login", methods=['GET', 'POST'])
def login():
    print(session)
    if session.get('username'):
        return redirect(url_for("home"))
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template('register.html')

@app.route("/auth", methods=['POST'])
def auth():
    db = sqlite3.connect(DB_FILE)
    u = db.cursor()
    givenUname=request.form["username"]
    givenPwd=request.form["password"]
    u.execute("SELECT name, pass FROM users");
    found = False #if the user is found
    for person in u: #for every person in the users table
        if givenUname==person[0]:
            found = True #user exists
            if givenPwd==person[1]:
                session["username"]=givenUname
                if session.get("error"):
                    session.pop("error")
            else:
                flash("Please recheck your credentials and try again.")#means password was wrong
        if (found):
            break #exit for loop is user is found
    if (not found):
        flash("Please recheck your credentials and try again.")#username was wrong
    db.commit();
    db.close();
    return redirect(url_for("login"))

@app.route("/logout", methods=['GET', 'POST'])
def logout():
    if session.get('username'):
        session.pop('username')
    return redirect(url_for('home'))

#==================================== FAVES ====================================

@app.route("/faves")
def faves():
    username=session.get('username')
    return render_template('user.html', user_name=username)

@app.route("/add_fav")
def add_fave():
    db = sqlite3.connect(DB_FILE)
    u = db.cursor()
    db.commit()
    db.close()
    return ""
#==================================== OTHER ====================================

@app.route("/genre", methods=['POST'])
def genre():
    media_type = request.form['media']
    types = ['Books', 'Movies', 'Video Games', 'Music']
    for type in types:
        if media_type == type:
            return render_template('genre.html', media_type=media_type)
    print("if you get here, something's very wrong")
    return "if you get here, something's very wrong"

@app.route("/scramble", methods=['POST'])
def scramble():
    genre_type = request.form['genre']
    apigenre_type = request.form['apigenre']
    types = ['Combined Print and E-Book Fiction', '', '', '']
    for type in types:
        if genre_type == type:
            info = BooksAPI.nyt(apigenre_type)
            #print(info)
            title = info['book_details'][0]['title']
            title_words_punctuated = title.split(" ")
            title_words = []
            for word in title_words_punctuated:
                no_period = word.replace('.', '')
                no_question = no_period.replace('?', '')
                no_exclamation = no_question.replace('!', '')
                no_semicolon = no_exclamation.replace(';', '')
                no_colon = no_semicolon.replace(':', '')
                no_leftparenth = no_colon.replace('(', '')
                no_rightparenth = no_leftparenth.replace(')', '')
                no_quote = no_rightparenth.replace('"', '')
                title_words.append(no_quote)
            scrambled_title_words = []
            correctly_guessed = []
            for word in title_words:
                scrambled_title_words.append(scrambler.scramble_word(word))
                correctly_guessed.append(False)
            print(title_words)
            print(scrambled_title_words)
            return render_template('scramble.html', genre_type=genre_type, title_words=title_words,
                                   scrambled_title_words=scrambled_title_words, correctly_guessed=correctly_guessed)
    print("if you get here, something's very wrong")
    return "if you get here, something's very wrong"

@app.route("/check", methods=['POST'])
def check():
    print(request.form)
    genre_type = request.form['genre']
    title_words = []
    scrambled_title_words = []
    correctly_guessed = []
    

    for each in request.form:
        print(each)

    print('---------------------')
    
    for each in request.form:
        if 'scrambled' in each:
            print('word:', request.form[each])
            word = each.split('_')[2]
            title_words.append(word)
            scrambled_title_words.append(request.form['scrambled_for_'+word])
            #print(request.form['scrambled_for_'+word])
            #print('scram-list', scrambled_title_words)
            
            #print('titlewords:', title_words)
            
            if word == request.form['guess_for_'+word].upper():
                print('correct!')
                correctly_guessed.append(True)
            else:
                print('incorrect')
                correctly_guessed.append(False)

    #print(request.form)
    print(correctly_guessed)
    for each in correctly_guessed:
        print('-----')
        print(each)
        print(correctly_guessed[each])
        print('-----')
        if not each:
            #print(request.form['status_for_'+word])
            return render_template('scramble.html', genre_type=genre_type, title_words=title_words, scrambled_title_words=scrambled_title_words, correctly_guessed=correctly_guessed)
    return render_template('result.html')
        
    
    #print(request.form)

@app.route("/result")
def result():
    return render_template('result.html')



@app.route("/testing")
def testing():
    baseurl = "http://api.musixmatch.com/ws/1.1/"
    apikey = "&apikey=13ac239b500b6542edd7120afe6078e1" #for Musixmatch
    letters = ["Hello", "Disturbi", "Payp"]
    word = random.choice(letters)
    url = baseurl + "track.search?q_track=" + word + apikey

    httpresponse = urllib.request.urlopen(url) #this is initial httpresponse
    readresponse = httpresponse.read() #we are reading response
    decodedresponse = readresponse.decode() #we decode it for the json to load later
    #print(readresponse)

    data = json.loads(decodedresponse)
    body = data["message"]["body"]["track_list"][0]["track"]["track_name"]
    artist = data["message"]["body"]["track_list"][0]["track"]["artist_name"]
    print(data)
    return render_template("TESTING_ONLY.html", body=body, artist=artist)


if __name__ == "__main__":
    app.debug = True
    app.run()
