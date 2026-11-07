s = input()
h = s.count(":-)")
sad = s.count(":-(")
if h == 0 and sad == 0:
    print("none")
elif h == sad:
    print("unsure")
elif h > sad:
    print("happy")
else:
    print("sad")

