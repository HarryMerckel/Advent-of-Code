with open('input.txt') as file:
    data = file.read().split("\n\n")

required_keys = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}  # not 'cid'

valid = 0

for entry in data:
    passport_raw = entry.replace("\n", " ").split(" ")
    passport = dict()
    for field in passport_raw:
        key, value = field.split(":")
        passport[key] = value

    if required_keys.issubset(set(passport.keys())):
        print(passport['hcl'], set(passport['hcl'][1:]).issubset(
            {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'}))
        if 1920 <= int(passport['byr']) <= 2002 \
                and 2010 <= int(passport['iyr']) <= 2020 \
                and 2020 <= int(passport['eyr']) <= 2030 \
                and passport['hgt'][-2:] in ["cm", "in"] \
                and (150 <= int(passport['hgt'][0:-2]) <= 193 if passport['hgt'][-2:] == "cm" else 59 <= int(
            passport['hgt'][0:-2]) <= 76) \
                and passport['hcl'][0] == '#' \
                and len(passport['hcl']) == 7 \
                and set(passport['hcl'][1:]).issubset(
            {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'}) \
                and len(passport['pid']) == 9 \
                and set(passport['pid']).issubset({'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}) \
                and passport['ecl'] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"] \
                :
            valid += 1

print(valid)
