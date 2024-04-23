from math import inf
i = 1
while True:
    try:
        numnums = int(input())
        bases = set()
        poss = set()
        for _ in range(numnums):
            num = int(input())
            for base in bases:
                poss.add(num+base)
            bases.add(num)
            
        numqueries = int(input())
        
        print(f"Case {i}:")
        for _ in range(numqueries):
            target = int(input())
            closest = inf
            for av in poss:
                if abs(av-target) < abs(closest-target):
                    closest = av
            print(f"Closest sum to {target} is {closest}.")
        i+=1
    except EOFError:
        break
