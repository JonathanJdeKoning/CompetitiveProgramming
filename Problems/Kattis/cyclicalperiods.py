from collections import defaultdict
from math import gcd
pos = defaultdict(list)
length = int(input())
order = []
for _ in range(length):
    num, letters = input().split()
    num = int(num)

    for letter in letters:
        pos[letter].append(num)
print(pos)


