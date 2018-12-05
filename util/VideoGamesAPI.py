import json, random
from urllib import request


# title
# genre
# id - way to store specific movie for favorites list

def get_genres():
    f = open("./VideoGamesKey.txt","r")
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


# def get_list(genres):
#     f=open("util/VideoGamesKey1.txt","r")
#     key=f.read()
#     f.close()
#     url_base = "https://api.themoviedb.org/3/discover/movie?api_key="+key+"&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=1"
#     g_query = "&with_genres="
#     for i in genres:
#         g_query += str(i) + "%2C"
#     #print(g_query)
#     url = url_base + g_query
#     raw = request.urlopen(url)
#     info = raw.read()
#     data = json.loads(info)
#     #for i in data['results']:
#         #print('popularity : ' + str(i['popularity']) + ' title : ' + i['title'])
#         #print(get_poster(i))
#     return data['results']
# 
# 
# def get_random_one(test):
#     list = get_list(test)
#     return random.choice(list)

# test = [878]
# print(get_random_one(test))
#print(get_list(test))
get_genres()
