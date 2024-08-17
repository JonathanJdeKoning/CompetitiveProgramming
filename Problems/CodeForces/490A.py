n = int(input())
nums = list(map(int, input().split()))

p = []
m = []
e = []
for i, num in enumerate(nums, start = 1):
    if num == 1:
        p.append(i)
    elif num ==2:
        m.append(i)
    else:
        e.append(i)

mn = min(len(p), len(m), len(e))
if mn == 0: print(0)
else:
    print(mn)
    for i in range(mn):
        print(p[i], m[i], e[i])
