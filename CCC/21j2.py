n = int(input())
winner = ""
max_bid = -1
for _ in range(n):
    name = input().strip()
    bid = int(input())
    if bid > max_bid:
        max_bid = bid
        winner = name
print(winner)

