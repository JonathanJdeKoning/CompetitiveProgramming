aCap, aAmount = list(map(int, input().split()))
bCap, bAmount = list(map(int, input().split()))
cCap, cAmount = list(map(int, input().split()))

for i in range(100):
    if i%3 == 0:
        cantake = bCap - bAmount
        give = min(aAmount, cantake)
        aAmount -= give
        bAmount += give
    elif i%3==1:
        canTake = cCap - cAmount
        give = min(bAmount, canTake)
        bAmount -= give
        cAmount += give
    elif i%3==2:
        canTake = aCap - aAmount
        give = min(cAmount, canTake)
        cAmount -= give
        aAmount += give
print(aAmount)
print(bAmount)
print(cAmount)
