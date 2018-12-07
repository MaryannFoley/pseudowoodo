import urllib.request
import json
import random

from flask import Flask, render_template


NYTSTUB="https://api.nytimes.com/svc/books/v3/lists.json?"
NYTKEY="031e6a0aa9cc40f69ac3128de3f9d7fb"

def nyt(genre):
    try:
        f=open("util/BooksKey.txt","r")
    except FileNotFoundError as e:
        raise Exception('Error: <key>.txt file not found')

    s=f.read().rstrip("\n")
    f.close()

    try:
        URL=NYTSTUB+"api-key="+s+"&list="+genre
        #f=open('./BooksKey.txt','r')
        #s=f.read().rstrip("\n")
        #f.close()
        #print(s)
        #URL=NYTSTUB+"api-key="+NYTKEY+"&list="+genre
        request1=urllib.request.urlopen(URL)
        raw1=request1.read()
        jdict1=json.loads(raw1)
        results=jdict1["results"]
    except Exception as e:
        raise Exception('Error: API error')

    rand=int(random.random()*len(results))
    #print(jdict1)
    #print(results)
    #print('\n')
    #print(rand)

    #print(len(results))
    #print('\n')
    #print(results)
    #print(results)
    #print(rand)
    bookChoice=results[rand]

    #print(bookChoice)
    return bookChoice

def nyt_genres():
    try:
        f=open("util/BooksKey.txt","r")
    except FileNotFoundError as e:
        raise Exception('Error: <key>.txt file not found')

    s=f.read().rstrip("\n")
    f.close()
    #f=open('./BooksKey.txt','r')
    #s=f.read().rstrip("\n")
    #f.close()

    try:
        URLbase="https://api.nytimes.com/svc/books/v3/lists/names.json?api-key="
        request1=urllib.request.urlopen(URLbase+NYTKEY)
        raw1=request1.read()
        jdict1=json.loads(raw1)
        results=jdict1["results"]
    except Exception as e:
        raise Exception('Error: API error')

    list_names = []
    list_names_encoded = []

    for each in results:
        list_names.append(each['list_name'])
        list_names_encoded.append(each['list_name_encoded'])

    return list_names, list_names_encoded

#nyt_genres()


#print(nyt("young-adult"))
