import json
import os
import random
import sqlite3
import urllib

from urllib.parse import urlparse

from flask import flash,Flask,request,render_template,session,url_for,redirect

from util import BooksAPI, dictAPI, MoviesAPI, MusicAPI, VideoGamesAPI, scrambler, db

DB_FILE = "data/database.db"
#
# db = sqlite3.connect(DB_FILE)
# c = db.cursor()
#
# #Creating our tables in our database
# c.execute("CREATE TABLE IF NOT EXISTS users (name TEXT PRIMARY KEY, pass TEXT)")
# c.execute("CREATE TABLE IF NOT EXISTS book_faves (user TEXT, isbn TEXT)")
# c.execute("CREATE TABLE IF NOT EXISTS movie_faves (user TEXT, movie_id TEXT)")
# c.execute("CREATE TABLE IF NOT EXISTS games_faves (user TEXT, game_id TEXT)")
# c.execute("CREATE TABLE IF NOT EXISTS music_faves (user TEXT, music_id TEXT)")

db.create()

app = Flask(__name__)
app.secret_key=os.urandom(32)

#============================== GLOBAL VARIABLES ==============================

#===== Book Genres =====
types_Books = BooksAPI.nyt_genres()[0]
types_Books_API = BooksAPI.nyt_genres()[1]

types_Movies = MoviesAPI.get_genres()[0]
types_Movies_API = MoviesAPI.get_genres()[1]

types_Music = MusicAPI.get_genres()[0]
types_Music_API = MusicAPI.get_genres()[1]

types_Games = VideoGamesAPI.get_genres()[0]
types_Games_API = VideoGamesAPI.get_genres()[1]

#======== Misc =========


#==================================== HOME ====================================

@app.route("/")
def home():
    print(session)
    if session.get('username'):
        return render_template('home.html', username=session.get('username'))
    return render_template('login.html')

#=============================== REGISTER/LOGIN ===============================

@app.route("/create_account", methods=['POST'])
def create_account():
    uname = request.form["new_username"]
    pwordA = request.form["new_password"]
    pwordB = request.form["confirm_password"]

    if ' ' in uname or pwordA or pwordB:
        flash('User credentials cannot contain spaces!')
        return render_template("register.html")

    if '' == uname or pwordA or pwordB:
        flash('User credentials cannot be empty!')
        return render_template("register.html")

    u = db.checkAccts()
    for person in u:
        if uname==person[0]: #checks if your username is unique
            flash("Username taken")# username already exists
            return render_template("register.html")
    if pwordA != pwordB:
        flash("Passwords don\'t match") # given passwords don't match
        return render_template("register.html")
    else:
        db.createAcct(uname,pwordA)
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
    givenUname=request.form["username"]
    givenPwd=request.form["password"]
    u = db.checkAccts()
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
    return redirect(url_for("login"))

@app.route("/logout", methods=['GET', 'POST'])
def logout():
    if session.get('username'):
        session.pop('username')
    return redirect(url_for('home'))

#==================================== FAVES ====================================

@app.route("/faves")
def faves():

    if not session.get('username'):
        return redirect(url_for("home"))
    username=session.get('username')

    user_faves = []

    temp=db.getFaves("book",username)
    user_faves.extend(temp)

    temp=db.getFaves("movie",username)
    user_faves.extend(temp)

    temp=db.getFaves("game",username)
    user_faves.extend(temp)

    temp=db.getFaves("music",username)
    user_faves.extend(temp)

    #print(user_faves)

    return render_template('user.html', user_name=username, favorites=user_faves)

@app.route("/add_fav")
def add_fave():

    if not session.get('username'):
        return redirect(url_for("home"))
    #print(request.args)
    user = session.get('username')
    media_type = request.args['Type']
    title = request.args['Title']

    if media_type == 'Books':
        author = request.args['Author']
        description = request.args['Description']
        date = request.args['Date']
        amazon = request.args['Amazon']
        db.addBook(user, media_type, title, author, description, date, amazon)

    elif media_type == 'Movies':
        poster = request.args['Poster']
        description = request.args['Description']
        date = request.args['Date']
        db.addMovie(user, media_type, title, poster, description, date)

    elif media_type == 'Music':
        artist = request.args['Artist']
        album = request.args['Album']
        date = request.args['Date']
        lyrics = request.args['Lyrics']
        db.addMusic(user, media_type, title, artist, album, date, lyrics)

    else:
        #-----------------------------------------------------------------------------VIDO GAME HERE-------------------------------------------------------
        db.addGame(user, media_type, title)

    return redirect(url_for('faves'))

@app.route("/remove_fav")
def remove_fav():
    if not session.get('username'):
        return redirect(url_for("home"))
    if request.args["Type"]=="Books":
        type="book"
    elif request.args["Type"]=="Movies":
        type="movie"
    elif request.args["Type"]=="Video Games":
        type="game"
    else:
        type="music"
    db.deleteFave(session.get("username"),type,request.args['Title'])
    return(redirect(url_for("faves")))

#==================================== MEDIA ====================================

@app.route("/genre", methods=['POST'])
def genre():

    if not session.get('username'):
        return redirect(url_for("home"))
    session['media_type'] = request.form['media']
    print(session)

    media_type = session.get('media_type')

    types = ['Books', 'Movies', 'Video Games', 'Music']
    for type in types:
        if media_type == type:

            if media_type == 'Books':
                types = types_Books
                types_API = types_Books_API
            elif media_type == 'Movies':
                types = types_Movies
                types_API = types_Movies_API
            elif media_type == 'Music':
                types = types_Music
                types_API = types_Music_API
            else:
                types = types_Games
                types_API = types_Games_API

            session['from'] = 'genre.html'
            return render_template('genre.html', media_type=media_type, genres=types, genres_API=types_API)
    print("if you get here, something's very wrong")
    return "if you get here, something's very wrong"

@app.route("/scramble", methods=['POST'])
def scramble():

    if not session.get('username'):
        return redirect(url_for("home"))
    if 'from' in session and session.get('from') == "genre.html":
        session['genre'] = request.form['genre']
        session['genre_encoded'] = request.form['apigenre']
        session.pop('from')

    media_type = session['media_type']
    genre = session.get('genre')
    genre_encoded = session.get('genre_encoded')


    if media_type == 'Books':
        types = types_Books
        types_API = types_Books_API
        info = BooksAPI.nyt(genre_encoded)

        title = info['book_details'][0]['title']
        date = info['published_date']
        description = info['book_details'][0]['description']
        link = info['amazon_product_url']
        author = info['book_details'][0]['author']

        session['Description'] = description
        session['Amazon'] = link
        session['Author'] = author

    #---------------------------

    elif media_type == 'Movies':
        types = types_Movies
        types_API = types_Movies_API
        info = MoviesAPI.get_random_one([genre_encoded])

        title = info['title'].upper()
        date = info['release_date']
        description = info['overview']
        poster = info['poster_path']

        session['Description'] = description
        session['Poster'] = "https://image.tmdb.org/t/p/w600_and_h900_bestv2" + poster

    #---------------------------

    elif media_type == 'Music':
        types = types_Music
        types_API = types_Music_API
        info = MusicAPI.get_song(genre_encoded)['track']

        title = info['track_name'].upper()
        date = info['first_release_date'][0:10]
        album = info['album_name']
        artist = info['artist_name']
        lyrics = info['track_share_url']

        session['Album'] = album
        session['Artist'] = artist
        session['Lyrics'] = lyrics

    #---------------------------

    else:
        types = types_Games
        types_API = types_Games_API
        info = VideoGamesAPI.get_rand_game(genre_encoded) #needs to be updated

        print(info)
        title = info['name'].upper()
        try:
            date = info['release_date']
        except Exception as e:
            date = 'N/A'
        try:
            link = info['url']
        except Exception as e:
            link = 'N/A'

        try:
            summary = info['summary']
        except Exception as e:
            summary = 'N/A'
        try:
            cover = info['cover']
        except Exception as e:
            cover = 'N/A'

        session['Link'] = link
        session['Description'] = summary
        session['Cover'] = cover


    #print(info)

    session['Title'] = title.upper()
    session['Date'] = date

    for type in types:
        if genre == type:
            title_words_punctuated = title.split(" ")
            title_words = []
            for word in title_words_punctuated:

                checked_word = remove_punct(word)
                title_words.append(checked_word)

            scrambled_title_words = []
            correctly_guessed = []
            dictionary = {}
            for word in title_words:
                scrambled_title_words.append(scrambler.scramble_word(word))
                correctly_guessed.append(False)
                dictionary[word] = dictAPI.get_def(word)

            #dictionary['emma'] = 'chin'
            session['dict'] = dictionary

            print('---------------------scramble')
            print(session)

            return render_template('scramble.html', genre=genre, title_words=title_words,
                                   scrambled_title_words=scrambled_title_words, correctly_guessed=correctly_guessed, dictionary=dictionary)


    print("if you get here, something's very wrong")
    return "if you get here, something's very wrong"

@app.route("/check", methods=['POST'])
def check():

    if not session.get('username'):
        return redirect(url_for("home"))
    print('---------------------check')
    print(session)
    print(request.form)
    genre = session.get('genre')
    dictionary = session.get('dict')
    title_words = []
    scrambled_title_words = []
    correctly_guessed = []


    #for each in request.form:
    #    print(each+': ', request.form[each])

    #print('---------------------')
    white_flag = request.form['surrender']
    session['surrender'] = white_flag
    if white_flag == 'no':
        for each in request.form:
            if 'scrambled' in each:
                word = each.split('_')[2]
                title_words.append(word)
                scrambled_title_words.append(request.form['scrambled_for_'+word])

                if word == request.form['guess_for_'+word].upper().strip(' '):
                    #print('correct!')
                    correctly_guessed.append(True)
                else:
                    #print('incorrect')
                    correctly_guessed.append(False)

    else:
        i = 0
        while i < len(correctly_guessed):
            correctly_guessed[i] = True
            i = i + 1

    for each in correctly_guessed:
        if not each:
            return render_template('scramble.html', genre=genre, title_words=title_words, scrambled_title_words=scrambled_title_words,
                    correctly_guessed=correctly_guessed, dictionary=dictionary)

    session['from'] = 'scramble'
    return redirect(url_for('result'))


    #print(request.form)

@app.route("/result")
def result():

    if not session.get('username'):
        return redirect(url_for("home"))
    book_deets = ['Title', 'Author', 'Description', 'Date', 'Amazon', 'Type']
    movie_deets = ['Title', 'Poster', 'Description', 'Date', 'Type']
    game_deets = ['Title', 'Cover', 'Description', 'Date', 'Link', 'Type']
    music_deets = ['Title', 'Artist', 'Album', 'Date', 'Lyrics', 'Type']

    pairing = {'Books': book_deets, 'Movies': movie_deets, 'Video Games': game_deets, 'Music': music_deets}

    details = {}
    if 'from' in session:
        session.pop('from')
        source = 'session'
        page_title = "Congratulations! You've Guessed It!"
        media_type = session.get('media_type')
    else:
        source = 'request'
        page_title = "Information"
        media_type = request.args['Type']
    if "surrender" in session:
        if session['surrender'] == "yes":
            page_title = "You gave up, better luck next time!"

    for media in pairing:
        if media == media_type:
            for deet in pairing[media]:
                if deet == 'Type':
                    details[deet] = media_type
                else:
                    if source == 'session':
                        details[deet] = session.get(deet)
                    else:
                        if deet == "Poster":
                            details[deet] = "https://image.tmdb.org/t/p/w600_and_h900_bestv2" + request.args[deet]
                        else:
                            details[deet] = request.args[deet]

    user = session.get('username')
    title = details['Title']
    if details['Type'] == 'Books':
        author = details['Author']
        dupes = db.getBook(user, title, author)
    elif details['Type'] == 'Movies':
        date = details['Date']
        dupes = db.getMovie(user, title, date)
    elif details['Type'] == 'Music':
        artist = details['Artist']
        dupes = db.getMusic(user, title, artist)
    else:
        dupes = db.getGame(user, title)

    #print('*****dupes_fetched*****', dupes_fetched)
    if len(dupes) > 0:
        in_faves = True
    else:
        in_faves = False

    print('in_faves', in_faves)


    #print(details)

    print(session)
    return render_template('result.html', details=details, title=page_title, in_faves=in_faves)

#==================================== HELPER ===================================

def remove_punct(word):
    no_period = word.replace('.', '')
    no_question = no_period.replace('?', '')
    no_exclamation = no_question.replace('!', '')
    no_semicolon = no_exclamation.replace(';', '')
    no_colon = no_semicolon.replace(':', '')
    no_leftparenth = no_colon.replace('(', '')
    no_rightparenth = no_leftparenth.replace(')', '')
    no_quote = no_rightparenth.replace('"', '')
    no_comma = no_quote.replace(',', '')
    no_left_brack = no_comma.replace('[', '')
    no_right_brack = no_left_brack.replace(']', '')
    return no_right_brack


#===================================== RUN  ====================================

if __name__ == "__main__":
    app.debug = True
    app.run()
