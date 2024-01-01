numnums = int(input())

mylist = list(map(int, input().split()))

sortedlist = sorted(mylist)

count = 0

for i in range(len(mylist)):
    if mylist[i] != sortedlist[i]:
        count += 1
print(count)