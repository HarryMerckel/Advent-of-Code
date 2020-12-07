with open('input.txt') as file:
    data = file.read().split("\n\n")

total = 0

for group in data:
    people = group.split("\n")
    yeses = set(people[0])
    for person in people:
        yeses = yeses.intersection(set(person))
    print(group)
    print("->", yeses, len(yeses))
    total += len(yeses)

print(total)
