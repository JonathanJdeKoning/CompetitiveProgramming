import math
while True:
    numer, denom = list(map(int, input().split()))
    if numer == 0 and denom == 0: break
    output = ""

    complete = int(math.floor(numer/denom))


    left = numer - (complete*denom)
    output = f"{complete} {left} / {denom}"
    print(output)

