length = int(input("how large is your list with duplicates? "))
dupe = []
for i in range(length):
    dupe.append(int(input(f"enter number{i}: ")))
seen = set()
ordered = list()
for i in range(len(dupe)):
    if dupe[i] not in seen:
        ordered.append(dupe[i])
    seen.add(dupe[i])
print(ordered)
