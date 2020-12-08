data = []

with open("input.txt") as file:
    for line in file:
        data.append(line.strip("\n").split(" "))

visited = {}

acc = 0
ptr = 0

while True:
    try:
        if visited[str(ptr)]:
            print(ptr, acc)
            break
    except KeyError:
        visited[str(ptr)] = 1

    row = data[ptr]
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

target = len(data)

jmps = []
nops = []
i = 0
for row in data:
    if row[0] == "jmp":
        jmps.append(i)
    elif row[0] == "nop":
        nops.append(i)
    i += 1

for i in jmps:
    data_mod = data.copy()
    data_mod[i] = ["nop", data_mod[i][1]]

    visited = {}

    acc = 0
    ptr = 0

    while True:
        try:
            if visited[str(ptr)]:
                break
        except KeyError:
            visited[str(ptr)] = 1

        try:
            row = data_mod[ptr]
        except IndexError:
            print(ptr, acc)
            break

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

for i in nops:
    data_mod = data.copy()
    data_mod[i] = ["jmp", data_mod[i][1]]

    visited = {}

    acc = 0
    ptr = 0

    while True:
        try:
            if visited[str(ptr)]:
                break
        except KeyError:
            visited[str(ptr)] = 1

        try:
            row = data_mod[ptr]
        except IndexError:
            print(ptr, acc)
            break

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
