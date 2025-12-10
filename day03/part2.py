with open("input.txt") as file:
    rows = [x.strip() for x in file.read().splitlines() if x.strip()]


s = 0
for row in rows:
    l = [0 for _ in range(12)]
    for i, char in enumerate(row):
        x = int(char)
        for j in range(12):
            if x > l[j] and i < len(row) - 11 + j:
                l[j] = x
                for k in range(j+1, 12):
                    l[k] = 0
                break
    n = 0
    for i in range(12):
        n += l[-i-1] * 10**i
    s += n


print(s)
