import math
from functools import reduce

def lcm(arr):

    l=reduce(lambda x,y:(x*y)//math.gcd(x,y),arr)
    return l
while True:
    try:
        print(lcm(list(map(int, input().split()))))
    except EOFError:
        break
