n,x,y = map(int, input().split())
from math import inf
dishes = []
for _ in range(n):
    sweet, salt = map(int, input().split())
    dishes.append((sweet, salt))


dishes.sort()
mx = 0
print(dishes)
for i, dish in enumerate(dishes, start=1):
    x-=dish[0]
    if x < 0:
        mx= max(mx, i)
        break
else:
    mx = n

dishes.sort(key=lambda x:x[1])
print(dishes)
for i, dish in enumerate(dishes, start=1):
    y-=dish[1]
    if y < 0:
        mx = max(mx, i)
        break
else:
    mx = n

print(mx)

