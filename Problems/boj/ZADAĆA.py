from math import gcd

input()
A = list(map(int, input().split()))
input()
B = list(map(int, input().split()))
a = 1
b = 1

for x in A:
    a*=x
for x in B:
    b*=x

ans = str(gcd(a,b))
print(ans[-9:])