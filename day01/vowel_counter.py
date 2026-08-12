question = input("Enter a word or sentence to find the number of vowels: ")
question2 = input("do you want to include y as a vowel? (y/n): ").upper()
if question2 == "Y":
    counter = 0
    for letter in question:
          if "aeiouy".find(letter.lower()) != -1:
              counter += 1
    print(f"There are {counter} vowels in your word or sentence")
elif question2 == "N":
    counter = 0
    for letter in question:
        if "aeiou".find(letter.lower()) != -1:
            counter += 1
    print(f"There are {counter} vowels in your word or sentence")
else:
    print("Invalid input. Please enter 'y' or 'n'.")