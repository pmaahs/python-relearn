number = int(input("enter a number to see if it's prime: "))
for i in range(2, number-1):
    if number % i == 0:
        print("not prime")
        break
else:
    print("prime")