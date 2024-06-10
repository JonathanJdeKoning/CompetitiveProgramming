from functools import reduce
factors = lambda n : set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

while True:
    n = int(input())
    if n ==-1: break
    facts = factors(n)
    facts.discard(n)
    facts = sorted(list(facts))
    if n == sum(facts):
        print(f"{n} = {' + '.join(map(str, facts))}")
    else:
        print(f"{n} is NOT perfect.")
