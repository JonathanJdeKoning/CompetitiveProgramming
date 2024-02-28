
c, n = map(float, input().split())
import math

r = ((c/math.pi)/2)
a = r*r*math.pi

if a >= n:
    print("Diablo is happy!")
else:
    print("Need more materials!")
