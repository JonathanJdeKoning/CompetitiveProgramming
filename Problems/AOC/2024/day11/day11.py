from collections import Counter
data = list(map(int, open("day11.in", "r").readlines()[0].strip().split()))
blinks = 75
stones = Counter(data)

def get_stone(n):
    if n == 0: return [1]
    s = str(n)
    m = len(s)//2
    return [2024*n] if len(s)%2 == 1 else [int(s[:m]), int(s[m:])]
    
for i in range(1,blinks+1):
    new = Counter()
    for stone, fq in stones.items():
        for s in get_stone(stone):
            new[s] += fq
    stones = new

    if i==25: print(sum(stones.values()))

print(sum(stones.values()))
