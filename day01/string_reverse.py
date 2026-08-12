word = input("Enter a word to reverse: ")
reverse_word = ""
counter = 0
while counter < len(word):
    reverse_word += word[-1-counter]
    counter+=1
print(reverse_word)