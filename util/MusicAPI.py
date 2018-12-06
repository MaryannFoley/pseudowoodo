import urllib.request
import json
import random

#another key: f5362a758e0fb53042df13ded7a45825
# the key: 13ac239b500b6542edd7120afe6078e1


def get_song(genre):
    try:
        f=open("util/MusicKey.txt","r")
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
        f=open("util/MusicKey.txt","r")
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
        return get_genres()

    genres = []
    genres_encoded = []

    list = data['message']['body']['music_genre_list']

    empty_genres = [34, 100029, 100028, 100024, 100025, 8217, 1279, 1246, 1245, 1244, 1239, 1238, 1236, 1235, 1234, 1233, ]
    non_english = [1686, 1656, 1278, 1269, 1268, 1267, 1266, 1265, 1264, 1263, 100034, 100033, 1185, 1247, 1240, 1237, 1287, 1286, 1285, 1284, 1229, 1228, 1227, 1226, 1224, 1223, 1222, 1221, 1220, 1262, 1243, 1232, 50000068, 50000066, 50000064, 50000063, 50000061, 100024, 1197, 1122, 51, 30, 29, 28, 27, 19, 12 ]

    for genre in list:
        if genre['music_genre']['music_genre_id'] not in empty_genres and genre['music_genre']['music_genre_id'] not in non_english:
            genres.append(genre['music_genre']['music_genre_name'])
            genres_encoded.append(genre['music_genre']['music_genre_id'])

    #print(genres_encoded)
    return genres, genres_encoded

#print(get_song('1086'))
