data = []

with open("input.txt") as file:
    for line in file:
        data.append(line.strip("\n"))

x = 0
y = 0
dx = 3
dy = 1

width = len(data[0])

trees = 0


def get_trees(dx, dy):
    x = 0
    y = 0
    trees = 0
    while True:
        try:
            if data[y][x % width] == '#':
                trees += 1
            x += dx
            y += dy
        except IndexError:
            print(x, y, trees)
            return trees


inputs = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
outputs = []
result = 1
for dx, dy in inputs:
    outputs.append(get_trees(dx, dy))
    result *= outputs[-1]

print(outputs, ":", result)
