n = int(input())
a = []
for _ in range(n):
    t, x = map(int, input().split())
    a.append((t, x))
a.sort()
m = 0
for i in range(n - 1):
    s = abs(a[i + 1][1] - a[i][1]) / (a[i + 1][0] - a[i][0])
    if s > m:
        m = s
print(m)

