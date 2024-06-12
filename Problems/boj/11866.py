n,k = map(int, input().split())
nums = list(range(1,n+1))
out = []
def josephus(ls, skip):
    skip -= 1 # pop automatically skips the dead guy
    idx = skip
    while len(ls) > 1:
        out.append(ls.pop(idx)) # kill prisoner at idx
        idx = (idx + skip) % len(ls)
    out.append(ls[0])

josephus(nums, k)
print(f"<{', '.join(map(str, out))}>")
