import operator

data = []

with open("input.txt") as file:
    for line in file:
        data.append(line.strip("\n"))

valid = 0

for row in data:
    policy, password = row.split(":")
    password = password.strip(" ")
    nums, character = policy.split(" ")
    minimum, maximum = nums.split("-")
    valid += 1 if int(minimum) <= password.count(character) <= int(maximum) else 0

print(valid)

valid = 0

for row in data:
    policy, password = row.split(":")
    password = password.strip(" ")
    nums, character = policy.split(" ")
    pos1, pos2 = nums.split("-")
    try:
        pos1valid = (password[int(pos1) - 1] == character)
    except IndexError:
        pos1valid = False
    try:
        pos2valid = (password[int(pos2) - 1] == character)
    except IndexError:
        pos2valid = False
    if operator.xor(pos1valid, pos2valid):
        valid += 1

print(valid)
