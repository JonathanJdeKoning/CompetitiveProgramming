import math

def lcm(a,b) :
    return abs(a*b) //math.gcd(a,b)
p,q,t = list(map(int, input().split()))
wig = lcm(p,q)
print("yes") if wig <=t else print("no")