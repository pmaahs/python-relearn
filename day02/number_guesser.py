import random

secret_number = random.randint(1, 101)
guessing = True
guesses = 1
while guessing:
    try:
        guess = int(input("Guess a number between 1 and 100"))
    except ValueError:
        print("Misinput, try again!")
        continue
    if guess == secret_number:
        print(f"you got it in {guesses} tries! ")
    elif guess>secret_number:
        print("too high! ")
        guesses+=1
    elif guess<secret_number:
        print("too low! ")
        guesses+=1

