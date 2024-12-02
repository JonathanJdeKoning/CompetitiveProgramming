with open("day2.in", "r") as file:
    ans1 = 0
    ans2 = 0
    for line in file.readlines():
        data = line.strip().split()
        start, end = map(int, data[0].split("-"))
        passw = data[-1]
        char = data[1][0]

        if passw.count(char) >= start and passw.count(char) <= end:
            ans1 += 1
        idxs = [passw[start-1], passw[end-1]]
        if idxs.count(char) == 1:
            ans2+=1
        
print(ans1)
print(ans2)