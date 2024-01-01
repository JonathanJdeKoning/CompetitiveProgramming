periods = int(input())
total = 0
for period in range(periods):
    a,b = list(map(float, input().split()))
    total += a*b
print(total)