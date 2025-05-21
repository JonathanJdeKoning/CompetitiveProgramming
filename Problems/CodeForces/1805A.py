from functools import reduce

def solve():
    N = int(input())
    A = list(map(int, input().replace(","," ").split()))
    for x in range(257):
        new = [num ^ x for num in A]
        if reduce(lambda a, b: a^b, new) == 0:
            return x
    return -1

for tc in range(int(input())):
    print(solve())