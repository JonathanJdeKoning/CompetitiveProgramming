k, n, w= map(int, input().split())

totalNeed = 0

for i in range(1, w+1):
    totalNeed += k*i

print(max(0, totalNeed-n))
