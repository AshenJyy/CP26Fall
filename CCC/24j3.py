length = int(input())
arr = []

for i in range(length):
    arr.append(int(input()))

arr.sort(reverse=True)

print(arr[arr.count(max(arr)) + arr.count(arr[arr.count(max(arr))])]," ",arr.count(arr[arr.count(max(arr)) + arr.count(arr[arr.count(max(arr))])]))
