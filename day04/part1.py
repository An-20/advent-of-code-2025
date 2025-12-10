with open("input.txt") as file:
    rows = [x.strip() for x in file.read().splitlines() if x.strip()]


s = 0

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
            s += 1

print(s)
