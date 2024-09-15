from collections import Counter
n = int(input())
nums = list(map(int, input().split()))

fq = Counter(nums)
d = {}

a = 0
for k,v in sorted(fq.items(), reverse=True):
    d[k] = a
    a+= v

print(" ".join(map(str, list(map(lambda x: d[x]+1, nums)))))
