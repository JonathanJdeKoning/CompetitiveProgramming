n = int(input())
a = list(map(int, input().split()))
o = []
for i in range(0,len(a), 2):
    o.append(a[i])
print(" ".join(map(str, o[::-1])))
