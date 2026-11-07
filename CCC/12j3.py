k = int(input())
for row in ["*x*", " xx", "* *"]:
    line = "".join(ch * k for ch in row)
    for _ in range(k):
        print(line)

