name = input("Enter your full name: ").upper().split()
initials = ""
for word in name:
    initials += word[0]
print(f"Your initials are: {initials}")