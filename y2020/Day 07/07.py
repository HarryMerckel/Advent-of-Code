data = {}

with open("input.txt") as file:
    for line in file:
        tmp = line.strip(".\n")
        tmp = tmp.replace("bags", "")
        tmp = tmp.replace("bag", "")
        main, contents = tmp.split("contain")
        main = main.strip()
        contents = contents.strip().split(" , ")
        data[main] = contents


def traverse(bag):
    if bag == " other":
        return False
    if bag == "shiny gold":
        return True
    contents = data[bag]
    for current_bag in contents:
        if traverse(current_bag[2:]):
            return True
    return False


total = 0

for bag in data:
    if traverse(bag):
        total += 1

print(total - 1)


def count_bags(bag):
    if bag == "no other":
        return 0
    bag_count = int(bag[0])
    contents = data[bag[2:]]
    for current_bag in contents:
        bag_count += int(bag[0]) * count_bags(current_bag)
    return bag_count


print(count_bags("1 shiny gold") - 1)
