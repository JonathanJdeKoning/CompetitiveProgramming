from functools import reduce
factors = lambda n : set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

for _ in range(int(input())):
    n = int(input())
    print(n, len(factors(n)))