direction = input("Which direction would you like to convert? Type 'C' for Celsius to Fahrenheit or 'F' for Fahrenheit to Celsius: ").upper()
if direction == 'C':
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = celsius * 9/5 + 32
    print(f"Temperature in Fahrenheit: {fahrenheit}")
elif direction == 'F':
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"Temperature in Celsius: {celsius}")
else:
    print("Invalid input. Please enter 'C' or 'F'.")