from math import ceil
for _ in range(int(input())):
    n = int(input())
    if n == 1:
        print(2)
        continue
    print(ceil(n/3))
