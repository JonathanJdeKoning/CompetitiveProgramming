t = 0
for _ in range(int(input())):
    d = list(map(int, input().split()))
    t += d[0]

if t==0:
    print(1)
else:
    print(t%2)