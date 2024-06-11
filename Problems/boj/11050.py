from math import factorial
n,k = map(int, input().split())

nfac = factorial(n)
kfac = factorial(k)
print(nfac//(kfac*factorial(n-k)))
