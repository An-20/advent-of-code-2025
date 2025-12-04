import math

with open("input.txt") as file:
    rows = [x.strip() for x in file.read().splitlines() if x.strip()]
ranges = rows[0].split(",")


s = set()
for r in ranges:
    lowers, uppers = r.split("-")
    lower = int(lowers)
    upper = int(uppers)
    for k in range(2, len(uppers) + 1):
        n = math.ceil(len(lowers) / k)
        if n == 0:
            continue
        left = 1
        while True:
            new = int("".join(str(left) for _ in range(k)))
            if new > upper:
                break
            if new >= lower:
                s.add(new)
            left += 1

print(sum(s))
