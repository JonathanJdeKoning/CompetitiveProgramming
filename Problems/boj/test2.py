
n = int(input())
primes = [True]*(n+1)
primes[0] = False
primes[1] = False

for i in range(n+1):
    if primes[i]:
        for j in range(i+i, n+1, i):
            primes[j] = False

s = 0
b = 0
bLast = False 
for i in range(1,n+1):
    if not primes[i]:
        b += 1
        bLast += 1
    else:
        if bLast:
            b -= 1
            s +=2 
        else:
            s += 1
        bLast = False
print(b, s)

