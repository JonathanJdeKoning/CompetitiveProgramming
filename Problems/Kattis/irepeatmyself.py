from functools import reduce
factors = lambda n : set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

n = int(input())
for _ in range(n):
    s = input()
    fs = factors(len(s))

    for f in sorted(list(fs)):
        if s[:f] * (len(s)//f) == s:
            print(f)
            break
