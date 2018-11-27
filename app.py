import urllib
from urllib.parse import urlparse
import urllib.request
import json
import random


from flask import Flask,request,render_template,session,url_for,redirect
app = Flask(__name__)

@app.route("/")
def home():
    return "No hablo queso!"

@app.route("/login")
def login():
    return "No hablo queso!"

@app.route("/signup")
def signup():
    return "No hablo queso!"

@app.route("/scramble")
def scramble():
    return "No hablo queso!"

@app.route("/result")
def result():
    return "No hablo queso!"

@app.route("/favs")
def favs():
    return "No hablo queso!"

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
