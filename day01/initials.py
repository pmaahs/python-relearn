name = input("enter your name for initials: ").upper().split()
initials = ""
for word in name:
    initials += word[0]
print(initials)