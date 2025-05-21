o,a,k= list(map(int, input().replace(","," ").split()))

A = []
K = []

for i in range(1, 151):
    A.append(a*i)
    K.append(k*i)

A = [x for x in A if x <= 150]
K = [x for x in K if x <= 150]

A = set(A)
for num in K:
    inv = o-num
    if inv in A:
        exit(print(1))
print(0) 