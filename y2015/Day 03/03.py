with open('input.txt') as file:
    data = file.read().strip()

grid = {}


def next_pos(cur_pos, instruction):
    try:
        grid[str(cur_pos)] += 1
    except KeyError:
        grid[str(cur_pos)] = 1
    if instruction == "^":
        return [cur_pos[0], cur_pos[1]+1]
    if instruction == "v":
        return [cur_pos[0], cur_pos[1]-1]
    if instruction == "<":
        return [cur_pos[0]-1, cur_pos[1]]
    if instruction == ">":
        return [cur_pos[0]+1, cur_pos[1]]


cur_pos = [0, 0]

for char in data:
    cur_pos = next_pos(cur_pos, char)

print(len(grid))

grid = {}

cur_pos = [[0, 0], [0, 0]]
ctr = 0

for char in data:
    if ctr % 2:
        cur_pos = [cur_pos[0], next_pos(cur_pos[1], char)]
    else:
        cur_pos = [next_pos(cur_pos[0], char), cur_pos[1]]
    ctr += 1

try:
    grid[str(cur_pos[0])] += 1
except KeyError:
    grid[str(cur_pos[0])] = 1

try:
    grid[str(cur_pos[1])] += 1
except KeyError:
    grid[str(cur_pos[1])] = 1

print(len(grid))
