from math import isclose
from decimal import Decimal
for case in range(1, int(input())+1):
    #print(f"CASE {case}:")
    N, P = map(int, input().split())

    chance = (P/100)**(N-1)
    print(f"{chance=}")
    low = 0
    high = 1

    while low <= high:
        mid = (low+high)/2
        print(f"low: {low}, mid: {mid}, high: {high}")
        v = mid**N
        print(f"val: {v}")
        if abs(chance-v) < 0.000000000001:
            break
        elif v > chance:
            high = mid
        elif v < chance:
            low = mid
    print(mid*100 - P)
    #print(f"Case #{case}: {ans}")

