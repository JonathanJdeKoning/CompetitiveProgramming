numKnots = int(input())

knotNums = list(map(int, input().split()))

learnedKnots = list(map(int, input().split()))

for kont in learnedKnots:
    knotNums.remove(kont)
print(knotNums[0])