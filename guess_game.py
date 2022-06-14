# A simple guess game my name "Daniel"
secret_message = "Daniel"

guess = input("Try guessing my First name:")
i = 1
no_guess = False
while guess != secret_message and not(no_guess):
    if i < 5:
        i += 1
        if i != 4:
            guess = input("Try guessing again:")
        else:
            print("Hint: It is a 6 letter name")
            guess = input("Try guessing again:")
    else:
        print("You lose")
        no_guess = True
if no_guess == True:
    print("You are out guesses")
else:
    print("You guessed correctly")
