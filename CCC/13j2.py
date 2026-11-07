word = input().strip()
valid = True
for ch in word:
    if ch not in "IOSHZXN":
        valid = False
if valid:
    print("YES")
else:
    print("NO")

