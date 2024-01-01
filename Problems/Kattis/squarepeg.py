import math
slen, crad = list(map(int, input().split()))

print("fits") if slen <= math.sqrt(2)*crad else print("nope")