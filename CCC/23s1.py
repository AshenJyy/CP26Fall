c = int(input())
r1 = list(map(int, input().split()))
r2 = list(map(int, input().split()))
ans = (r1.count(1) + r2.count(1)) * 3
for i in range(c):
    if i < c - 1:
        if r1[i] and r1[i + 1]:
            ans -= 2
        if r2[i] and r2[i + 1]:
            ans -= 2
    if i % 2 == 0 and r1[i] and r2[i]:
        ans -= 2
print(ans)

