x, y = list(map(int, input().split()))

mylist = list(range(x,y+1))

count = 0

for num in mylist:
    bad = False

    num = str(num)
    
    if "0" in num:
        continue
    numlist = [int(x) for x in num]
    if len(numlist) != len(set(numlist)):
        continue
    for c in num:
        if int(num) % int(c) != 0:
            bad = True
    if bad:
        continue
    count += 1
print(count)