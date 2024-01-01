import math
tests = int(input())

for _ in range(tests):
    testnum, base, num = list(map(int, input().split()))

    newnum = []

    while num != 0:
        newnum.append(num%base)
        num = math.floor(num/base)
    newnum = (newnum[::-1])
    total = 0

    for c in newnum:
        total += int(c)**2
    print(str(testnum) + " " + str(total))