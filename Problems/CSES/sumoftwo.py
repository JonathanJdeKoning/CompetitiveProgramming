from collections import defaultdict
arrsize, target = list(map(int, input().split()))
nums = list(map(int, input().split()))
def solve():
    d = defaultdict(list)
    for i, num in enumerate(nums):
        d[num].append(i)
        if target-num in d:
            poss = [x for x in d[target-num] if x != i]
            if not poss: continue
            return [str(i+1),str(poss[0]+1)]
    return["IMPOSSIBLE"]
print(" ".join(solve()))
