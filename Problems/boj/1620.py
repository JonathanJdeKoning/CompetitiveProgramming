n, qs = map(int, input().split())

d = {}
for i in range(1,n+1):
    poke = input()
    d[poke] = i
    d[str(i)] = poke

for q in range(qs):
    print(d[input()])
