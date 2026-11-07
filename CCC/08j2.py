p = ["A", "B", "C", "D", "E"]
while True:
    b = int(input())
    n = int(input())
    for _ in range(n):
        if b == 1:
            p = p[1:] + [p[0]]
        elif b == 2:
            p = [p[-1]] + p[:-1]
        elif b == 3:
            p[0], p[1] = p[1], p[0]
    if b == 4:
        print(" ".join(p))
        break

