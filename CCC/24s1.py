n = int(input())
h = []
for _ in range(n):
    h.append(int(input()))
ans = 0
for i in range(n):
    if h[i] == h[(i + n // 2) % n]:
        ans += 1
print(ans)

