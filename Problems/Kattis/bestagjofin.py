best = ""
mx = -1

for _ in range(int(input())):
    data = input().split()
    if int(data[1]) > mx:
        mx = int(data[1])
        best = data[0]
print(best)
