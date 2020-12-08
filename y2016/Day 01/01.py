with open("input.txt") as file:
    data = file.read().strip("\n").split(", ")

bearings = [
    [0, 1],  # N
    [1, 0],  # E
    [0, -1],  # S
    [-1, 0]  # W
]

visited = {}

bearing = 0
pos = [0, 0]

for instruction in data:
    if instruction[0] == "R":
        bearing += 1
    else:
        bearing -= 1
    bearing %= 4
    for i in range(int(instruction[1:])):
        delta = bearings[bearing]
        pos = [x + y for x, y in zip(pos, delta)]
        try:
            if visited[str(pos)] == 1:
                print(pos)
        except KeyError:
            visited[str(pos)] = 1

print(pos)
