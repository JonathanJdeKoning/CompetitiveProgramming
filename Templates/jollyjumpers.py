from itertools import pairwise

while True:
    try:
        A=list(map(int,input().split()))[1:]
    except EOFError: break

    diffs=[abs(a-b)for a,b in pairwise(A)]
    
    print("Jolly") if sorted(diffs)==list(range(1,len(diffs)+1)) else print("Not jolly")
