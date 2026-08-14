import random

secret_number = random.randint(1, 100)
guesses = 1
guessing = True
while guessing:
    try:
        guess = int(input("Guess a number from 1 to 100: "))
    except ValueError:
        print("input error try again")
        continue
    if guess == secret_number:
        print(f"you got it in {guesses} tries!")
        guessing = False
    elif guess > secret_number:
        print("too high!")
        guesses+=1
    elif guess < secret_number:
        print("too low!")
        guesses+=1

