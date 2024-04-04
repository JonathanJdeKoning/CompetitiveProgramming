from functools import reduce
factors = lambda n : set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


while True:
    try:
        n = int(input())
        facts = factors(n)
        facts.discard(n)

        facts = list(facts)
        tot = sum(facts)
        if tot == n :
            print(f"{n} perfect")
        elif tot >= n-2 and tot <= n+2:
            print(f"{n} almost perfect")
        else:
            print(f"{n} not perfect")
    except EOFError:
        break
