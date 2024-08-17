n,v = map(int, input().split())
ans = []
for i in range(n):
    data = list(map(int, input().split()))
    if v > min(data[1:]):
        ans.append(i+1)

print(len(ans))
print(" ".join(map(str, sorted(ans))))
