t1 = int(input())
t2 = int(input())
count = 2
while t1 >= t2:
    t1, t2 = t2, t1 - t2
    count += 1
print(count)

