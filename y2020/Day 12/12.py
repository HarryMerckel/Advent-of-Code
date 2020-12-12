data = []

with open('input.txt') as file:
    for line in file:
        data.append(line.strip('\n'))

print(data)

directions = [
    [0, 1],  # N
    [1, 0],  # E
    [0, -1],  # S
    [-1, 0]  # W
]

orientation = 1
position = [0, 0]

for instruction in data:
    key = instruction[0]
    value = int(instruction[1:])
    if key == "N":
        position = [sum(x) for x in zip(position, [y * value for y in directions[0]])]
    elif key == "E":
        position = [sum(x) for x in zip(position, [y * value for y in directions[1]])]
    elif key == "S":
        position = [sum(x) for x in zip(position, [y * value for y in directions[2]])]
    elif key == "W":
        position = [sum(x) for x in zip(position, [y * value for y in directions[3]])]
    elif key == "F":
        position = [sum(x) for x in zip(position, [y * value for y in directions[orientation]])]
    elif key == "R":
        orientation += value // 90
        orientation %= 4
    elif key == "L":
        orientation -= value // 90
        orientation %= 4

print(position, abs(position[0]) + abs(position[1]))


def rotate(coords, angle):
    x, y = coords
    if angle == 90:
        return y, -x
    if angle == 180:
        return -x, -y
    if angle == 270:
        return -y, x
    else:
        return x, y


position = [0, 0]
waypoint = [10, 1]

for instruction in data:
    key = instruction[0]
    value = int(instruction[1:])
    if key == "N":
        waypoint = [sum(x) for x in zip(waypoint, [y * value for y in directions[0]])]
    elif key == "E":
        waypoint = [sum(x) for x in zip(waypoint, [y * value for y in directions[1]])]
    elif key == "S":
        waypoint = [sum(x) for x in zip(waypoint, [y * value for y in directions[2]])]
    elif key == "W":
        waypoint = [sum(x) for x in zip(waypoint, [y * value for y in directions[3]])]
    elif key == "F":
        position = [sum(x) for x in zip(position, [y * value for y in waypoint])]
    elif key == "R":
        waypoint = rotate(waypoint, value)
    elif key == "L":
        waypoint = rotate(waypoint, 360 - value)
    print(instruction, waypoint, position)

print(position, abs(position[0]) + abs(position[1]))
