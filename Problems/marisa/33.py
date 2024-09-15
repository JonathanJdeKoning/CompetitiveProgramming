from functools import cache
from itertools import pairwise, groupby
from math import ceil, floor, sqrt
from collections import deque, defaultdict, Counter

def debug(val, name): print(f"#{val}# DEBUG{{{name}}}")
def inInts(): return list(map(int, input().split()))
def outInts(A): print(" ".join(map(str, A)))


N = int(input())
A = list(map(lambda x: x>0, inInts())) 

print(max((len(list(v)) for k,v in groupby(A) if k), default=0))
      

