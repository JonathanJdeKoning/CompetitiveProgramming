from itertools import permutations
a = [0,1,2,3,4,5,6,7,8,9]
c = 0
for perm in permutations(a):
    c += 1
    if c == 1000000:
        print(perm)
        break