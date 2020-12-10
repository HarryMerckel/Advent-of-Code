data = []

with open("input.txt") as file:
    for line in file:
        data.append(int(line.strip("\n")))

data = sorted(data)

gaps = {1: 1, 3: 1}

for i in range(len(data)-1):
    diff = data[i+1]-data[i]
    gaps[diff] += 1

print(gaps[1]*gaps[3])

combinations = {0: 1}
for number in data:

    combinations[number] = combinations.get(number-3, 0) + combinations.get(number-2, 0) + combinations.get(number-1, 0)

print(combinations[max(data)])
