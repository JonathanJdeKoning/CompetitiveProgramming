numnums = int(input())
numlist = []
baddies = []
for num in range(numnums):
    numlist.append(int(input()))

maxo = numlist[-1]
for i in range(1,maxo+1):
    if i not in numlist:
        baddies.append(i)

if baddies == []:
    print("good job")
else:
    for baddy in baddies:
        print(baddy)
    