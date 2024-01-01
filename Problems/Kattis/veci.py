from itertools import permutations
num = input()

perms = [''.join(p) for p in permutations(num)]

perms = sorted(list(set([int(x) for x in perms])))
try:
    print(perms[perms.index(int(num))+1])
except:
    print(0)
