data = []

with open("input.txt") as file:
    for line in file:
        data.append(int(line.strip("\n")))

preamble_len = 25


def is_valid(num, preamble):
    while len(preamble) > 2:
        cur_check = preamble.pop(0)
        for item in preamble:
            if item + cur_check == num:
                return True
    return False


def get_contiguous_group(target, data):
    total = 0
    i = 0
    while total < target:
        total += data.pop(0)
        i += 1
    if total == target:
        return i
    return False


for i in range(preamble_len, len(data)):
    if not is_valid(data[i], data[i-25:i]):
        print("p1", data[i])
        for j in range(len(data)):
            result = get_contiguous_group(data[i], data[j:])
            if result:
                print(result)
                print(data[j:j+result])
                print(min(data[j:j+result]) + max(data[j:j+result]))
