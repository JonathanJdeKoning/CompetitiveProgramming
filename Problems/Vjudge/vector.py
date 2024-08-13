arr = []
for _ in range(int(input())):
    data = input().split()
    if data[0] == "2":
        arr.pop()
    elif data[0] == "1":
        print(arr[int(data[1])])
    else:
        arr.append(data[1])
