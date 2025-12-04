with open("input.txt") as file:
    rows = [x.strip() for x in file.read().splitlines() if x.strip()]


count = 0
dial = 50
for row in rows:
    d = row[0]
    n = int(row[1:])
    if d == "L":
        dial -= n
    else:
        dial += n
    dial %= 100
    if dial == 0:
        count += 1

print(count)
