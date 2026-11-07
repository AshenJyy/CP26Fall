coldest = ""
min_temp = 200
while True:
    city, temp = input().split()
    temp = int(temp)
    if temp < min_temp:
        min_temp = temp
        coldest = city
    if city == "Waterloo":
        break
print(coldest)

