with open('input.txt') as file:
    data = file.read().strip()

floor = 0
count = 0

for move in data:
    if floor == -1:
        print(count)
    count += 1
    if move == '(':
        floor += 1
    else:
        floor -= 1

print(floor)
