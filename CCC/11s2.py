n = int(input())

a = []
for i in range(n):
    a.append(input().strip())

ans = 0
for i in range(n):
    b = input().strip()
    if a[i] == b:
        ans += 1

print(ans)
