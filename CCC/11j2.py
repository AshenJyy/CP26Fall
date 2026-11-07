h = int(input())
m = int(input())
touched = False
for t in range(1, m + 1):
    a = -6 * (t ** 4) + h * (t ** 3) + 2 * (t ** 2) + t
    if a <= 0:
        print("The balloon first touches the ground at hour:")
        print(t)
        touched = True
        break
if not touched:
    print("The balloon does not touch the ground in the given time period.")

