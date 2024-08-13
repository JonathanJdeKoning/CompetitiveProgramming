from itertools import pairwise
def solve():
    s = input()
    for i, (a,b) in enumerate(pairwise(s)):
        if a == b:
            if a != "a":
                return(s[:i+1]+"a"+s[i+1:])
            return(s[:i+1]+"b"+s[i+1:])
    
    if s[0] != "a":
        return "a"+s 
    return "b"+s


for i in range(int(input())):
    print(solve())
