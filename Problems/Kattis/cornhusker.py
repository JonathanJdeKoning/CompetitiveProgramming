import math
data = list(map(int, input().split()))

kernsround = data[::2]
kernslong= data[1::2]
ears, weight = list(map(int, input().split()))

total = 0
for i in range(5):
    total += kernsround[i]*kernslong[i]

avg = int(math.floor(total/5))

print(int(math.floor((ears*avg)/weight)))
