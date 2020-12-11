from hashlib import md5
import time

data = "yzbqklnj"

num = 0

t1 = time.time()

while True:
    output = md5((data + str(num)).encode())
    if output.hexdigest()[:6] == "000000":
        print(num)
        break
    num += 1

print(time.time()-t1)

# V2 optimisation

num = 0

t2 = time.time()

while True:
    output = md5(f"{data}{num}".encode())
    if output.digest()[:3] == b'\x00\x00\x00':
        print(num)
        break
    num += 1

print(time.time()-t2)
