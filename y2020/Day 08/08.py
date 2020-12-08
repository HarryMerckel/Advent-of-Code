data = []

with open("input.txt") as file:
    for line in file:
        data.append(line.strip("\n").split(" "))


def run(program):
    visited = {}

    acc = 0
    ptr = 0

    while True:
        try:
            if visited[str(ptr)]:
                return (ptr, acc)
        except KeyError:
            visited[str(ptr)] = 1

        try:
            row = program[ptr]
        except IndexError:
            return (ptr, acc)

        if row[0] == "acc":
            if row[1][0] == "+":
                acc += int(row[1][1:])
            else:
                acc -= int(row[1][1:])
            ptr += 1

        elif row[0] == "jmp":
            if row[1][0] == "+":
                ptr += int(row[1][1:])
            else:
                ptr -= int(row[1][1:])

        else:
            ptr += 1


print(run(data))

i = 0
for row in data:
    if row[0] == "jmp":
        data_mod = data.copy()
        data_mod[i] = ["nop", data_mod[i][1]]

        ptr, acc = run(data_mod)

        if ptr == len(data):
            print(ptr, acc)
    elif row[0] == "nop":
        data_mod = data.copy()
        data_mod[i] = ["jmp", data_mod[i][1]]

        ptr, acc = run(data_mod)

        if ptr == len(data):
            print(ptr, acc)
    i += 1
