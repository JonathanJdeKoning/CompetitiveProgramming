from math import log2, factorial
ops, size, bigo = map(int, input().split())
if bigo == 1:
    if factorial(size) > ops:
        print("TLE")
    else:
        print("AC")
if bigo == 2:
    if 2**size > ops:
        print("TLE")
    else:
        print("AC")
if bigo == 3:
    if size**4 > ops:
        print("TLE")
    else:
        print("AC")
if bigo == 4:
    if size**3 > ops:
        print("TLE")
    else:
        print("AC")
if bigo == 5:
    if size**2 > ops:
        print("TLE")
    else:
        print("AC")
if bigo == 6:
    if size * log2(size) > ops:
        print("TLE")
    else:
        print("AC")
if bigo == 7:
    if size > ops:
        print("TLE")
    else:
        print("AC")
