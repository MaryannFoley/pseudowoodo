import json, random
from urllib import request


# title
# genre
# id - way to store specific movie for favorites list

base_url = "https://api-2445582011268.apicast.io/"


def get_genres():
    '''Generate a dictionary of genre ids as key and genre names as values'''
    f = open("VideoGamesKey.txt","r")
    key=f.read()
    f.close()
    key = key.rstrip("\n")
    url = base_url + "genres/"
    header = {
            "Accept": "application/json",
            "User-key" : key,
            }


    r = request.Request(url, headers = header )

    try:
        raw = request.urlopen(r)
    except urllib.HTTPError as err:
        if err.code == 403:
            print("WHY")


    info = raw.read()
    genres = json.loads(info)

    req = request.Request(url + '2', headers = header)
    raw = request.urlopen(req).read()
    temp = json.loads(raw)
    name = temp[0]['games'][0]
    print(name)

def get_game_list(genre_id):
    '''Generates list of game ids containing given genre'''
    f = open("VideoGamesKey.txt","r")
    key=f.read()
    f.close()
    key = key.rstrip("\n")
    url = base_url + "genres/"
    header = {
            "Accept": "application/json",
            "User-key" : key,
            }

    req = request.Request(url + str(genre_id), headers = header)
    raw = request.urlopen(req).read()
    temp = json.loads(raw)
    id_list = temp[0]['games']
    return id_list

def get_rand_game(id_list):
    '''Gets information of a game randomly chosen from id_list'''
    f = open("VideoGamesKey.txt","r")
    key=f.read()
    f.close()
    key = key.rstrip("\n")
    url = base_url + "games/"
    header = {
            "Accept": "application/json",
            "User-key" : key,
            }

    game = random.choice(id_list)
    req = request.Request(url + str(game), headers = header)
    raw = request.urlopen(req).read()
    data = json.loads(raw)[0]
    print(data['name'])

    return data['name']


#get_genres()
get_rand_game(get_game_list(2))
