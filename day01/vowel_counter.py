word = input("enter a word or sentence: ").upper()
yorno = input("do you want to include y? (Y or N) ").upper()
if yorno == "Y":
    test = "AEIOUY"
    counter = 0
    for character in word:
        if character in test: 
            counter+=1
    print(f"There are {counter} vowels in your word/sentence")
elif yorno == "N":
    test = "AEIOU"
    counter = 0
    for character in word:
        if test.find(character) != -1:
            counter +=1
    print(f"There are {counter} vowels in your word/sentence")
else:
    print("misinput")

