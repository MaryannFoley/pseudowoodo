import json
from urllib import request

from flask import Flask

# title
# genre
# id - way to store specific movie for favorites list


url = "https://api.themoviedb.org/3/genre/movie/list?api_key=fa2c0e8dd8956b932e67bbe3a99c3255&language=en-US"
raw = request.urlopen(url)
info = raw.read()
genres = json.loads(info)
# i { 'id' : int, 'name' : 'genre name' }
for i in genres["genres"]:
    print(i)


def get_list(genres):
    url_base = "https://api.themoviedb.org/3/discover/movie?api_key=fa2c0e8dd8956b932e67bbe3a99c3255&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=1"
    g_query = "&with_genres="
    for i in genres:
        g_query += str(i) + "%2C"
    #print(g_query)
    url = url_base + g_query
    raw = request.urlopen(url)
    info = raw.read()
    data = json.loads(info)
    #for i in data['results']:
    #    print('id : ' + str(i['id']) + ' title : ' + i['title'])

test = [28, 35]
get_list(test)

