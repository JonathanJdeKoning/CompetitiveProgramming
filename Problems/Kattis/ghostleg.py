eles, rungs = list(map(int, input().split()))
linearr = list(range(1,eles+1))
for i in range(rungs):
    inst = int(input())
    for i in range(len(linearr)):
        if linearr[i] == inst:
            linearr[i] += 1
        elif linearr[i] == inst+1:
            linearr[i] -=1


for i in range(1,len(linearr)+1):
    print(linearr.index(i)+1)

