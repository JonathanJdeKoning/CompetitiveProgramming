from functools import reduce
factors = lambda n : set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
while True:
    n = int(input())
    if n ==0: break
    
    f = factors(n)
    if len(f)%2 ==0:
        print("no")
    else:
        print("yes")
    