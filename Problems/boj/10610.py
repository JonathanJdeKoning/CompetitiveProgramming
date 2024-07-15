def solve(s):
    if "0" not in s: return -1 
    if sum([int(x) for x in s])%3!=0: return -1
    return "".join(sorted(s, reverse=True))


print(solve(input()))
