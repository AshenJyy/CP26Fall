n = int(input())
t = s = 0
for _ in range(n):
    line = input().lower()
    t += line.count("t")
    s += line.count("s")
print("English" if t > s else "French")

