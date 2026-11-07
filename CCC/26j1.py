b = int(input())
t = int(input())
p = int(input())
if t - p < b:
    print("N")
else:
    print("Y", t - p - b)

