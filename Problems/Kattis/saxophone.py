d = {"c": [2,3,4,7,8,9,10],
     "d": [2,3,4,7,8,9],
     "e": [2,3,4,7,8],
     "f": [2,3,4,7],
     "g": [2,3,4],
     "a": [2,3],
     "b": [2],
     "C": [3],
     "D": [1,2,3,4,7,8,9],
     "E": [1,2,3,4,7,8],
     "F": [1,2,3,4,7],
     "G": [1,2,3,4],
     "A": [1,2,3],
     "B": [1,2]}
from itertools import pairwise

for _ in range(int(input())):
    
    s = input()
    if not s:
        print("0 0 0 0 0 0 0 0 0 0")
        continue
    count = [0]*11
    for x in d[s[0]]:
        count[x]+=1
    for a,b in pairwise(s):
        old = d[a]
        new = d[b]

        for x in new:
            if x not in old:
                count[x] += 1

    print(" ".join(map(str, count[1:])))



