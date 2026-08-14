numbers = [2, 7, 11, 15]
target = 9
answer = []
storage = set(numbers)
for number in numbers:
    check = target - number
    if check in storage:
        print([check, number])
        break