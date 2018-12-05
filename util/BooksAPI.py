import urllib.request
import json
import random

from flask import Flask, render_template


NYTSTUB="https://api.nytimes.com/svc/books/v3/lists.json?"
NYTKEY="031e6a0aa9cc40f69ac3128de3f9d7fb"

def nyt(genre):
    try:
        f=open("util/BooksKey.txt","r")
        s=f.read().rstrip("\n")
        f.close()
        URL=NYTSTUB+"api-key="+s+"&list="+genre
        #f=open('./BooksKey.txt','r')
        #s=f.read().rstrip("\n")
        #f.close()
        #print(s)
        URL=NYTSTUB+"api-key="+NYTKEY+"&list="+genre
        request1=urllib.request.urlopen(URL)
        raw1=request1.read()
        jdict1=json.loads(raw1)
        results=jdict1["results"]
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

    except Exception as e:
        raise

def nyt_genres():
    try:
        f=open("util/BooksKey.txt","r")
        s=f.read().rstrip("\n")
        f.close()
        #f=open('./BooksKey.txt','r')
        #s=f.read().rstrip("\n")
        #f.close()
        URLbase="https://api.nytimes.com/svc/books/v3/lists/names.json?api-key="
        request1=urllib.request.urlopen(URLbase+NYTKEY)
        raw1=request1.read()
        jdict1=json.loads(raw1)
        results=jdict1["results"]

        list_names = []
        list_names_encoded = []

        for each in results:
            list_names.append(each['list_name'])
            list_names_encoded.append(each['list_name_encoded'])

        return list_names, list_names_encoded

        #print(results)
        return results
    except Exception as e:
        raise

#nyt_genres()


#print(nyt("young-adult"))

def getInfo():
    try:
        URL="https://www.goodreads.com/book/title.json?key=lKPxIV6sgpHQ2rZ51dwn9A&title=LOOK+ALIVE+TWENTY-FIVE"
        request1=urllib.request.urlopen(URL)
        raw1=request1.read()
        jdict1=json.loads(raw1)
        #print(jdict1)
    except Exception as e:
        raise

#print(nyt("combined-print-and-e-book-fiction"))
#getInfo()
