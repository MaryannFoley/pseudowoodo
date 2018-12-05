import json, random
from urllib import request

movie_key = "fa2c0e8dd8956b932e67bbe3a99c3255"

def open_file():
    try:
        f=open("MoviesKey.txt","r")
        s=f.read().rstrip("\n")
        f.close()
        
        return s

    except FileNotFoundError as e:
        raise Exception('Error b/c file not found')


print(open_file())

