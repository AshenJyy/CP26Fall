d = int(input())
e = int(input())
for _ in range(e):
    op = input().strip()
    q = int(input())
    if op == "+":
        d += q
    else:
        d -= q
print(d)

