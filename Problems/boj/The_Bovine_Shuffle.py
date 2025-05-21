from copy import copy
N = int(input()) 
shuff = list(map(int, input().replace(","," ").split()))
cows = input().split()
orig = copy(cows)


new = [None]*N
for i,c in enumerate(cows):
    curr = i
    for _ in range(3):
        spot = curr+1
        mover = shuff.index(spot)+1
        curr = mover-1
    new[curr] = c

print("\n".join(map(str, new )))
