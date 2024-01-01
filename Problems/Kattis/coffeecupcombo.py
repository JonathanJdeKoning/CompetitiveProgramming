coffeeleft = 0

length = int(input())

total = 0

for c in input():
    if c == "1":
        total += 1
        coffeeleft = 2
    if c == "0":
        if coffeeleft >0:
            total += 1
            coffeeleft -=1
        else:
            continue
print(total)
