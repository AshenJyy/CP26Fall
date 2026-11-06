rounds = int(input())
antonia = 100
david = 100

for i in range(rounds):
    dice_1, dice_2 = map(int, input().split())
    if dice_1 > dice_2:
        david -= dice_1
    elif dice_2 > dice_1:
        antonia -= dice_2
print(antonia)
print(david)
