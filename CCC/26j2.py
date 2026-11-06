s = []
for i in range(5):
    s.append(int(input()))
d = int(input())

s.sort()
ans = (s[1] + s[2] + s[3]) * d
print(ans)
