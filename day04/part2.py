with open("input.txt") as file:
    rows = [list(x.strip()) for x in file.read().splitlines() if x.strip()]


t = 0
prev = -1

while True:
    for y, row in enumerate(rows):
        for x, char in enumerate(row):
            if char != "@":
                continue
            n = 0
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if dx == dy == 0:
                        continue
                    if x + dx not in range(len(row)):
                        continue
                    if y + dy not in range(len(rows)):
                        continue
                    if rows[y + dy][x + dx] == "@":
                        n += 1
            if n < 4:
                t += 1
                row[x] = "."
    if t == prev:
        break
    prev = t

print(t)
