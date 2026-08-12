word = input("Enter a word or phrase to check if it is a palindrome: ").upper().replace(" ", '')
if word == word[::-1]:
    print("word is a palindrome")
else:
    print("word is not a palindrome")
