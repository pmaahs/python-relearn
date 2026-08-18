input_list = [1,2,2,3,3,3,1,6,1,5]
seen = set()
result = []
for item in input_list:
    if item not in seen:
        result.append(item)
        seen.add(item)
print(result)