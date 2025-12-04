import math

with open("input.txt") as file:
    rows = [x.strip() for x in file.read().splitlines() if x.strip()]
ranges = rows[0].split(",")


s = 0
for r in ranges:
    lower, upper = r.split("-")
    n = math.floor(len(lower) / 2)
    if n == 0:
        left = 1
    else:
        left = int(lower[:n])
    lower = int(lower)
    upper = int(upper)
    while True:
        new = int(str(left) + str(left))
        if new > upper:
            break
        if new >= lower:
            s += new
        left += 1

print(s)
