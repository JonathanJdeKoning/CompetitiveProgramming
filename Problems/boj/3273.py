n = int(input())
nums = list(map(int, input().split()))
from collections import Counter
target = int(input())
freq = Counter(nums)
total = 0
used = set()
for num in nums:
    pair = target-num
    if num in used: continue
    if pair != num:
        total += freq[num]*freq[pair]
        used.add(num)
        used.add(pair)
    elif pair == num:
        count = freq[num]
        count -= 1
        total += (count*(count+1))//2
        used.add(num)
print(total)
