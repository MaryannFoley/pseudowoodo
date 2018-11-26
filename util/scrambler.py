from random import shuffle

def scramble_word(word):
    wordletters = []
    for letter in word:
        wordletters.append(letter)
    shuffle(wordletters)
    scrambled = ""
    for letter in wordletters:
        scrambled = scrambled + letter
    print(scrambled)
    
scramble_word('hello')
scramble_word('goodbye')
