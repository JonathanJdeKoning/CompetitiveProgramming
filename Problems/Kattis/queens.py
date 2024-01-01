n = int(input())
pos = []
bad = False
for _ in range(n):
    queen = tuple(map(int, input().split()))

    if not bad:
        for other in pos:
            if abs(queen[0] - other[0]) == abs(queen[1]-other[1]):
                bad = True
                break
    else:
        continue
    pos.append(queen)
    

if len(set([x[0] for x in pos])) != n or len(set(x[1] for x in pos)) != n:
    bad = True


if bad:
    print("INCORRECT")
else:
    print("CORRECT")
