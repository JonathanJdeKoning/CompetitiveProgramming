x, n = map(int, input().split())

total = 0
for i in range(2,n+1,2):
    total += x**i
print(total)
