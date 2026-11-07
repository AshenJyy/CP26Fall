n = int(input())
y = input().strip()
t = input().strip()
ans = 0
for i in range(n):
    if y[i] == "C" and t[i] == "C":
        ans += 1
print(ans)

