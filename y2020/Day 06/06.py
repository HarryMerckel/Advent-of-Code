with open('input.txt') as file:
    data = file.read().split("\n\n")

total = 0

for group in data:
    people = group.split("\n")
    yeses = set(people[0])
    for person in people:
        yeses = yeses.union(set(person))
    total += len(yeses)

print(total)

total = 0

for group in data:
    people = group.split("\n")
    yeses = set(people[0])
    for person in people:
        yeses = yeses.intersection(set(person))
    total += len(yeses)

print(total)
