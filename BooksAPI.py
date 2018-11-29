
import urllib.request
import json

from flask import Flask, render_template


NYTSTUB="https://api.nytimes.com/svc/books/v3/lists.json?"
NYTKEY="031e6a0aa9cc40f69ac3128de3f9d7fb"

def nyt(genre):
    URL=NYTSTUB+"api-key="+NYTKEY+"&list="+genre
    request1=urllib.request.urlopen(URL)
    raw1=request1.read()
    jdict1=json.loads(raw1)
    print(jdict1)
nyt("combined-print-and-e-book-fiction")
