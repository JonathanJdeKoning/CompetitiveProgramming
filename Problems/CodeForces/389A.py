from math import gcd
n = int(input())
print(n*gcd(*list(map(int, input().split()))))
