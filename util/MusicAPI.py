import urllib.request
import json
import random

#another key: f5362a758e0fb53042df13ded7a45825

def get_song(genre):
    try:
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
        return data

    except Exception as e:
        raise


def get_genres():
    try:
        baseurl = "http://api.musixmatch.com/ws/1.1/"
        apikey = "&apikey=13ac239b500b6542edd7120afe6078e1" #for Musixmatch
        url = baseurl + "music.genres.get?" + apikey
        
        httpresponse = urllib.request.urlopen(url) #this is initial httpresponse
        readresponse = httpresponse.read() #we are reading response
        decodedresponse = readresponse.decode() #we decode it for the json to load later
        
        data = json.loads(decodedresponse)

        genres = []
        genres_encoded = []
        
        list = data['body']['music_genre_list']

        for genre in list:
            genres.append(genre['music_genre']['music_genre_name'])
            genres.append(genre['music_genre']['music_genre_id'])
            
    except:
        raise
        
#print(get_song())
print(get_genres())

