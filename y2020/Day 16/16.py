rules = []
mine = []
nearby = []

with open('input.txt') as file:
    raw_rules, raw_mine, raw_nearby = file.read().split("\n\n")
    raw_rules = raw_rules.split("\n")[1:]
    raw_mine = raw_mine.split("\n")[1:]
    raw_nearby = raw_nearby.split("\n")[1:]
    for rule in raw_rules:
        name, remainder = rule.split(":")
        range1, range2 = remainder.strip().split(" or ")
        range1 = [int(x) for x in range1.split("-")]
        range2 = [int(x) for x in range2.split("-")]
        rules.append([name, range1, range2])
    mine = [int(x) for x in raw_mine[0].split(",")]
    for n in raw_nearby:
        nearby.append([int(x) for x in n.split(",")])


print(rules)
print(mine)
print(nearby)

error_rate = 0

for ticket in nearby:
    for field in ticket:
        valid = False
        for name, range1, range2 in rules:
            if range1[0] <= field <= range1[1] or range2[0] <= field <= range2[1]:
                valid = True
                break
        if not valid:
            error_rate += field

print(error_rate)
