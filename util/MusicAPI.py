import urllib.request
import json
import random

#another key: f5362a758e0fb53042df13ded7a45825
# the key: 13ac239b500b6542edd7120afe6078e1


def get_song(genre):
    try:
        f=open("MusicKey.txt","r")
    except FileNotFoundError as e:
        raise Exception('Error: <key>.txt file not found')
    
    s=f.read().rstrip("\n")
    #print(type(s))
    f.close()

    try:
        baseurl = "http://api.musixmatch.com/ws/1.1/"
        url = baseurl + "track.search?f_lyrics_language=en&f_music_genre_id=" + genre + '&apikey=' + s

        httpresponse = urllib.request.urlopen(url) #this is initial httpresponse
        readresponse = httpresponse.read() #we are reading response
        decodedresponse = readresponse.decode() #we decode it for the json to load later
        #print(readresponse)

        data = json.loads(decodedresponse)['message']['body']['track_list']
        
    except Exception as e:
        raise Exception('Error: API error')
        
    song_choice = random.choice(data)
    
    #print(song_choice)

    #body = data["message"]["body"]["track_list"][0]["track"]["track_name"]
    return song_choice



def get_genres():
    try:
        f=open("MusicKey.txt","r")
    except FileNotFoundError as e:
        raise Exception('Error: <key>.txt file not found')
    
    s=f.read().rstrip("\n")
    f.close()

    try:
        baseurl = "http://api.musixmatch.com/ws/1.1/"
        #f=open("./MusicKey.txt","r")
        #s=f.read().rsplit("\n")
        #f.close()
        url = baseurl +"music.genres.get?apikey="+s

        httpresponse = urllib.request.urlopen(url) #this is initial httpresponse
        readresponse = httpresponse.read() #we are reading response
        decodedresponse = readresponse.decode() #we decode it for the json to load later

        data = json.loads(decodedresponse)
        
    except Exception as e:
        raise Exception('Error: API error')

    genres = []
    genres_encoded = []

    list = data['message']['body']['music_genre_list']

    for genre in list:
        if genre['music_genre']['music_genre_id'] != 34:
            genres.append(genre['music_genre']['music_genre_name'])
            genres_encoded.append(genre['music_genre']['music_genre_id'])

    return genres, genres_encoded

print(get_song('1086'))
