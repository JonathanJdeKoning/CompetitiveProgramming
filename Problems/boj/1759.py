n, k = map(int, input().split())
letters = input().split()
from itertools import combinations 
vowels = {"a","e","i","o","u"}
vs = [x for x in letters if x in vowels]
cs = [x for x in letters if x not in vowels]

out = []
import sys
perms = sorted([sorted(perm) for perm in list(combinations(letters, n))])
for perm in perms:
    if len([x for x in perm if x in vowels])==0: continue
    if len([x for x in perm if x not in vowels]) < 2: continue
    sys.stdout.write("".join(perm)+"\n")

