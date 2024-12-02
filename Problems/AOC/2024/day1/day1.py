from collections import Counter
with open("day1.in", "r") as file:
    A, B = zip(*[(int(x), int(y)) for x, y in (line.split() for line in file.readlines())])
    A, B = list(A), list(B)
    
    print(sum([abs(x-y) for x,y in zip(sorted(A), sorted(B))]))
    print(sum([Counter(B)[k]*k for k in Counter(A).keys()]))