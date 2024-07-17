n = int(input())
nums = list(map(int, input().split()))
from collections import Counter 
freq = Counter(nums)
inst = []
start = {}
stack = []
for i , c in enumerate(nums):
    if c not in start:
        start[c]= i+1
        stack.append(c)

    freq[c] -= 1
    if freq[c] == 0:
        x = stack.pop()
        if x != c:  print("IMPOSSIBLE");break

        inst.append((start[c], i+1, c))
else:
    print(len(inst))
    for row in inst[::-1]:
        print(" ".join(map(str, row)))

