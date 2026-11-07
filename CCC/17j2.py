n = int(input())
k = int(input())
ans = n
for _ in range(k):
    n *= 10
    ans += n
print(ans)

