data = [9, 6, 0, 10, 18, 2, 1]

numbers = {}
prev_num = 0

for i in range(30000000):
    if i < len(data):
        num = data[i]
    else:
        if prev_num in numbers:
            num = i - 1 - numbers[prev_num]
        else:
            num = 0
    numbers[prev_num] = i - 1
    prev_num = num
    # print(num)

print(num)
