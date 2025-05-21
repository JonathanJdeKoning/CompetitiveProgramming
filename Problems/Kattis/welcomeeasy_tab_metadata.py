from functools import cache

x = "welcome to code jam"
out = []
for tc in range(int(input())):
    s = input()
    @cache
    def ways_using_x(s_idx, x_idx):
        if x_idx == len(x) - 1: return 1
        w = []
        look = x[x_idx+1]
        for i in range(s_idx+1, len(s)):
            if s[i] == look:
                w.append(ways_using_x(i, x_idx+1))
        w = [d for d in w if d]
        if not w: return 0
        return sum(w) 
    poss = []
    for i, c in enumerate(s):
        if c == "w":
            poss.append(ways_using_x(i,0))
    out.append(sum(poss))
for i in range(1 , len(out) + 1):
    print(f"Case #{i}: {str(out[i-1]%10000).zfill(4)}")