orig, dest = map(int, input().split())
n = int(input())

total = 4*(abs(orig-dest))
a,b = sorted([orig, dest])
for i in range(n):
    floor = int(input())

    if floor>= b or floor <= a: continue
    
    total += 10

print(total)

