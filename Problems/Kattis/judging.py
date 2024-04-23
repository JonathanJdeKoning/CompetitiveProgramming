from collections import Counter
numSubs = int(input())
results = dict(Counter([input() for _ in range(2*numSubs)])).values()
total = 0
for res in results:
    if res%2==1: 
        total += (res-1)//2
    else:
        total += res//2
print(total)

