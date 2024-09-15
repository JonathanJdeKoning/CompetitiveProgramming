n,k = map(int, input().split())
days = 0
stems = 0
while n:
    days += 1
    n -=1
    stems += 1
    if stems == k:
        n += 1
        stems = 0
print(days)

