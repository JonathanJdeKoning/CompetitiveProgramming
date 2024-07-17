n, m = map(int, input().split())
from itertools import combinations_with_replacement 
perms = list(combinations_with_replacement(sorted(list(map(int, input().split()))), m))
import sys
for perm in sorted(set(perms)):
    sys.stdout.write(" ".join(map(str,perm))+"\n")
