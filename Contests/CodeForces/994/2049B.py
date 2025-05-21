def solve():
    N = int(input())
    t = input()
   
    found = False
    for c in t:
        if c == "p":
            found = True
        if c == "s" and found:
            return "NO"
    
    if t.count("s") == 0 or t.count("p") == 0: return "YES"
    
    lasts = 0
    for i, c in enumerate(t):
        if c == "s":
            lasts = i
    firstp = t.index("p")
    if lasts == 0 or firstp == len(t)-1:
        return "YES"
    return "NO" 

for tc in range(int(input())):
    print(solve())