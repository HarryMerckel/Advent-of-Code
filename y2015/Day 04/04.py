from hashlib import md5

input = "yzbqklnj"

num = 0

while True:
    output = md5((input + str(num)).encode())
    if output.hexdigest()[:6] == "000000":
        print(num)
        break
    num += 1
