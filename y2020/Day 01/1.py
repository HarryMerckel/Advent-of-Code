data = []

with open('input.txt') as file:
    for line in file:
        data.append(line.strip("\n"))

print(data)

for item in data:
    target = 2020 - int(item)
    if str(target) in data:
        print(item, "*", target, "=", int(item) * target)

for item1 in data:
    target1 = 2020 - int(item1)
    for item2 in data:
        target2 = target1 - int(item2)
        if str(target2) in data:
            print(f"{item1} * {item2} * {target2} = {int(item1) * int(item2) * target2}")
