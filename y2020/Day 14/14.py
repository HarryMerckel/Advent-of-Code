data = []

with open('input.txt') as file:
    for line in file:
        data.append(line.strip('\n').replace(" ", "").split('='))

mem = {}
mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"  # Could be empty, it gets overwritten straight away

for instruction in data:
    if instruction[0] == 'mask':
        mask = instruction[1]
    else:
        addr = int(instruction[0][4:-1])
        value = int(instruction[1])
        value |= int(mask.replace("X", "0"), 2)  # Boolean OR forces 1s in mask to overwrite
        value &= int(mask.replace("X", "1"), 2)  # Boolean AND forces 0s in mask to overwrite
        mem[addr] = value

print(sum(mem.values()))


def get_masks(mask):
    if not mask:
        yield ''
        return
    else:
        for submask in get_masks(mask[1:]):  # Work your way down the mask
            if mask[0] == "X":  # X -> 'floating', so force both 1 and 0 as separate masks
                yield f"0{submask}"
                yield f"1{submask}"
            elif mask[0] == "1":  # 1 -> force 1 (as in previous part)
                yield f"1{submask}"
            elif mask[0] == "0":  # 0 -> no change (as X did in previous part)
                yield f"X{submask}"


mem2 = {}
mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

for instruction in data:
    if instruction[0] == 'mask':
        mask = instruction[1]
    else:
        value = int(instruction[1])
        for submask in get_masks(mask):  # Basically do part 1 on the address, not the value, for all masks generated
            subaddr = int(instruction[0][4:-1])
            subaddr |= int(submask.replace("X", "0"), 2)
            subaddr &= int(submask.replace("X", "1"), 2)
            mem2[subaddr] = value

print(sum(mem2.values()))
