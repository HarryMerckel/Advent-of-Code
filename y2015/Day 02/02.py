data = []

with open('input.txt') as file:
    for line in file:
        x, y, z = line.strip("\n").split("x")
        data.append([int(x), int(y), int(z)])

area = 0

for present in data:
    side1 = present[0] * present[1]
    side2 = present[1] * present[2]
    side3 = present[2] * present[0]
    area += 2 * side1 + 2 * side2 + 2 * side3 + min(side1, side2, side3)

print(area)

ribbon = 0

for present in data:
    ribbon += 2 * min(present) + 2 * sorted(present)[1] + present[0] * present[1] * present[2]

print(ribbon)