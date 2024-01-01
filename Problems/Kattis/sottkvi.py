friends, daysuntil, today = list(map(int, input().split()))

total = 0
for friend in range(friends):
    
    qday = int(input())
    if (today - qday) + daysuntil >= 14:
        total += 1
print(total)