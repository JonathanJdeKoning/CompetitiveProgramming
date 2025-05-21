from itertools import takewhile
n,m = list(map(int, input().replace(","," ").split()))
A = list(map(int, input().replace(","," ").split()))
B = list(map(int, input().replace(","," ").split()))

new = [0]*(n+m)

for i, a in enumerate(A):
    for j, b in enumerate(B):
        co = i+j
        new[co] += a*b

new = list(takewhile(lambda x: x != 0, new))
if not new: print(0)
else:print(" ".join(map(str, new )))
