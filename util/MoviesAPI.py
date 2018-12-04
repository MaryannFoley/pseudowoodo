import json, random
from urllib import request


# title
# genre
# id - way to store specific movie for favorites list

def get_genres():
    url = "https://api.themoviedb.org/3/genre/movie/list?api_key=fa2c0e8dd8956b932e67bbe3a99c3255&language=en-US"
    raw = request.urlopen(url)
    info = raw.read()
    genres = json.loads(info)['genres']

    genre_numbers = []
    genre_names = []

    #print(genres)
    
    for genre in genres:
        #print(genre)
        genre_numbers.append(genre['id'])
        genre_names.append(genre['name'])

    return genre_names, genre_numbers
    
# i { 'id' : int, 'name' : 'genre name' }
#for i in genres["genres"]:
#    print(i)


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
        #print('popularity : ' + str(i['popularity']) + ' title : ' + i['title'])
        #print(get_poster(i))
    return data['results']

#input movie from data['results']
def get_poster(movie):
    url = "https://image.tmdb.org/t/p/w600_and_h900_bestv2/"
    img = movie['poster_path']
    return url + img

def get_random_one(test):
    list = get_list(test)
    return random.choice(list)

test = [878]
print(get_random_one(test))
#print(get_list(test))

#notes for thomas
#title, author/director/artist/publisher, link_to_purchase
