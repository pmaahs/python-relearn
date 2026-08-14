count = int(input("how many words? "))
dupe = []
output = {}
for i in range(count):
    dupe.append(input(f"enter word {i+1}: "))
for word in dupe:
    if word[0] in output:
        output[word[0]].append(word)
    else:
        output[word[0]] = [word]
print(output)