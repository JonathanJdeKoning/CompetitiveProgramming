from functools import cmp_to_key
def mysort(a,b):
    if a.startswith(b):
        return 1
    if b.startswith(a):
        return -1
    
    for A,B in zip(a,b):
        if A==B: continue
        if A == "-":
            return 1
        if B == "-":
            return -1
        if A.lower() != B.lower():
            if A.lower() < B.lower():
                return - 1
            return 1
        if A == A.upper():
            return -1
        return 1
    

for _ in range(int(input())):
    N = int(input())
    words = [input() for _ in range(N)]
    print("\n".join(sorted(words, key=mysort)))
