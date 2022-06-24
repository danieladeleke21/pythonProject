# A Program to guess a random nae
#API
import requests

url = "https://random-name-generator1.p.rapidapi.com/first_name"

headers = {
	"X-RapidAPI-Key": "4bba004fbamshb627297475caac4p106a0ejsnd396c6896533",
	"X-RapidAPI-Host": "random-name-generator1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

name = response.json()["first_name"]



#Beginning of code
guess = input("Try guessing the name: ")
i = 1
no_guess = False

while guess.lower() != name.lower() and not(no_guess):
    if i < 5:
        i += 1
        guess = input("Try guessing again: ")
    else:
        print("You lose")
        no_guess = True
if no_guess == True:
    print("You are out of guesses")
    print("The random name is: " + name)
else:
    print("You guessed correctly")