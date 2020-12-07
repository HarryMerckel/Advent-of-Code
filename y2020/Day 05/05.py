data = []

with open("input.txt") as file:
    for line in file:
        data.append(line.strip("\n"))


def decode_row(sequence):
    binary = sequence.replace("F", "0").replace("B", "1")
    return int(binary, 2)


def decode_col(sequence):
    binary = sequence.replace("L", "0").replace("R", "1")
    return int(binary, 2)


seat_ids = []

for boarding_pass in data:
    row = decode_row(boarding_pass[:7])
    col = decode_col(boarding_pass[-3:])
    seat_id = row * 8 + col
    print(f"{boarding_pass}: row {row}, column {col}, seat ID {seat_id}.")
    seat_ids.append(seat_id)

print(min(seat_ids), max(seat_ids))

seat_id = set(range(min(seat_ids), max(seat_ids))) - set(seat_ids)
print(seat_id)
