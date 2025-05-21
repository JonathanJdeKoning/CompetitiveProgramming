from collections import defaultdict
from itertools import accumulate
N = int(input())
class1 = [0]*(N)
class2 = [0]*(N)
for i in range(N):
    clss, score = list(map(int, input().replace(","," ").split()))
    if clss == 1:
        class1[i] = score
    else:
        class2[i] = score

pref1 = list(accumulate(class1, initial=0))
pref2 = list(accumulate(class2, initial=0))
#print(pref1)
#print(pref2)

M = int(input())

for _ in range(M):
    l, r = list(map(int, input().replace(","," ").split()))
    l -= 1
    r -= 1
    print(pref1[r+1] - pref1[l], pref2[r+1] - pref2[l])   




