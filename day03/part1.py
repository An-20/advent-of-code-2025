with open("input.txt") as file:
    rows = [x.strip() for x in file.read().splitlines() if x.strip()]


s = 0
for row in rows:
    a = 0
    b = 0
    for i, char in enumerate(row):
        x = int(char)
        if x > a and i < len(row) - 1:
            a = x
            b = 0
        elif x > b:
            b = x
    s += 10 * a + b


print(s)
