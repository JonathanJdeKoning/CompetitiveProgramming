from functools import reduce
factors = lambda n : set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

x = 1
i = 0
while True:
    i+=x
    x+=1
    if len(factors(i)) >500:
        print(i)
