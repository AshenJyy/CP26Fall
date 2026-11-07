key = input().strip()
msg = [ch for ch in input().strip() if ch.isalpha()]
ans = ""
for i in range(len(msg)):
    shift = ord(key[i % len(key)]) - 65
    ans += chr((ord(msg[i]) - 65 + shift) % 26 + 65)
print(ans)

