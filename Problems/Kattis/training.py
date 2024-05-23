qs, curr = map(int, input().split())

arr = []
for _ in range(qs):
    arr.append(tuple(map(int, input().split())))

for s,e in arr:
    if s<=curr and e>= curr:
        curr+=1
print(curr)
