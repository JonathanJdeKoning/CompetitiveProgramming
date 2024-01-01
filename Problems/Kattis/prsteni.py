import math
rings = int(input())

ringlist = list(map(int, input().split()))

bigboi = ringlist[0]

for ring in ringlist[1:]:
    mygcd = math.gcd(bigboi, ring)
    print(f"{bigboi//mygcd}/{ring//mygcd}")
