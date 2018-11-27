import json, os, random, sqlite3, urllib
from urllib.parse import urlparse
from flask import Flask,request,render_template,session,url_for,redirect

DB_FILE = "database.db"

db = sqlite3.connect(DB_FILE)
c = db.cursor()

#Creating our tables in our database
c.execute("CREATE TABLE IF NOT EXISTS users (name TEXT, pass TEXT)")

app = Flask(__name__)
app.secret_key=os.urandom(32)

@app.route("/")
def home():
    #flash errors need to be implemented
    return render_template('home.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/signup")
def signup():
    return render_template('signup.html')

@app.route("/scramble")
def scramble():
    return render_template('scramble.html')

@app.route("/result")
def result():
    return render_template('result.html')

@app.route("/faves")
def faves():
    return render_template('faves.html')

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
