n,m,k = map(int, input().split())
mat = []
new = []
for _ in range(n):
    row = input()
    newrow = []
    for c in row:
        newrow.append(c*k)
    for i in range(k):
        new.append("".join(newrow))
for row in new:
    print(row)

