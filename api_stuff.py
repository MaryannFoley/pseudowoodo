import json
from urllib import request

from flask import Flask

url = "https://api.themoviedb.org/3/genre/movie/list?api_key=fa2c0e8dd8956b932e67bbe3a99c3255&language=en-US"
raw = request.urlopen(url)
info = raw.read()
genres = json.loads(info)
# # i { 'id' : int, 'name' : 'genre name' }
# for i in genres["genres"]:
#     print(i)
