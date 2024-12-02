N = int(input())
from collections import Counter
fq = Counter(list(map(int, input().split())))
print(fq[int(input())])