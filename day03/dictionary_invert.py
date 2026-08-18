user_dict = {1: "apple", 2:"banana", 3:"grape"}
print(f"original dictionary: {user_dict}")
reverse_dict = {}
for key, value in user_dict.items():
    if value not in reverse_dict:
        reverse_dict[value] = [key]
    else:
        reverse_dict[value].append(key)
print(f"reverse dictionary: {reverse_dict}")