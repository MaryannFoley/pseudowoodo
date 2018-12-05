import json, random
from urllib import request


# title
# genre
# id - way to store specific movie for favorites list

def get_def():
    f=open("./dictKey.txt","r")
    s=f.read().rstrip("\n")
    f.close()
    url = ""
    raw = request.urlopen(url)
    info = raw.read()
    genres = json.loads(info)['genres']




word = "velocity"
print(get_def(word))
