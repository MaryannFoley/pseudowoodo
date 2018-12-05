import json, random
from urllib import request


# title
# genre
# id - way to store specific movie for favorites list

def get_def(word):
    f=open("./dictKey.txt","r")
    s=f.read().rstrip("\n")
    f.close()
    url = "https://dictionaryapi.com/api/v3/references/collegiate/json/" + word + "?key=" + s
    raw = request.urlopen(url)
    info = json.loads(raw.read())
    defin = []
    for i in info:
        defin.append(i['shortdef'])

    #for i in defin:
    #    print(i)
    #    print("\n")

    return defin

word = "jack"
get_def(word)
