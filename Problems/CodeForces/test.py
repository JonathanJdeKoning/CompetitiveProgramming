from random import randint, seed

n = 99
seed(69)
for _ in range(n):
    N = randint(1,10)
    K = randint(1,N)

    total = 0
    for i in range(1, N):
        total += i**i

    for i in range(1,(N-K)+1):
        total -= i**i
    if total%2 ==0:
        aAns = ("YES")
    else:
        aAns = ("NO")

    base = N
    back = (N-K)+1
    numOdds = None
    numNums = (base-back)+1
    if numNums == 1:
        numOdds = base%2
    elif base%2==0 and back%2==0:
        numOdds = (numNums-1)//2
    elif base%2==1 and back%2==1:
        numOdds = (numNums+1)%2
    else:
        numOdds = numNums//2
    #print(f"{numOdds=}")
    if numOdds%2==1:
        bAns = "NO"
    else: bAns ="YES"

    if aAns != bAns:
        print(f"OOP: {N}, {K}")
    else:
        print("YEP")