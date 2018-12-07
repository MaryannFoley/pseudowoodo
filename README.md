# pseudowoodo
PM: Maryann Foley
Thomas Zhao, Jack Lu, Sarar Aseer

Soft Dev Project 1


Our website is a game in which visitors have to unscramble the title of a piece of media (books/movies/video games/music). They are hinted as to what these words may be, thanks to dictionary definitions of the words displayed.

When they either 1.) correctly enter the full title or 2.) click “Give up”, they will be taken to an information page for that particular work. They have the option of doing another unscrambling, just a button away.  We also have a favorites page, so if somebody sees a book, movie, game, or song they like they are able to add it to a list that is accesible at a later date.

### Instructions for setup:

#### Virtual enviornment:
- It is important to use a venv because it creates an isolated python enviornment to run code.  It allows you to
have your dependencies installed exclusively on it, not globally. (you don't need root access!)  This is especially useful if you need to use 2 different versions of a package with 2 pieces of code.

Steps to create a venv:
1. In a terminal, go to the folder in which you want to keep your venv
2. Run `python3 -m venv EXVENV`
   1. We are using EXVENV as the name of the virtual enviornment; you can use any name you would like
3. Activate your virtual enviornment by running `source EXVENV/bin/activate`
   1. Your computer's name will now be preceded by (EXVENV).  You are now inside of the virtual enviornment.
4. Install dependencies (see below)
5. To exit the venv, run `deactivate`
6. You can now activate your virtual enviornment from any cwd by running `source ~/ROUTE/TO/ENV/EXVENV/bin/activate`


#### Dependencies!
- sqlite3

This allows us to access the DB to save favorites
- flask

The back end framework that allows you to host the website
- wheel

__NOTE:__ Activate your virtual enviornment and cd into this directory before installing this!

To install dependencies, run `pip3 install -r requirements.txt`

## Where to obtain API keys

[NYT Books API (Bestseller lists)](http://developer.nytimes.com/signup)
- No account needed

[tMDB API (Movie API)](https://www.themoviedb.org/settings/api)
- Requires account to get a key. Once logged in, click the link above

[igdb API (video game API)](https://api.igdb.com/signup?plan_ids[]=2357355916792)
- Requires account to get a key. Click link to create account

[Musixmatch API (music API)](https://developer.musixmatch.com/signup)
- Requires account to get a key. Click link to create account

[Merriam-Webster API (dictonary API)](https://dictionaryapi.com/register/index)
- Requires developer account to get a key. Click link to create account

#### Where to put your keys

Put each of your keys in a different file in the `util` folder. Each of these documents should contain only the key and no new lines or other characters.
- NYT Books API Key goes in a file named `BooksKey.txt`
- tMDB API Key goes in a file named `MoviesKey.txt`
- igdb API Key goes in a file named `VideoGamesKey.txt`
- Musixmatch API key goes in a file named `MusicKey.txt`
- Merriam-Webster API key goes in a file named `dictKey.txt`

## Launch instructions:
1. Activate your virtual enviornment
2. Clone and cd into this repo
3. Run `python3 app.py`
    - Note: run app.py in pseudowoodo directory because our files utilize relative paths.
4. Enjoy!
