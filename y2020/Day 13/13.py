from math import lcm

data = []

with open('input.txt') as file:
    for line in file:
        data.append(line.strip('\n'))

start = int(data[0])
buses = data[1].split(",")

waits = []

for bus in buses:
    if bus == "x":
        continue
    bus_id = int(bus)
    next_bus = start - (start % bus_id) + bus_id
    print(start, bus_id, next_bus - start, bus_id * (next_bus - start))

step = 1
t = 0

for i in range(len(buses)):
    if buses[i] == 'x':
        continue  # Important - just increases i though
    while (t + i) % int(buses[i]) != 0:  # i is also the number of minutes delay after the first bus (0) that you need
        t += step  # t + n * step is always valid for previous buses, so just increase n until valid for the current bus
    step = lcm(step, int(buses[i]))  # Lowest common multiple is actually just step * bus ID because all IDs are prime

print(t)
