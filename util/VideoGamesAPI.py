import json, random
from urllib import request


# title
# genre
# id - way to store specific movie for favorites list

base_url = "https://api-2445582011268.apicast.io/"


# return genre in list, id in list, indices matching
def get_genres():
    '''Generate a dictionary of genre ids as key and genre names as values'''
    try:
        f = open("util/VideoGamesKey.txt","r")
    except FileNotFoundError as e:
        raise Exception('file was not found')
        
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

    req = request.Request(url, headers = header)
    raw = request.urlopen(req).read()
    data = json.loads(raw)

    g_list = ""
    genre_numbers = []
    genre_names = []
    for i in data:
        g_list += str(i['id']) + ","
    print(g_list)
    #req = request.Request(url + str(i['id']), headers = header)
    #raw = request.urlopen(req).read()
    #data = json.loads(raw)[0]['name']

    #genre_numbers.append(i['id'])
    #genre_names.append(data)
    print(genre_names)
    return genre_names, genre_numbers

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

# return: name, url, summary, human date, cover url (image)
def get_rand_game(genre_id):
    '''Gets information of a random game within the provided genre'''

    id_list = get_game_list(genre_id)

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
    info = json.loads(raw)[0]

    data = {}
    data['name'] = info['name']
    data['url'] = info['url']
    data['summary'] = info['summary']
    data['release_date'] = info['release_dates'][0]['human']
    data['cover'] = info['cover']['url']

    #for i in data:
    #    print(i, data[i]) 

    return data


get_genres()
#get_rand_game(25)
