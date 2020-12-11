data = []

with open('input.txt') as file:
    for line in file:
        data.append(list(line.strip('\n')))


def get_occupied_neighbours(input_data, x, y, p2):
    occupied = 0
    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            if i == 0 and j == 0:
                continue
            if p2:
                n = 1
                while (n * i) + x in range(len(input_data)) and (n * j) + y in range(len(input_data[0])):
                    if input_data[(n * i) + x][(n * j) + y] == '.':
                        n += 1
                        continue
                    else:
                        if input_data[(n * i) + x][(n * j) + y] == '#':
                            occupied += 1
                    break
            else:
                if i + x in range(len(input_data)) and j + y in range(len(input_data[0])):
                    if input_data[i + x][j + y] == '#':
                        occupied += 1
    return occupied


def iterate(input_data, p2):
    output_data = [['' for j in range(len(input_data[0]))] for i in range(len(input_data))]
    occupied_seats = 0
    for i in range(len(input_data)):
        for j in range(len(input_data[0])):
            occupied_neighbours = get_occupied_neighbours(input_data, i, j, p2)
            if input_data[i][j] == 'L':
                if occupied_neighbours == 0:
                    output_data[i][j] = '#'
                else:
                    output_data[i][j] = 'L'
            elif input_data[i][j] == '#':
                if occupied_neighbours >= 5:
                    output_data[i][j] = 'L'
                else:
                    output_data[i][j] = '#'
            else:
                output_data[i][j] = input_data[i][j]
            if output_data[i][j] == '#':
                occupied_seats += 1
    return output_data


prev_data = data
iterations = 0

while True:
    cur_data = iterate(prev_data, False)
    # for row in cur_data:
    #     for col in row:
    #         print(col, end='')
    #     print()
    # print()
    if cur_data == prev_data:
        print(iterations, "iterations")
        print(sum(cur_data, []).count("#"), "occupied")
        break
    prev_data = cur_data
    iterations += 1

prev_data = data
iterations = 0

while True:
    cur_data = iterate(prev_data, True)
    # print(get_occupied_neighbours(cur_data, 0, 3, True))
    # for row in cur_data:
    #     for col in row:
    #         print(col, end='')
    #     print()
    # print()
    # for i in range(len(cur_data)):
    #     for j in range(len(cur_data[0])):
    #         print(get_occupied_neighbours(cur_data, i, j, True), end='')
    #     print()
    # print()
    if cur_data == prev_data:
        print(iterations, "iterations")
        print(sum(cur_data, []).count("#"), "occupied")
        break
    prev_data = cur_data
    iterations += 1
