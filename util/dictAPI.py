import json, random
import urllib
from urllib import request


# title
# genre
# id - way to store specific movie for favorites list

def get_def(word):
    try:
        f=open("util/dictKey.txt","r")
    except FileNotFoundError as e:
        raise Exception('<file>.txt is not found')

    s=f.read().rstrip("\n")
    f.close()
    url = "https://dictionaryapi.com/api/v3/references/collegiate/json/" + word + "?key=" + s

    defin = []
    try:
        raw = request.urlopen(url)
        info = json.loads(raw.read())
        for i in info:
            defin.append(i['shortdef'])

        #for i in defin:
        #    print(i)
        #    print("\n")
    except:
        # wont be scrambled
        print("NO")

    #print(defin)

    if len(defin) != 0:
        success = True
        random_def = random.choice(defin[0])
    else:
        success = False
        random_def = ''
        #print(random_def)

    return (success, random_def)

word = "tom"
print(get_def(word))
