import json
import requests
from api_edit import *

i = 1
print("Definition of the word:")
print(define)
guess = input("Input the word defined above:")
no_guess = False
while guess.lower() != word.lower() and not(no_guess):
    if i < 3:
        i += 1 
        guess = input("Try guessing again:")
    else:
        print("You lose")
        no_guess = True
if no_guess == True:
    print("You are out guesses")
    print("The word is: " + word)

else:
    print("You guessed correctly")