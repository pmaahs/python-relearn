number = int(input("give a number to be collatz sequenced: "))
while number > 1:
    print(number)
    if number % 2 == 0:
        number //= 2
    else:
        number = number*3+1
print("1")