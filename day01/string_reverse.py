word = input("Enter a word to reverse: ")
reverse_word = ""
for i in range(len(word)):
    reverse_word += word[-1-i]
print(reverse_word)