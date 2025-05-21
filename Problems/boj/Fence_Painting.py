ans = set()
a,b = list(map(int, input().replace(","," ").split()))
for i in range(a, b):
    ans.add(i)
a,b = list(map(int, input().replace(","," ").split()))
for i in range(a, b):
    ans.add(i)
print(len(ans))