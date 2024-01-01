all = []
with open("input.txt", "r") as file:
    lines = file.readlines()
    
    maxi = 0
    
    sum = 0
    for line in lines:
        if line != "\n":
            sum += int(line.strip())
        else:
            all.append(sum)
            sum = 0

all= sorted(all)
print(all)
print(all[-1]+all[-2]+all[-3])

