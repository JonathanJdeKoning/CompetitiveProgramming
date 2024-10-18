N = int(input())
A = list(map(int, input().split()))
negs = [x for x in A if x < 0]
negSum = sum([abs((-1) - x) for x in negs])
ans = sum([x-1 for x in A if x > 0])
if A.count(0) != 0:
    print(A.count(0) + ans + negSum)
else:
    if len(negs)%2==0:
        print(ans + negSum)
    else:
        print(ans + negSum + 2)


