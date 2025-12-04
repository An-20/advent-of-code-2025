with open("input.txt") as file:
    rows = [x.strip() for x in file.read().splitlines() if x.strip()]


count = 0
dial = 50
for row in rows:
    d = row[0]
    n = int(row[1:])
    od = dial
    if d == "L":
        dial -= n
    else:
        dial += n
    if dial >= 100:
        count += dial // 100
    elif dial <= 0:
        count += abs(dial // 100)
        if dial % 100 == 0:
            count += 1
        if od == 0:
            count -= 1
    dial %= 100

print(count)
