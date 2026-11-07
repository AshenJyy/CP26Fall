k = int(input())
s = input().strip()
ans = ""
for i in range(len(s)):
    shift = 3 * (i + 1) + k
    ans += chr((ord(s[i]) - 65 - shift) % 26 + 65)
print(ans)

