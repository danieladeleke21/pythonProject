import requests
import json

#Api to get a word
q = requests.get('https://random-word-api.herokuapp.com/word')
word = q.json()[0]

#Word dictionary API
response = requests.get('https://api.dictionaryapi.dev/api/v2/entries/en/' + word)

#Extracting the definition of the word from the dictionary API
a = response.json()[0]
b = a["meanings"][0]
c = b["definitions"]
d = c[0]
define = d["definition"]