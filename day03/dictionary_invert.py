num_items = int(input("How many items? "))
user_dict = {}
for i in range(num_items):
    key = input("Enter key: ")
    value = input("Enter value: ")
    user_dict[key] = value
print(f"original dictionary: {user_dict}")
reverse_dict = {}
for key, value in user_dict.items():
    if value not in reverse_dict:
        reverse_dict[value] = [key]
    else:
        reverse_dict[value].append(key)
print(f"reverse dictionary: {reverse_dict}")