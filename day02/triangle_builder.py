height = int(input("how tall do you want the triangle to be? "))
for i in range(1, height + 1):
	spaces = height - i
	stars = 2 * i - 1
	print(' ' * spaces + '*' * stars)