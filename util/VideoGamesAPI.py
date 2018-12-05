import json, random
from urllib import request


# title
# genre
# id - way to store specific movie for favorites list

def get_genres():
    f = open("../VideoGamesKey.txt","r")
    key=f.read()
    f.close()
    key = key.rstrip("\n")
    #print("|" + key + "|")

    base_url = "https://api-endpoint.igdb.com"
    header = {
            "Accept": "application/json",
            "User-key" : key,
            }
    url = base_url + "/genres/"

    print(url)
    print(header)
    print(header['User-key'])

    r = request.Request(url, headers = header )

    print(r.has_header("User-key"))
    print(r.has_header("Accept"))
    print(r)

    raw = request.urlopen(r)
    #info = raw.read()
    #print(info)
    #genres = json.loads(info)

    #print(genres)

    # genre_numbers = []
    # genre_names = []

    #print(genres)

    # for genre in genres:
    #     #print(genre)
    #     genre_numbers.append(genre['id'])
    #     genre_names.append(genre['name'])

    # return genre_names, genre_numbers

# i { 'id' : int, 'name' : 'genre name' }
#for i in genres["genres"]:
#    print(i)

get_genres()
